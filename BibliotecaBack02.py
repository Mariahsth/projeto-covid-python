def diagnostico(cidadaos, sintomas, diagnosticos):
    cpf=input("\nDigite o CPF:")
    if cpf not in cidadaos:
        print("\nCPF não cadastrado no sistema\n")
    else:
        tam=len(sintomas)
        if tam<1:
            print("\nNão há sintomas cadastrados. Primeiro cadastre os sintomas no sistema\n")
        else:
            diagnosticos[cpf]={}
            print("\nCPF:", cpf)
            for chave in sintomas:
                print(sintomas.get(chave))
                resp=input()
                respupper=resp.upper()
                diagnosticos[cpf][sintomas.get(chave)]=respupper
            print(diagnosticos)