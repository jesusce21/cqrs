from abc import abstractmethod

from cqrs.message.message import Message


class MessageHandle:
    """
    Query/Command Handler
    """

    @abstractmethod
    def handle(self, query: Message):
        pass
