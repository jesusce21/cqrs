from uuid import UUID


class Message:
    """
    Query/Command
    """

    def __init__(self, message_uuid: UUID, payload):
        self.uuid: UUID = message_uuid
        for attr in getattr(self, '__slots__'):
            setattr(self, attr, payload.get(attr))
        getattr(self, 'assert_payload')()

    @property
    def message_action(self) -> str:
        """
        Allows to get the event name
        :return:
        """
        return ""

    @property
    def project_name(self) -> str:
        """
        Allows to get the project name
        :return:
        """
        return ""

    @property
    def message_version(self) -> int:
        """
        Allows to get the event version
        :return:
        """
        return 1

    @property
    def message_type(self) -> str:
        """
        Allows to get the event type
        :return:
        """
        return "query"

    @property
    def message_name(self) -> str:
        """
        Allows to get the even message name
        :return:
        """
        return f"{self.project_name}.{self.message_version}.{self.message_type}.{self.message_action}"

    @property
    def payload(self) -> dict:
        """
        Allows to get the payload
        :return:
        """
        res = {}
        for attr in getattr(self, '__slots__'):
            res[attr] = getattr(self, attr)
        return res
