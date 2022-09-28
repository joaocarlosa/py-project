# py-project

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=IN%20PROGRESS&color=GREEN&style=for-the-badge)

implementation of a Rest API for company org chart

Library needed:

Flask 
```bash
$ pip install -U Flask
```
Flask RestFul
```bash
$ pip install -U flask_restful
```

Create a project folder and a venv folder within (Windows):
```bash
> mkdir myproject
> cd myproject
> py -3 -m venv venv
```

Before you work on your project, activate the corresponding environment (Windows):
```bash
> venv\Scripts\activate
```

---

# Working with company data


* ![GET](https://img.shields.io/badge/-GET-blue) - listing all company data

```bash
0.0.0.0/companies
```

* ![GET](https://img.shields.io/badge/-GET-blue) - listing company data by id

```bash
0.0.0.0/companies/{id}
```


* ![POST](https://img.shields.io/badge/-POST-brightgreen) - register a new company data
```bash
: 0.0.0.0/companies/{id}
```
```JSON
{
    "id": "0",
    "name": "John Doe",
    "email": "john@mail.com",
    "business": "Google",
    "role": "dev",
    "manager": "David"
}
```



* ![PUT](https://img.shields.io/badge/-PUT-orange) - update a company data 

```bash
: 0.0.0.0/companies/{id}
```

```JSON
{
    "id": "0",
    "name": "John Doe - new",
    "email": "john@mail.com - new",
    "business": "Google - new",
    "role": "Dev - New",
    "manager": "David - New"
}
```

* `DELETE` - delete a company data
```bash
: 0.0.0.0/companies/{id}
```

---

# working with employee data

* ![GET](https://img.shields.io/badge/-GET-blue) - listing contributor information by name
```bash
0.0.0.0/collaborator/{name}
```

* ![GET](https://img.shields.io/badge/-GET-blue) - list employees of a company
```bash
0.0.0.0/collaborator/{business}
```

* ![POST](https://img.shields.io/badge/-POST-brightgreen)  - Register data of a new collaborator
```bash
: 0.0.0.0/collaborator/{id}
```
```JSON
{
    "id": "0",
    "name": "John Doe",
    "email": "john@mail.com",
    "business": "Google",
    "role": "dev",
    "manager": "David"
}
```



* ![DELETE](https://img.shields.io/badge/-DELETE-red) - delete a company data 

```bash
: 0.0.0.0/companies/{id}
```


## project structure
```
├── app
│   ├── main.py
│   ├── controllers             // Our API core handlers - Common response functions 
│   │   ├── collaborator.py    
│   │   ├── company.py          
│   │   └── organization.py     
│   └── model
│       └── data.py             // Models for our application
└── main.py
```
