import re

from tokens import *
import errors
import localization as loc


class Lexer:
    """
    Converte stringhe in liste di token.

    Ogni token è rappresentato da una tupla (`TokenID`, `Any`, `int`) perché mi piace l'immutabilità.

    Per andare a vedere i significati di ogni token vai a vedere la classe `TokenID`.
    """

    
    RE_NUMBER = re.compile(r"(?P<int>[-+]?\d+)(?P<float>\.\d+|f)?")
    """
    Matcha un numero con un segno (esempio -0123.45).

    Può matchare sia un intero che un numero decimale (in quel caso il gruppo <float> matcha).

    Un numero intero seguito da "f" (esempio 25f) conta come decimale.
    """
    RE_NAME = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*")
    """
    Matcha un nome, ossia una qualsiasi sequenza di caratteri alfanumerici e/o underscore.

    Il primo carattere non può essere una cifra.
    """
    RE_STRING = re.compile(r"\"(|(?:\\\\)+|.*?[^\\](?:\\\\)+|.*?[^\\])\"")
    """
    Matcha una stringa rinchiusa tra due virgolette. Include l'escape delle virgolette e dello slash.
    """


    @staticmethod
    def number_match(s: str, pos: int) -> tuple[int | float, str] | tuple[None, None]:
        """
        Restituisce, se presente, l'intero o float che parte da `pos` nella stringa
        con la stringa che rappresenta il numero.
        """
        re_match = Lexer.RE_NUMBER.match(s, pos)
        if re_match == None:
            return (None, None)
        whole_number = re_match.group()
        float_part = re_match.group("float")
        int_part = re_match.group("int")
        if float_part == "f":
            return (float(int_part), whole_number)
        elif float_part:
            return (float(whole_number), whole_number)
        return (int(whole_number), whole_number)


    @staticmethod
    def token_follows_binary_op(token: Token | None) -> bool:
        if token == None:
            return False
        if token[0] in {TokenID.INT, TokenID.FLOAT, TokenID.PREPARSED, TokenID.NAME}:
            return True
        if token[0] == TokenID.PARENTHESIS and token[1] == CLOSED:
            return True
        return False


    @staticmethod
    def unescape_str(string: str) -> str:
        return (string
                .replace('\\"', '"')
                .replace("\\\\", "\\")
                )


    @staticmethod
    def get_multiline_comment_lenght(string: str, start: int) -> int:
        """Restituisce la lunghezza dell'intero commento multilinea partendo dopo il simbolo del commento multilinea `#[`"""
        bracket_count = 1
        current_pos = start
        while current_pos + 1 < len(string) and bracket_count > 0:
            if string[current_pos:current_pos + 2] == "#[":
                bracket_count += 1
                current_pos += 1
            if string[current_pos:current_pos + 2] == "]#":
                bracket_count -= 1
                current_pos += 1
            current_pos += 1
        if bracket_count > 0:
            raise errors.UnclosedComment(loc.ErrorDesc.unclosed_comment, start)
        return current_pos - start + 2


    @classmethod
    def tokenize(cls, s: str) -> list[Token]:
        """A partire dal testo di input `s`, restituisce una lista di token rappresentati come tuple."""
        current_pos: int = 0
        answer: list[Token] = []
        while current_pos < len(s):
            last_token = answer[-1] if len(answer) > 0 else None
            match s[current_pos]:
                case " ":
                    current_pos += 1
                case ";" | "\n":
                    answer.append((TokenID.LINE_BREAK, None, current_pos))
                    current_pos += 1
                case "+":
                    answer.append((TokenID.PLUS if cls.token_follows_binary_op(last_token) else TokenID.UNARY_PLUS, None, current_pos))
                    current_pos += 1
                case "-":
                    answer.append((TokenID.MINUS if cls.token_follows_binary_op(last_token) else TokenID.UNARY_MINUS, None, current_pos))
                    current_pos += 1
                case "*":
                    answer.append((TokenID.TIMES, None, current_pos))
                    current_pos += 1
                case "/":
                    answer.append((TokenID.DIV, None, current_pos))
                    current_pos += 1
                case "(":
                    if cls.token_follows_binary_op(last_token):
                        answer.append((TokenID.CALL_OP, None, current_pos))
                    answer.append((TokenID.PARENTHESIS, False, current_pos))
                    current_pos += 1
                case ")":
                    answer.append((TokenID.PARENTHESIS, True, current_pos))
                    current_pos += 1
                case ",":
                    answer.append((TokenID.COMMA, None, current_pos))
                    current_pos += 1
                case '"':
                    str_match = cls.RE_STRING.match(s, current_pos)
                    if str_match == None:
                        raise errors.UnterminatedString(loc.ErrorDesc.unterminated_comma, current_pos)
                    answer.append((TokenID.STRING, cls.unescape_str(str_match.group(1)), current_pos))
                    current_pos += len(str_match.group())
                case ".":
                    answer.append((TokenID.DOT, None, current_pos))
                    current_pos += 1
                case "#":
                    if current_pos + 1 < len(s) and s[current_pos + 1] == "[":
                        current_pos += cls.get_multiline_comment_lenght(s, current_pos + 2)
                        continue
                    while s[current_pos] != "\n":
                        current_pos += 1
                        if current_pos >= len(s):
                            break
                case char:
                    number_value, number_str = cls.number_match(s, current_pos)
                    if number_str != None:
                        answer.append((
                                TokenID.INT if isinstance(number_value, int)
                                else TokenID.FLOAT, number_value, current_pos
                        ))
                        current_pos += len(number_str)
                        continue
                    name_match = cls.RE_NAME.match(s, current_pos)
                    if name_match != None:
                        answer.append((TokenID.NAME, name_match.group(), current_pos))
                        current_pos += len(name_match.group())
                        continue
                    raise errors.UnknownCharacter(
                            loc.ErrorDesc.unknown_character.format(char=char), current_pos
                    )
        return answer


if __name__ == "__main__":
    print(Lexer.tokenize(input("Inserisci stringa da tokenizzare -> ").replace("\\n", "\n")))