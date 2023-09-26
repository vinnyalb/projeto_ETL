import pandas as pd
import json

# Processo de extração de dados de um CSV e o transformando em um DataFrame

import pandas as pd

df = pd.read_csv('data.csv')


# Processo de Transformação
print("Bem vindo(a) a verificação de idade para a campanha de degustação de cerveja artesanal\n")

for index, row in df.iterrows():
    idade = row['idade']
    if idade < 18:
        print(f'Olá {index}, você é menor de idade e por isso não poderá participar da campanha')
    else:
        print(f'Olá {index}, vovê é maior de idade e poderá participar da campanha')

# Processo de Load: Transformando o DataFrame em um Dicionário de dados, e em seguida, armazenando 
# em um JSON

dados_json = df.to_dict(orient='records')
print(json.dumps(dados_json, indent=4))