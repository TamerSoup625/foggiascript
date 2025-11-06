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


class Builtins(ABC):
    """
    Contiene nomi di funzioni e variabili builtin.
    """
    print_ = "print"
    javascript = "JavaScript"


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
    extra_comma = "C'è una virgola di troppo."
    no_reason_comma = "Questa virgola non ha significato qui."
    undefined_variable = 'La variabile "{name}" non è definita.'
    unterminated_comma = "Stringa non è stata chiusa."
    expected_member = "Aspettavo il nome del metodo o attributo dopo il punto."
    no_member = "Non c'è il nome del metodo o attributo dopo il punto."
    dot_without_expr = "Aspettavo un'espressione prima del punto."
    cannot_access_attribute = "Non puoi accedere all'attributo \"{name}\" dell'oggetto."
    unclosed_comment = 'Commento multilinea non è stato chiuso, utilizzare "]#".'