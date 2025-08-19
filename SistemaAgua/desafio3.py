# Sistema de Recomendação de Consumo de Água Diária

'''
usuario = input('Digite seu nome: ').strip().upper()
numeroZapp = int(input('Digite seu numero de Whatsapp: '))
peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metro): '))

imc = peso / (altura ** 2) # calculo do imc (massa corporal)
print(f'- Nome: {usuario}\n- Numero: {numeroZapp} (Whatsapp)\n- Peso: {peso}kg\n- Altura: {altura}M')
print(f'- Seu IMC(indice de massa corporal) é de: {imc:.2f}')
agua_diaria = (peso * 35) / 1000 # calculo pra ficar em litros
print(f'- Ingestão de Água diaria: {agua_diaria:.2f} Litros/dia')
'''

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular_agua_diaria(peso):
    return (peso * 35) / 1000 # em litros

def coleta_dados():
    print('=== Sistema de Recomendação de Consumo de Água diária ===')
    
    usuario = input('Digite seu nome: ').strip().title()
    
    try:
        numero_zapp = int(input('Digite seu número de whatsapp (apenas números): '))
        peso = float(input('Digite seu peso (em kg): '))
        altura = float(input('Digite sua altura (em metros): '))
        
        if peso <= 0 or altura <= 0:
            print('Peso e Altura devem ser maiores que zero.')
            return
        
        imc = calcular_imc(peso, altura)
        agua_diaria = calcular_agua_diaria(peso)
        
        print('\n Informações do Usuário:')
        print(f'- Nome: {usuario}')
        print(f'- Número: {numero_zapp} (Whatapp)')
        print(f'- Peso: {peso:.1f} kg')
        print(f'- Altura: {altura:.2f} m')
        print(f'- IMC (Índice de Massa Corporal): {imc:.2f}')
        print(f'- Ingestão diária recomendada de água: {agua_diaria:.1f} litros ')
    except ValueError:
        print('Entrada inválida. Certifique-se de digitar números corretamente!')

def main():
    while True:
        coleta_dados()
        
        continuar = input('\nDeseja calcular para outro usuário? (S/N): ').strip().lower()
        if continuar != 's':
            print('\n=== Encerrando o sistema. Beba água e cuide-se! ===')
            break
           
main()
        