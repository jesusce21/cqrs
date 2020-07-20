from abc import ABCMeta, abstractmethod


class MessageInterface(metaclass=ABCMeta):
    """
    Message Interface
    """

    @property
    @abstractmethod
    def message_action(self) -> str:
        """
        Allows to get the name
        :return:
        """
        raise NotImplementedError
