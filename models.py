class Pessoa:
    def __init__(self, id_pessoa, cpf_pessoa, nome_pessoa, endereco, numero_endereco,  cep, complemento, email, numero_telefone, numero_celular):
        self.id_pessoa = id_pessoa
        self.cpf_pessoa = cpf_pessoa
        self.nome_pessoa = nome_pessoa
        self.endereco = endereco
        self.numero_endereco = numero_endereco
        self.cep = cep
        self.complemento = complemento
        self.email = email
        self.numero_telefone = numero_telefone
        self.numero_celular = numero_celular



class Rifa_lote:
    def __init__(self, valor_rifa, id_pessoa, data_reserva, data_compensacao, status_rifa, numero_rifa = None):
        self.valor_rifa = valor_rifa
        self.id_pessoa = id_pessoa
        self.data_reserva = data_reserva
        self.data_compensacao = data_compensacao
        self.status_rifa = status_rifa
        self.numero_rifa = numero_rifa

class n_rifa:
    def __init__(self, numero_rifa):
        self.numero_rifa = numero_rifa


class exibe_rifa:
    def __init__(self, nome_pessoa, cpf_pessoa, numero_rifa, status_rifa, data_compensacao):
        self.nome_pessoa = nome_pessoa
        self.cpf_pessoa = cpf_pessoa
        self.numero_rifa = numero_rifa
        self.status_rifa = status_rifa
        self.data_compensacao = data_compensacao

class exibe_nome:
    def __init__(self, nome_pessoa, cpf_pessoa):
        self.nome_pessoa = nome_pessoa
        self.cpf_pessoa = cpf_pessoa