from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    # Obtener valor y escala de origen
    valor = datos.get('valor')
    escala = datos.get('escala')

    if valor is None or escala is None:
        return jsonify({"error": "Debes proporcionar 'valor' y 'escala'"}), 400

    # Conversión según la escala
    if escala.lower() == "celsius":
        resultado = (valor * 9/5) + 32
        escala_destino = "Fahrenheit"
    elif escala.lower() == "fahrenheit":
        resultado = (valor - 32) * 5/9
        escala_destino = "Celsius"
    else:
        return jsonify({"error": "Escala no válida. Usa 'Celsius' o 'Fahrenheit'"}), 400

    # Respuesta en JSON
    return jsonify({
        "valor_original": valor,
        "escala_origen": escala,
        "valor_convertido": round(resultado, 2),
        "escala_destino": escala_destino
    })

if __name__ == '__main__':
    app.run(debug=True)
