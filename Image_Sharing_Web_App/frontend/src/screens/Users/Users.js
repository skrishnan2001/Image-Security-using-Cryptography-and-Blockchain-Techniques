import React from "react";
import "@innovaccer/design-system/css/dist/index.css";
import { Card, Table } from '@innovaccer/design-system';

const User = () => {
  const data = [
    {
      "firstName": "Krishnan",
      "lastName": "S",
      "email": "skrishnan2001@gmail.com",
      "status": "Active"
    },
    {
      "firstName": "Pranay",
      "lastName": "V",
      "email": "pranayv01@gmail.com",
      "status": "Active"
    },
    {
      "firstName": "Aravind",
      "lastName": "J",
      "email": "aravindusj@gmail.com",
      "status": "Inactive"
    },
    {
      "firstName": "Brooke",
      "lastName": "Heeran",
      "email": "bheeran0@altervista.org",
      "status": "Active"
    },
    {
      "firstName": "Frazer",
      "lastName": "Cathro",
      "email": "fcathro1@ucla.edu",
      "status": "Active"
    },
    {
      "firstName": "Lemmie",
      "lastName": "Ciric",
      "email": "lciric2@dmoz.org",
      "status": "Inactive"
    },
    {
      "firstName": "Randy",
      "lastName": "Boatwright",
      "email": "rboatwright3@arstechnica.com",
      "status": "Active"
    },
    {
      "firstName": "Rolando",
      "lastName": "Cyples",
      "email": "rcyples4@biglobe.ne.jp",
      "status": "Inactive"
    },
    {
      "firstName": "Lem",
      "lastName": "Males",
      "email": "lmales5@admin.ch",
      "status": "Inactive"
    },
    {
      "firstName": "Sayres",
      "lastName": "Adelberg",
      "email": "sadelberg6@uol.com.br",
      "status": "Active"
    },
    {
      "firstName": "Murray",
      "lastName": "Bravington",
      "email": "mbravington7@drupal.org",
      "status": "Active"
    },
    {
      "firstName": "Jena",
      "lastName": "Swatheridge",
      "email": "jswatheridge8@npr.org",
      "status": "Active"
    },
    {
      "firstName": "Annabel",
      "lastName": "Nelsey",
      "email": "anelsey9@google.com",
      "status": "Inactive"
    }
  ];

  const schema = [
    {
      name: 'name',
      displayName: 'Name',
      width: '30%',
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
      width: 250,
      sorting: false
    },
    {
      name: 'status',
      displayName: 'Status',
      width: 200,
      cellType: 'STATUS_HINT',
      sorting: false,
      translate: a => ({
        title: a.status,
        statusAppearance: (a.status === 'Inactive') ? 'default' : 'success'
      }),
    },
  ];
  return (
    <Card>
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
  );
};

export default User;
