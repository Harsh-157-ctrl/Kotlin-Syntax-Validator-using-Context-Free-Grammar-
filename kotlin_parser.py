# kotlin_parser.py
# -----------------------------------------
# Parser for Kotlin subset using PLY YACC
# -----------------------------------------

import ply.yacc as yacc
from kotlin_lexer import tokens, lexer

# Operator precedence
precedence = (
    ('left', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
)

# --------- GRAMMAR RULES ---------

def p_program(p):
    '''program : stmt_list'''
    p[0] = ('program', p[1])

def p_stmt_list(p):
    '''stmt_list : stmt_list stmt
                 | empty'''
    if len(p) == 3:
        if p[1] is None:
            p[0] = [p[2]]
        else:
            p[1].append(p[2])
            p[0] = p[1]
    else:
        p[0] = []

def p_stmt(p):
    '''stmt : var_decl
            | while_stmt
            | for_stmt
            | return_stmt
            | block_stmt'''
    p[0] = p[1]

# ---------- Variable declaration ----------
def p_var_decl(p):
    '''var_decl : VAR IDENT opt_type opt_init opt_semi
                | VAL IDENT opt_type opt_init opt_semi'''
    p[0] = ('var_decl', p[1], p[2], p[3], p[4])

def p_opt_type(p):
    '''opt_type : COLON IDENT
                | empty'''
    p[0] = p[2] if len(p) == 3 else None

def p_opt_init(p):
    '''opt_init : ASSIGN expr
                | empty'''
    p[0] = p[2] if len(p) == 3 else None

def p_opt_semi(p):
    '''opt_semi : SEMI
                | empty'''
    pass

# ---------- Return statement ----------
def p_return_stmt(p):
    '''return_stmt : RETURN opt_expr opt_semi'''
    p[0] = ('return', p[2])

def p_opt_expr(p):
    '''opt_expr : expr
                | empty'''
    p[0] = p[1] if len(p) == 2 and p[1] is not None else None

# ---------- While loop ----------
def p_while_stmt(p):
    '''while_stmt : WHILE LPAREN expr RPAREN block_stmt'''
    p[0] = ('while', p[3], p[5])

# ---------- For loop ----------
def p_for_stmt(p):
    '''for_stmt : FOR LPAREN IDENT IN expr RPAREN block_stmt'''
    p[0] = ('for_in', p[3], p[5], p[7])

# ---------- Blocks and Statements ----------
def p_block_stmt(p):
    '''block_stmt : LBRACE stmt_list RBRACE
                  | stmt_single'''
    p[0] = ('block', p[2]) if len(p) == 4 else p[1]

def p_stmt_single(p):
    '''stmt_single : var_decl
                   | return_stmt
                   | expr_stmt'''
    p[0] = p[1]

def p_expr_stmt(p):
    '''expr_stmt : expr opt_semi'''
    p[0] = ('expr_stmt', p[1])

# ---------- Expressions ----------
def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIV expr
            | expr LT expr
            | expr GT expr
            | expr LE expr
            | expr GE expr
            | expr EQ expr
            | expr NE expr'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_expr_number(p):
    'expr : NUMBER'
    p[0] = ('number', p[1])

def p_expr_string(p):
    'expr : STRING'
    p[0] = ('string', p[1])

def p_expr_ident(p):
    'expr : IDENT'
    p[0] = ('ident', p[1])

# ---------- Empty ----------
def p_empty(p):
    'empty :'
    pass

# ---------- Error ----------
def p_error(p):
    if p:
        print(f"❌ Syntax Error: Unexpected token '{p.value}' (type {p.type}) at line {p.lineno}")
    else:
        print("❌ Syntax Error: Unexpected end of file")

# ---------- Build parser ----------
parser = yacc.yacc()

# ---------- Helper function ----------
def validate_code(source):
    try:
        result = parser.parse(source, lexer=lexer)
        return True, result
    except Exception as e:
        return False, str(e)
