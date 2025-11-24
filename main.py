import argparse
from localization import CommandArgs, CommandHelp
from lexer import Lexer
from parser import Parser
from transpiler import Transpiler


def main():
    parser = argparse.ArgumentParser(prog="foggiascript", description=CommandHelp.description)

    parser.add_argument("source", type=str, help=CommandHelp.help_source)
    parser.add_argument(*CommandArgs.output_file, type=str, help=CommandHelp.help_output, default=CommandArgs.output_default)

    args = parser.parse_args()

    source_str = ""
    with open(args.source) as input_file:
        source_str = input_file.read()
    tokens = Lexer.tokenize(source_str)
    ast = Parser.parse(tuple(tokens), source_str)
    output_str = Transpiler.transpile(ast)
    with open(args.output, "w") as output_file:
        output_file.write(output_str)


main()