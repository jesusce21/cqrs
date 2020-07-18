class BadRequest(Exception):
    """
    Exception raised for not found data.
    """

    def __init__(self, message_payload_var: str):
        self.message = f"The malformed variable: '{message_payload_var}'"
        self.http_code = 400
