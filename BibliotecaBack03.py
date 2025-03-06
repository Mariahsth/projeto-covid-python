def relatorios_cid(cidadaos):
    print("\n===RELATÓRIOS POR CIDADÃOS===\n")
    tam=len(cidadaos)
    if tam<1:
        print("Não há cidadãos cadastrados no sistema")
    else:
        qtd_cri=0
        qtd_ado=0
        qtd_adu=0
        qtd_ido=0
        qtd_f=0
        qtd_m=0
        qtd_x=0
        for cpfs in cidadaos:
            subdic=cidadaos.get(cpfs)
            for subchave in subdic:
                if subchave=="Faixa etária" and subdic.get(subchave)=="Criança":
                    qtd_cri=qtd_cri+1
                if subchave=="Faixa etária" and subdic.get(subchave)=="Adolescente":
                    qtd_ado=qtd_ado+1
                if subchave=="Faixa etária" and subdic.get(subchave)=="Adulto":
                    qtd_adu=qtd_adu+1
                if subchave=="Faixa etária" and subdic.get(subchave)=="Idoso":
                    qtd_ido=qtd_ido+1
                if subchave=="Sexo" and subdic.get(subchave)=="F":
                    qtd_f=qtd_f+1
                if subchave=="Sexo" and subdic.get(subchave)=="M":
                    qtd_m=qtd_m+1
                if subchave=="Sexo" and subdic.get(subchave)=="X":
                    qtd_x=qtd_x+1
        print("\nQuantidade de crianças cadastradas:", qtd_cri)
        print("Quantidade de adolescentes cadastrados:", qtd_ado)
        print("Quantidade de adultos cadastrados:", qtd_adu)
        print("Quantidade de idosos cadastrados:", qtd_ido)
        print("Quantidade de mulheres cadastradas:", qtd_f)
        print("Quantidade de homens cadastrados:", qtd_m)
        print("Quantidade de LGBTQIA+ cadastrades:", qtd_x)


def relatorios_cruzados(cidadaos, sintomas, diagnosticos):
    contsin={}
    contsex={}
    contfxe={}
    contfiltro={}
    print("\n===RELATÓRIOS CRUZADOS===\n")
    tam=len(cidadaos)
    tam2=len(sintomas)
    if tam<1 or tam2<1:
        print("Não há cidadãos cadastrados no sistema")
    else:
        for cpfs in cidadaos:
            subdic=cidadaos.get(cpfs)
            for subchave in subdic:
                if subchave=="Sexo":
                    contsex[subdic.get(subchave)]={}
                if subchave=="Faixa etária":
                    contfxe[subdic.get(subchave)]={}
        for cpfs in cidadaos:
            subdic=cidadaos.get(cpfs)
            for subchave in subdic:
                if subchave=="Sexo":
                    contsex[subdic.get(subchave)][cpfs]=subdic.get("Nome")
                if subchave=="Faixa etária":
                    contfxe[subdic.get(subchave)][cpfs]=subdic.get("Nome")
            #POR SEXO
        print("\n-------Relatórios analíticos--------\n")
        for chave4 in contsex:
            subdic4=contsex.get(chave4)
            print(f"\nFiltro: {chave4}")
            for subchave4 in subdic4:
                print(subchave4)
            #POR FAIXA ETÁRIA
        for chave6 in contfxe:
            subdic6=contfxe.get(chave6)
            print(f"\nFiltro: {chave6}")
            for subchave6 in subdic6:
                print(subchave6)
            #CRUZADO
        for chave1 in contsex:
            subdic1=contsex.get(chave1)
            for subchave1 in subdic1:
                for chave2 in contfxe:
                    subdic2=contfxe.get(chave2)
                    for subchave2 in subdic2:
                        if subchave1==subchave2:
                            contfiltro[chave1+"-"+chave2]={}
        for chave1 in contsex:
            subdic1=contsex.get(chave1)
            for subchave1 in subdic1:
                for chave2 in contfxe:
                    subdic2=contfxe.get(chave2)
                    for subchave2 in subdic2:
                        if subchave1==subchave2:
                            contfiltro[chave1+"-"+chave2][subchave1]="OK"
        for chave in contfiltro:
            subdic=contfiltro.get(chave)
            print(f"\nFiltro Cruzado: {chave}")
            for subchave in subdic:
                print(subchave)
        print("\n-------Relatórios sintéticos--------\n")
        for chave in contfiltro:
            subdic=contfiltro.get(chave)
            print(f"Filtro Cruzado: {chave} - Quantidade:", len(subdic))


def relatorios_diag(diagnosticos):
    print("\n===RELATÓRIOS POR DIAGNÓSTICOS===\n")
    tam=len(diagnosticos)
    if tam<1:
        print("Não há nenhum diagnóstico cadastrado no sistema")
    else:
        contsin={}
        for cpfs in diagnosticos:
            subdic = diagnosticos.get(cpfs)
            for subchave in subdic:
                contsin[subchave]={}
        for cpfs in diagnosticos:
            subdic=diagnosticos.get(cpfs)
            for subchave in subdic:
                if subdic.get(subchave) == "SIM":
                    contsin[subchave][cpfs]="SIM"
        print(contsin)
        for chave in contsin:
            subdic=contsin.get(chave)
            contador=len(subdic)
            print(f"{chave} - ", contador)


