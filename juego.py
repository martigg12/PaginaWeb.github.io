
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jugar', methods=['GET', 'POST'])
def jugar():
    if request.method == 'POST':
        respuesta_usuario = request.form['respuesta_usuario']
        pregunta_id, pregunta, respuesta_correcta = obtener_pregunta_respuesta()

        if respuesta_usuario.lower() == respuesta_correcta.lower():
            mensaje_resultado = "¡Correcto! ¡Has acertado!"
        else:
            mensaje_resultado = f"Incorrecto. La respuesta correcta es: {respuesta_correcta}"

        return render_template('resultado.html', pregunta=pregunta, mensaje_resultado=mensaje_resultado)

    pregunta_id, pregunta, _ = obtener_pregunta_respuesta()
    return render_template('juego.html', pregunta_id=pregunta_id, pregunta=pregunta)

def obtener_pregunta_respuesta():
    conn = sqlite3.connect("preguntas_respuestas.db")
    cursor = conn.cursor()
    cursor.execute('SELECT id, pregunta, respuesta FROM trivia ORDER BY RANDOM() LIMIT 1')
    pregunta_id, pregunta, respuesta_correcta = cursor.fetchone()
    conn.close()
    return pregunta_id, pregunta, respuesta_correcta

if __name__ == '__main__':
    app.run(debug=True)