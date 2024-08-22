class Todo:
    def __init__(self, code_id: int, tittle: str, description: str):
        self.code_id: int = code_id
        self.title: str = tittle
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

