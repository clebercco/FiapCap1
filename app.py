import json
import cx_Oracle

dsn = cx_Oracle.makedsn("localhost", 1521, service_name="fiap")
connection = cx_Oracle.connect(user="sys", password="123456", dsn=dsn)

# Lista global de insumos
lista_de_insumos = []

class Produto:
    def __init__(self, id, produto, areaplantio, sementes, produtividade, producao):
        self.id = id
        self.produto = produto
        self.areaplantio = areaplantio
        self.sementes = sementes
        self.produtividade = produtividade
        self.producao = producao

    def __str__(self):
        return (f"Produto(id={self.id}, produto='{self.produto}', "
                f"areaplantio={self.areaplantio}, sementes={self.sementes}, "
                f"produtividade={self.produtividade}, producao={self.producao})")

def inserir_oracle(id,produto,areaplantio):
    global lista_de_insumos
    
    novo_insumo = Produto(id, produto, areaplantio, 0, 0, 0)
    lista_de_insumos.append(novo_insumo)
    
    # Inserção de dados
    cursor = connection.cursor()
    sql_insert = "INSERT INTO Insumos (id, produto, areaplantio,sementes,produtividade,producao) VALUES (:1, :2, :3)"
    dados = (produto, areaplantio,0,0,0)
    cursor.execute(sql_insert, dados)

    connection.commit()
    cursor.close()
    connection.close()
    print("Dados inseridos com sucesso!")

def listar_insumos_oracle():
    cursor = connection.cursor()
    sql_select = "SELECT * FROM Insumos"
    cursor.execute(sql_select)

    lista_de_insumos.clear()

    for row in cursor:
        id, produto, areaplantio, sementes, produtividade, producao = row
        novo_insumo = Produto(id, produto, areaplantio, sementes, produtividade, producao)
        lista_de_insumos.append(novo_insumo)


    # Fecha a conexão
    cursor.close()
    connection.close()


def grava_json(id,produto,areaplantio):
    global lista_de_insumos
    
    novo_insumo = Produto(id, produto, areaplantio, 0, 0, 0)
    lista_de_insumos.append(novo_insumo)
    
    #"""Salva os dados em um arquivo JSON."""
    # Converter objetos Produto para dicionários
    insumos_dict = [vars(insumo) for insumo in lista_de_insumos]
    with open('producao_insumo.json', 'w') as arquivo:
        json.dump(insumos_dict, arquivo, indent=4)

def ler_json():
    """Lê os dados do arquivo JSON e os carrega na lista de insumos."""
    global lista_de_insumos
    try:
        with open('producao_insumo.json', 'r') as arquivo:
            insumos_dict = json.load(arquivo)
            lista_de_insumos = [Produto(**insumo) for insumo in insumos_dict]
    except FileNotFoundError:
        print("Arquivo JSON não encontrado. Inicializando lista de insumos.")
        #inicializar_insumos()

def inserir_insumo_json():
    """Insere um novo produto na lista e salva no arquivo JSON."""
    global lista_de_insumos
    produto = input("Nome da plantação: ")
    areaplantio = float(input("Área (hectares): "))
    novo_id = len(lista_de_insumos) + 1
    grava_json(novo_id,produto,areaplantio)
   
    print("Plantação inserida com sucesso!")
    
def inserir_insumo_oracle():
    """Insere um novo produto na lista e salva no arquivo JSON."""
    global lista_de_insumos
    produto = input("Nome da plantação: ")
    areaplantio = float(input("Área (hectares): "))
    novo_id = len(lista_de_insumos) + 1
    grava_json(novo_id,produto,areaplantio)
   
    print("Plantação inserida com sucesso!")

def listar_insumos():
    """Lista todos os insumos presentes na lista."""
    print("\nLista de Produtos:")
    for insumo in lista_de_insumos:
        print(insumo)

def exibir_nome_do_programa():
    print("""
    𝙁𝙖𝙧𝙢𝙏𝙚𝙘𝙝_𝘼𝙥𝙥
    """)

def exibir_menu_culturas():
    print("\nOpções de Culturas:")
    print("1. Inserir plantação")
    print("2. Listar Produtos")
    print("3. Inserir plantação Oracle")
    print("4. Listar Produtos Oracle")
    print("6. Sair do Programa")

def main():
    ler_json()
    exibir_nome_do_programa()
    while True:
        exibir_menu_culturas()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_insumo_json()
        elif opcao == "2":
            listar_insumos()
        elif opcao == "3":
            inserir_oracle()
        elif opcao == "4":
            listar_insumos_oracle()
        elif opcao == "6":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


