import pandas as pd

lojas = pd.read_excel(r'C:/CTP/checkpoint2/lojas.xlsx')
produtos = pd.read_excel(r'C:/CTP/checkpoint2/produtos.xlsx')

df_lojas = pd.DataFrame(data=lojas)
df_lojas = df_lojas.rename(columns={"Código da loja": "Cod_loja", "Nome da loja": "Nome_loja"})

df_produtos = pd.DataFrame(data=produtos)
df_produtos = df_produtos.rename(columns={"Código do produto": "Cod_prod", "Nome do produto": "Nome_Produto",
                                          "Código da loja": "Cod_loja", "preço": "preco_valor"})



def listar_lojas():
    print("------------------------------------------\n"
          "LOJAS CADASTRADAS\n"
          "__________________________________________")

    print(df_lojas.to_string(index=False))
    print("------------------------------------------\n")
    print("--------------------------------------------------------------------------------\n")

def listar_produtos():
    print("--------------------------------------------------------------------------------\n"
          "PRODUTOS CADASTRADOS\n"
          "________________________________________________________________________________")
    print(df_produtos.to_string(index=False))
    print("--------------------------------------------------------------------------------\n")


def produtos_loja():
    print("------------------------------------------\n"
          "Relatório Produto por Loja\n")

    for value in df_lojas.sort_values(by='Cod_loja').itertuples():
        codLoja = str(value.Cod_loja)
        nomeLoja = str(value.Nome_loja)
        print("-------------------------------------------------------------")
        print(codLoja + " - " + nomeLoja)
        pd.options.display.float_format = '{:,.2f}'.format
        df_produtos_filtro = df_produtos.loc[df_produtos['Cod_loja'] == int(value.Cod_loja)][['Nome_Produto', 'preco_valor']]
        df_produtos_filtro = df_produtos_filtro.sort_values(by='Nome_Produto')
        produtos = df_produtos_filtro.to_string(index=False, header=False)
        print(produtos)


    print("\n")
def produtos_nome_produto():
    print("------------------------------------------\n"
          "Relatório Produto por Nome do Produto\n")

    for value in df_produtos.sort_values(by='Nome_Produto').itertuples():
        nomeProd = str(value.Nome_Produto)
        precoProd = str(value.preco_valor)
        codLoja = str(value.Cod_loja)
        print("-------------------------------------------------------------")
        print(nomeProd + " - " + precoProd)
        pd.options.display.float_format = '{:,.2f}'.format
        df_lojas_filtro = df_lojas.loc[df_lojas['Cod_loja'] == int(value.Cod_loja)]['Nome_loja']
        produtos_loj = df_lojas_filtro.to_string(header=False, index=False)
        print(codLoja + " " + produtos_loj)

    print("\n")


def menu():

    escolha = ' '
    while (escolha != '5'):

        print('\n-----------------------------------\n'
              'MENU - LOJA E PRODUTOS:\n'
              '-----------------------------------\n'
              '1 - Listar Lojas\n'
              '2 - Listas Produtos\n'
              '3 - Relatório - Produtos por loja\n'
              '4 - Relatório - Produtos por nome do produto\n'
              '5 - Sair\n'
              '-----------------------------------')

        escolha = input("Digite uma opção: ")

        if (escolha == '1'):
            listar_lojas()

        elif (escolha == '2'):
            listar_produtos()

        elif (escolha == '3'):
            produtos_loja()

        elif (escolha == '4'):
            produtos_nome_produto()

menu()