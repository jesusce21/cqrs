from typing import Callable, Any, List, Dict
from abc import ABC, abstractmethod

CallNextMiddleware = Callable[[object], Any]
Middleware = Callable[[object, CallNextMiddleware], Any]
MiddlewareList = List[Middleware]
Handler = Callable
Handlers = Dict[type, Handler]
WrapperFunction = Callable[[object], Any]


class MessageBusInterface(ABC):
    """
    Message Interface
    """

    @abstractmethod
    def add_handler(self, message_class: type,
                    message_handler: Callable) -> None:
        """
        Required Method
        :param message_class:
        :param message_handler:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def handle(self, message: object) -> List[Any]:
        """
        Required Method
        :param message:
        :return:
        """
        raise NotImplementedError
