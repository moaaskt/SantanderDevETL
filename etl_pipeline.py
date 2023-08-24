import pandas as pd
import requests
import openai
import os

# Defina a URL da API da Santander Dev Week 2023
sdw2023_api_url = "https://sdw-2023-prd.up.railway.app"

# Defina sua chave de API da OpenAI
openai.api_key = "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"

def get_user(id):
    response = requests.get(f"{sdw2023_api_url}/users/{id}")
    return response.json() if response.status_code == 200 else None

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário.",
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)",
            },
        ],
    )
    return completion.choices[0].message.content.strip('"')

def update_user_news(user_id, news):
    user = get_user(user_id)
    if user:
        user["news"].append(
            {
                "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
                "description": news,
            }
        )
        response = requests.put(f"{sdw2023_api_url}/users/{user_id}", json=user)
        if response.status_code == 200:
            print(f"Dados atualizados para o usuário {user_id}")
        else:
            print(f"Falha ao atualizar dados para o usuário {user_id}")

# Carrega os IDs dos usuários do CSV
df = pd.read_csv("santanderdevWEEK.csv")
user_ids = df["UserID"].tolist()

# Itera sobre os IDs dos usuários, gera notícias e atualiza os dados
for user_id in user_ids:
    user = get_user(user_id)
    if user:
        news = generate_ai_news(user)
        update_user_news(user_id, news)
