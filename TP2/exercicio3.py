"""Exercício 3
Desenvolva uma GIC para definir uma linguagem que permita escrever listas mistas de números e palavras, de tal forma que as 3 frases abaixo sejam frases válidas dessa linguagem:

LISTA 1 .

Lista aaa .

Lista 1, 2, agora, 3, 4, fim, 7, 8.

Resolva as seguintes alíneas recorrendo ao uso de Transformer :

(a) Calcule, retorne e imprima quantos elementos existem numa lista.

(b) Identifique, retorne e imprima o elemento que mais se repete numa lista.

(c) Calcule, retorne e imprima a soma de todos os números que se encontrem entre as palavras agora e fim de uma lista.

(d) Verifique se uma lista é válida de acordo com os seguintes parâmetros :

Caso a palavra "agora" ocorra então a palavra "fim" também tem de aparecer posteriormente na lista e o contrário também.
Entre "agora" e "fim" tem de aparecer pelo menos um número.
[ ]
"""

from lark import Lark, Transformer
from lark import Lark
from lark.tree import pydot__tree_to_png
from lark import Transformer
from lark import Discard

class MyTransformer(Transformer):
    def __init__(self):
        self.sum = -1
        self.agora = 0
        self.erro = ""
        self.elems = {}

    def start(self, items):
        if self.erro != "":
            print(self.erro)
            return None
        elif self.agora > 0:
            print("Agora sem fim")
            return None
        elif self.agora < 0:
            print("Fim sem agora")
            return None

        output = {}
        output["soma"] = self.sum
        output["num_elementos"] = len(items)
        output["elemento_repetido"] = max(self.elems, key=self.elems.get)
        
        return output
    
    def elemento(self, items):
        return items[0]

    def WORD(self,word):
        if word == "agora":
            self.agora += 1
        elif word == "fim":
            if self.agora == 0:
                self.erro = "Fim sem agora"
            else:
                self.agora -= 1

            if self.sum == -1:
                self.erro = "Fim sem inteiro"
        
        if word in self.elems:
            self.elems[word] += 1
        else:
            self.elems[word] = 1
        return word

    def INT(self,numero):
        if self.agora > 0:
            if self.sum == -1:
                self.sum = 0
            self.sum += int(numero)
        
        if numero in self.elems:
            self.elems[numero] += 1
        else:
            self.elems[numero] = 1
        return int(numero)
    
    def LISTA(self,lista):
        return Discard
    
    pass

## Primeiro precisamos da GIC
grammar = '''
start:  LISTA elemento* "."
elemento :  INT ("," elemento)*
            | WORD ("," elemento)*
LISTA :  "Lista"
        | "LISTA"
INT : DIGIT+
VIR:","

%import common.WS
%import common.DIGIT
%import common.WORD
%ignore WS
'''

p = Lark(grammar)
parse_tree = p.parse("Lista 1, 2, agora, 2, 0, 0, 2, 3, 4, fim, 7, 8, 4.")
#parse_tree = p.parse("Lista agora, fim.")
#parse_tree = p.parse("Lista agora, aaa, fim.")
#parse_tree = p.parse("Lista agora, 1, fim.")
#parse_tree = p.parse("Lista agora, 1, 2, 3.")


data = MyTransformer().transform(parse_tree)
if data is not None:
    print(f"""-> O número de elementos é: {data["num_elementos"]}
-> O elemento que mais se repete é: {data["elemento_repetido"]}""")
    if data["soma"] == -1:
        print('-> Não existiram elementos "agora" e "fim" na lista')
    else:
        print(f'-> A soma dos números entre agora e fim é: {data["soma"]}')