from sqlalchemy import inspect
from src.orm.models.user_models import UserModel
from src.orm.database import SESSION_FACTORY
from dataclasses import asdict

from src.orm.orm_registry import run_mappers


class UserRepository:
    def __init__(self):
        self.session = SESSION_FACTORY()

    def create(self, user: UserModel):
        self.session.add(user)
        self.session.commit()
        return user

    def get_all_user(self):
        return self.session.query(UserModel).all()

    def get_single_user(self, user_id: int):
        return self.session.query(UserModel).filter(UserModel.id == user_id).first()

    def delete_user(self, user_id: int):
        self.session.query(UserModel).filter(UserModel.id == user_id).delete()
        self.session.commit()

    def update(self, new_data: UserModel):
        db_user = self.session.query(UserModel).filter(UserModel.id == new_data.id).first()
        if not db_user:
            raise ValueError(f"User with id {new_data.id} not found")

        # Ensure only actual table columns are updated
        for key, value in vars(new_data).items():
            if key in inspect(UserModel).columns:
                setattr(db_user, key, value)

        self.session.commit()
        return db_user  # Return updated user


if __name__ == '__main__':
    run_mappers()
    repo = UserRepository()
    result = repo.get_all_user()
    result = [asdict(user) for user in result]
    print(result)
