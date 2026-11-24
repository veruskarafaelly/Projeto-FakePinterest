#criar as rotas do nosso site (links)
from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms

@app.route('/', methods=["GET", "POST"])
def homepage():
    formlogin = Formlogin()
    return render_template('homepage.html', formlogin=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    form = FormCriarConta()
    return render_template('criarconta.html', form=formcriarconta)

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)