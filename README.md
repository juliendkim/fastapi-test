# FastAPI test with SQLAlchemy

### Ready
```shell script
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip setuptools wheel pylint
(venv) $ pip install -r requirements.txt
``` 

### Run
```shell script
$ yarn start
OR
$ uvicorn main:app --reload --host=0.0.0.0 --port=8000
```

### Database URL
dialect+driver://username:password@host:port/database

CONNECTION_STRING='sqlite:///./notes.db'
CONNECTION_STRING='mysql://username:password@localhost:3306/notes'
CONNECTION_STRING='postgresql://username:password@localhost:5432/notes'


### See document
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
