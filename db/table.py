import sqlalchemy

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    sqlalchemy.Column("fullname"  , sqlalchemy.String),
    sqlalchemy.Column("email"     , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
)