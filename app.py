insumos = [{"id":1, "produto": "arroz", "areaplantio": 0, "sementes": 0, "produtividade": 0, "producao": 0 },
           {"id":2, "produto": "feijao", "areaplantio": 0, "sementes": 0, "produtividade": 0, "producao": 0 }]

def exibir_nome_do_programa():
    print("""
    𝙁𝙖𝙧𝙢𝙏𝙚𝙘𝙝_𝘼𝙥𝙥
""")

def exibir_menu_culturas():
    print("\nOpções de Culturas:")
    print("1. Arroz")
    print("2. Feijão")
    print("3. Listar Produtos")
    print("4. Sair do Programa")

def alterar_insumo(id):
    area_plantio = float(input("Digite a área do plantio em hectares: "))  # Área de plantio em hectares  
    densidade_sementes = 100  # Densidade de sementes por hectare  
    produtividade_media = 6.0  # Produtividade média de arroz em toneladas por hectare  
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
    print("""
    🇱​​​​​🇮​​​​​🇸​​​​​🇹​​​​​🇦​​​​​🇷​​​​​ 🇵​​​​​🇷​​​​​🇴​​​​​🇩​​​​​🇺​​​​​🇹​​​​​🇴​​​​​🇸​​​​​
        """)
    for insumo in insumos:
        print(f'{insumo}')

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
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()