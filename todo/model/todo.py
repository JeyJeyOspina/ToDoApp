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
        for _ in self.tags:
            if tag == self.tags:
                tag_count += 1
        if tag_count == 0:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        code_id: int = len(self.todos) + 1
        self.todos[code_id] = Todo(code_id, title, description)
        return code_id

    def pending_todos(self) -> list[Todo]:
        return [self.todos[todo] for todo in self.todos if self.todos[todo].completed == False]

    def completed_todos(self) -> list[Todo]:
        return [self.todos[todo] for todo in self.todos if self.todos[todo].completed == True]

    def tags_todo_count(self) -> dict[str, int]:
        tag: int = 1
        todo_tag: int = 1
        count_object_for_tag: dict[str, int] = {}
        all_tags = [self.todos[tag].tags for tag in self.todos[tag].tags]
        for tag in all_tags:
            count_tag: int = 0
            tag_string: str = all_tags[tag]
            for todo in self.todos:
                for todo_tag in self.todos[todo].tags[todo_tag]:
                    if all_tags[tag] == self.todos[todo].tags[todo_tag]:
                        count_tag += 1
            count_object_for_tag[tag_string] = count_tag
        return count_object_for_tag


tareas = TodoBook()
tareas.add_todo("tarea 1", "prueba")
tareas.add_todo("tarea 2", "prueba 2")

print(tareas.todos[1])
print(tareas.todos[1].completed)
tareas.todos[1].mark_completed()
print(tareas.todos[1].completed)
print(tareas.pending_todos())
