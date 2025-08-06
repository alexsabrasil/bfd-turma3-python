# aula4_exercicios.py
# Exercício prático - Aula 4

# 1. STRING
nome = input("Digite seu nome: ")
print(f"\n🔹 Olá, {nome}! Seja bem-vindo(a) 😊\n")

# 2. INTEIRO
idade = int(input("Digite sua idade: "))
idade_futura = idade + 10
print(f"🔸 Daqui a 10 anos, você terá {idade_futura} anos.\n")

# 3. FLOAT
preco = float(input("Digite o preço do produto (R$): "))
desconto = preco * 0.10
preco_com_desconto = preco - desconto
print(f"🔹 O valor com 10% de desconto é: R$ {preco_com_desconto:.2f}\n")

# 4. BOOLEANO
resposta = input("Você está matriculado? (sim/não): ").strip().lower()
matriculado = True if resposta == "sim" else False
print(f"🔸 Status de matrícula: {matriculado}\n")
