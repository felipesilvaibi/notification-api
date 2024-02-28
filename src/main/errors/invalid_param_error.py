class InvalidParamError(Exception):
    def __init__(self, errors: dict):
        self.errors = errors
        super().__init__("Invalid Params Error")
