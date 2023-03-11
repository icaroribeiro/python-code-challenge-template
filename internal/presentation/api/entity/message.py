from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Message:
    text: str

    def to_json(self):
        return {"message": self.text}
