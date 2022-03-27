import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACeb462c201c155a6b37bad8bb8cb7526c"
# Your Auth Token from twilio.com/console
auth_token  = "2c9f6087b48a5bc3bd7b0ab5404c249b"
client = Client(account_sid, auth_token)

# --->>> Passo a Passo de Solução!!!!.

# I-Abrir os 6 Arquivos em Excel.
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']


for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511967099419",
            from_="+12565738582",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# -->>>>Para Cada Arquivo:

# Verificar se ALgum Valor na Coluna Vendas  Daqule Arquivo e Maior que 55.000.

# II- Se for Maior do que 55.000 -> Envia um SMS com o Nome, o Mês e as Vendas Daquele Vendedor.

# Caso não Haja Valor Maior do que 55.000 Não Fazer Nada.

# Ajuda a encontra especificamente na tabela usando .values[0]