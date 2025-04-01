from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Permitir requisições entre diferentes domínios

# Carregar os dados do CSV
data = pd.read_csv('backend/Relatorio_cadop.csv', sep=';', encoding='utf-8-sig')

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Query não fornecida"}), 400

    # Filtrar os registros mais relevantes
    resultados = data[data['Razao_social'].str.contains(query, case=False, na=False)].head(10)
    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)