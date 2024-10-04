from flask import Flask, request, jsonify, render_template
from models.model3 import cargar_csv_y_crear_modelo

# Crear la app Flask
app = Flask(__name__)

# Cargar el modelo RAG desde el CSV
csv_path = 'reservas_turisticas.csv'
modelo = cargar_csv_y_crear_modelo(csv_path)

# Definir la ruta principal
@app.route('/')
def home():
    return render_template('chatbox.html')

# Ruta para manejar el chat
@app.route('/chat', methods=['POST'])
def chat():
    # Recibir el mensaje del usuario
    user_message = request.form['message']
    
    # Usar el modelo para generar una respuesta basada en la consulta del usuario
    result = modelo({"query": user_message})
    
    # La respuesta generada por el modelo
    response = result['result']
    
    return jsonify({'response': response})
