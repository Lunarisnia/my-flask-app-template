from src.base.BaseController import BaseController
from src.libs.User import User


class UserController(BaseController):
    def getUser(self, query) -> dict:
        return self.model.get(query)


userController = UserController(User())
