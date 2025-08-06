# Aula 4 - Exercício prático com diferentes tipos de dados

# 1. String
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo(a)")

# 2. Inteiro
idade = int(input("Digite sua idade: "))
idade_futura = idade + 10
print(f"Daqui a 10 anos, você terá {idade_futura} anos.")

# 3. Float
preco = float(input("Digite o preço do produto: R$ "))
desconto = preco * 0.10
preco_com_desconto = preco - desconto
print(f"O valor com 10% de desconto é: R$ {preco_com_desconto:.2f}")

# 4. Booleano
resposta = input("Você está matriculado? (sim/não): ").strip().lower()
# Convertendo para booleano
matriculado = True if resposta == "sim" else False
print(f"Status de matrícula: {matriculado}")
