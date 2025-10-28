"""
Contiene qualsiasi tipo di frasi o parole utilizzate in FoggiaScript.

Qui si troverà il vero spirito foggiano.
"""
from abc import ABC


class Misc(ABC):
    """
    Contiene frasi varie
    """
    code_marker = 'Codice scritto con FoggiaScript'


class ErrorDesc(ABC):
    """
    Contiene frasi di errore.
    """
    unknown_character = 'Carattere invalido: "{char}".'
    expected_literal = 'Aspettavo un valore letterale.'
    closed_bracket = 'Parentesi chiusa inaspettata.'
    unclosed_bracket = 'Parentesi aperta non è stata chiusa.'
    empty_bracket = 'Parentesi è vuota nel suo interno.'
    no_left_side_expr = "Aspettavo un'espressione a sinistra di \"{char}\"."
    no_right_side_expr = "Aspettavo un'espressione a destra di \"{char}\"."