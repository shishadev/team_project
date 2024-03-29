from typing import final
import jsonschema
from parsers.services.mixins.InitFromJsonMixin import InitFromJson
from parsers.core.protocols.ValidatorProtocol import ValidatorProtocol


@final
class JsonValidator(ValidatorProtocol, InitFromJson):
    """Validates json file against the schema provided"""
    
    def __init__(self, schema: dict):
        self._schema = schema
    
    def validate(self, data: dict, schema: dict = None) -> bool:
        
        if schema is None:
            schema = self._schema
        
        validator = jsonschema.Draft7Validator(schema=schema)
        return validator.is_valid(data), validator.iter_errors(data)
