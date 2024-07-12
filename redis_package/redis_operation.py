from app.main import client
class Queue:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, value: str) -> int:
        try:
            return self.db.rpush(self.name, value)
        except Exception as e:
            return e

    def read(self ) -> [bytes]:
        try:
            return self.db.lpop(self.name)
        except Exception as e:
            return e

class Stack:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def write(self, value: str) -> int:
        try:
            return self.db.lpush(self.name, value)
        except Exception as e:
            return e

    def read(self ) -> [bytes]:
        try:
            return self.db.lpop(self.name)
        except Exception as e:
            return e

class Delete:
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def delete(self) -> bool:
        try:
            return self.db.delete(self.name) == 1
        except Exception as e:
            return e

