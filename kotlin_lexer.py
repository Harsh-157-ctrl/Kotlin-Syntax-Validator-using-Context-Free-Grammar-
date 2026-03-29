# kotlin_lexer.py
# -----------------------------------------
# Lexer for Kotlin subset (comments, vars, while, for, return)
# -----------------------------------------

import ply.lex as lex

# List of token names
tokens = (
    'VAR', 'VAL',
    'WHILE', 'FOR', 'IN', 'RETURN',
    'IDENT', 'NUMBER', 'STRING',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'COLON', 'SEMI', 'ASSIGN',
    'PLUS', 'MINUS', 'TIMES', 'DIV',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'COMMA'
)

# Reserved keywords
reserved = {
    'var': 'VAR',
    'val': 'VAL',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'return': 'RETURN'
}

# Simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_COLON   = r':'
t_SEMI    = r';'
t_ASSIGN  = r'='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV     = r'/'
t_LE      = r'<='
t_GE      = r'>='
t_LT      = r'<'
t_GT      = r'>'
t_EQ      = r'=='
t_NE      = r'!='
t_COMMA   = r','

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# ---------------- COMMENTS -----------------
def t_COMMENT_SINGLE(t):
    r'//.*'
    pass

def t_COMMENT_MULTI(t):
    r'/\*([^*]|\*+[^*/])*\*+/'
    pass

# ---------------- STRINGS & NUMBERS -----------------
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# ---------------- IDENTIFIERS -----------------
def t_IDENT(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
