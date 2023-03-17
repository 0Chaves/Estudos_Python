name = input("What's your name? ")
print(len(name))

#função len traz o tamanho da string
# !!!!range é outra coisa!!!!! 

print( len( input("What is your name? ")))

#Lembrando que funções podem estar umas dentro das outras, e essas vão seguir uma certa ordem de prioridade. Nesse caso, começa com input mostrando a mensagem, então recebe 
#o que o usuario digitar, len transforma o texto no numero de indices, e então o print mostra esse numero

#Porem não é a forma mais clara de escrever !!!!! a forma mais clara ta abaixo

nome = input("Qual seu nome? ")
tamanho = len(nome)
print('O seu nome "%s" tem %d letras'% (nome, tamanho))