from tokens import Token, TokenID
from astnodes import *
import errors
import localization as loc
from util import reversed_enumerate, split_when


class Parser:
    """
    Converte liste di `Token` in un albero di sintassi astratto rappresentato da un `ASTNode` radice.
    """


    OP_ORDER: tuple[tuple[TokenID, ...], ...] = (
        (TokenID.PLUS, TokenID.MINUS),
        (TokenID.TIMES, TokenID.DIV),
        (TokenID.UNARY_PLUS, TokenID.UNARY_MINUS),
    )
    """L'ordine delle varie operazioni, dalla meno prioritaria alla più prioritaria."""


    @classmethod
    def parse_literal(cls, tokens: tuple[Token, ...], src: str) -> ExpressionNode | None:
        if len(tokens) == 1 and tokens[0][0] in [TokenID.INT, TokenID.FLOAT]:
            return LiteralValue(tokens[0][1])
        return None


    @classmethod
    def get_first_parentheses(cls, tokens: tuple[Token, ...]) -> tuple[int, int] | tuple[None, None]:
        open_count = 0
        open_parenthesis_character_pos = None
        open_parenthesis_pos = None
        for i, x in enumerate(tokens):
            if x[0] != TokenID.PARENTHESIS:
                continue
            if not x[1]:
                # Parentesi aperta
                if open_count == 0:
                    open_parenthesis_pos = i
                    open_parenthesis_character_pos = x[2]
                open_count += 1
            else:
                # Parentesi chiusa
                if open_count <= 0:
                    raise errors.ClosedBracket(loc.ErrorDesc.closed_bracket, x[2])
                open_count -= 1
                if open_count == 0:
                    assert open_parenthesis_pos != None
                    return (open_parenthesis_pos, i)
        if open_count > 0:
            assert open_parenthesis_character_pos != None
            raise errors.UnclosedBracket(loc.ErrorDesc.unclosed_bracket, open_parenthesis_character_pos)
        return (None, None)


    @classmethod
    def parse_expression(cls, tokens: tuple[Token, ...], src: str) -> ExpressionNode:
        """
        `tokens` deve contenere almeno un elemento.
        """
        assert len(tokens) > 0
        # Singolo valore
        if len(tokens) == 1 and tokens[0][0] == TokenID.PREPARSED:
            return tokens[0][1]
        literal_maybe = cls.parse_literal(tokens, src)
        if literal_maybe != None:
            return literal_maybe
        # Parsing delle parentesi
        l_parenthesis_pos, r_parenthesis_pos = cls.get_first_parentheses(tokens)
        if l_parenthesis_pos != None and r_parenthesis_pos != None:
            part_before = tokens[:l_parenthesis_pos]
            part_after = tokens[r_parenthesis_pos + 1:]
            part_inside = tokens[l_parenthesis_pos + 1 : r_parenthesis_pos]
            if len(part_inside) == 0:
                raise errors.EmptyBracket(loc.ErrorDesc.empty_bracket, tokens[l_parenthesis_pos][2])
            inside_token: Token = (TokenID.PREPARSED, cls.parse_expression(part_inside, src), tokens[l_parenthesis_pos][2])
            return cls.parse_expression(part_before + (inside_token,) + part_after, src)
        # Parsing delle operazioni in ordine
        for opers in cls.OP_ORDER:
            # An operator § is right-associative if (x § y § z) = (x § (y § z))
            # Most operators are left-associative (x - y - z) = ((x - y) - z)
            # Unary operators must be set as right-associative or there'd be something on the left side
            is_left_associative = opers != (TokenID.UNARY_PLUS, TokenID.UNARY_MINUS)
            for i, token in reversed_enumerate(tokens) if is_left_associative else enumerate(tokens):
                if token[0] not in opers:
                    continue
                if token[0] in {TokenID.UNARY_PLUS, TokenID.UNARY_MINUS}:
                    assert i == 0
                    right_side = tokens[i + 1:]
                    if len(right_side) == 0:
                        raise errors.NoRightSideExpr(loc.ErrorDesc.no_right_side_expr.format(char=src[tokens[i][2]]), tokens[i][2])
                    right_expr = cls.parse_expression(right_side, src)
                    return UnaryOp(token[0], right_expr)
                else:
                    left_side = tokens[:i]
                    if len(left_side) == 0:
                        raise errors.NoLeftSideExpr(loc.ErrorDesc.no_left_side_expr.format(char=src[tokens[i][2]]), tokens[i][2])
                    right_side = tokens[i + 1:]
                    if len(right_side) == 0:
                        raise errors.NoRightSideExpr(loc.ErrorDesc.no_right_side_expr.format(char=src[tokens[i][2]]), tokens[i][2])
                    left_expr = cls.parse_expression(left_side, src)
                    right_expr = cls.parse_expression(right_side, src)
                    return BinaryOp(token[0], left_expr, right_expr)
        # TODO: Puoi arrivare qui con (1)(1)
        raise errors.ReallyMessedUp()


    @classmethod
    def parse(cls, tokens: tuple[Token, ...], src: str) -> ASTNode:
        answer = BasicBlock([])
        token_lines = split_when(tokens, lambda x : x[0] == TokenID.LINE_BREAK)
        for x in token_lines:
            if len(x) > 0:
                answer.expressions.append(cls.parse_expression(tuple(x), src))
        return answer


if __name__ == "__main__":
    from lexer import Lexer
    i = input("Inserire espressione -> ")
    print(Parser.parse(tuple(Lexer.tokenize(i)), i))