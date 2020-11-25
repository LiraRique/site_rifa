from models import Pessoa, sorteio_rifa, status_rifa


SQL_CADASTRAR_CLIENTE = 'INSERT INTO Pessoa(id_pessoa, cpf_pessoa, nome_pessoa, endereco, cep, complemento, email, numero_telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

SQL_CADASTRAR_NUMERO_RIFA = 'INSERT INTO sorteio_rifa(id_pessoa, numero_rifa, status_rifa, data_reserva, data_compensacao) VALUES (?, ?, ?, ?, ?)'

SQL_ID_PESSOA = 'select max(id_pessoa) as id_pessoa from Pessoa'

class cadastrar_cliente:
    def __init__(self, db):
        self.__db = db


    def cadastrar_cliente_sistema(self, Pessoa):
        cursor= self.__db

        cursor.execute(SQL_CADASTRAR_CLIENTE, (Pessoa.id_pessoa, Pessoa.cpf_pessoa, Pessoa.nome_pessoa, Pessoa.endereco, Pessoa.cep, Pessoa.complemento, Pessoa.email, Pessoa.numero_telefone))
        #cursor.execute(SQL_CADASTRAR_NUMERO_RIFA, (sorteio_rifa.id_pessoa, sorteio_rifa.numero_rifa, sorteio_rifa.status_rifa, sorteio_rifa.data_reserva, sorteio_rifa.data_compensacao))
        
        

    def ultima_posicao_id(self):
        cursor = self.__db.execute(SQL_ID_PESSOA)
        dados = cursor.fetchone()
        idpessoa = int(dados[0])
        return idpessoa