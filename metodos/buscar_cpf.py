from models import exibe_rifa, Pessoa, exibe_nome


QUERY = 'SELECT a.nome_pessoa, a.cpf_pessoa, b.numero_rifa, c.descricao_status, b.data_compensacao '
QUERY+= 'FROM pessoa a '
QUERY+='INNER JOIN rifa_lote b ' 
QUERY+='ON a.id_pessoa= b.id_pessoa '
QUERY+='INNER JOIN status_rifa c ' 
QUERY+='ON b.status_rifa= c.status '
QUERY+= 'WHERE cpf_pessoa = %s '

SQL_NOME_CPF= 'SELECT nome_pessoa, cpf_pessoa from pessoa WHERE cpf_pessoa= %s '


class busca_lista_rifa:
    def __init__(self, db):
        self.__db = db

    def listar(self,id):
            cursor = self.__db
            cursor.execute(QUERY, (id,))
            rifa_lista = traduz_rifa(cursor.fetchall())
            return rifa_lista

    def listar_nome(self,id):
            cursor = self.__db
            cursor.execute(SQL_NOME_CPF, (id,))
            nome_cpf = traduz_nome_cpf(cursor.fetchall())
            return nome_cpf



    
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db
        cursor.execute(SQL_CPF_POR_ID, (id,))
        dados = cursor.fetchone()
        pessoa = traduz_login(dados) if dados else None
        return pessoa


def traduz_rifa(lista_rifa):
    def cria_usuario_com_tupla(tupla):
        
        
        return exibe_rifa(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
        
    return list(map(cria_usuario_com_tupla, lista_rifa))




def traduz_nome_cpf(lista_nome):
    def cria_nome_cpf_com_tupla(tupla):
        
        
        return exibe_nome(tupla[0], tupla[1])
        
    return list(map(cria_nome_cpf_com_tupla, lista_nome))








SQL_CPF_POR_ID = 'SELECT * from pessoa where cpf_pessoa = %s'







def traduz_login(tupla):
    return Pessoa(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9],  tupla[0])