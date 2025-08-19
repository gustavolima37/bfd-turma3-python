# Problema - Calculo de Salario com Descontos

hora_trabalhada = int(input('Digite quantas horas trabalhou no mês: '))
valor_hora = float(input('Digite o valor por hora trabalhada: '))

salario_bruto = valor_hora * hora_trabalhada
print(f'Valor Hora: R$ {valor_hora:.2f} \nHoras no mês: {hora_trabalhada}' )

imposto_renda = salario_bruto * 0.11

desconto_inss = salario_bruto * 0.08

desconto_sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - imposto_renda - desconto_inss - desconto_sindicato

print(f'+ Salario Bruto: R$ {salario_bruto:.2f} \n- IR (11%): R$ {imposto_renda:.2f}\n- INSS(8%): R$ {desconto_inss:.2f}\n- Sindicato(5%): R$ {desconto_sindicato:.2f}\n Salario Liquido: R$ {salario_liquido:.2f}')
