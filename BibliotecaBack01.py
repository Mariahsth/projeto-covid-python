
def verifica_cpf(cpf):
    cpf_limpo = cpf.replace('.', '').replace('-', '')
    tam_cpf = len(cpf_limpo)
    while tam_cpf != 11:
        print("\nCPF inválido. Digite novamente")
        cpf = input("\nDigite seu CPF:\n")
        cpf_limpo = cpf.replace('.', '').replace('-', '')
        tam_cpf = len(cpf_limpo)
    return cpf

def importa_arquivo(cidadaos):
    print("\n Entrou no importa arquivo")
    arquivo=open("Base_Cidadaos.txt", "r")
    for linha in arquivo:
        dadoslinha=linha.split(",")
        for info in dadoslinha:
            sexo_corrigido=dadoslinha[3].replace("\n","")
            cidadaos[dadoslinha[0]]={}
            cidadaos[dadoslinha[0]]["Nome"]=dadoslinha[1]
            cidadaos[dadoslinha[0]]["Idade"] = int(dadoslinha[2])
            cidadaos[dadoslinha[0]]["Sexo"]=sexo_corrigido
            if int(dadoslinha[2])<13:
                cidadaos[dadoslinha[0]]["Faixa etária"] = "Criança"
            if int(dadoslinha[2])>12 and int(dadoslinha[2])<18:
                cidadaos[dadoslinha[0]]["Faixa etária"] = "Adolescente"
            if int(dadoslinha[2])>17 and int(dadoslinha[2])<60:
                cidadaos[dadoslinha[0]]["Faixa etária"] = "Adulto"
            if int(dadoslinha[2])>59:
                cidadaos[dadoslinha[0]]["Faixa etária"] = "Idoso"
    for cpf in cidadaos:
        subdic=cidadaos.get(cpf)
        print("CPF:", cpf, "-", subdic)
    arquivo.close()



def cadastro_cidadao(cidadaos):
    users = int(input("\nDigite o número de entrevistados: \n"))
    cont = 1
    while cont <= users:
        print("\n\nCadastro do usuário", cont)
        nome = input("\nDigite o nome do usuário:\n")
        idade = int(input("\nDigite a idade do usuário:\n"))
        sexo = input("\nDigite o sexo do usuário [F] ou [M] ou outro[X]:\n")
        cpf = input("\nDigite seu CPF:\n")
        #cpf=verifica_cpf(cpf)
        sexomax = sexo.upper()
        cidadaos[cpf]={}
        cidadaos[cpf]["Nome"]=nome
        cidadaos[cpf]["Sexo"] = sexomax
        cidadaos[cpf]["Idade"] = idade
        if idade <= 12:
            cidadaos[cpf]["Faixa etária"]= "Criança"
        if idade >12 and idade < 18:
            cidadaos[cpf]["Faixa etária"] = "Adolescente"
        if idade >= 18 and idade < 60:
            cidadaos[cpf]["Faixa etária"] = "Adulto"
        if idade > 60:
            cidadaos[cpf]["Faixa etária"] = "Idoso"
        cont += 1

def cadastro_usuario(usuarios):
    users=int(input("\nQuantos usuários deseja cadastrar?\n"))
    cont=1
    while cont<=users:
        usuarios[cont]={}
        nome=input("\nDigite o nome:\n")
        usuarios[cont]["Nome"]=nome
        login=input("Digite o login:\n")
        usuarios[cont]["Login"] = login
        senha=input("Digite a senha:\n")
        usuarios[cont]["Senha"] = senha
        perfilmin = input("Digite o perfil do usuário:[A]Administrador, [G]Gestor ou [C]Cidadão\n")
        perfil=perfilmin.upper()
        while perfil !="A" and perfil!="G":
            perfilmin = input("Opção inválida. Digite o perfil do usuário:[A]Administrador ou [G]Gestor\n")
            perfil=perfilmin.upper()
        if perfil=="A":
            usuarios[cont]["Perfil"] = "Administrador"
        if perfil == "G":
            usuarios[cont]["Perfil"] = "Gestor"
        if perfil == "C":
            usuarios[cont]["Perfil"] = "Cidadão"
        cont=cont+1
    #print(usuarios)



def cadastro_sintomas(sintomas):
    qtd_perguntas = int(input("\nDigite o número de Perguntas: \n"))
    cont2 = 1
    while cont2 <= qtd_perguntas:
        print(f"\nDigite a {cont2}a pergunta")
        pergunta = input()
        sintomas[cont2]=pergunta
        cont2 = cont2 + 1
    #print(sintomas)


def cadastro_saudacoes(saudacoes):
    qtd = int(input("\nEscolha quantas saudações deseja?\n"))
    cont = 1
    while cont <= qtd:
        print(f"Escreva a {cont}a saudação")
        saud = input()
        saudacoes[cont]=saud
        cont += 1
    #print(saudacoes)


def listar_cidadao(cidadaos):
    if not cidadaos:
        print("A lista está vazia. Primeiro faça o cadastro dos cidadões.")
    else:
        for cpfs in cidadaos:
            subdic = cidadaos.get(cpfs)
            print("CPF:", cpfs, "Dados do entrevistado:", subdic)

def listar_usuarios(usuarios):
    tam=len(usuarios)
    if tam<1:
        print("\nNão há usuários cadastrados\n")
    else:
        for chave in usuarios:
            subdic=usuarios.get(chave)
            print("Usuário -", chave, subdic)

def listar_sintomas(sintomas):
    if not sintomas:
        print("A lista está vazia. Primeiro faça o cadastro das perguntas de sintomas")
    else:
        print("Lista de perguntas de sintomas cadastradas:")
        cont=1
        for cont in sintomas:
            print("\n", cont, "-", sintomas.get(cont))
            cont+=1

def listar_saudacoes(saudacoes):
    if not saudacoes:
        print("A lista está vazia. Primeiro faça o cadastro das saudações")
    else:
        print("Lista de saudações cadastradas:")
        cont=1
        for cont in saudacoes:
            print("\n", cont, "-", saudacoes.get(cont))
            cont+=1