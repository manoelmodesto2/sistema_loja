from model import *
from DAO import *
from datetime import datetime

class CategoriaController:
    def cadastrar_categoria(self, categoria):
        existe_categoria = False
        x = CategoriaDAO.ler()
        for i in x:
            i.categoria
            if i.categoria == categoria:
                existe_categoria = True
        
        if not existe_categoria:        
            CategoriaDAO.salvar(Categoria(categoria))
            print('Categoria cadastrada com sucesso.')
        else:
            print('A categoria que deseja cadastrar já existe.')

    def deletar_categoria(self, delCategoria):
        categorias = CategoriaDAO.ler()

        verificar_categorias = list(filter(lambda x: x.categoria == delCategoria, categorias))

        if len(verificar_categorias) == 0:
            print('A categoria que você deseja remover não existe.')
        else:
            for i in range(len(categorias)):
                if categorias[i].categoria == delCategoria:
                    del categorias[i]
                    break
            print('Categoria Removida com sucesso.')

            with open('categoria.txt', 'w') as arq:
                for i in categorias:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        
        estoque = EstoqueDAO.ler()

        estoque = list(map(lambda x: Estoque(Produto(x.produto.produto, x.produto.valor, "Sem Categoria"), x.quantidade) if(x.produto.categoria == delCategoria) else(x), estoque))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.produto + ' ' + str(i.produto.valor) + ' ' + i.produto.categoria + ' ' + str(i.quantidade) + '\n')


    def alterar_categoria(self, antigaCategoria, categoriaAlterada):
        categorias = CategoriaDAO.ler()

        cat_filtrar = list(filter(lambda x: x.categoria == antigaCategoria, categorias))

        if len(cat_filtrar) > 0:
            
            filtrar_nova_cat = list(filter(lambda x: x.categoria == categoriaAlterada, categorias))
            
            if len(filtrar_nova_cat) == 0:
                categorias = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == antigaCategoria) else(x), categorias))
                print('A alteração foi bem sucedida.')

                estoque = EstoqueDAO.ler()

                estoque = list(map(lambda x: Estoque(Produto(x.produto.produto, x.produto.valor, categoriaAlterada), x.quantidade) if(x.produto.categoria == antigaCategoria) else(x), estoque))

                with open('estoque.txt', 'w') as arq:
                
                    for i in estoque:
                        arq.writelines(i.produto.produto + ' ' + str(i.produto.valor) + ' ' + i.produto.categoria + ' ' + str(i.quantidade) + '\n')
            
            else: 
                print('A categoria para qual você deseja alterar já existe.')
        
        else:
            print('A categoria que deseja alterar não existe')

        with open('categoria.txt', 'w') as arq:
            for i in categorias:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrar_categoria(self):
        categorias = CategoriaDAO.ler()
        if len(categorias) == 0:
            print('Não há categorias registradas ainda.')
        
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')


class EstoqueController:
    def cadastrar_produto(self, produto, valor, categoria, quantidade):
        x = CategoriaDAO.ler()
        y = EstoqueDAO.ler()    
        
        filtro_categoria = list(filter(lambda x: x.categoria == categoria, x))
        filtro_produto = list(filter(lambda x: x.produto.produto == produto, y))
        
        if len(filtro_categoria) > 0:
            if len(filtro_produto) == 0:
                EstoqueDAO.salvar(Produto(produto, valor, categoria), quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('O produto já está cadastrado no estoque')
        else:
            print('Categoria não existente, cadastre-a antes.')
    
    
    def remover_produto(self, delProduto):
        produtos = EstoqueDAO.ler()

        filtro_produtos = list(filter(lambda x: x.produto.produto == delProduto, produtos))

        if len(filtro_produtos) > 0:
            for i in range(len(produtos)):
                if produtos[i].produto.produto == delProduto:
                    del produtos[i]
                    print('Produto removido com sucesso.')
                    break
        else:
            print('Produto inexistente.')
        
        with open('estoque.txt', 'w') as arq:
            for i in produtos:
                arq.writelines(i.produto.produto + ' ' + str(i.produto.valor) + ' ' + i.produto.categoria + ' ' + str(i.quantidade) + '\n')



    def alterar_produto(self, oldProduto, newProduto, newValor, newCategoria, newQuantidade):
        x = CategoriaDAO.ler()
        y = EstoqueDAO.ler()

        filtro_categoria = list(filter(lambda x: x.categoria == newCategoria, x))
        filtro_produto = list(filter(lambda x: x.produto.produto == oldProduto, y))

        if len(filtro_categoria) > 0:
            
            if len(filtro_produto) > 0:
                
                filtro_novo_produto = list(filter(lambda x: x.produto.produto == newProduto, y))
                if len(filtro_novo_produto) == 0:
                    produto_novo = list(map(lambda x: (Estoque(Produto(newProduto, newValor, newCategoria), newQuantidade)) if(x.produto.produto == oldProduto) else(x), y))
                    print('Produto alterado com sucesso.')
                    
                    with open('estoque.txt', 'w') as arq:
                        for i in produto_novo:
                            arq.writelines(i.produto.produto + ' ' + str(i.produto.valor) + ' ' + i.produto.categoria + ' ' + str(i.quantidade))
                            arq.writelines('\n')
                
                else:
                    print('O produto para qual deseja alterar já existe.')
            
            else:
                print('O produto que deseja alterar não existe.')
        
        else: 
            print('Para alterar o produto é necessário informar uma categoria existente')



    def mostrar_produto(self):
        x = EstoqueDAO.ler()
        if len(x) > 0:
            for i in x:
                print(f'Produto: {i.produto.produto}\nValor: {i.produto.valor}\nCategoria: {i.produto.categoria}\nQuantidade: {i.quantidade}')
        
        else:
            print('Não há produtos cadastrados.')


class VendaController:
    def cadastrar_venda(self, nomeProduto, vendedor, comprador, quantidade_vendida):
        x = EstoqueDAO.ler()
        
        existe = False
        quant = False
        temp = []

        for i in x:
            if existe == False:
                if i.produto.produto == nomeProduto:
                    existe = True
                    if int(i.quantidade) >= int(quantidade_vendida):
                        quant = True
                        i.quantidade = int(i.quantidade) - int(quantidade_vendida)
                        
                        venda = Venda(Produto(i.produto.produto, i.produto.valor, i.produto.categoria), vendedor, comprador, quantidade_vendida)
                        valor_compra = int(i.produto.valor) * int(quantidade_vendida)

                        VendaDAO.salvar(venda)
        
        temp.append([Produto(i.produto.produto, i.produto.valor, i.produto.categoria), i.quantidade])
        
        arq = open('estoque.txt', 'w')
        arq.write('')

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].produto + ' ' + i[0].valor + ' ' + i[0].categoria + ' ' + str(i[1]))
                arq.writelines('\n')

        if existe == False:
            print('O produto não existe.')
            return None
        elif not quant:
            print('Não há quantidade suficiente do produto em estoque.')
            return None
        else:
            print(f'Venda realizada com sucesso, no valor total de R$ {valor_compra}!')
            return valor_compra


    def relatorio_vendas(self):
        vendas = VendaDAO.ler()
        produtos = []

        for i in vendas:
            nome = i.item_vendido.produto
            quantidade = i.quantidade_vendida

            quant = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(quant) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} if(x['produto'] == nome) else(x), produtos))
            else: 
                produtos.append({'produto': nome, 'quantidade': quantidade})
            
        ordenado = sorted(produtos, key = lambda k: k['quantidade'], reverse = True)
        
        print('Abaixo estão os produtos mais vendidos em ordem decrescente')
        print('===' * 5, 'PRODUTOS', '===' * 5)
        
        p = 1
        for i in ordenado:
            print('===' * 3, f'Produto {p}', '===' * 3)
            print(f'Produto: {i["produto"]}\nQuantidade: {i["quantidade"]}')
            print('-' * 20)
            p += 1

    def mostrar_vendas(self, iData, tData):
        vendas = VendaDAO.ler()
        data_inicio = datetime.strptime(iData, '%d/%m/%Y')
        data_fim = datetime.strptime(tData, '%d/%m/%Y')

        filtro_vendas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= data_inicio and datetime.strptime(x.data, '%d/%m/%Y') <= data_fim, vendas))

        cont = 1
        totalvenda = 0
        total = 0
        for i in filtro_vendas:
            print(f'==========Venda [{cont}]==========')
            print(f'Produto: {i.item_vendido.produto}\nCategoria: {i.item_vendido.categoria}\nData: {i.data}\nQuantidade: {i.quantidade_vendida}\nVendedor: {i.vendedor}\nComprador: {i.comprador}')
            
            totalvenda += int(i.quantidade_vendida) * int(float(i.item_vendido.valor))
            print(f'Valor total da Venda: R$ {totalvenda}')
            
            total += int(i.quantidade_vendida) * int(float(i.item_vendido.valor))
            totalvenda = 0
            cont += 1
        print('=====' * 8)
        print(f'Valor total das vendas: R$ {total}')


class FornecedorController:
    def cadastrar_fornecedor(self, nome, cnpj, categoria, telefone):
        x = FornecedorDAO.ler()

        filtro_cnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        filtro_telefone = list(filter(lambda x: x.telefone == telefone, x))

        if len(filtro_cnpj) > 0:
            print('CNPJ já cadastrado.')
       
        elif len(filtro_telefone) > 0:
            print('Telefone ja cadastrado.')
        
        else:
            if len(str(cnpj)) == 14 and len(str(telefone)) == 11:
                FornecedorDAO.salvar(Fornecedor(nome, cnpj, categoria, telefone))
            else:
                print('CNPJ ou Telefone inválidos.')
        
    def alterar_fornecedor(self, antFornecedor, novFornecedor, cnpj: str, categoria, telefone: str):
        x = FornecedorDAO.ler()

        if len(cnpj) == 14 and len(telefone) == 11:

            filtro_nome = list(filter(lambda x: x.nome == antFornecedor, x))
            
            if len(filtro_nome) > 0:
                filtro_cnpj = list(filter(lambda x: x.cnpj == cnpj, x))
                fornecedor = list(map(lambda x: Fornecedor(novFornecedor, cnpj, categoria, telefone) if(x.nome == antFornecedor) else(x), x))
                print('Fornecedor alterado com sucesso.')

                with open('fornecedores.txt', 'w') as arq:
                    for i in fornecedor:
                        arq.writelines(i.nome + ' ' + str(i.cnpj) + ' ' + i.categoria + ' ' + str(i.telefone))
                        arq.writelines('\n')

            else:
                print('Fornecedor não cadastrado e ou não encontrado.')

        else:
            print('CNPJ ou Telefone inválidos, tente novamente!')
    
    def remover_fornecedor(self, cnpj):
        x = FornecedorDAO.ler()

        filtro_cnpj = list(filter(lambda x: x.cnpj == cnpj, x))

        if len(filtro_cnpj) > 0:
            for i in range(len(x)):
                x[i].cnpj == cnpj
                del x[i]
                print('Fornecedor removido com sucesso.')
                break

        else:
            print('Fornecedor não encontrado.')

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + ' ' + str(i.cnpj) + ' ' + i.categoria + ' ' + str(i.telefone) + '\n')

    def mostrar_fornecedores(self):
        x = FornecedorDAO.ler()

        f = 1
        if len(x) > 0:
            for i in x:
                print('----' * 3, f'Fornecedor {f}', '----' * 3)
                print(f'Fornecedor: {i.nome}\n CNPJ: {i.cnpj}\n Categoria: {i.categoria}\n Telefone: {i.telefone}')
                print('-----' * 6)
                f += 1
        
        else:
            print('Não há fornecedores cadastrados.')


class ClienteController:
    def cadastrar_cliente(self, nome, idade, cpf, endereco, telefone):
        x = PessoaDAO.ler()

        filtro_cpf = list(filter(lambda x: x.cpf == cpf, x))
        filtro_telefone = list(filter(lambda x: x.telefone == telefone, x))

        if len(filtro_cpf) == 0:
            
            if len(filtro_telefone) == 0:
                PessoaDAO.salvar(Pessoa(nome, idade, cpf, endereco, telefone))
                print('Cliente cadastrado com sucesso.')
            else:
                print('Telefone já cadastrado por outro cliente')
        
        else:
            print('CPF já cadastrado.')
        
        
    def alterar_cliente(self, antNome, novNome, idade, cpf, endereco, telefone):
        x = PessoaDAO.ler()

        filtro_nome = list(filter(lambda x: x.nome == antNome, x))
        
        if len(cpf) == 11 and len(telefone) == 11:
            if len(filtro_nome) > 0:
                cliente = list(map(lambda x: Pessoa(novNome, idade, cpf, endereco, telefone) if(x.nome == antNome) else (x), x))
                print('Alteração realizada com sucesso.')

            else:
                print('Cliente não encontrado.')

            with open('clientes.txt', 'w') as arq:
                for i in cliente:
                    arq.writelines(i.nome + ' ' + str(i.idade) + ' ' + str(i.cpf) + ' ' + i.endereco + ' ' + str(i.telefone) + '\n')
        else:
            print('CPF ou Telefone inválidos, tente novamente!')
        
    def remover_cliente(self, cpf):
        x = PessoaDAO.ler()

        filter_cpf = list(filter(lambda x: x.cpf == cpf, x))
        
        if len(filter_cpf) > 0:
            for i in range(len(x)):
                if x[i].cpf == cpf:
                    del x[i]
                    print('Cliente removido com sucesso.')
                else:
                    print('Cliente não encontrado.')

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + ' ' + str(i.idade) + ' ' + str(i.cpf) + ' ' + i.endereco + ' ' + str(i.telefone) + '\n')

    def mostrar_clientes(self):
        x = PessoaDAO.ler()

        c = 1
        if len(x) > 0:
            for i in x:
                print('---' * 3, f'Cliente {c}', '---' * 3)
                print(f'Nome: {i.nome}\n Idade: {i.idade}\n CPF: {i.cpf}\n Endereço: {i.endereco}\n Telefone: {i.telefone}')
                print('------' * 5)
                c += 1
        else:
            print('Não há clientes cadastrados.')


class FuncionarioController:
    def cadastrar_funcionario(self, nome, idade, cpf, endereco, telefone, id):
        x = FuncionarioDAO.ler()

        
        filtro_cpf = list(filter(lambda x: x.cpf == cpf, x))

        if len(filtro_cpf) > 0:
            print('CPF já cadastrado por outra pessoa.')
        else:
            FuncionarioDAO.salvar(Funcionario(nome, idade, cpf, endereco, telefone, id))
            print('Funcionário cadastrado com sucesso.')

    def alterar_funcionario(self, antcpf, nome, idade, novocpf, endereco, telefone, id):
        x = FuncionarioDAO.ler()

        filtro_cpf = list(filter(lambda x: x.cpf == antcpf, x))
        
        if len(novocpf) == 11 and len(telefone) == 11:
            if len(filtro_cpf) > 0:
                funcionario = list(map(lambda x: Funcionario(nome, idade, novocpf, endereco, telefone, id) if(x.cpf == antcpf) else(x), x))
                print('Alteração realizada com sucesso.')
            
                with open('funcionarios.txt', 'w') as arq:
                    for i in funcionario:
                        arq.writelines(i.nome + ' ' + str(i.idade) + ' ' + str(i.cpf) + ' ' + i.endereco + ' ' + str(i.telefone)  + ' ' + str(i.id_funcionario) + '\n')

            else:
                print('Funcionário não encontrado.')
        
        else:
            print('CPF ou Telefone inválidos, tente novamente!')
    
    def deletar_funcionario(self, cpf):
        x = FuncionarioDAO.ler()

        filtro_cpf = list(filter(lambda x: x.cpf == cpf, x))

        if len(filtro_cpf) > 0:
            for i in range(len(x)):
                if x[i].cpf == cpf:
                    del x[i]
                    print('Funcionário removido com sucesso.')
                    break
        else:
            print('Funcionário não encontrado.')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + ' ' + str(i.idade) + ' ' + str(i.cpf) + ' ' + i.endereco + ' ' + str(i.telefone)  + ' ' + str(i.id_funcionario) + '\n')

    def mostrar_funcionarios(self):
        x = FuncionarioDAO.ler()

        f = 1
        if len(x) > 0:
            for i in x:
                print('---' * 3, f'Funcionário {f}', '---' * 3)
                print(f'Nome: {i.nome}\n Idade: {i.idade}\n CPF: {i.cpf}\n Endereço: {i.endereco}\n Telefone: {i.telefone}\n ID: {i.id_funcionario}')
                print('------' * 5)
                f += 1
        else:
            print('Não há funcionários cadastrados.')