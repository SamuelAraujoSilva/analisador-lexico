import lex

with open('codigo.py', 'r') as file:
    data = file.read()

# Give the lexer some input
lex.lexer.input(data)

# Tokenize
while True:
    tok = lex.lexer.token()
    if not tok:
        break
    print(tok)
