import lex

with open('codigo.py', 'r') as file:
    data = file.read()

lex.lexer.input(data)

while True:
    tok = lex.lexer.token()
    if not tok:
        break
    print(tok)
