class GenericClientError(Exception):
    def __init__(self, error: str):
        super().__init__(error)


class GenericServerError(Exception):
    def __init__(self, error: str):
        super().__init__(error)
