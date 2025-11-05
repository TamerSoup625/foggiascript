from typing import TypeAlias, Any
from enum import auto, Enum


OPEN = False
CLOSED = True


class TokenID(Enum):
    """
    Enumerazione degli identificatori dei token.
    """


    INT = auto()
    """Numero intero. Il secondo elemento della tupla è il valore dell'intero."""
    FLOAT = auto()
    """Numero decimale. Il secondo elemento della tupla è il valore del float."""
    PLUS = auto()
    """Operatore di addizione binario (x + y). Il secondo elemento è sempre `None`."""
    MINUS = auto()
    """Operatore di sottrazione binario (x - y). Il secondo elemento è sempre `None`."""
    TIMES = auto()
    """Operatore di moltiplicazione (*). Il secondo elemento è sempre `None`."""
    DIV = auto()
    """Operatore di divisione (/). Il secondo elemento è sempre `None`."""
    UNARY_PLUS = auto()
    """Operatore di addizione unario (+x). Il secondo elemento è sempre `None`."""
    UNARY_MINUS = auto()
    """Operatore di sottrazione unario (-x). Il secondo elemento è sempre `None`."""
    PARENTHESIS = auto()
    """Parentesi tonda. Il secondo elemento è `false` se è parentesi aperta, `true` se chiusa."""
    LINE_BREAK = auto()
    """Ritorno a capo, sia effettivo (\\n) o un punto e virgola. Il secondo elemento è sempre `None`."""
    CALL_OP = auto()
    """Token tra un oggetto e una parentesi contenente i suoi argomenti per chiamare quell'ogggetto. Il secondo elemento è sempre `None`."""
    NAME = auto()
    """Nome di una variabile, funzione, eccetera. Il secondo argomento è il suo nome effettivo."""
    COMMA = auto()
    """Una virgola (,). Il secondo elemento è sempre `None`."""
    STRING = auto()
    """Stringa di caratteri. Il secondo elemento è il valore della stringa."""
    DOT = auto()
    """Punto (.) utilizzato per accedere a un attributo o metodo. Il secondo argomento è sempre `None`."""
    PREPARSED = auto()
    """Valore speciale, indica qualcosa già parsato. Il secondo elemento è l'`ASTNode`."""
    PREPARSED_LIST = auto()
    """Valore speciale, indica qualcosa già parsato separato da virgole. Il secondo elemento è la lista di `ASTNode`."""


Token: TypeAlias = tuple[TokenID, Any, int]