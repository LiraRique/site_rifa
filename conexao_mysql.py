import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="rifa"
    )




mycursor = banco.cursor()


#mycursor.execute("DROP DATABASE rifa")

#mycursor.execute("CREATE DATABASE rifa")



'''
mycursor.execute("CREATE TABLE status_rifa(status TINYINT, descricao_status VARCHAR(50), CONSTRAINT statuspk PRIMARY KEY (status))")

mycursor.execute("INSERT INTO status_rifa(status, descricao_status) VALUE ('1', 'Reservado')")

mycursor.execute("INSERT INTO status_rifa(status, descricao_status) VALUE ('2', 'Confirmado')")
mycursor.execute("INSERT INTO status_rifa(status, descricao_status) VALUE ('3', 'Aberto')")
banco.commit()

mycursor.execute("CREATE TABLE Pessoa (id_pessoa BIGINT NOT NULL, cpf_pessoa VARCHAR(40), nome_pessoa VARCHAR(50), endereco VARCHAR(50),cep INT, complemento VARCHAR(20), email VARCHAR(50), numero_telefone VARCHAR(14), status_rifa TINYINT, CONSTRAINT id_pessoa PRIMARY KEY (id_pessoa), CONSTRAINT cpf_pessoa UNIQUE  (cpf_pessoa), CONSTRAINT id_pessoa_fk FOREIGN KEY (status_rifa) REFERENCES status_rifa(status))")


mycursor.execute("CREATE TABLE sorteio_rifa(id_rifa INT AUTO_INCREMENT, id_pessoa BIGINT NOT NULL, numero_rifa BIGINT, data_reserva DATE, data_compensacao DATE, CONSTRAINT id_rifa_pke PRIMARY KEY (id_rifa), CONSTRAINT id_pessoa_fke FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa), CONSTRAINT numero_rifa_unique UNIQUE (numero_rifa))")
'''
