class Message:
    def __init__(self, text: str):
        self.text = text

    def to_json(self):
        return {"message": self.text}
