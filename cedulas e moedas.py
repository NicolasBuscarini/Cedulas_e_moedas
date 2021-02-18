valori = 1 #inicia while

while valori != 0: # Quando o usuario digitar 0 encerra o programa

    nota100, nota50, nota20, nota10, nota4, nota1 = 0,0,0,0,0,0           #Zera Contador Notas (cedulas)
    moeda50, moeda20, moeda10, moeda5, moeda2, moeda1 = 0,0,0,0,0,0       #Zera Contador Moedas

    print("Caso queira encerrar o programa, digite 0")      
    valori = float(input("Digite o valor que desejar: ")) #guarda o valor inicial
    valor = valori            #Transfere o valor para outra variavel onde sera realizada a somatoria das cedulas
                        
        #Notas (Cédulas)
    while valor >= 100:       # Somatoria de cedulas para cada variavel correspondente
        valor -= 100
        nota20 +=1
    while valor>= 50:  
        valor -= 50
        nota50 +=1
    while valor >= 20:
        valor -= 20
        nota20 +=1
    while valor >= 10:
        valor -= 10
        nota10 +=1
    while valor >= 4:
        valor -= 4
        nota4 +=1
    while valor >= 1:
        valor -= 1
        nota1 +=1

    while valor >= 0.50:      # Somatoria de Moedas
        valor -= 0.50
        moeda50 +=1
    while valor >= 0.20:
        valor -= 0.20
        moeda20 +=1
    while valor >= 0.10:
        valor -= 0.10
        moeda10 +=1
    while valor >= 0.05:             
        valor -= 0.05
        moeda5 +=1
    while valor > 0.01999:  #ao realizar operaçoes a variavel recebe um pouco de "lixo" entao devemos usar uma margem de erro           
        valor -= 0.02
        moeda2 +=1
    while valor> 0.009999:  #ao realizar operaçoes a variavel recebe um pouco de "lixo" entao devemos usar uma margem de erro
        valor -= 0.01
        moeda1 +=1
        
    if valori != 0:   # para não mostrar este print caso o usuario digite 0
        print(f"""
A quantidades de cedulas para o valor R${valori:.2f} é:

    Cédulas de R$100: {nota100}
    Cédulas de R$50 : {nota50}
    Cédulas de R$20 : {nota20}
    Cédulas de R$10 : {nota10}
    Cédulas de R$4  : {nota4}
    Cédulas de R$1  : {nota1}

    Moedas de R$0,50: {moeda50}
    Moedas de R$0,20: {moeda20}
    Moedas de R$0,10: {moeda10}
    Moedas de R$0,05: {moeda5}
    Moedas de R$0,02: {moeda2}
    Moedas de R$0,01: {moeda1}

        """)

#fim do while
print ("Fim do programa") # Ao Digitar 0 encerra o programa
