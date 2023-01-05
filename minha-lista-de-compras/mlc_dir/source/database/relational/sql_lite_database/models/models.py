from typing import Any

try:
    from mlc_dir import sql_db as db
    from mlc_dir import login_manager
except ImportError:  # Used by tests
    from .......mlc_dir import sql_db as db  # type:ignore
    from .......mlc_dir import login_manager


@login_manager.user_loader
def load_user(user_id: str) -> Any:
    return UserModel.query.get(user_id)


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username
