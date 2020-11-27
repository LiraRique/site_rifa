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


class sorteio_rifa:
    def __init__(self, id_pessoa, numero_rifa, data_reserva, data_compensacao, id_rifa=None):
        self.id_rifa = id_rifa
        self.id_pessoa = id_pessoa
        self.numero_rifa = numero_rifa
        self.data_reserva = data_reserva
        self.data_compensacao = data_compensacao

        
class status_rifa:
    def __init__(self, status, descricao_status, id_rifa=None):
        self.id_rifa = id_rifa
        self.status = status
        self.descricao_status = descricao_status

class Rifa_lote:
    def __init__(self, id_pessoa, numero_rifa = None):
        self.id_pessoa = id_pessoa
        self.numero_rifa = numero_rifa