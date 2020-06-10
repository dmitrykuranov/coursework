from CodeGenerator import CodeGen
from LexicalAnalyzer import Lexer
from SyntaxAnalyzer import Parser

with open("TestCode.txt") as file:
    text_input = file.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
new_tokens = lexer.lex(text_input)

token_stream = []
for i in new_tokens:
    token_stream.append(i)
    print(i)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parse = parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("CodeFin.ll")


