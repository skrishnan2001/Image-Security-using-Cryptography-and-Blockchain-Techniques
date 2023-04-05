import React, { useState, useEffect } from "react";
import "@innovaccer/design-system/css/dist/index.css";
import { Card, Table } from '@innovaccer/design-system';
import ImageUpload from "../ImageUpload/ImageUpload";
import Loader from "../../components/Loader/Loader";
import { useUserAuth } from "../../context/UserAuthContext";


const AllUsers = () => {
  const { user } = useUserAuth();
  const [showComponent, setShowComponent] = useState(false);
  const [recipientEmail, setRecipientEmail] = useState();

  const renderComponent = (rowIndex) => {
    setShowComponent(true);
    setRecipientEmail(rowIndex["email"])
  }

  const [data, setData] = useState([]);
  useEffect(() => {
    fetch(`/users`).then(
      res => res.json()
    ).then(
      data => {
        setData(data)
      }
    ).catch(err => {
      console.log(err)
    })
  }, [])


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
      {
        data.length > 0 ?
          <Card className="mb-5 mt-7">
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
              pageSize={6}
              onPageChange={newPage => console.log(`on-page-change:- ${newPage}`)}
            />
          </Card>
          :
          <Loader />
      }
      {showComponent && <ImageUpload sender={user.email} recipientEmail={recipientEmail} />}


    </>
  );
};

export default AllUsers;
