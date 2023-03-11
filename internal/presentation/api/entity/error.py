from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Error:
    text: str

    def to_json(self):
        return {"error": self.text}
