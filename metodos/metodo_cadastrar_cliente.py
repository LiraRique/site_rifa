from models import Pessoa, Rifa_lote


SQL_CADASTRAR_CLIENTE = 'INSERT INTO Pessoa(id_pessoa, cpf_pessoa, nome_pessoa, endereco, numero_endereco, cep, complemento, email, numero_telefone,numero_celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

SQL_ID_PESSOA = 'select max(id_pessoa) as id_pessoa from Pessoa'
SQL_NUMERO_RIFA_ID = """SELECT * from rifa_lote where numero_rifa = %s"""

class cadastrar_cliente:
    def __init__(self, db):
        self.__db = db


    def cadastrar_pessoa_sistema(self, Pessoa):
        cursor= self.__db
        cursor.execute(SQL_CADASTRAR_CLIENTE, (Pessoa.id_pessoa, Pessoa.cpf_pessoa, Pessoa.nome_pessoa, Pessoa.endereco, Pessoa.numero_endereco, Pessoa.cep, Pessoa.complemento, Pessoa.email, Pessoa.numero_telefone, Pessoa.numero_celular))
        
    

    def ultima_posicao_id(self):
        cursor = self.__db
        cursor.execute(SQL_ID_PESSOA)
        dados = cursor.fetchone()
        idpessoa = int(dados[0])
        return idpessoa

    def buscar_por_id(self, id):
        cursor = self.__db
        cursor.execute(SQL_NUMERO_RIFA_ID, (id,))
        dados = cursor.fetchone()
        n_rifa = traduz_nrifa(dados) if dados else None
        return n_rifa

   


def traduz_nrifa(tupla):
    return Rifa_lote(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])