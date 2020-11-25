import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="rifa"
    )




mycursor = banco.cursor()
'''
mycursor.execute("CREATE DATABASE rifa")


mycursor.execute("CREATE TABLE Pessoa (id_pessoa BIGINT NOT NULL, cpf_pessoa VARCHAR(40), nome_pessoa VARCHAR(50), endereco VARCHAR(50),cep INT, complemento VARCHAR(20), email VARCHAR(50), numero_telefone VARCHAR(14), CONSTRAINT id_pessoa PRIMARY KEY (id_pessoa), CONSTRAINT cpf_pessoa UNIQUE  (cpf_pessoa))")

mycursor.execute("CREATE TABLE sorteio_rifa(id_rifa INT AUTO_INCREMENT, id_pessoa BIGINT NOT NULL, numero_rifa BIGINT, status_rifa TINYINT, data_reserva DATE, data_compensacao DATE, CONSTRAINT id_rifa_pk PRIMARY KEY (id_rifa), CONSTRAINT id_pessoa_fk FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa), CONSTRAINT numero_rifa_unique UNIQUE (numero_rifa))")


mycursor.execute("CREATE TABLE status_rifa(id_rifa INT AUTO_INCREMENT, status TINYINT, descricao_status VARCHAR(50), CONSTRAINT id_rifa_fk FOREIGN KEY (id_rifa) REFERENCES sorteio_rifa(id_rifa))")
'''
mycursor.execute('INSERT INTO Pessoa(id_pessoa) VALUE (1)')
banco.commit()
