from uuid import UUID

from cqrs.exception.bad_request import BadRequest


class Message:
    """
    Query/Command
    """

    def __init__(self, message_uuid: UUID, payload):
        self.uuid: UUID = message_uuid
        if hasattr(self, 'default_values'):
            for k, v in getattr(self, 'default_values').items():
                setattr(self, k, v)

        if hasattr(self, '__slots__'):
            for attr in getattr(self, '__slots__'):
                value = payload.get(attr) if payload.get(attr) != None or not hasattr(self,
                                                                                      'default_values') else getattr(
                    self, 'default_values').get(attr)
                setattr(self, attr, value)
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
        if hasattr(self, 'required_fields'):
            for required_field in getattr(self, 'required_fields'):
                if not getattr(self, required_field):
                    raise BadRequest(required_field)
