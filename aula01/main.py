
name = input("Digite seu nome?\n")
salary = float(input("Digite seu salário?\n"))
bonus = float(input("Digite a porcentagem de bônus?\n"))
kpi = 1000 + salary * bonus

print("Hello, " + name + "! Seu valor bonus foi de: " + str(kpi))