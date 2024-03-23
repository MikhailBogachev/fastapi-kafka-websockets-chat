from dataclasses import dataclass

from logic.exceptions.base import LogicExceprion


@dataclass(eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicExceprion):
    title: str

    @property
    def message(self):
        return f'Чат с таким названием "{self.title}" уже суествует'
