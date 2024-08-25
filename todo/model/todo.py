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
        all_tags: list[str] = []
        count_object_for_tag: dict[str, int] = {}
        # all_tags = [self.todos[tag].tags[tag] for tag in self.todos[tag].tags]
        # No se puede utilizar este list comprehension debido a que se necesitan dos iteradores de diferente tipo
        for todo in self.todos:
            for tag in self.todos[todo].tags:
                all_tags.append(tag)
        for tag in all_tags:
            count_object_for_tag[tag] = all_tags.count(tag)
        return count_object_for_tag


tareas = TodoBook()
tareas.add_todo("tarea 1", "prueba")
tareas.add_todo("tarea 2", "prueba 2")
tareas.todos[1].add_tag("work")
tareas.todos[1].add_tag("study")
tareas.todos[2].add_tag("work")

print(tareas.todos[1])
print(tareas.todos[1].completed)
tareas.todos[1].mark_completed()
print(tareas.todos[1].completed)
print(tareas.pending_todos())
print(tareas.tags_todo_count())
