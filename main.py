nome_cliente = input("Digite o seu nome: ")
salario = float(input("Digite o seu salario: "))
bonus = float(input("Digite o valor do bonus: "))
constante_bonus = 1000
kpi = constante_bonus + salario*bonus

print(f"Parabéns {nome_cliente}, seu bônus foi de: {kpi}")
