import googlemaps
import pandas as pd

# Substitua 'SUA_CHAVE_API' pela sua chave de API do Google Cloud
gmaps = googlemaps.Client(key='AIzaSyADZZz1rdQxyxJZDh5UmRrDv-VY2doPc3I')

# Pesquise por empresas de estacionamento em São Paulo
result = gmaps.places(query='estacionamento')

# Crie uma lista para armazenar os resultados
data = []

for place in result['results']:
    nome = place['name']
    endereco = place['formatted_address']
    telefone = place.get('formatted_phone_number', '')  # Use o método get para evitar KeyError
    data.append({'Nome': nome, 'Endereço': endereco, 'Telefone': telefone})

# Crie um DataFrame com os resultados
df = pd.DataFrame(data)

# Salve o DataFrame em um arquivo Excel
df.to_excel('estacionamentos_sp.xlsx', index=False)

print("Os dados foram salvos em 'estacionamentos_sp.xlsx'")
