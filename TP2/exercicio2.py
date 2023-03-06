"""
####Exercício 2
Retome uma das GIC escrita em extended-BNF para definir uma linguagem que permita escrever uma lista possívelmente vazia de números inteiros separados por vírgulas,
mas agora use o respetivo Transformer e escreva funções para visitar os nodos da árvore de parsing e escrever o conteúdo de cada uma.
"""

from lark import Lark
from lark.tree import pydot__tree_to_png
from lark import Transformer
from lark import Discard

class MyTransformer(Transformer):
    def __init__(self):
        self.sum = 0
        self.elems = []

    def start(self, items):
        print("raiz")
        return [self.sum, self.elems]

    def elemento(self, elemento):
        pass

    def VIR(self,op):
        print(str(op))

    def NUMERO(self,numero):
        self.sum += int(numero)
        self.elems.append(int(numero))
        return numero

    def PE(self,pe):
        print(str(pe))

    def PD(self,pd):
        print(str(pd))

## Primeiro precisamos da GIC
grammar = '''
start: PE elemento* PD
elemento : primeiro resto 
primeiro : NUMERO
resto : (VIR NUMERO)*
NUMERO:"0".."9"+
PE:"["
PD:"]"
VIR:","

%import common.WS
%ignore WS
'''

frase = "[1,2,3]"
p = Lark(grammar)

parse_tree = p.parse(frase)
print(parse_tree.pretty())

data = MyTransformer().transform(parse_tree)

print("\n\nSomatório: " + str(data[0]))
print("Elementos: " + str(data[1]))