class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        tag_count = 0
        for i in self.tags:
            if tag == self.tags:
                tag_count += 1
        if tag_count == 0:
            self.tags.append(tag)




