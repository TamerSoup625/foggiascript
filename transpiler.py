from tokens import TokenID
from astnodes import *
import localization as loc
from errors import ReallyMessedUp


class Transpiler:
    """
    Converte un albero di sintassi astratto `ASTNode` in codice JavaScript.
    """


    @classmethod
    def transpile_generic(cls, node: ASTNode) -> str:
        if isinstance(node, LiteralValue):
            return str(node.value)
        elif isinstance(node, UnaryOp):
            operator = {TokenID.UNARY_PLUS: "+", TokenID.UNARY_MINUS: "-"}[node.operator]
            return f"({operator}{cls.transpile_generic(node.operand)})"
        elif isinstance(node, BinaryOp):
            operator = {
                TokenID.PLUS: "+",
                TokenID.MINUS: "-",
                TokenID.TIMES: "*",
                TokenID.DIV: "/",
            }[node.operator]
            return f"({cls.transpile_generic(node.l_operand)}{operator}{cls.transpile_generic(node.r_operand)})"
        elif isinstance(node, BasicBlock):
            return "".join(f"console.log({cls.transpile_generic(x)});" for x in node.expressions)
        raise ReallyMessedUp()


    @classmethod
    def transpile(cls, root: ASTNode) -> str:
        return f"// {loc.Misc.code_marker}\n{cls.transpile_generic(root)}"


if __name__ == "__main__":
    from lexer import Lexer
    from parser import Parser
    i = input("Inserire espressione -> ")
    print(Transpiler.transpile(Parser.parse(tuple(Lexer.tokenize(i)), i)))