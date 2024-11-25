from twilio.rest import Client

# Credenciais da sua conta Twilio
account_sid = 'SEU_ACCOUNT_SID'  # Substitua pelo seu Account SID
auth_token = 'SEU_AUTH_TOKEN'    # Substitua pelo seu Auth Token
client = Client(account_sid, auth_token)

# Configuração da chamada
numero_origem = '+SEU_NUMERO_TWILIO'  # Substitua pelo número Twilio
numero_destino = input("Digite o número de destino (com código do país, ex: +5511999999999): ")
mensagem = "Olá! Esta é uma chamada de teste feita em um ambiente controlado."

try:
    # Faz a chamada
    chamada = client.calls.create(
        to=numero_destino,
        from_=numero_origem,
        twiml=f'<Response><Say>{mensagem}</Say></Response>'
    )
    print(f"Chamada iniciada com sucesso! SID: {chamada.sid}")
except Exception as e:
    print(f"Erro ao realizar a chamada: {e}")
