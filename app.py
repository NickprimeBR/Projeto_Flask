from flask import Flask, render_template, request, redirect, flash
from dao.db_cofig import get_connection
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)

app = Flask(__name__)
app.secret_key = "uma_chave_muito_secreta_e_unica"


@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre_o_Sistema():
    return render_template('dashboard/sobre.html')

@app.route('/aluno')
def lista_aluno():

        dao = AlunoDAO()
        
        lista = dao.listar()
        return render_template('aluno/lista.html', lista=lista)


@app.route('/aluno/form') 
def form_aluno():
    
    return render_template('aluno/form.html',aluno=None)


@app.route('/aluno/salvar/', methods=['POST'])
def salvar_aluno(id=None):
        nome = request.form['nome'],
        idade = request.form['idade'],
        cidade = request.form['cidade']
        dao=AlunoDAO()
        result=dao.salvar(id, nome, idade, cidade)
        if result["status"] == "ok":
                flash("Aluno salvo com sucesso!", "success")
        else:
                flash(result["mensagem"], "danger")
        return redirect('/aluno')

 

@app.route('/professor')
def lista_professor():
    
        dao = ProfessorDAO()
                
        lista = dao.listar()
        return render_template('professor/lista.html', lista=lista)
    
@app.route('/turma')
def lista_turma():
    
        dao = TurmaDAO()
                        
        lista = dao.listar()
        return render_template('turma/lista.html', lista=lista)
    
@app.route('/curso')
def lista_curso():
    
        dao = CursoDAO()
                        
        lista = dao.listar()
        return render_template('curso/lista.html', lista=lista)
    


@app.route('/ajuda')
def ajuda():
    return 'Ajuda Sobre o Sistema!'


@app.route('/saudacao1/<nome>')
def saudacao1(nome):
      return render_template('saudacao/saudacao.html',valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
      nome= request.args.get('nome')
      return render_template('saudacao/saudacao.html',valor_recebido=nome)  


@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
                usuario = request.form['usuario']
                senha = request.form['senha']

                return f'''
                        <h1>Login realizado!</h1>
                        <p>Usuário: {usuario}</p>
                        <p>Senha: {senha}</p>
                '''


        return render_template('login.html')


@app.route('/desafio1/<nome>')
def desafio1(nome):
      return render_template('desafio1/desafio.html',valor_recebido=nome)

@app.route('/desafio', methods=['GET', 'POST'])
def loginDesafio():
        nome= request.form['nome']
        dataNasc= request.form['dataNasc']
        cpf= request.form['cpf']
        nomeMae= request.form['nomeMae']

        return render_template('/desafio1/dada.html', nome=nome, dataNasc=dataNasc, cpf=cpf, nomeMae=nomeMae )

@app.route('/formdesafio')
def formdesafio():
      return render_template('desafio1/desafio.html')
        






      

if __name__ == '__main__':
    app.run(debug=True)
