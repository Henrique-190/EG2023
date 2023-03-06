"""
1. Uma frase sintaticamente correta, só é considerada válida se satisfizer as seguintes condições de contexto:
- em cada intervalo o limite esquerdo tem de ser menos que o limite direito;
- os intervalos não se podem intercetar;
- a sequência de intervalos tem de ser crescente.
São exemplos de frases sintática e semanticamente corretas
  
  + [-4,-2][1,2][3,5][7,10][12,14][15,19]
  - [19,15][12,6][-1,-3]
  - [1000,200][30,12]
Exemplos de frases incorretas
+ [100,200][3,12]
2. Se a frase de entrada estiver correta, pretende-se saber:
- o número de intervalos;
- o comprimento de cada Intervalo (Lsup-Linf);
- o intervalo mais longo e o mais curto;
- a amplitude da sequência, considerando-a como a diferença (em valor absoluto) entre o limite superior do último intervalo e o limite inferior do 1º intervalo."""

from ply import lex

tokens = (
    'NUMERO',
    'MENOS',
    'MAIS'
)

literals = ['[', ']', ',']
t_MENOS = r'\-'
t_MAIS = r'\+'

def t_NUMERO(t):
    r'\-?\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore  = ' \t'


lexer = lex.lex()
"""
while True:
    try:
        s = input('input > ')
    except EOFError:
        break
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
"""