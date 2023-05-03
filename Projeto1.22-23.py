###########################
#                         #
#  Projeto 1 - FP         #
#  Antonio Dias da Silva  #
#  nº 102879              #
#                         #
###########################

# TASK2
'''
limpa_texto: cad. caracteres -> cad. caracteres
'''


def limpa_texto(frase):
    '''
    A funcao limpa_texto, recebe uma cadeia de caracteres qualquer e devolve a cadeia de caracteres
    corrigida, ou seja, sem caracteres especiais e espacos.
    '''
    cadLimpa = ''

    for i in range(len(frase)):
        if 41 <= ord(frase[i]) <= 91 or 97 <= ord(frase[i]) <= 122:
            cadLimpa += frase[i]

        elif i >= 1 and (41 <= ord(frase[i - 1]) <= 91 or 97 <= ord(frase[i - 1]) <= 122):
            cadLimpa += ' '

    return cadLimpa.strip()


'''
corta_texto: cad. caracteres x inteiro -> cad. caracteres x cad. caracteres
'''


def corta_texto(textoLimpo, larguraColuna):
    '''
    A funcao corta_texto, recebe uma cadeia de caracteres e um inteiro positivo correspondentes
    a um texto limpo e uma largura de coluna, respetivamente, e devolve duas subcadeias de caracteres
    limpas, ou seja, contem a cadeia inicial cortada ate a largura de coluna recebida e a segunda
    subcadeia o resto do texto.
    '''
    cadeiaCortada1 = list()
    cadeiaCortada2 = list()
    textoLimpo = textoLimpo.split()
    i = 0

    while i <= len(textoLimpo) - 1:
        if len(textoLimpo[i]) <= larguraColuna:
            cadeiaCortada1.append(textoLimpo[i])
            cadeiaCortada1.append(' ')
            larguraColuna -= len(textoLimpo[i]) + 1

        else:
            cadeiaCortada2.append(textoLimpo[i])
            cadeiaCortada2.append(' ')
            larguraColuna = 0

        i += 1

    return (''.join(cadeiaCortada1)).strip(), (''.join(cadeiaCortada2)).strip()


'''
insere_espacos: cad. caracteres x inteiro -> cad. caracteres
'''


def insere_espacos(textoLimpo, larguraColuna):
    '''
    A funcao insere_espacos, recebe uma cadeia de caracteres e um inteiro, correspondentes a um texto
    limpo e a uma largura de coluna, e devolve uma cadeia de caracteres de comprimento igual a largura de
    coluna formada pela cadeia original com espacos entre palavras.
    '''
    textoLimpo = textoLimpo.split()
    tamanhoTextoLimpo = len(textoLimpo)
    espacosColocados = 0
    posicaoDoEspaco = 1
    posicaoInicialDoEspaco = 1
    proximaPalavra = 2
    i = 0

    if tamanhoTextoLimpo == 1:
        tamanhoPalavra = len(textoLimpo[i])
        numeroEspacos = larguraColuna - tamanhoPalavra

        while i <= numeroEspacos:
            textoLimpo.append(' ')
            i += 1

        return ''.join(textoLimpo)

    else:
        tamanhoPalavra = len(''.join(textoLimpo))
        numeroEspacos = larguraColuna - tamanhoPalavra

        while espacosColocados < numeroEspacos:
            while i < tamanhoTextoLimpo - 1:
                textoLimpo.insert(posicaoDoEspaco, ' ')
                posicaoDoEspaco += proximaPalavra
                espacosColocados += 1
                i += 1

                if espacosColocados == numeroEspacos:
                    break

            proximaPalavra += 1
            i = 0
            posicaoDoEspaco = posicaoInicialDoEspaco

        return ''.join(textoLimpo)


'''
justifica_texto: cad. caracteres x inteiro -> tuplo
'''


def justifica_texto(texto, larguraColuna):
    '''
    A funcao justifica_texto, recebe uma cadeia de caracteres nao vazia e um inteiro positivo
    correspondentes a um texto qualquer e uma largura de coluna e devolve cadeias de caracteres
    justificadas.
    '''
    if type(texto) != str or type(larguraColuna) != int:
        raise ValueError('justifica_texto: argumentos invalidos')

    if len(texto) == 0:
        raise ValueError('justifica_texto: argumentos invalidos')

    if larguraColuna < 0:
        raise ValueError('justifica_texto: argumentos invalidos')

    texto = limpa_texto(texto)
    texto_cortado = corta_texto(texto, larguraColuna)

    res = ()
    cadeiaCortada0 = 0
    cadeiaCortada1 = 1
    tamanhoFrase1 = len(texto_cortado[cadeiaCortada1])

    while tamanhoFrase1 != 0:
        res += (texto_cortado[cadeiaCortada0],)
        texto_cortado = corta_texto(texto_cortado[cadeiaCortada1], larguraColuna)
        tamanhoFrase1 = len(texto_cortado[cadeiaCortada1])

        if tamanhoFrase1 == 0:
            res += (texto_cortado[cadeiaCortada0],)

    cadeiaJustificada = ()
    tamanhoRes = len(res)
    i = 0

    while i <= tamanhoRes - 1:

        if i == tamanhoRes - 1:
            ultimaCadeia = list(res[i])
            tamanhoUltimaCadeia = len(ultimaCadeia)

            while tamanhoUltimaCadeia != larguraColuna:
                ultimaCadeia.append(' ')
                tamanhoUltimaCadeia += 1

            ultimaCadeia = ''.join(ultimaCadeia)
            cadeiaJustificada += (ultimaCadeia,)

        else:
            fraseJustificada = insere_espacos(res[i], larguraColuna)
            cadeiaJustificada += (fraseJustificada,)

        i += 1

    return cadeiaJustificada


# TASK2
'''
calcula_quocientes: dicionario x inteiro -> dicionario
'''


def calcula_quocientes(votosApurados, numDeputados):
    '''
    A funcao calcula_quocientes, recebe um dicionario com os votos apurados num circulo e um inteiro
    positivo correspondente ao numero de deputados e devolve o dicionario com as mesmas chaves do
    dicionario do argumento contendo a lista com os quocientes calculados do metodo de Hondt, colocados
    de ordem decrescente.
    '''
    res = {}

    for chave in votosApurados:
        votosPartido = votosApurados[chave]
        divisores = 1
        listaDivisores = []

        while divisores <= numDeputados:
            quociente = votosPartido / divisores
            listaDivisores.append(quociente)
            divisores += 1

        res[chave] = listaDivisores

    return res


'''
atribui_mandatos: dicionario x inteiro -> lista
'''


def atribui_mandatos(votosApurados, numDeputados):
    '''
    A funcao atribui_mandatos, recebe um dicionario com os votos apurados num circulo e um inteiro
    representando o numero de deputados e devolve a lista ordenada de tamanho igual ao numero de deputados
    contendo os partidos que obtiveram cada mandato.
    '''
    mandatos = []
    quocientes = calcula_quocientes(votosApurados, numDeputados)

    while numDeputados != 0:
        num = 0
        numMenorGuardado = 0
        chaveNum = ''

        for chave in quocientes:
            numeroMaior = max(quocientes[chave])
            numeroMenor = min(quocientes[chave])
            if numeroMaior > num or (numeroMaior == num and numeroMenor < numMenorGuardado):
                num = numeroMaior
                numMenorGuardado = numeroMenor
                chaveNum = chave

        quocientes[chaveNum].remove(num)
        mandatos.append(chaveNum)

        numDeputados -= 1

    return mandatos


'''
obtem_partidos: dicionario -> lista
'''


def obtem_partidos(info):
    '''
    A funcao obtem_partidos, recebe um dicionario com a informacao sobre as eleicoes num territorio
    com varios circulos eleitorais e devolve a lista ordenada por ordem alfabetica com o nome de
    todos os partidos participantes nas eleicoes.
    '''
    partidosParticipantes = []
    for regiao in info:
        for partidos in info[regiao]['votos']:
            if partidos not in partidosParticipantes:
                partidosParticipantes.append(partidos)

    partidosParticipantes.sort()

    return partidosParticipantes


'''
obtem_resultados_eleicoes: dicionario -> lista
'''


def obtem_resultado_eleicoes(info):
    '''
    A funcao obtem_resultados_eleicoes recebe um dicionario com a informacao sobre as eleicoes num
    territorio com varios circulos eleitorais e devolve a lista ordenada de comprimento igual ao numero
    total de partidos com os resultados das eleicoes.
    '''
    if type(info) != dict:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')

    if len(info) == 0:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')

    for chave in info:
        if type(chave) != str or len(chave) == 0:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')

        if 'deputados' not in info[chave] and 'votos' not in info[chave]:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')

        if info[chave]['deputados'] <= 0:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')

        if len(info[chave]['votos']) == 0:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')

        for elem in info[chave]['votos']:
            if type(info[chave]['votos'][elem]) != int:
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')

    partidos = obtem_partidos(info)

    partidosLowerCase = [i.lower() for i in partidos]
    duplicado = [x for i, x in enumerate(partidosLowerCase) if i != partidosLowerCase.index(x)]

    if len(duplicado) != 0:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')

    resultados = []

    for elem in partidos:
        numVotos = 0
        contador = 0
        infos = ()
        for regiao in info:
            mandatos = atribui_mandatos(info[regiao]['votos'], info[regiao]['deputados'])

            if elem in mandatos:
                numVezes = mandatos.count(elem)
                contador += numVezes

            if elem in info[regiao]['votos']:
                numVotos += info[regiao]['votos'][elem]

        infos += (elem, contador, numVotos)
        resultados.append(infos)

    resultadosFinais = []
    e = 0
    tamanhoResultados = len(resultados)

    while e <= tamanhoResultados - 1:
        maiorNumDeputados = 0
        maiorNumVotos = 0
        tuploGuardado = ()

        for i in range(len(resultados)):
            if (resultados[i][1] > maiorNumDeputados) or (
                    resultados[i][1] == maiorNumDeputados and resultados[i][2] > maiorNumVotos):
                maiorNumDeputados = resultados[i][1]
                maiorNumVotos = resultados[i][2]
                tuploGuardado = resultados[i]

        resultados.remove(tuploGuardado)
        resultadosFinais.append(tuploGuardado)

        e += 1

    return resultadosFinais


# TASK3

'''
produto_interno: tuplo x tuplo -> real
'''


def produto_interno(vetor1, vetor2):
    '''
    A funcao produto_interno, recebe dois tuplos correspondentes a vetores com a mesma dimensao e
    devolve o produto interno entre estes.
    '''

    resultado = 0

    for coluna in range(len(vetor1)):
        multiplicacao = vetor1[coluna] * vetor2[coluna]
        resultado += multiplicacao

    return float(resultado)


'''
verifica_convergencia: tuplo x tuplo x tuplo x real -> booleano
'''


def verifica_convergencia(matriz, constantes, solucao, precisao):
    '''
    A funcao verifica_convergencia, recebe tres tuplos de igual dimensao e um valor real positivo,
    correspondentes a uma matriz quadrada, um vetor de constantes, a solucao atual e uma precisao
    pretendida. Devolve True se |Fi(x)-ci| < precisao, e False caso contrario.
    '''
    for linha in range(len(matriz)):
        res = produto_interno(matriz[linha], solucao)

        res -= constantes[linha]

        if res < 0:
            res *= -1

        if res > precisao:
            return False

    return True


'''
retira_zeros_diagonal: tuplo x tuplo -> tuplo x tuplo
'''


def troca_linhas(m, l1, l2):
    '''
    A funcao troca_linhas, e uma funcao auxiliar que recebe um tuplo de tuplos, correspondente a uma matriz
    quadrada, e dois inteiros, correspondentes ao numero das linhas que se quer trocar. Devolve a matriz
    com as duas linhas trocadas.
    '''
    li = min(l1, l2)
    lf = max(l1, l2)
    res = m[:li] + (m[lf],) + m[li + 1:lf] + (m[li],) + m[lf + 1:]
    return res


def retira_zeros_diagonal(matriz,constantes):
    '''
    A funcao retira_zeros_diagonal, recebe dois tuplos correspondentes a uma matriz quadrada e a um vetor de
    constantes e devolve um tuplo de dois tuplos, em que o primeiro e a matriz porem sem zeros na diagonal
    e o segundo o vetor de constantes alterado da mesma forma que a matriz.
    '''
    for linha in range(min(len(matriz), len(matriz[0]))):
        if matriz[linha][linha] == 0:

            for coluna in range(len(matriz)):
                if matriz[coluna][linha] != 0:

                    matriz = troca_linhas(matriz,linha,coluna)
                    constantes = troca_linhas(constantes,linha,coluna)

                    break

    return matriz,constantes


'''
eh_diagonal_dominante: tuplo -> booleano
'''


def eh_diagonal_dominante(matriz):
    '''
    A funcao eh_diagonal_dominante, recebe um tuplo de tuplos representado uma matriz quadrada e devolve
    True caso seja uma matriz diagonal dominante e False caso contrario.
    '''
    linha = 0
    coluna = 0

    while linha <= len(matriz) - 1:
        somaColuna = 0
        while coluna <= len(matriz) - 1:

            valorDiagonal = matriz[linha][coluna]

            if valorDiagonal < 0:
                valorDiagonal *= -1

            for elem in matriz[linha]:

                if elem < 0:
                    elem *= -1

                somaColuna += elem

            somaColuna -= valorDiagonal

            if valorDiagonal < somaColuna:
                return False

            coluna += 1

            break

        linha += 1

    return True


'''
resolve_sistema: tuplo x tuplo x real -> tuplo
'''


def resolve_sistema(matriz, constantes, precisao):
    '''
    A funcao resolve_sistema, recebe uma matriz quadrada (tuplo de tuplos), um vetor de constantes (tuplo)
    e uma precisao e devolve um tuplo que e a solucao do sistema de equacoes de entrada aplicando o metodo
    de Jacobi.
    '''
    if (type(matriz) != tuple) and (type(constantes) != tuple) and (precisao != float):
        raise ValueError('resolve_sistema: argumentos invalidos')

    if precisao < 0:
        raise ValueError('resolve_sistema: argumentos invalidos')

    tamanhoMatriz = len(matriz)
    tamanhoConstantes = len(constantes)

    if tamanhoMatriz != tamanhoConstantes:
        raise ValueError('resolve_sistema: argumentos invalidos')

    for elem1 in range(tamanhoMatriz):
        if type(matriz[elem1]) != tuple or len(matriz[elem1]) != tamanhoMatriz:
            raise ValueError('resolve_sistema: argumentos invalidos')

        for num in range(len(matriz[elem1])):
            if type(matriz[elem1][num]) != int:
                raise ValueError('resolve_sistema: argumentos invalidos')

    for elem2 in constantes:
        if type(elem2) != int:
            raise ValueError('resolve_sistema: argumentos invalidos')

    matrizSemZerosDiagonal = retira_zeros_diagonal(matriz, constantes)

    matriz = matrizSemZerosDiagonal[0]
    constantes = matrizSemZerosDiagonal[1]

    if not eh_diagonal_dominante(matriz):
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')

    solucao = ()
    i = 0

    while i <= tamanhoMatriz - 1:
        solucao += (0,)
        i += 1

    while not verifica_convergencia(matriz, constantes, solucao, precisao):

        novaSolucao = ()

        for linha in range(len(matriz)):
            resultado = produto_interno(matriz[linha], solucao)
            resultado = solucao[linha] + ((constantes[linha] - resultado) / matriz[linha][linha])
            novaSolucao += (resultado,)

        solucao = novaSolucao

    return solucao
