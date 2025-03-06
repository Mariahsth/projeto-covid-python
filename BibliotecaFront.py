import random
from BibliotecaBack01 import cadastro_cidadao, cadastro_sintomas,cadastro_usuario, listar_cidadao, listar_usuarios, listar_sintomas, cadastro_saudacoes, listar_saudacoes, importa_arquivo
from BibliotecaBack02 import diagnostico
from BibliotecaBack03 import relatorios_cid, relatorios_diag, relatorios_cruzados

def gerasaudacoes(saudacoes):
    tam=len(saudacoes)
    x=random.randint(1, tam)
    for chave in saudacoes:
        if chave==x:
            print("\n", saudacoes.get(chave),"\n")

def verificausuario(login):
    for chave in login:
        if chave=="Login":
            codigo=login.get(chave)
            tam=len(codigo)
            if tam<=4:
                perfil="Administrador"
            if tam>=5:
                perfil="Gestor"
            return perfil

def login(usuarios, cidadaos):
    print("\n=========LOGIN=========\n")
    print("Digite seu código de login ou CPF:\n")
    codigo=input()
    for chave in usuarios:
        subdic=usuarios.get(chave)
        for subchave in subdic:
            if codigo==subdic.get(subchave):
                print("Digite sua senha:\n")
                senha=input()
                if senha==subdic.get("Senha"):
                    perf=subdic.get("Perfil")
                    return perf
                else:
                    print("\nSenha inválida...")
                    return 0
    tam_cidadaos=len(cidadaos)
    if tam_cidadaos>0:
        for chave2 in cidadaos:
            cid_id=str(chave2)
            if cid_id==codigo:
                perf="Cidadão"
                return perf
        print("Usuário ou cidadão não cadastrado")
        return 999
    else:
        print("Usuário ou cidadão não cadastrado")
        return 999


def menu(cidadaos, saudacoes, sintomas, diagnosticos, usuarios):
    tam = len(saudacoes)
    if tam < 1:
        print("\n=========SEJA BEM VINDO(A)=========\n")
    else:
        gerasaudacoes(saudacoes)
    print("\n=========ACESSO=========\n")
    print("Digite [1]Login ou [2]Sair")
    entrar=int(input())
    while entrar<1 or entrar>2:
        print("Opção inválida. Digite [1]Login ou [2]Sair")
        entrar = int(input())
    if entrar==2:
        print("Saindo do programa...")
        exit()
    else:
        y=88
        while y==88:
            x=0
            acesso=login(usuarios, cidadaos)
            if acesso=="Administrador":
                x=99
                while x==99:
                    print("\n\n------------------MENU ADMINISTRADOR--------------------\n\n")
                    print("\nEscolha uma opção: [1]Cadastrar, [2]Listar, [3]Diagnóstico, [4]Relatórios, [5]Voltar ao Login ou [6]Sair\n")
                    op=int(input())
                    while op<1 or op>6:
                        op = int(input("\nOpção inválida. [1]Cadastrar, [2]Listar, [3]Diagnóstico, [4]Relatórios, [5]Voltar ao Login ou [6]Sair\n"))
                    if op==6:
                        print("\nSaindo do programa...\n")
                        exit()
                    if op==1:
                        print("\nDeseja cadastrar [1]Cidadão, [2] Usuários, [3]Sintomas ou [4]Saudações?\n")
                        sub1=int(input())
                        while sub1<1 or sub1>4 :
                            print("Opção inválida! Deseja cadastrar [1]Cidadão, [2] Usuários, [3]Sintomas ou [4]Saudações? ")
                            sub1=int(input())
                        if sub1==1:
                            print("\nDeseja [1]Importar arquivo ou [2]Cadastrar manual?\n")
                            subsub=int(input())
                            while subsub!=1 and subsub!=2:
                                print("Opção inválida! Deseja [1]Importar arquivo ou [2]Cadastrar manual?")
                                subsub=int(input())
                            if subsub==1:
                                importa_arquivo(cidadaos)
                            if subsub==2:
                                cadastro_cidadao(cidadaos)
                        if sub1==2:
                            cadastro_usuario(usuarios)
                        if sub1==3:
                            cadastro_sintomas(sintomas)
                        if sub1==4:
                            cadastro_saudacoes(saudacoes)
                    if op==2:
                        print("\nDeseja listar [1]Listar Cidadões, [2]Listar usuários, [3]Listar Sintomas ou [4]Listar Saudações?\n")
                        sub2=int(input())
                        while sub2<1 or sub2>4:
                            print("Opção inválida! Deseja listar [1]Listar Cidadões, [2]Listar usuários, [3]Listar Sintomas ou [4]Listar Saudações\n")
                            sub2=int(input())
                        if sub2==1:
                            listar_cidadao(cidadaos)
                        if sub2==2:
                            listar_usuarios(usuarios)
                        if sub2==3:
                            listar_sintomas(sintomas)
                        if sub2==4:
                            listar_saudacoes(saudacoes)
                    if op==3:
                        diagnostico(cidadaos, sintomas, diagnosticos)
                    if op==4:
                        print("\nDeseja acessar os relatórios [1]Consolidado por Cidadãos, [2]Consolidado por Diagnósticos? ou [3]Filtro Cruzados?\n")
                        sub4 = int(input())
                        while sub4 < 1 or sub4 > 3:
                            print("Opção inválida! Deseja acessar os relatórios [1]Consolidado por Cidadãos, [2]Consolidado por Diagnósticos? ou [3]Filtro Cruzados?\n")
                            sub4 = int(input())
                        if sub4==1:
                            relatorios_cid(cidadaos)
                        if sub4==2:
                            relatorios_diag(diagnosticos)
                        if sub4==3:
                            relatorios_cruzados(cidadaos, sintomas, diagnosticos)
                    if op==5:
                        x=0


            if acesso=="Gestor":
                x = 99
                while x == 99:
                    print("\n\n------------------MENU GESTOR--------------------\n\n")
                    print("\nEscolha uma opção de relatório: [1]Consolidado por Cidadãos, [2]Consolidado por Diagnósticos?, [3]Filtro Cruzados?, [4]Voltar ao Login ou [5]Sair\n")
                    op=int(input())
                    while op<1 or op>5:
                        op = int(input("\nOpção inválida. Digite [1]Consolidado por Cidadãos, [2]Consolidado por Diagnósticos?, [3]Filtro Cruzados?, [4]Voltar ao Login ou [5]Sair\n"))
                    if op==5:
                        print("\nSaindo do programa...\n")
                        exit()
                    if op==1:
                        relatorios_cid(cidadaos)
                    if op==2:
                        relatorios_diag(diagnosticos)
                    if op==3:
                        relatorios_cruzados(cidadaos, sintomas, diagnosticos)
                    if op==4:
                        x=0
            if acesso=="Cidadão":
                x=99
                while x==99:
                    print("\n\n------------------MENU CIDADÃO--------------------\n\n")
                    print("\nEscolha uma opção: [1]Diagnóstico, [2]Voltar ao Login ou [3]Sair\n")
                    op = int(input())
                    while op < 1 or op > 3:
                        op = int(input("\nOpção inválida. Digite [1]Diagnóstico, [2]Voltar ao Login ou [3]Sair\n"))
                    if op == 3:
                        print("\nSaindo do programa...\n")
                        exit()
                    if op == 1:
                        diagnostico(cidadaos, sintomas, diagnosticos)
                    if op==2:
                        x=0


