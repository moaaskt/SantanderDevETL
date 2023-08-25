# Santander Dev Week 2023 - ETL e Marketing

Este é um projeto de exemplo que demonstra como realizar um processo de Extração, Transformação e Carga (ETL) em dados bancários e, em seguida, usar a API OpenAI para gerar mensagens de marketing personalizadas para os clientes, enfatizando a importância dos investimentos. As mensagens são então enviadas de volta para a API Santander Dev Week para atualizar os dados do cliente.

## Pré-requisitos

Antes de executar o código, certifique-se de ter as seguintes bibliotecas instaladas:

- pandas
- requests
- openai

Além disso, você precisa de uma chave de API válida para a API OpenAI. Certifique-se de configurar as variáveis de ambiente `SDW2023_API_URL` e `OPENAI_API_KEY` com os valores corretos.

## Etapas do Projeto

1. Crie um arquivo CSV chamado `santanderdevWEEK.csv` com os IDs dos usuários que você deseja processar.

2. Execute o código `etl_pipeline.py` para realizar a extração, transformação e carga dos dados do usuário. Isso também gerará mensagens de marketing personalizadas usando a API OpenAI e atualizará as informações do usuário na API Santander Dev Week.

## Fluxo do Projeto

1. O código começa carregando os IDs dos usuários do arquivo CSV `santanderdevWEEK.csv`.

2. Ele itera sobre esses IDs, faz uma solicitação GET para buscar os dados de cada usuário na API Santander Dev Week e armazena os dados relevantes.

3. Para cada usuário, uma mensagem de marketing personalizada é gerada usando a API OpenAI. Essa mensagem é então adicionada à lista de notícias do usuário.

4. Os dados do usuário atualizados são enviados de volta para a API Santander Dev Week usando o método PUT para atualização.

## Observações

Certifique-se de configurar as variáveis de ambiente `SDW2023_API_URL` e `OPENAI_API_KEY` com os valores corretos antes de executar o código.

Este projeto é um exemplo simplificado e pode ser expandido para lidar com casos mais complexos, como lidar com erros de conexão, tratar diferentes cenários de mensagem ou gerenciar mais atributos do usuário na API.

## Aviso

Este projeto é apenas para fins de demonstração e pode ser modificado e expandido de acordo com suas necessidades. Certifique-se de entender os termos de uso das APIs utilizadas e seguir práticas de segurança recomendadas ao lidar com informações sensíveis.
