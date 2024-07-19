from sqlalchemy import Column, Integer, String, MetaData, Table

metadata = MetaData()

user = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("username", String, unique=True, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column("hashed_password", String, nullable=False),

)
