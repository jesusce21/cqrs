from uuid import UUID

from cqrs.exception.bad_request import BadRequest


class Message:
    """
    Query/Command
    """

    def __init__(self, message_uuid: UUID, payload):
        self.uuid: UUID = message_uuid
        for k, v in getattr(self, 'default_values'):
            setattr(self, k, v)
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

    def assert_payload(self) -> None:
        for required_field in self.required_fields:
            if not getattr(self, required_field):
                raise BadRequest(required_field)