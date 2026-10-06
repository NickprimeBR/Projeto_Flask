from flask import Flask, render_template
from dao.db_cofig import get_connection
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)




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




if __name__ == '__main__':
    app.run(debug=True)
