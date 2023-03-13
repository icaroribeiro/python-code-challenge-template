import uuid


class User:
    def __init__(self, id: uuid.UUID, username: str):
        self.id = id
        self.username = username

    @staticmethod
    def from_domain(domain):
        return User(id=domain.id, username=domain.username)

    def to_json(self):
        return {"id": str(self.id), "username": self.username}
