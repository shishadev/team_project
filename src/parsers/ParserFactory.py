from typing import Final, final
from parsers.hse.basic.BasicParser import BasicParser
from parsers.core.protocols.ParserProtocol import ParserProtocol


@final
class ParserFactory:
    """Parser Factory to resolve a parser based on their properties"""
    
    _parsers: Final = {
        "hse": {
            "basic": {
                "table": BasicParser
            },
            "annual": {
               # Not implemented
            }
        },
        "psu": {
            # Not implemented
        }
    }
    
    @staticmethod
    def choose_parser(data_type: str, university: str, plan_type: str) -> ParserProtocol:
        """Chooses parser based on features provided

        Args:
            data_type (str): data type to parse
            university (str): university for which parser is made
            plan_type (str): curricula type ["basic" | "annual"]

        Returns:
            ParserProtocol: A parser if exists, otherwise shall throw KeyError exception
        """
        return ParserFactory._parsers[university][plan_type][data_type]()
