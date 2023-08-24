import pandas as pd
import requests
import openai
import os
import json

# Defina a URL da API da Santander Dev Week 2023
SDW2023_API_URL = os.environ.get("https://sdw-2023-prd.up.railway.app")
OPENAI_API_KEY = os.environ.get("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")

openai.api_key = OPENAI_API_KEY

# Função para obter os dados de um usuário
def get_user(id):
    response = requests.get(f"{SDW2023_API_URL}/users/{id}")
    return response.json() if response.status_code == 200 else None

# Função para gerar notícias usando a OpenAI
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

# Função para atualizar os dados de um usuário
def update_user_news(user_id, news):
    user = get_user(user_id)
    if user:
        user["news"].append(news)
        response = requests.put(f"{SDW2023_API_URL}/users/{user_id}", json=user)
        if response.status_code == 200:
            print(f"Dados atualizados para o usuário {user_id}")
        else:
            print(f"Falha ao atualizar dados para o usuário {user_id}")

# Carrega os IDs dos usuários do CSV
df = pd.read_csv("santanderdevWEEK.csv")
user_ids = df["UserID"].tolist()

# Lista para armazenar os dados dos usuários
users = []

# Itera sobre os IDs dos usuários, faz a requisição GET e armazena os dados
for user_id in user_ids:
    user_data = get_user(user_id)
    if user_data:
        users.append(user_data)

# Itera sobre os dados dos usuários, gera notícias e atualiza os dados
for user in users:
    news = generate_ai_news(user)
    print(news)
    user["news"].append(
        {
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news,
        }
    )
    update_user_news(user["id"], user)
