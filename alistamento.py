# Importa a classe date do módulo datetime
# Ela será utilizada para obter o ano atual do sistema
from datetime import date

# Obtém o ano atual do computador
atual = date.today().year

# strip() remove espaços extras no início e no fim
# upper() converte a letra para maiúscula
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Qual é o seu sexo: M/F: ')).strip().upper()

if sexo not in ['M', 'F']:
    print('Sexo Inválido.')

idade = atual - nasc

# Verifica se o usuário é do sexo masculino
if sexo == 'M':
    print(f'Quem nasceu em {nasc} tem {idade} em {atual}.')

    # Verifica se a idade é exatamente 18 anos
    if idade == 18 and sexo in 'M':
        print('Você tem que se alistar IMEDIATAMENTE!')
    # Verifica se a idade é menor que 18 anos
    elif idade < 18:
        # Calcula quantos anos faltam para completar 18
        saldo = 18 - idade
        # Mostra quantos anos faltam para o alistamento
        print(f'Ainda faltam {saldo} ano(s) para o alistamento.')
        # Calcula o ano em que deverá se alistar
        print(f'Seu alistamento será em {atual + saldo}.')
    # Caso a idade seja maior que 18 anos
    else:
        # Calcula há quantos anos o alistamento deveria ter ocorrido
        saldo = idade - 18
        # Exibe o atraso do alistamento
        print(f'Você deveria ter se alistado há {saldo} ano(s).')
        # Calcula o ano em que deveria ter se alistado
        print(f'Seu alistamento foi em {atual - saldo}.')
# Caso o usuário não seja do sexo masculino
else:
    print('Você não precisa fazer o alistamento militar obrigatório.')
