from src.base.BaseModel import BaseModel


class User(BaseModel):
    def get(self, query):
        super().get(query)
        return {"query": query, "data": [{"name": "Aan"}]}
