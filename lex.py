import ply.lex as lex

reserved = {
    'and': 'AND',
    'as': 'AS',
    'assert': 'ASSERT',
    'break': 'BREAK',
    'class': 'CLASS',
    'continue': 'CONTINUE',
    'def': 'DEF',
    'del': 'DEL',
    'elif': 'ELIF',
    'else': 'ELSE',
    'except': 'EXCEPT',
    'finally': 'FINALLY',
    'False': 'FALSE',
    'for': 'FOR',
    'from': 'FROM',
    'global': 'GLOBAL',
    'if': 'IF',
    'import': 'IMPORT',
    'in': 'IN',
    'is': 'IS',
    'lambda': 'LAMBDA',
    'nonlocal': 'NONLOCAL',
    'None': 'NONE',
    'not': 'NOT',
    'or': 'OR',
    'pass': 'PASS',
    'print': 'PRINT',
    'raise': 'RAISE',
    'return': 'RETURN',
    'True': 'TRUE',
    'try': 'TRY',
    'with': 'WITH',
    'while': 'WHILE',
    'yield': 'YIELD',
    'self': 'SELF',
}

tokens = [
             'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'RCOLC', 'LCOLC', 'RBRACE',
             'LBRACE', 'COMMA', 'SEMICOLON', 'EXPLAMATION', 'COLON',
             'EQUALS', 'DIFF', 'MENOR', 'MAIOR', 'MENOREQUALS', 'MAIOREQUALS', 'SUMEQUALS', 'MINUSEQUALS',
             'TIMESEQUALS', 'DIVIDEEQUALS', 'MOD', 'EQUALSEQUALS', 'ASPASSIMPLES', 'ASPASDUPLA', 'NORMALSTRING', 'WHITESPACE'
         ] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_RCOLC = r'\]'
t_LCOLC = r'\['
t_RBRACE = r'\}'
t_LBRACE = r'\{'

t_COMMA = r','
t_SEMICOLON = r';'
t_EXPLAMATION = r'!'
t_COLON = r':'
t_EQUALS = r'='
t_EQUALSEQUALS = r'=='
t_DIFF = r'!='
t_MENOR = r'<'
t_MAIOR = r'>'
t_MENOREQUALS = r'<='
t_MAIOREQUALS = r'>='
t_SUMEQUALS = r'\+='
t_MINUSEQUALS = r'-='
t_TIMESEQUALS = r'\*='
t_DIVIDEEQUALS = r'/='
t_MOD = r'%='
t_ASPASSIMPLES = r'\''
t_ASPASDUPLA = r'\"'

# t_ignore = ' \t'

t_ignore_COMMENT = r'\#.*'


def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_NORMALSTRING(t):
    r"""(\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\')"""
    return t


def t_WHITESPACE(t):
    r"""[^\S\n\t]"""
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Caractere não existe '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
