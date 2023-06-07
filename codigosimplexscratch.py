def funcaoDeCalculo():
    indexMaximo = 1
    indexDivisor = 0
    maximo = 0

    # DEFINE A COLUNA PIVOT E QUAL VALOR FOI DEFINIDO
    while indexMaximo < tamanhoDaMatriz:
        if matriz[0][indexMaximo] < maximo:
            maximo = matriz[0][indexMaximo]
            indexDivisor = indexMaximo
        indexMaximo += 1

    iterationDivisor = 0
    menorPositivo = 0
    linhaMenorPositivo = 0

    # DEFINE A LINHA COM MENOR VALOR POSITIVO
    while iterationDivisor < numeroRestricoes:
        iterationDivisor += 1
        if matriz[iterationDivisor][indexDivisor] != 0:
            teste = matriz[iterationDivisor][tamanhoDaMatriz] / matriz[iterationDivisor][indexDivisor]
            if teste > 0:
                if menorPositivo == 0:
                    menorPositivo = teste
                    linhaMenorPositivo = iterationDivisor
                elif teste < menorPositivo:
                    menorPositivo = teste
                    linhaMenorPositivo = iterationDivisor

    matriz[linhaMenorPositivo] = [x / matriz[linhaMenorPositivo][indexDivisor] for x in matriz[linhaMenorPositivo]]

    iterationMultiplicador = 0
    while iterationMultiplicador <= numeroRestricoes:
        if iterationMultiplicador != linhaMenorPositivo:
            linhaMultiplicada = [y * (-matriz[iterationMultiplicador][indexDivisor]) for y in
                                 matriz[linhaMenorPositivo]]
            matriz[iterationMultiplicador] = [a + b for a, b in zip(matriz[iterationMultiplicador], linhaMultiplicada)]
            iterationMultiplicador += 1
        else:
            matriz[iterationMultiplicador] = matriz[iterationMultiplicador]
            iterationMultiplicador += 1
    return matriz


def MostrarVariaveisBasicasENaoBasicas(matriz):
    iterationColuna = 0

    while iterationColuna < (numeroRestricoes + numeroVariaveis):
        iterationColuna += 1
        coluna = [row[iterationColuna] for row in matriz]
        soma = sum(coluna)
        if soma == 1:
            iterationOtimo = 0
            while iterationOtimo < numeroRestricoes:
                iterationOtimo += 1
                multiplicado = matriz[iterationOtimo][iterationColuna] * matriz[iterationOtimo][tamanhoDaMatriz]
                if multiplicado == matriz[iterationOtimo][tamanhoDaMatriz] != 0:
                    print('O valor ótimo para a variável de número', iterationColuna, 'é:', multiplicado)


def MostrarValorDeZ(matriz):
    print(f"O valor do lucro ótimo: R$", matriz[0][tamanhoDaMatriz])
    PrecoSombra(matriz)


# ITERAÇÃO DE CHECAGEM
def ChecarSeOtima(matriz):
    otima = 0
    for a in matriz[0]:
        if a >= 0:
            otima += 0
        else:
            otima += 1
    if otima > 0:
        funcaoDeCalculo()
        ChecarSeOtima(matriz)
    else:
        print('\n\n\n\n\n\n\n\n\nFoi encontrada a solução ótima')
        MostrarVariaveisBasicasENaoBasicas(matriz)
        MostrarValorDeZ(matriz)


def PrecoSombra(matriz):
    i = 0
    for j in range(tamanhoDaMatriz - numeroVariaveis, tamanhoDaMatriz):
        preco_sombra = matriz[0][j]
        print(f"Preço Sombra para X{i + 1}: R${preco_sombra:.2f}")
        i = i + 1


def ChecarViabilidade(matriz):
    print('Se não quiser alterar o delta insira o valor 1')
    deltas = []
    aux = 0

    for i in range(numeroRestricoes):
        aux = aux + 1
        valor = float(input(f'Digite a variação da restrição X{aux}: '.format(i)))
        deltas.append(valor)

    novasVariaveisBasicas = []

    for i in range(numeroRestricoes):
        novoValor = []
        for j in range(numeroRestricoes):
            valor = deltas[j] * matriz[i + 1][numeroVariaveis + (j + 1)]
            novoValor.append(valor)

        novasVariaveisBasicas.append(novoValor)

    flag = False
    for i in range(numeroRestricoes):
        valor = matriz[i + 1][tamanhoDaMatriz]
        for j in range(numeroRestricoes):
            valor = valor + novasVariaveisBasicas[i][j]
        if valor < 0:
            flag = True

    if flag == True:
        print('Com as alterações das variáveis o resultado não foi viável!')
    else:
        z = matriz[0][tamanhoDaMatriz]
        for i in range(numeroRestricoes):
            z = z + deltas[i] * matriz[0][(tamanhoDaMatriz - numeroRestricoes)+i]
        print(f'O novo lucro será de: R${z:.2f}')

# MAIN
print('******************** Método Simplex ********************')
numeroVariaveis = int(input('São quantas variáveis de decisão: '))
numeroRestricoes = int(input('Quantas restrições: '))
matrizPrimeira = [[1.0]]
iterationVariaveis = 0
iterationRestricoes = 0
matriz = [[1]]
novaLinha = [0]
tamanhoDaMatriz = 0

print('\nInsira os coeficientes da função objetivo')

# INSERÇÃO DOS COEFICIENTES DA FUNÇÃO OBJETIVO
while iterationVariaveis < numeroVariaveis:
    iterationVariaveis += 1
    item = float(input(f'Insira o coeficiente {iterationVariaveis} da função objetivo: '))
    matriz[0].insert(iterationVariaveis, item)
    tamanhoDaMatriz += 1
    restante_matriz = [linha[1:] for linha in matriz]
iterationVariaveis = 0

# INSERÇÃO DOS COEFICIENTES DO QUE FALTA E O B
while iterationRestricoes <= numeroRestricoes:
    iterationRestricoes += 1
    matriz[0].insert(numeroVariaveis + 1, 0)
    tamanhoDaMatriz += 1
    restante_matriz = [linha[1:] for linha in matriz]
iterationRestricoes = 0

# INSERÇÃO DOS COEFICIENTES DAS RESTRÇÕES e dos resultados
print('\nInsira os coeficientes das restrições')
while iterationRestricoes < numeroRestricoes:
    iterationRestricoes += 1
    while iterationVariaveis < numeroVariaveis:
        iterationVariaveis += 1
        item = float(input(f'Insira o coeficiente {iterationVariaveis} da restrição: '))
        novaLinha.append(item)
    indexDaFalta = iterationVariaveis + iterationRestricoes

    while iterationVariaveis < tamanhoDaMatriz - 1:
        iterationVariaveis += 1
        if iterationVariaveis == indexDaFalta:
            novaLinha.insert(iterationVariaveis, 1)
        else:
            novaLinha.insert(iterationVariaveis, 0)

    item = float(input('Insira o lado direito da restrição: '))
    novaLinha.append(item)

    matriz.append(novaLinha)
    novaLinha = [0]
    restante_matriz = [linha[1:] for linha in matriz]
    iterationVariaveis = 0

iterationRestricoes = 0
funcaoDeCalculo()
ChecarSeOtima(matriz)
print('Quer modificar o delta das variáveis para checar a viabilidade ?')

modDelta = -1
while modDelta != 1 and modDelta != 0:
    modDelta = int(input('Digite 0 para sair e 1 para adicionar o delta: '))

    if modDelta == 1:
        ChecarViabilidade(matriz)

    elif modDelta == 0:
        break

    else:
        print("Digite somente 0 ou 1. Tente novamente.")

print('\nPrograma finalizado.')