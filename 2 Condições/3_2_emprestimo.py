salario = float(input('O salário do cliente: '))
emprestimo = float(input('O empréstimo pretendido: '))

parcela = emprestimo / 60
parcela_mes_pagar = parcela + (parcela / 100 * 1 )
parcela_mes_pode = salario / 4

if parcela_mes_pagar <= parcela_mes_pode:
    print('O empréstimo foi aprovado!')
    print(f'O cliente deve pagar R${parcela_mes_pagar:.2f} por mês.')
else:
    print('O empréstimo foi reprovado!')
    print(f'O valor a ser pago é de R${parcela_mes_pagar:.2f} é o', end=' ')
    print(f'cliente só pode pagar R${parcela_mes_pode:.2f}.')
