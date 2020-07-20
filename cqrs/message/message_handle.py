from abc import abstractmethod

from cqrs.message.message import Message


class MessageHandler:
    """
    Message Handler
    """

    @abstractmethod
    def handle(self, query: Message):
        pass
