from models import n_rifa

t = """SELECT numero_rifa FROM rifa_lote WHERE status_rifa = 1 or status_rifa = 2 """




class busca_numero_rifa:
    def __init__(self, db):
        self.__db = db

    def listar(self):
        cursor = self.__db
        cursor.execute(t)
        nrifa = traduz_usuario(cursor.fetchall())
        return nrifa



def traduz_usuario(lista_rifa):
    def cria_usuario_com_tupla(tupla):
        
        
        return n_rifa(tupla[0])
        
    return list(map(cria_usuario_com_tupla, lista_rifa))