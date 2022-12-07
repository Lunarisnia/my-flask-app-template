from src.base.BaseRouter import BaseRouter
from src.controllers.UserController import userController
from flask import request

class HomeRouter(BaseRouter):
    def run():
        query_name = request.args.get("name")
        return userController.getUser(query=query_name)