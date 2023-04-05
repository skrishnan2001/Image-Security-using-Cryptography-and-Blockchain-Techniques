import React, { useState, useEffect } from "react";
import "@innovaccer/design-system/css/dist/index.css";
import { Card, Table } from '@innovaccer/design-system';
import ImageUpload from "../ImageUpload/ImageUpload";
import SharedImages from "../SharedImages/SharedImages";
import first_upload from './ImageTemplates/first_upload.png';

const SharedWith = ({ email }) => {
  //email denotes the mail ID of the signed in user

  const [showComponent, setShowComponent] = useState(false);
  const [recipientEmail, setRecipientEmail] = useState();

  const renderComponent = (rowIndex) => {
    setShowComponent(true);
    // console.log(rowIndex["email"])
    setRecipientEmail(rowIndex["email"])
  }

  const [data, setData] = useState([]);
  useEffect(() => {
    fetch(`/${email}/communications`).then(
      res => res.json()
    ).then(
      data => {
        setData(data)
      }
    ).catch(err => {
      console.log(err)
    })
  }, [email])


  const schema = [
    {
      name: 'name',
      displayName: 'Name',
      width: '50%',
      separator: true,
      translate: a => ({
        title: `${a.lastName}, ${a.firstName}`,
        firstName: a.firstName,
        lastName: a.lastName
      }),
      cellType: 'AVATAR_WITH_TEXT',
      sorting: false
    },
    {
      name: 'email',
      displayName: 'E-Mail',
      width: "50%",
      sorting: false
    },
  ];
  return (
    <>
      {data.length > 0 ?
        <Card className="mb-5">
          <Table
            type="resource"
            data={data}
            schema={schema}
            showMenu={false}
            withHeader={true}
            withCheckbox={true}

            onSelect={(rowIndex, selected, selectedList, selectAll) =>
              console.log(`on-select:- rowIndex: ${rowIndex} selected: ${selected} selectedList: ${JSON.stringify(selectedList)} selectAll: ${selectAll}`)
            }

            onRowClick={renderComponent}

            headerOptions={{
              withSearch: true
            }}
            onSearch={(currData, searchTerm) => {
              return currData.filter(d =>
                d.firstName.toLowerCase().match(searchTerm.toLowerCase())
                || d.lastName.toLowerCase().match(searchTerm.toLowerCase())
              );
            }}
            withPagination={true}
            pageSize={5}
            onPageChange={newPage => console.log(`on-page-change:- ${newPage}`)}
          />
        </Card>
        :
        <div className="justify-content-md-center">
          <h3 className="text-center mb-5 text-success">Search for a user & start sharing now! </h3>
          <img className="d-block mx-auto img-fluid w-35" src={first_upload} alt="first upload" />
        </div>

      }
      {showComponent && <ImageUpload sender={email} recipientEmail={recipientEmail} />}
      {showComponent && <SharedImages sender={email} receiver={recipientEmail} />}
    </>
  );
};

export default SharedWith;
