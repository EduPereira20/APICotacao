# Biblioteca python para realizações HTTP
import requests;

# o smtplib fornece funcionalidades para enviar emails utilizando SMTP.
import smtplib
# Fornece a estrutura para a criação do email.
import email.message

# Extraindo a cotação em python para que se possa obter seu valor
requisição = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
json_requisicao = requisição.json()
cotacao = float(json_requisicao['USDBRL']['bid'])

destinatario = input("Digite o destinátario")

# Construção da def que enviará o email
def enviar_email(cotacao, destinatario):
    estrutura_email = f"""
        Atual cotação do dólar: R${cotacao}
    """

    mensagem = email.message.Message()
    mensagem['Subject'] = "Dólar está abaixo de R$5.20!"
    mensagem['From'] = ''
    mensagem['To'] = destinatario
    # Como obter a senha -> Gerenciar sua conta -> Segurança -> Verificação de duas etapas -> Senhas de APP -> Selecionar APP -> Outros(Qualquer nome).
    password = ''
    mensagem.add_header('Content_Type', 'text/html')
    mensagem.set_payload(estrutura_email)

    # SMTP responsável pelo envio e recebimento de emails, porta 587 padrão do SMTP, faz o envio de emails criptografados
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(mensagem['From'], password)
    s.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
    print("Email enviado com sucesso")

# Executando a função
enviar_email(cotacao, destinatario)

    



