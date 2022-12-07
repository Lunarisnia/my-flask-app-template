class BaseRouter():    
    def __new__(self, endpoint, endpoint_name=None, methods=['GET']):
        self.endpoint = endpoint
        self.methods = methods
        self.endpoint_name = endpoint_name

        return {
            "endpoint": self.endpoint,
            "endpoint_name": self.endpoint_name,
            "handler": self.run,
            "methods": self.methods
        }

    def run():
        return "Hello, Welcome to the default template."