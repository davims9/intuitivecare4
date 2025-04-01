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
        return jsonify({"error": "Por favor, forneça um termo de busca."}), 400

    # Filtra os registros mais relevantes com base em Razao_Social
    results = data[data['Razao_Social'].str.contains(query, case=False, na=False, regex=False)].head(10)

    if results.empty:
        return jsonify({"message": "Nenhum registro encontrado para o termo de busca."}), 404

    return jsonify(results.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)