from dataclasses import dataclass

from logic.exceptions.base import LogicExceprion


@dataclass(eq=False)
class EventHandlersNotRegisteredException(LogicExceprion):
    event_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчики для события {self.event_type}'


@dataclass(eq=False)
class CommandHandlersNotRegisteredException(LogicExceprion):
    command_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчики для команды {self.command_type}'
