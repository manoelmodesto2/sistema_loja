from Controller import *
import os.path

def arquivos(*nomes):
    for i in nomes:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")
                
arquivos('categoria.txt', 'vendas.txt', 'estoque.txt', 'fornecedores.txt', 'clientes.txt', 'funcionarios.txt')

print('Seja Bem vindo')

while True:
    print('Selecione a função desejada abaixo.')

    print('1 - Cadastro')
    print('2 - Alteração')
    print('3 - Remoção')
    print('4 - Vender')
    print('5 - Relatórios')
    print('6 - Sair')

    funcao = int(input('Escolha: '))

    #CADASTRO
    if funcao == 1: 
        print('1 - Cadastro de Produto')
        print('2 - Cadastro de Categoria')
        print('3 - Cadastro de Fornecedor')
        print('4 - Cadastro de Funcionário')
        print('5 - Cadastro de Cliente')
        funcao = int(input('Escolha: '))
        
        #CADASTRO DE PRODUTO
        if funcao == 1:
            func = EstoqueController()
            
            produto = input('Informe o nome do produto: ')
            valor = input('Informe o valor em R$: ')
            categoria = input('Informe a categoria do produto: ')
            quantidade = int(input('Informe a quantidade em unidades: '))
            
            func.cadastrar_produto(produto, valor, categoria, quantidade)


        #CADASTRO DE CATEGORIA
        elif funcao == 2:
            func = CategoriaController()
            
            categoria = input('Informa o nome da categoria: ').strip()
            
            func.cadastrar_categoria(categoria)


        #CADASTRO DE FORNECEDOR
        elif funcao == 3:
            func = FornecedorController()

            nome = input('Informe o nome da Empresa: ')
            cnpj = int(input('Informe o CNPJ: '))
            categoria = input('Informe a categoria: ')
            telefone = int(input('Informe o Telefone: '))
            
            func.cadastrar_fornecedor(nome, cnpj, categoria, telefone)
            print('Fornecedor cadastrado com sucesso!')


        #CADASTRO DE FUNCIONÁRIO
        elif funcao == 4:
            func = FuncionarioController()

            nome = input('Informe o nome do funcionário: ')
            idade = int(input('Digite a idade do funcionário: '))
            cpf = int(input('Digite o CPF do funcionário: '))
            endereco = input('Informe seu endereço: ')
            telefone = int(input('Qual o número do telefone: '))
            id_funcionario = int(input('Defina um ID para o funcionário: '))
            
            func.cadastrar_funcionario(nome, idade, cpf, endereco, telefone, id_funcionario)
            

        #CADASTRO DE CLIENTE
        elif funcao == 5:
            func = ClienteController()

            nome = input('Informe o nome do cliente: ')
            idade = int(input('Digite a idade do cliente: '))
            cpf = input('Digite o CPF: ')
            endereco = input('Informe o endereço do cliente: ')
            telefone = int(input('Telefone: '))

            func.cadastrar_cliente(nome, idade, cpf, endereco, telefone)
        
        #ESCOLHA INCORRETA
        else:
            print('Opção incorreta, tente novamente!')
    
    #ALTERAÇÃO
    elif funcao == 2:
        print('1 - Alteração de Produto')
        print('2 - Alteração de Categoria')
        print('3 - Alteração de Fornecedor')
        print('4 - Alteração de Funcionário')
        print('5 - Alteração de Cliente')
        funcao = int(input('Escolha: '))

        #ALTERAÇÃO PRODUTO
        if funcao == 1:              
            func = EstoqueController()
            
            produto_ant = input('Digite o nome do produto que deseja alterar: ')
            produto_novo = input('Digite o nome do novo produto: ')
            preco_novo = float(input('Defina novamente o preço: '))
            categoria = input('Qual a categoria do produto: ')
            quantidade_novo = int(input('Defina novamente a quantidade: '))
            
            
            func.alterar_produto(produto_ant, produto_novo, preco_novo, categoria, quantidade_novo)
        
        #ALTERAÇÃO DE CATEGORIA        
        elif funcao == 2:
            func = CategoriaController()
            ant_cat = input('Qual a categoria que deseja alterar: ')
            nov_cat = input('Para qual categoria que deseja alterar: ')

            func.alterar_categoria(ant_cat, nov_cat)

        #ALTERAÇÃO DE FORNECEDOR
        elif funcao == 3:
            func = FornecedorController()
            ant_fornec = input('Deseja alterar informações de qual fornecedor: ')
            nov_fornec = input('Digite o novo nome do fornecedor: ')
            cnpj = input('CNPJ: ')
            categoria = input('Qual a categoria: ')
            telefone = input('Informe o telefone:')

            func.alterar_fornecedor(ant_fornec, nov_fornec, cnpj, categoria, telefone)

        #ALTERAÇÃO DE FUNCIONÁRIO
        elif funcao == 4:
            func = FuncionarioController()
            ant_cpf = input('Qual o CPF do funcionário que deseja realizar a alteração: ')
            nome = input('Novo nome: ')
            idade = int(input('Idade: '))
            novo_cpf = input('Novo CPF: ')
            endereco = input('Endereço: ')
            telefone = input('Telefone: ')
            id = input('Defina o novo ID: ')

            func.alterar_funcionario(ant_cpf, nome, idade, novo_cpf, endereco, telefone, id)

        #ALTERAÇÃO DE CLIENTE
        elif funcao == 5:
            func = ClienteController()
            ant_nome = input('Qual o nome do cliente que deseja realizar a alteração: ')
            nov_nome = input('Novo nome: ')
            idade = int(input('Idade: '))
            cpf = input('Novo CPF: ')
            endereco = input('Endereço: ')
            telefone = input('Telefone: ')

            func.alterar_cliente(ant_nome, nov_nome, idade, cpf, endereco, telefone)
        
        else:
            print('Opção incorreta, tente novamente')
            
    #REMOÇÃO
    elif funcao == 3:
        print('1 - Remoção de Produto')
        print('2 - Remoção de Categoria')
        print('3 - Remoção de Fornecedor')
        print('4 - Remoção de Funcionário')
        print('5 - Remoção de Cliente')
        funcao = int(input('Escolha: '))

        #REMOÇÃO DE PRODUTO
        if funcao == 1:
            func = EstoqueController()
            produto = input('Qual o nome do produto que deseja remover ? ')
            
            func.remover_produto(produto)
        
        #REMOÇÃO DE CATEGORIA
        elif funcao == 2:
            func = CategoriaController()
            categoria = input('Qual a categoria que deseja remover? ')

            func.deletar_categoria(categoria)
        
        #REMOÇÃO DE FORNECEDOR
        elif funcao == 3:
            func = FornecedorController()
            cnpj = input('Digite o CNPJ do fornecedor para removê-lo: ')

            func.remover_fornecedor(cnpj)
        
        #REMOÇÃO DE FUNCIONÁRIO
        elif funcao == 4:
            func = FuncionarioController()
            cpf = input('Digite o CPF do funcionário para removê-lo: ')

            func.deletar_funcionario(cpf)

        #REMOÇÃO DE CLIENTE
        elif funcao == 5:
            func = ClienteController()
            cpf = input('Digite o CPF do cliente para removê-lo: ')
            
            func.remover_cliente(cpf)
        
        else:
            print('Opção inválida, tente novamente!')
    
    #VENDA
    elif funcao == 4:
        print('1 - Cadastrar de venda')
        funcao = int(input('Escolha: '))

        if funcao == 1:
            func = VendaController()
            produto = input('Qual o nome do produto vendido? ')
            vendedor = input('Quem fez a venda? ')
            comprador = input('Quem comprou? ')
            quantidade = input('Quantidade vendida: ')
            
            func.cadastrar_venda(produto, vendedor, comprador, quantidade)
        else:
            print('Opção incorreta, tente novamente.')


    #RELATORIOS
    elif funcao == 5:
        print('1 - Relatório de vendas')
        print('2 - Relatório de venda por data')
        print('3 - Relatório de fornecedores cadastrados')
        print('4 - Relatório de funcionários cadastrados')
        print('5 - Relatório de clientes cadastrados')
        funcao = int(input('Escolha: '))

        #RELATORIO DE VENDAS
        if funcao == 1:
            func = VendaController()
            func.relatorio_vendas()
        
        #RELATORIO DE VENDAS POR DATA
        elif funcao == 2:
            func = VendaController()
            print('Formato de data: DD/MM/AAAA')
            i_data = input('Informe apartir de qual data: ')
            t_data = input('Informe o fim da data: ')
           
            func.mostrar_vendas(i_data, t_data)
        
        #RELATORIO DE FORNECEDORES CADASTRADOS
        elif funcao == 3:
            func = FornecedorController()
            func.mostrar_fornecedores()

        #RELATORIO DE FUNCIONÁRIOS CADASTRADOS
        elif funcao == 4:
            func = FuncionarioController()
            func.mostrar_funcionarios()
    
        #RELATORIO DE CLIENTES CADASTRADOS
        elif funcao == 5:
            func = ClienteController()
            func.mostrar_clientes()

        else: 
            print('Opção incorreta, tente novamente.')

    elif funcao == 6:
        break