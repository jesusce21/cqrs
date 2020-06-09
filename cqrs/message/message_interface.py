from abc import ABCMeta, abstractmethod


class MessageInterface(metaclass=ABCMeta):
    """
    Query Interface
    """

    @property
    @abstractmethod
    def message_action(self) -> str:
        """
        Allows to get the name
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def assert_payload(self) -> None:
        """
        Allows to validate the payload
        """
        raise NotImplementedError
