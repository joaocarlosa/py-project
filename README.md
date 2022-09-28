# py-project

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

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

Examples of API method calls:



list companies in the system
*GET:
```bash
: 0.0.0.0/collaborator/{name}
```

register a company (attributes: [:name])

```bash
: 0.0.0.0/collaborator/{name}
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
