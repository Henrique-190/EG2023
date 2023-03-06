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


def sequencia(sinal, lista):
    a = lista[0][1]
    lista = lista[1:]

    for t in lista:
        if (a > t[0] and sinal == "+") or (a < t[0] and sinal == "-"):
            return False
        a = t[1]
    return True

def intervalos(lista):
    comprimentos = []
    maisCurtoDif = None
    maisCurto = None
    maisLongoDif = None
    maisLongo = None

    for elem in lista:
        comprimento = abs(elem[0] - elem[1])
        comprimentos.append(comprimento)
        if maisCurtoDif == None or maisCurtoDif > comprimento:
            maisCurtoDif = comprimento
            maisCurto = elem
        if maisLongoDif == None or maisLongoDif < comprimento:
            maisLongoDif = comprimento
            maisLongo = elem

    return (comprimentos, maisCurto, maisLongo)




from ply import yacc
from lex import tokens

def p_start(p):
    '''start : MAIS intervalos
             | MENOS intervalos'''
    p[0] = p[1], p[2]
    if sequencia(p[1], p[2]):
        print("Número de intervalos: " + str(len(p[2])))
        comprimento, maisCurto, maisLongo = intervalos(p[2])
        print("Comprimento de cada intervalo: " + str(comprimento))
        print("Intervalo mais curto: " + str(maisCurto))
        print("Intervalo mais longo: " + str(maisLongo))
        print("Amplitude da sequência: " + str(abs(p[2][-1][1] - p[2][0][0])))
    else:
        print("Frase não válida")


def p_intervalos(p):
    '''intervalos : intervalo
                  | intervalo intervalos'''
    #Vai ser uma lista
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]
    

def p_intervalo(p):
    '''intervalo : '[' NUMERO ',' NUMERO ']' '''
    #Vai ser um tuplo
    p[0] = p[2], p[4]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
while True:
    try:
        s = input('input > ')
    except EOFError:
        break
    result = parser.parse(s)