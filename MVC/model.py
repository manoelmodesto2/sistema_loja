from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria


class Produto:
    def __init__(self, produto, valor, categoria):
        self.produto = produto
        self.valor = valor
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:
    def __init__(self, item_vendido: Produto, vendedor, comprador, quantidade_vendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.item_vendido = item_vendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade_vendida = quantidade_vendida
        self.data = data


class Fornecedor:
    def __init__(self, nome, cnpj, categoria, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.categoria = categoria
        self.telefone = telefone


class Pessoa:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, telefone, id_funcionario):
        super().__init__(nome, idade, cpf, endereco, telefone)
        self.id_funcionario = id_funcionario
