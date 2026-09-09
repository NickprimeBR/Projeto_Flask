from flask import Flask, render_template
import sqlite3

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre_o_Sistema():
    return render_template('dashboard/sobre.html')

@app.route('/aluno')
def lista_aluno():

        DB_PATH = "banco_escola.db"
        con = sqlite3.connect(DB_PATH)
        
        cursor = con.cursor()
        cursor.execute("SELECT id, nome, idade, cidade FROM aluno")
        
        lista = cursor.fetchall()
        return render_template('aluno/lista.html', lista=lista)
 

@app.route('/professor')
def lista_professor():
    
        DB_PATH = "banco_escola.db"
        con = sqlite3.connect(DB_PATH)
        
        cursor = con.cursor()
        cursor.execute("SELECT id,nome,disciplina from professor")
        
        lista = cursor.fetchall()
        return render_template('professor/lista.html', lista=lista)
    
@app.route('/turma')
def lista_turma():
    
        DB_PATH = "banco_escola.db"
        con = sqlite3.connect(DB_PATH)
        
        cursor = con.cursor()
        cursor.execute("select turma.id,turma.semestre,curso.nome_curso,professor.nome,professor.disciplina from turma join curso on curso.id=turma.curso_id join professor on professor.id=turma.professor_id")
        
        lista = cursor.fetchall()
        return render_template('turma/lista.html', lista=lista)
    


@app.route('/ajuda')
def ajuda():
    return 'Ajuda Sobre o Sistema!'



if __name__ == '__main__':
    app.run(debug=True)
