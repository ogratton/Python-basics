import ast

expr="""
def foo():
   print("hello world")
"""

#p=ast.parse(expr)

#p.body[0].body = [ ast.parse("return 42").body[0] ] # Replace function body with "return 42"

p=ast.compile(expr)
