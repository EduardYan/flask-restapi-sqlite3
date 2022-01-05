# Flask Sqlite RestAPI.

__This is a restapi made with python and flask, using as sqlite as database.__

# Docker installation.

```bash
docker build -d -p 3000:3000 eduarddan/houses-app
```

# Manual Installation.

```bash
git clone https://github.com/EduardYan/flask-restapi-sqlite3.git
```

## Dependencies.

__Install dependecies with requirements file:__

```bash
$ pip3 install -r requirements.txt
```

## Enviroment Variables

__Create this enviroment variables for the database and run the restapi:__

```bash
SQLITE_PATH=
```

## Run
```bash
cd flask-restapi-sqlite3
python3 index.py
```


# Routes.

__The server is running in port 3000. The keys for add books in POST are name= and price=__

* GET / or /books
* GET /books/1
* POST /books
* PUT /books/1
* DELETE /books/2
