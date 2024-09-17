from model import *


class CategoriaDAO:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria.categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))    
        
        lista_categoria = []     
        for i in cls.categoria:
            lista_categoria.append(Categoria(i))
        
        return lista_categoria


class VendaDAO:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.item_vendido.produto + ' ' + str(venda.item_vendido.valor) + ' ' + venda.item_vendido.categoria + ' ' + 
            venda.vendedor + ' ' + venda.comprador + ' ' + str(venda.quantidade_vendida) + ' ' + venda.data + '\n')
    
    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.vendas = arq.readlines()
        cls.vendas = list(map(lambda x: x.replace('\n', ' '), cls.vendas))
        cls.vendas = list(map(lambda x: x.split(), cls.vendas))
        
        lista_vendas = []
        for i in cls.vendas:
            lista_vendas.append(Venda(Produto(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
            
        return lista_vendas


class EstoqueDAO:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.produto + ' ' + str(produto.valor) + ' ' + produto.categoria + ' ' + str(quantidade) + '\n')
    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        cls.estoque = list(map(lambda x: x.replace('\n', ' '), cls.estoque))
        cls.estoque = list(map(lambda x: x.split(), cls.estoque))
        
        lista_estoque = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                lista_estoque.append(Estoque(Produto(i[0], i[1], i[2]), i[3]))
                
        return lista_estoque


class FornecedorDAO:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + ' ' + str(fornecedor.cnpj) + ' ' + fornecedor.categoria + ' ' + str(fornecedor.telefone) + '\n')
    
    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()
        cls.fornecedores = list(map(lambda x: x.replace('\n', ' '), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split(), cls.fornecedores))
        
        lista_fornecedor = []
        for i in cls.fornecedores:
            lista_fornecedor.append(Fornecedor(i[0], i[1], i[2], i[3]))
        
        return lista_fornecedor


class PessoaDAO:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoa.nome + ' ' + str(pessoa.idade) + ' ' + str(pessoa.cpf) + ' ' + pessoa.endereco + ' ' + str(pessoa.telefone) + '\n')
    
    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.pessoa = arq.readlines()
        cls.pessoa = list(map(lambda x: x.replace('\n', ' '), cls.pessoa))
        cls.pessoa = list(map(lambda x: x.split(), cls.pessoa))

        lista_cliente = []
        for i in cls.pessoa:
            lista_cliente.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        
        return lista_cliente


class FuncionarioDAO:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.nome + ' ' + str(funcionario.idade) + ' ' + str(funcionario.cpf) + ' ' + funcionario.endereco + ' ' + str(funcionario.telefone)  + ' ' + str(funcionario.id_funcionario) + '\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionario = arq.readlines()
        cls.funcionario = list(map(lambda x: x.replace('\n', ' '), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split(), cls.funcionario))
        
        lista_funcionario = []
        for i in cls.funcionario:
            lista_funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
            
        return lista_funcionario
        