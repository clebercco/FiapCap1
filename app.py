insumos = [{"id": 1, "produto": "arroz", "areaplantio": 0, "sementes": 0, "produtividade": 0, "producao": 0 },
           {"id": 2, "produto": "feijao", "areaplantio": 0, "sementes": 0, "produtividade": 0, "producao": 0 }]

def exibir_nome_do_programa():
    print("""
    𝙁𝙖𝙧𝙢𝙏𝙚𝙘𝙝_𝘼𝙥𝙥
""")

def exibir_menu_culturas():
    print("\nOpções de Culturas:")
    print("1. Arroz")
    print("2. Feijão")
    print("3. Listar Produtos")  
    print("4. Cálculo do Manejo de Insumos")  
    print("5. Cálculo da Produtividade (Com Insumos)")  
    print("6. Sair do Programa")

def alterar_insumo(id):
    area_plantio = float(input("Digite a área do plantio em hectares: "))    
    densidade_sementes = 100    
    produtividade_media = 6.0  

    if id == 2:  
        densidade_sementes = 80  
        produtividade_media = 3.5  

    # Cálculo da quantidade de sementes necessária  
    quantidade_sementes = area_plantio * densidade_sementes  
    # Cálculo da produção estimada  
    producao_estimativa = area_plantio * produtividade_media

    for insumo in insumos:
        if id == insumo['id']:
            insumo['areaplantio'] = area_plantio     
            insumo['sementes'] = quantidade_sementes
            insumo['produtividade'] = produtividade_media
            insumo['producao'] = producao_estimativa

def listar_insumos():
    print("\nLista de Produtos:")
    for insumo in insumos:
        print(f"Produto: {insumo['produto']}, Área de plantio: {insumo['areaplantio']}, Sementes: {insumo['sementes']}, Produtividade: {insumo['produtividade']}, Produção: {insumo['producao']}")

def calcular_manejo_insumos():
    print("\nCálculo do Manejo de Insumos")
    print("Escolha a cultura:")
    print("1. Arroz")
    print("2. Feijão")
    
    opcao_cultura = input("Escolha uma opção: ")
    if opcao_cultura == "1":
        produto = "Arroz"
    elif opcao_cultura == "2":
        produto = "Feijão"
    else:
        print("Opção inválida!")
        return

    insumo = input(f"Digite o nome do insumo a ser aplicado no {produto} (ex: Fosfato, adubo): ")
    quantidade_por_hectare = float(input(f"Digite a quantidade de {insumo} por hectare (em L ou kg): "))
    
    area_plantio = float(input(f"Digite a área do plantio de {produto} em hectares: "))
    
    # Cálculo da quantidade total de insumo necessária
    quantidade_total_insumo = quantidade_por_hectare * area_plantio
    
    print(f"\nPara a cultura de {produto}, aplicando {insumo}:")
    print(f"Área do plantio: {area_plantio} hectares")
    print(f"Quantidade total de {insumo} necessária: {quantidade_total_insumo:.2f} L ou kg")

def calcular_produtividade():
    print("\nCálculo da Produtividade (Com Insumos)")

    print("Escolha a cultura:")
    print("1. Arroz")
    print("2. Feijão")
    
    opcao_cultura = input("Escolha uma opção: ")
    if opcao_cultura == "1":
        produto = "Arroz"
        produtividade_media = 6.0  
    elif opcao_cultura == "2":
        produto = "Feijão"
        produtividade_media = 3.5  
    else:
        print("Opção inválida!")
        return

    area_plantio = float(input(f"Digite a área do plantio de {produto} em hectares: "))
    
    # Aplicação de insumos
    aplicar_insumos = input("Deseja aplicar insumos nesta safra? (s/n): ")
    
    if aplicar_insumos.lower() == 's':
        quantidade_por_hectare = float(input("Digite a quantidade de insumo por hectare (em kg ou L): "))
        efetividade = float(input(f"Qual a efetividade do insumo (em % de aumento da produtividade)? "))
        
        
        aumento_produtividade = (efetividade / 100) * produtividade_media
        produtividade_com_insumos = produtividade_media + aumento_produtividade
        print(f"Produtividade estimada com os insumos: {produtividade_com_insumos:.2f} toneladas por hectare")

        
        producao_com_insumos = produtividade_com_insumos * area_plantio
        print(f"Estimativa de produção com insumos: {producao_com_insumos:.2f} toneladas")
    else:
        print("Sem aplicação de insumos, a produtividade permanece a mesma.")
    
def main():
    exibir_nome_do_programa()
    while True:
        exibir_menu_culturas()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
           alterar_insumo(1)
        elif opcao == "2":
            alterar_insumo(2)
        elif opcao == "3":
            listar_insumos()  
        elif opcao == "4":
            calcular_manejo_insumos() 
        elif opcao == "5":
            calcular_produtividade()  
        elif opcao == "6":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()