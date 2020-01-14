import pickle
import os

class Candidato:
    def __init__(self, cod_candidato, nome, cargo, regiao, num_votos):
        self.cod_candidato = cod_candidato
        self.nome = nome
        self.cargo = cargo
        self.regiao = regiao
        self.num_votos = num_votos


def gravar_candidatos(candidatos):
    try:
        arquivo = open('candidato.dat', 'wb')
        for candidato in candidatos:
            pickle.dump(candidato.cod_candidato, arquivo)
            pickle.dump(candidato.nome, arquivo)
            pickle.dump(candidato.cargo, arquivo)
            pickle.dump(candidato.regiao, arquivo)
            pickle.dump(candidato.num_votos, arquivo)

        arquivo.close()
        print('Banco de dados atualizado!')
    except:
        print('Ocorreu um erro ao gravar o arquivo')


def ler_candidatos():
    try:
        arquivo = open('candidato.dat', 'rb')
        while True:
            try:
                codigo = pickle.load(arquivo)
                nome = pickle.load(arquivo)
                cargo = pickle.load(arquivo)
                regiao = pickle.load(arquivo)
                votos = pickle.load(arquivo)
                candidato = Candidato(codigo, nome, cargo, regiao, votos)
                candidatos.append(candidato)
            except EOFError:
                break
        arquivo.close()
    except:
        print('Falha ao ler o arquivo')


def listar_candidatos():
    print('-- LISTA DE CANDIDATOS --')

    lista = []
    for candidato in candidatos:        
        if candidato.cod_candidato not in lista:
            lista.append(candidato.cod_candidato)
            print(candidato.cod_candidato, ' - ', candidato.nome)


def listar_votos_por_candidato():
    print('-- LISTA DE VOTOS POR CANDIDATO --')
    
    for candidato in candidatos:
        print(candidato.cod_candidato, candidato.nome, candidato.regiao, candidato.num_votos)    


def listar_total_votos_por_candidato():
    print('-- TOTAL DE VOTOS CANDIDATO --')
    votos = {}

    for candidato in candidatos:
        if candidato.cod_candidato not in votos:
            votos[candidato.cod_candidato] = { 'Nome' : candidato.nome, 'Votos' : int(candidato.num_votos)}
        else:
            votos[candidato.cod_candidato]['Votos'] += int(candidato.num_votos)
    
    for codigo, candidato in votos.items():
        print(codigo, candidato['Nome'], candidato['Votos'])

def listar_votos_por_regiao():
    print('-- LISTA DE VOTOS POR REGIAO --')
    votos = {}

    for candidato in candidatos:
        if candidato.regiao not in votos:
            votos[candidato.regiao] =  int(candidato.num_votos)
        else:
            votos[candidato.regiao] += int(candidato.num_votos)
    
    for regiao, votos in votos.items():
        print(regiao, votos)

def montar_menu():
    print('#------ M E N U ------#')
    print('1 - Adicionar candidato')
    print('2 - Listar todos os candidatos')
    print('3 - Listar votos por candidatos')
    print('4 - Listar total por candidatos')
    print('5 - Listar total por região')
    print('0 - Sair')
    escolha = input('O que deseja fazer: ')
    print()
    if escolha == '1':
        adicionar_candidato()
        gravar_candidatos(candidatos)
    elif escolha == '2':
        listar_candidatos()
    elif escolha == '3':
        listar_votos_por_candidato()
    elif escolha == '4':
        listar_total_votos_por_candidato()
    elif escolha == '5':
        listar_votos_por_regiao()
    elif escolha == '0':
        exit()
    else:
        print("Opção invalida! ") 
        return
    print()
    print()
    input('Pressione enter para continuar ...') 

def adicionar_candidato():
    codigo = input('Informe o código do candidato: ')
    nome = input('Informe o nome do candidato: ')
    cargo = input('Informe o cargo: ')
    regiao = input('Informe a região: ')
    num_votos = input('Informe o número de votos: ')
    candidatos.append(Candidato(codigo, nome, cargo, regiao, num_votos))

candidatos = list()

ler_candidatos()

while True:
    montar_menu()
