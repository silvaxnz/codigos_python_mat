'''

Essa estrutura de repetição é o mais comum em qualquer outra Linguagem de programação 
for (contador = 1; contador <=5; contador++){

}

'''
print("-=-"*30)
for contador in range (1,6):
    print(contador)

    #2ª Exemplo
    for contador in range(1,11,2):# o 3ª parâmetro irá aumentar o incremento dos valores que estão sendo exibidos
        print(contador)

print("-"*30)
#3ª Exemplo - Números do maior para o menor
for contador in range(10,0,-1):
    print(contador,end="")# o comando end, informa como o python irá mostrar o final de uma exibiçâo, por padrão irá dar um enter(\n)
