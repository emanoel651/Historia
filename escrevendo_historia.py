"""Armazenando arquivos em Json"""

"""JSON (JavaScript Object Notation) é um formato leve de troca de dados, fácil de ler e escrever"""


"""O módulo os em Python fornece funções para interagir com o sistema operacional"""

#Importando arquivo json
import json
# Importando modulo os 
import os
# Criando o caminho
CAMINHO = 'exemplo.json' 

# Usando modulo os, podemos pegar o caminho absoluto inicial até o arquivo
CAMINHO_OS = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        CAMINHO
    )
)


# Criando a classe pai Pessoa
# Nessa classe, será passado os atributos que deverar ter em todas as outras classes
class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: str):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    
# Classe filho Aluno. Recebe da classe pai Pessoas os atributos
class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, matricula:int, hist):
        super().__init__(nome, idade, sexo)
        self._matriculas = matricula
        self.hist = hist
    
    """Fazendo o get e o setter no modo paytonico. Assim
    pode alterar o valor conforme o necessario"""
    @property
    def matricula(self):
        return self._matriculas
    
    @matricula.setter
    def matricula(self, valor):
        self._matriculas = valor
    

    # Utlizando str, pois a classe tem que passar um texto de apresentação
    def __str__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}: Olá, meu nome é {self.nome}, tenho {self.idade}, e sou {self.sexo}, minha matricula é {self._matriculas}. Qual sua historia {self.hist}'
    
    # Colocando a classe em dicionario
    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "sexo": self.sexo,
            "matricula": self.matricula,
            "Gostos": self.hist
        }

# Criando a função que salva os dados
def anotar(valor1):
    with open(CAMINHO_OS, 'a') as arquivo:  # Use 'a' for append mode
        json_line = json.dumps(valor1.to_dict(), ensure_ascii=False, indent=2)
        arquivo.write(json_line + '\n')






nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo: ')
matricula = int(input('Digite sua matricula: '))
historia = input('Digite sua historia: ')





aluna1 = Aluno(nome, idade, sexo, matricula, historia)
aluna1.matricula = 8290
anotar(aluna1)

print(aluna1)


