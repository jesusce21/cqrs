from typing import List, Callable, Any, Type

from cqrs.message.message import Message
from cqrs.message_bus.message_bus_interface import Middleware, \
    MessageBusInterface, Handlers, MiddlewareList, Handler, \
    WrapperFunction


class MessageBus(MessageBusInterface):
    """
    MessageBus (chain)
    """

    def __init__(self, middleware: MiddlewareList = None) -> None:
        self._handlers: Handlers = {}
        all_middleware = (middleware or []) + [self._trigger_handler]
        self._middleware_chain = self._get_middleware_chain(
            all_middleware)

    def add_handler(self, message_class: Type[Message], message_handler: Callable) -> None:
        """
        Allows to add a handler to message class
        :param message_class:
        :param message_handler:
        :return:
        """
        self._handlers[message_class] = message_handler

    def handle(self, message: Message) -> List[Any]:
        """
        Allows to handle the message
        :param message:
        :return:
        """
        if type(message) not in self._handlers:
            return []
        return self._middleware_chain(message)

    def _trigger_handler(self, message: Message, unused_next: Callable) -> List[Any]:
        handler: Handler = self._handlers[message.__class__]
        return handler(message)

    @staticmethod
    def _get_middleware_chain(all_middleware: MiddlewareList) -> WrapperFunction:
        chain: callable = lambda _: None
        for middle in reversed(all_middleware):
            chain = MessageBus._get_middleware_wrapper(middle, chain)
        return chain

    @staticmethod
    def _get_middleware_wrapper(middleware: Middleware, next_middleware: Callable) -> WrapperFunction:
        def middleware_callable(message: object):
            return middleware(message, next_middleware)

        return middleware_callable
