pregunta = 's'
while pregunta.lower() in {'s', 'y', '', ' '}:
    print('\n')

    abecedario = list(map(chr, range(97, 123)))                                                         # Abecedario en minusculas

    proposicion = str(input('Proposicion =>> '))                                                                    # Espacio para escribir la ecuacion logica

    Psimples = list(set([i for i in proposicion if i.lower() in abecedario]))                           # Proposiciones simples existentes en la ecuacion
    Psimples.sort()                                                                                     # Orden de las proposiciones simbles alfabeticamente
    copiaP = Psimples.copy()

    sustitucion = ['z', 'i', 'u', 'm' ,'f', 'j']
    s = 0
    for i in copiaP:
        if i in ['a','n','d', 'o', 'r', 't']:
            Psimples.insert(Psimples.index(i), sustitucion[s % 6])
            Psimples.pop(Psimples.index(i))
        s += 1
    for i in range(len(copiaP)): proposicion = proposicion.replace(copiaP[i], Psimples[i])

    proposicion = ''.join(proposicion.split())

    proposicion = ((((proposicion.replace('||', ' or ')).replace('&&', ' and ')).replace('!', ' not ')).replace('+', ' or ')).replace('*', ' and ')    # reemplazar nomenclatura

    if '<-->' in proposicion or '<->' in proposicion:
        inex = proposicion.index('<-->')
        if '<->' in proposicion: inex = proposicion.index('<-->')

        pass    # no hace nada aun


    if '->' in proposicion:
        inex = proposicion.index('->')
        if '-->' in proposicion: inex = proposicion.index('-->')
        proposicion = proposicion[:inex - 1] + ' not ' +proposicion[inex - 1:]
        proposicion = proposicion.replace('-->', ' or ')
        
        pass    # solo un --> acepta bien

    for x in copiaP: print('|' + x, end='')                                                           # Imprime las proposiciones
    print('|')
    print(' -'*len(Psimples))

    print(proposicion) #####################

    cantidad = 2**len(Psimples)                                                                         # Cantidad de valores de verdad por proposicion
    permuta = []                                                                                        # Valores de verdad
    for i in range(len(Psimples)):                                                                      # Generador de listas de valores de verdad por posicion de Psimple
        h = []
        while len(h) != cantidad:
            unos = ('1'*2**i)
            ceros = ('0'*2**i)
            try:
                unos = unos.split('')
                ceros = ceros.split('')
            except ValueError: pass
            total = list(map(lambda x: int(x), unos+ceros))
            h += total
        permuta.append(h)


    for i in range(cantidad):
        print('|', end='')
        iterador = 0
        ans = proposicion
        for j in range(len(Psimples) - 1, -1, -1):
            if j != len(Psimples) - 1: print('', permuta[j][i], end='')
            else: print(permuta[j][i], end='')
            ans = ans.replace(str(Psimples[iterador]), str(permuta[j][i]))
            iterador += 1
        print('|  ', int(bool(eval(ans))), bool(eval(ans)))
    print('\n')
    pregunta = str(input('Otra proposicion? (y/n) '))