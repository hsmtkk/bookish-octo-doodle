import factory.alchemy
import factory.faker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

import model

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_SESSION_PERSISTENCE = "commit"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.metadata.create_all(engine)


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    email = factory.faker.Faker("email")

    class Meta:
        model = model.User
        sqlalchemy_session = session
        sqlalchemy_session_persistence = SQLALCHEMY_SESSION_PERSISTENCE


class ItemFactory(factory.alchemy.SQLAlchemyModelFactory):
    title = factory.faker.Faker("word")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = model.Item
        sqlalchemy_session = session
        sqlalchemy_session_persistence = SQLALCHEMY_SESSION_PERSISTENCE
