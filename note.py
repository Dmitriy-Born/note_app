from datetime import datetime


class Note:
    def __init__(self, id_note, title, body, created_at=None, updated_at=None):
        self.id = id_note
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __str__(self):
        return f"Заметка #{self.id}: {self.title}\n{self.body}\nСоздана: {self.created_at}\nИсправлена: {self.updated_at}"

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.now()
