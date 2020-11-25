#################################### APLICAÇÃO FLASK #####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import hashlib
from models import Pessoa, sorteio_rifa, status_rifa
from metodos import metodo_cadastrar_cliente

import mysql.connector

from datetime import date, datetime


app = Flask(__name__)
app.secret_key = 'alura'
#################################### ^^^^^^^^^^^^^^^^^^ ####################################


#################################### CONEXÃO SQL SERVER ####################################

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="rifa"
    )
    
db = banco.cursor()

cadastrar_cliente_numero_rifa = metodo_cadastrar_cliente.cadastrar_cliente(db)

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

####################################        VIEWS ADMINISTRADOR       ######################

@app.route('/')
def pagina_rifa():
    proxima = request.args.get('proxima')
    return render_template('pagina_rifa.html')


@app.route('/formulario')
def formulario():
    proxima = request.args.get('proxima')
    return render_template('formulario.html')


#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### AUTENTICAÇÃO ##########################################
'''
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = login_usuario.buscar_por_id(request.form['email_usuario'])
    password = request.form['senha_usuario']
    password_app = hashlib.md5(password.encode())
    senha_aplicacao = password_app.hexdigest()
    if usuario:
        if usuario.senha_aplicacao == senha_aplicacao:
                session['usuario_logado'] = usuario.email_usuario
                flash('Administrador(a)  ' + usuario.nome_usuario + ' logado!')
                proxima_pagina = url_for('deash_usuario')
                return redirect(proxima_pagina)
        else:
            flash('Senha invalida, tente denovo!')
            return redirect(url_for('login'))
    else:
        flash('Usuario não encontrado!')
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Deslogado com sucesso!')
    return redirect(url_for('login'))



'''
#################################### ^^^^^^^^^^^^^^^^^^ ####################################



@app.route('/cadastrar_cliente', methods= ['POST',])
def cadastrar_cliente():
    id_pessoa = 3
    nome = request.form['nome_usuario']
    cpf = 15455455
    endereco = 'teste'
    cep = 11111111
    complemento = 'casa'
    email = 'lira.apren@gmail.com'
    numero_telefone = 1111111

    numero_rifa = 3
    status_rifa = 0
    data_reserva = 20/10/2020
    data_compensacao = 21/10/2020

    p = Pessoa(id_pessoa,cpf, nome, endereco, cep, complemento, email, numero_telefone)
    s = sorteio_rifa(id_pessoa, numero_rifa, status_rifa, data_reserva, data_compensacao)

    cadastro = cadastrar_cliente_numero_rifa.cadastrar_cliente_sistema(p)

    banco.commit()

   
    return redirect(url_for('pagina_rifa'))


app.run(debug=True)