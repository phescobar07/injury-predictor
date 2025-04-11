from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_risco(treino, descanso, tipo):
    risco = 0
    if treino > 120:
        risco += 40
    elif treino > 90:
        risco += 25
    elif treino > 60:
        risco += 15
    else:
        risco += 5

    if descanso < 8:
        risco += 30
    elif descanso < 6:
        risco += 45

    if tipo == 'intenso':
        risco += 20
    elif tipo == 'moderado':
        risco += 10

    if risco < 30:
        status = 'Baixo risco'
    elif risco < 60:
        status = 'Risco moderado'
    else:
        status = 'ALTO RISCO ⚠️'

    return status

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        treino = int(request.form['tempo_treino'])
        descanso = float(request.form['descanso'])
        tipo = request.form['tipo_treino']
        resultado = calcular_risco(treino, descanso, tipo)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
