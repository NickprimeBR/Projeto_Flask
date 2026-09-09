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
    return render_template('professor/lista.html')


@app.route('/ajuda')
def ajuda():
    return 'Ajuda Sobre o Sistema!'



if __name__ == '__main__':
    app.run(debug=True)
