class CompilationError(Exception):
    """
    Un errore che avviene durante la compilazione.

    `args` è una tupla `(str, int)`:
    - `args[0]` spiega in modo leggibile qual è l'errore
    - `args[1]` è la posizione in caratteri dove c'è l'errore
    """


    def __init__(self, exp: str, pos: int):
        super().__init__(exp, pos)


class LexerError(CompilationError):
    """Errore durante la fase di tokenizzazione."""

class UnknownCharacter(LexerError):
    """Errore di carattere sconosciuto."""

class UnterminatedString(LexerError):
    """Errore di stringa non terminata."""

class UnclosedComment(LexerError):
    """Errore di commento non chiuso."""


class ParserError(CompilationError):
    """Errore durante la fase di parsing."""

class ExpectedLiteral(ParserError):
    """Errore di literal aspettato."""

class ClosedBracket(ParserError):
    """Errore di parentesi chiusa inaspettata."""

class UnclosedBracket(ParserError):
    """Errore di parentesi non chiusa."""

class EmptyBracket(ParserError):
    """Errore di parentesi vuota."""

class NoLeftSideExpr(ParserError):
    """Errore di nessun'espressione a sinistra di un simbolo."""

class NoRightSideExpr(ParserError):
    """Errore di nessun'espressione a destra di un simbolo."""

class ExtraComma(ParserError):
    """Errore di un comma di troppo (espressione vuota)."""

class NoReasonComma(ParserError):
    """Errore di una virgola in un posto in cui non dovrebbe stare."""

class ExpectedMember(ParserError):
    """Errore quando si aspettava il nome del membro dopo il punto."""

class NoMember(ParserError):
    """Errore quando non c'è il nome del membro dopo il punto."""

class DotWithoutExpr(ParserError):
    """Errore di punto senza espressione su cui accedere."""


class TranspilerError(CompilationError):
    """Errore durante la fase di transpiliazione (si dice?)."""

class UndefinedVariable(TranspilerError):
    """Errore di variabile non definita."""

class CannotAccessAttribute(TranspilerError):
    """Errore di membro non accessibile."""





class ReallyMessedUp(Exception):
    """Errore per qualcosa che è andato veramente storto."""