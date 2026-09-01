from flask import Flask, render_template


app = Flask(__name__)




@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre_o_Sistema():
    return render_template('dashboard/sobre.html')

@app.route('/aluno')
def lista_aluno():
    lista=[
       (1,"Ana Beatriz Silva",20,"Teresina"),
       (2,"Bruno Carvalho Santos",21,"Parnaíba"),
        (3,"Carlos Eduardo Lima",19,"Picos"),
        (4,"Daniela Ferreira Costa",22,"Floriano"),
        (5,"Eduardo Henrique Alves",20,"Teresina"),
        (6,"Fernanda Oliveira Sousa",21,"Piripiri"),
        (7,"Gabriel Martins Rocha",23,"Campo Maior"),
        (8,"Helena Vitória Mendes",19,"Teresina"),
        (9,"Igor Rodrigues Silva",22,"Bom Jesus"),
        (10,"Juliana Alves Pereira",20,"Oeiras")
        ]
    
    return render_template('aluno/lista.html', lista=lista)

@app.route('/professor')
def lista_professor():
    return render_template('professor/lista.html')


@app.route('/ajuda')
def ajuda():
    return 'Ajuda Sobre o Sistema!'



if __name__ == '__main__':
    app.run(debug=True)
