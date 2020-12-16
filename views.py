#################################### APLICAÇÃO FLASK #####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import hashlib
from api_mercadopago import payment, pesquisa_pagamento_aprovado, pesquisa_pagamento_pendente, pesquisa_pagamento_recusado
from metodos import metodo_cadastrar_cliente , buscar_rifa, buscar_cpf
from models import Pessoa, Rifa_lote, n_rifa, exibe_rifa, exibe_nome
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


db = banco.cursor()

cadastrar_cliente_numero_rifa = metodo_cadastrar_cliente.cadastrar_cliente(db)

busca_n_rifa = buscar_rifa.busca_numero_rifa(db)
buscarcpfexibe = buscar_cpf.busca_lista_rifa(db)

data_atual = date.today()

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

####################################        VIEWS ADMINISTRADOR       ######################

@app.route('/')
def pagina_rifa():
    proxima = request.args.get('proxima')
    lista_nrifa = busca_n_rifa.listar()
    pesquisar_pagamento_mp_aprovado("e5bad9a1-e5ad-484c-bfea-ffa395a2b42e")
    pesquisar_pagamento_mp_pendente("e5bad9a1-e5ad-484c-bfea-ffa395a2b42e")
    pesquisar_pagamento_mp_recusado("e5bad9a1-e5ad-484c-bfea-ffa395a2b42e")
    return render_template('pagina_rifa.html', lista_rifa= lista_nrifa)


@app.route('/formulario', methods=['POST', 'GET'])
def formulario():
    proxima = request.args.get('proxima')
    return render_template('formulario.html')




@app.route('/consultar', methods=['POST', 'GET'])
def consultar():
    valida_cpf = request.form['validar_cpf_consulta']
    cpf_pessoa = buscarcpfexibe.buscar_por_id(request.form['validar_cpf_consulta'])
    if valida_cpf == "":
        flash('...')
        return redirect(url_for('pagina_rifa'))
    exibelista = buscarcpfexibe.listar(valida_cpf)
    exibenome = buscarcpfexibe.listar_nome(valida_cpf)
    if cpf_pessoa:
        print(cpf_pessoa, valida_cpf)
        return render_template('consultar.html', exibe_lista_rifa= exibelista, exibe_lista_nome = exibenome)
    flash('CPF nã encontrado !')
    return redirect(url_for('pagina_rifa'))

'''
@app.route('/consultar', methods=['POST', 'GET'])
def consultar():
    valida_cpf = request.form['validar_cpf_consulta']
    print(valida_cpf)
    exibelista = buscarcpfexibe.listar(valida_cpf)
    return render_template('consultar.html', exibe_lista_rifa= exibelista)
#################################### ^^^^^^^^^^^^^^^^^^ ####################################
'''
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
    id_pessoa = cadastrar_cliente_numero_rifa.ultima_posicao_id() + 1
    nome = request.form['nome_usuario']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    numero_endereco = request.form['numero_endereco']
    cep = request.form['cep']
    complemento = request.form['cidade']
    email = request.form['email']
    numero_telefone = request.form['telefone']
    numero_celular = request.form['celular']
    
   
    b=1
    numerolote_rifa = request.form['numero_rifa']
    n_rifa = cadastrar_cliente_numero_rifa.buscar_por_id(numerolote_rifa)

    p = Pessoa(id_pessoa,cpf, nome, endereco, numero_endereco, cep, complemento, email, numero_telefone, numero_celular)
    cadastropessoa = cadastrar_cliente_numero_rifa.cadastrar_pessoa_sistema(p)
    banco.commit()
    contador= int(request.form['contador'])


    dt_reserva = data_atual
    print(dt_reserva)
    
    status_rifa = 1



    v = """UPDATE rifa_lote SET id_pessoa = %s, data_reserva =%s, status_rifa = %s WHERE numero_rifa = %s"""
    db.execute(v,(id_pessoa, dt_reserva, status_rifa, numerolote_rifa,))
   
    contador-=1
    while int(contador) >= 1:
        v = """UPDATE rifa_lote SET id_pessoa = %s, data_reserva = %s, status_rifa=%s  WHERE numero_rifa = %s"""
        contador-=1
        numerolote_rifa2 = request.form['numero_rifa'+str(b)]
        db.execute(v,(id_pessoa, dt_reserva, status_rifa, numerolote_rifa2,))
        b+=1
            
        print(contador)
    
    banco.commit()
    return buy_product(2)








def buy_product(id_product):
    product = 2
    return redirect(payment(request, product=product))



def pesquisar_pagamento_mp_recusado(id_product):
    product = 'e5bad9a1-e5ad-484c-bfea-ffa395a2b42e'                
    return redirect(pesquisa_pagamento_recusado(request, product=product))


def pesquisar_pagamento_mp_aprovado(id_product):
    product = 'e5bad9a1-e5ad-484c-bfea-ffa395a2b42e'                
    return redirect(pesquisa_pagamento_aprovado(request, product=product))


def pesquisar_pagamento_mp_pendente(id_product):
    product = 'e5bad9a1-e5ad-484c-bfea-ffa395a2b42e'                
    return redirect(pesquisa_pagamento_pendente(request, product=product))
                
                
 

app.run(debug=True)


