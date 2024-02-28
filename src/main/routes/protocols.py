from pydantic import BaseModel, ValidationError

from main.errors.invalid_param_error import InvalidParamError


class InputDTO(BaseModel):

    @classmethod
    def model_validate(cls, data):
        try:
            return cls(**data)
        except ValidationError as e:
            raise InvalidParamError(errors=e.errors()) from e


class OutputDTO(BaseModel):
    pass
