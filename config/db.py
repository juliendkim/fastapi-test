import databases
import sqlalchemy


CONNECTION_STRING = 'sqlite:///./notes.db'

database = databases.Database(CONNECTION_STRING)
metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("content", sqlalchemy.String),
    sqlalchemy.Column("created", sqlalchemy.DateTime),
)


engine = sqlalchemy.create_engine(
    CONNECTION_STRING,
    connect_args={
        "check_same_thread": False
    }
)
metadata.create_all(engine)
