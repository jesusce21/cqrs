class MessageAssertion(Exception):
    """Exception raised for errors in the message.

    Attributes:
        message_payload_var
    """

    def __init__(self, message_payload_var):
        self.message = f"The malformed variable: '{message_payload_var}'"
