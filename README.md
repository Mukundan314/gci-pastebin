# Pastebin

## Administration

User for administration can be created by doing `python manage.py createsuperuser`  
Pastes can be edited and deleted at: `<domain>/admin/pasteapp/paste/`

## Running the server

```
python manage.py runserver
```

## API Endpoints

##### `/api/create`

**Method:** POST  
**Params:** title, content, language  
**Output:** id

Example Request:
```sh
$ curl -X POST -H "Content-Type: application/json" -d '{"title": "Example Title", "content": "console.log(1)", "language": "javascript"}' http://127.0.0.1:8000/api/create/
{"id": "a5cce9ce-1662-4152-818d-792144de3111"}
```

---

##### `/api/view/<paste_id>`

**Method:** GET  
**Params:** paste_id  
**Output:** title, content, language, createdOn

Example Request:
```sh
$ curl http://127.0.0.1:8000/api/view/a5cce9ce-1662-4152-818d-792144de3111
{"title": "Example Title", "content": "console.log(1)", "language": "javascript", "createdOn": "2019-12-25"}
```

---
