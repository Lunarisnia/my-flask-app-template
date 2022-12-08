from src.routes.HomeRouter import HomeRouter

routes = [
    HomeRouter('/', 'Get User', HomeRouter.getUser),
    HomeRouter('/add', 'Add User', HomeRouter.addUser, methods=['POST']),
    HomeRouter('/update', 'Update User', HomeRouter.updateUser, methods=['PUT']),
    HomeRouter('/delete', 'Delete User', HomeRouter.deleteUser, methods=['PUT']),
]