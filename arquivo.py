print("Hello Word")
# Entrada de dados
nome = input("Digite seu nome:")

ano = int(input("Digite o ano de nascimento:")) #É possível declarar uma variável em python e o seu tipo dessa forma.

#Saída de dados
#Colocar um f antes das aspas no print permite incluir expressões dentro da string e que elas sejam substituidas por seus valores
if(ano>2025):
    print("Ano inválido!")
elif (2025-ano)<18:
    print(f"Olá {nome} este ano você está fazendo {2025-ano} anos, parabéns.")
    print("Você é menor de idade.\nNão pode ter habilitação!")

else:
    print(f"Olá {nome} este ano você está fazendo {2025-ano} anos, parabéns.")
    print("Você é maior de idade.\nVocê já pode ter habilitação!")
