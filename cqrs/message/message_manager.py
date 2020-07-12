from typing import Type, List, Any

from cqrs.message.message import Message
from cqrs.message.message_handle import MessageHandle
from cqrs.message_bus.message_bus import MessageBus


class MessageManager:
    """
    MessageManager class
    """

    @classmethod
    def do_action(cls, bus: Type[MessageBus], message: Type[Message], payload: dict, handler_config: dict) -> List[Any]:
        """
        Allows to do de action
        :param bus:
        :param message:
        :param payload:
        :param handler_config:
        :return:
        """
        message_handler: MessageHandle = cls._get_message_handler(message, handler_config)
        message_bus: MessageBus = bus()
        message_bus.add_handler(message, message_handler.handle)
        message: Message = message(**payload)
        return message_bus.handle(message)

    @staticmethod
    def _get_message_handler(message: Type[Message], handler_config: dict) -> MessageHandle:
        handler_mod: str = f"{message.__module__}_handler"
        handler_class_name: str = f"{message.__name__}Handler"
        handler: MessageHandle = getattr(__import__(handler_mod, fromlist=[
            handler_class_name]), handler_class_name)
        return handler(**handler_config)
