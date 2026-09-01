from flask import Flask, render_template


app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sobre')
def sobre_o_Sistema():
    return render_template('sobre.html')


@app.route('/ajuda')
def ajuda():
    return 'Ajuda Sobre o Sistema!'



if __name__ == '__main__':
    app.run(debug=True)
