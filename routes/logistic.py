import requests
from flask import Blueprint, request, jsonify

logistic_bp = Blueprint('logistic', __name__)

GEOAPIFY_API_KEY = "335345c197c74640b2da2c95040d1dca"

def buscar_coordenadas(cep):
    viacep_url = f"https://viacep.com.br/ws/{cep}/json/"
    viacep_response = requests.get(viacep_url)
    if viacep_response.status_code != 200:
        raise Exception("Erro ao buscar CEP no ViaCEP.")
    
    endereco = viacep_response.json()
    local = f"{endereco['logradouro']}, {endereco['localidade']}, {endereco['uf']}"
    
    geoapify_url = "https://api.geoapify.com/v1/geocode/search"
    params = {
        "text": local,
        "apiKey": GEOAPIFY_API_KEY
    }
    geoapify_response = requests.get(geoapify_url, params=params)
    if geoapify_response.status_code != 200:
        raise Exception("Erro ao buscar coordenadas no Geoapify.")
    
    features = geoapify_response.json()["features"]
    if not features:
        raise Exception("Nenhuma coordenada encontrada para o endereço.")
    
    coords = features[0]["geometry"]["coordinates"]
    return coords[1], coords[0]

@logistic_bp.route('/calcular_frete', methods=['POST'])
def calcular_frete():
    data = request.get_json()
    cep_origem = data.get('cep_origem')
    cep_destino = data.get('cep_destino')

    try:
        lat1, lon1 = buscar_coordenadas(cep_origem)
        lat2, lon2 = buscar_coordenadas(cep_destino)

        distance_url = "https://api.geoapify.com/v1/routing"
        params = {
            "waypoints": f"{lat1},{lon1}|{lat2},{lon2}",
            "mode": "drive",
            "apiKey": GEOAPIFY_API_KEY
        }
        distance_response = requests.get(distance_url, params=params)
        if distance_response.status_code != 200:
            raise Exception("Erro ao calcular distância.")

        route_info = distance_response.json()
        distancia_metros = route_info["features"][0]["properties"]["distance"]
        distancia_km = round(distancia_metros / 1000, 2)

        valor_frete = round(distancia_km * 3.5, 2)

        return jsonify({
            "cep_origem": cep_origem,
            "cep_destino": cep_destino,
            "distancia_km": distancia_km,
            "valor_frete": valor_frete
        }), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
