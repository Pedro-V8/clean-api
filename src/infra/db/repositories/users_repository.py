from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UserEntity


class UsersRepository:
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int):
        with DBConnectionHandler() as database:
            try:
                new_register = UserEntity(
                    first_name=first_name, last_name=last_name, age=age
                )
                database.session.add(new_register)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
