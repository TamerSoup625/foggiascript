from abc import ABC, abstractmethod
from tokens import TokenID
from dataclasses import dataclass
from errors import ReallyMessedUp


@dataclass
class ASTNode(ABC):
    """
    Classe astratta per rappresentare un nodo dell'albero di sinstassi astratto.
    """
    src_position: int


class ExpressionNode(ASTNode):
    """Una qualsiasi espressione che restituisce un valore e può eseguire funzioni."""

@dataclass
class LiteralValue(ExpressionNode):
    """Una costante scritta letteralmente."""
    value: int | float | str

@dataclass
class NamedVariable(ExpressionNode):
    """Una variabile o funzione con un certo nome."""
    name: str

@dataclass
class UnaryOp(ExpressionNode):
    """Un operatore unario applicato ad un'espressione."""
    operator: TokenID
    operand: ExpressionNode

@dataclass
class BinaryOp(ExpressionNode):
    """Un operatore binario applicato a due espressioni."""
    operator: TokenID
    l_operand: ExpressionNode
    r_operand: ExpressionNode

@dataclass
class FunctionCall(ExpressionNode):
    """Una chiamata a funzione"""
    function_node: ExpressionNode
    arguments: tuple[ExpressionNode, ...]


@dataclass
class BasicBlock(ASTNode):
    """Lista di espressioni molto semplice."""
    expressions: list[ExpressionNode]


@dataclass
class Block(ASTNode):
    """Una lista di espressioni chiamata in modo sequenziale."""
    expressions: list[ExpressionNode]