# 🌡️ API Conversor de Temperatura con Flask

Esta es una **API REST desarrollada con Python y Flask** que permite convertir temperaturas entre **Celsius y Fahrenheit** utilizando solicitudes **HTTP POST** con datos en formato JSON.

La API fue probada utilizando **Postman** para enviar solicitudes y verificar los resultados de conversión.

---

# 🚀 Tecnologías utilizadas

- 🐍 Python
- 🌐 Flask
- 📬 Postman
- 📦 JSON

---

# 📂 Estructura del proyecto

```
api_conversor_unidades/
│
├── app.py
├── img/
│   └── Captura de pantalla 2026-03-10 150018.png
└── README.md
```

---

# ⚙️ Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Hugo-Guerrero/api_conversor_unidades.git
cd api_conversor_unidades
```

### 2️⃣ Instalar dependencias

```bash
pip install flask
```

### 3️⃣ Ejecutar la API

```bash
python app.py
```

El servidor se ejecutará en:

```
http://127.0.0.1:5000
```

---

# 📡 Endpoint disponible

## POST /convertir-temperatura

Este endpoint permite **convertir temperaturas entre Celsius y Fahrenheit**.

### URL

```
http://127.0.0.1:5000/convertir-temperatura
```

---

# 📥 Ejemplo de solicitud (Request)

```json
{
  "valor": 100,
  "escala": "Celsius"
}
```

---

# 📤 Ejemplo de respuesta (Response)

```json
{
  "valor_original": 100,
  "escala_origen": "Celsius",
  "valor_convertido": 212,
  "escala_destino": "Fahrenheit"
}
```

---

# ❌ Ejemplo de error

Si no se envían los datos necesarios:

```json
{
  "error": "Debes proporcionar 'valor' y 'escala'"
}
```

Si la escala no es válida:

```json
{
  "error": "Escala no válida. Usa 'Celsius' o 'Fahrenheit'"
}
```

---

# 🧪 Prueba en Postman

Para probar la API se utilizó **Postman** enviando una solicitud **POST**.

Pasos:

1. Seleccionar el método **POST**
2. Usar la URL:

```
http://127.0.0.1:5000/convertir-temperatura
```

3. Ir a **Body**
4. Seleccionar **raw**
5. Elegir formato **JSON**
6. Enviar los datos de temperatura

---

# 📷 Ejemplo de prueba en Postman

![Prueba en Postman](img/Captura%20de%20pantalla%202026-03-10%20150018.png)

---

# 📘 Código principal

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    valor = datos.get('valor')
    escala = datos.get('escala')

    if valor is None or escala is None:
        return jsonify({"error": "Debes proporcionar 'valor' y 'escala'"}), 400

    if escala.lower() == "celsius":
        resultado = (valor * 9/5) + 32
        escala_destino = "Fahrenheit"
    elif escala.lower() == "fahrenheit":
        resultado = (valor - 32) * 5/9
        escala_destino = "Celsius"
    else:
        return jsonify({"error": "Escala no válida. Usa 'Celsius' o 'Fahrenheit'"}), 400

    return jsonify({
        "valor_original": valor,
        "escala_origen": escala,
        "valor_convertido": round(resultado, 2),
        "escala_destino": escala_destino
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

# 👨‍💻 Autor

Proyecto desarrollado como práctica de **creación de APIs con Flask** y pruebas con **Postman**.
