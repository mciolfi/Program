def determinante(m):
    #Módulo para obtenção de determinante de matriz 2x2 ou 3x3
    #det2x2=+x[0][0]*x[1][1]
    #       -x[0][1]*x[1][0]
    #det3x3=+x[0][0]*x[1][1]*x[2][2]
    #       +x[0][1]*x[1][2]*x[2][0]
    #       +x[0][2]*x[1][0]*x[2][1]
    #       -x[0][2]*x[1][1]*x[2][0]
    #       -x[0][1]*x[1][0]*x[2][2]
    #       -x[0][0]*x[1][2]*x[2][1]
    # Definindo as variáveis
    a = 0
    b = 0
    c = len(x)-1
    mult1 = 1
    mult2 = 1
    loop = 0
    det = 0
    soma = []
    if len(x) == 2: d = len(x)-1 #Matriz 2x2
    if len(x) == 3: d = len(x)-2 #Matriz 3x3
    while loop == 0:
        mult1 = mult1*x[a][b]
        mult2 = mult2*x[a][c]
        if a == len(x)-1 and b == d: loop = 1
        a = a+1
        b = b+1
        c = c-1
        if a > len(x)-1:
            a = 0
            soma.append(mult1-mult2)
            # print (mult1,-mult2) #Apresenta os valores obtidos pela Regra de Sarrus
            mult1 = 1
            mult2 = 1
            b = len(soma)
            c = len(x)-len(soma)-1
        if b > len(x)-1: b = 0
        if c < 0: c = len(x)-1
    for cont in range(len(soma)): det += soma[cont]
    return det
def matrizinv(x,det): #Faz inversão das matrizes com base no determinante
    #Definindo variáveis
    xt = []
    madj = []
    #Transpondo a matriz
    for i in range(len(x)):
        linha = []
        for j in range(len(x)):
            linha.append(x[j][i])
        xt.append(linha)
    #Obtendo a matriz adjunta atraves o determinante das matrizes menores 2x2, aplicando o sinal e 1/det
    #madj[0][0]=xt[1][1]*xt[2][2]-xt[1][2]*xt[2][1]
    #madj[0][1]=xt[1][0]*xt[2][2]-xt[1][2]*xt[2][0]
    #madj[0][2]=xt[1][0]*xt[2][1]-xt[1][1]*xt[2][0]
    #madj[1][0]=xt[0][1]*xt[2][2]-xt[0][2]*xt[2][1]
    #madj[1][1]=xt[0][0]*xt[2][2]-xt[0][2]*xt[2][0]
    #madj[1][2]=xt[0][0]*xt[2][1]-xt[0][1]*xt[2][0]
    #madj[2][0]=xt[0][1]*xt[1][2]-xt[0][2]*xt[1][1]
    #madj[2][1]=xt[0][0]*xt[1][2]-xt[0][2]*xt[1][0]
    #madj[2][2]=xt[0][0]*xt[1][1]-xt[0][1]*xt[1][0]
    for i in range(len(x)):
        if i == 0: a = 1
        else: a = 0
        if i == 2: b = 1
        else: b = 2
        linha = []
        for j in range(len(x)):
            if j == 0: c = 1
            else: c = 0
            if j == 2: d = 1
            else: d = 2
            #Adiciona os sinais conforme posição na matriz
            if (i+j)%2 == 0: calc = (xt[a][c]*xt[b][d]-xt[a][d]*xt[b][c])/int(det)
            else: calc = -(xt[a][c]*xt[b][d]-xt[a][d]*xt[b][c])/int(det)
            if calc == -0: calc = 0 #Corrige sinal negativo no zero
            linha.append(calc)
        madj.append(linha)
    #Inversa da matriz XtX (inversão por matriz adjunta)
    #det=XtX[0][0]*XtX[1][1]-XtX[0][1]*XtX[1][0]
    #inv=[[0,0],[0,0]]
    #inv[0][0]=XtX[1][1]/det
    #inv[1][1]=XtX[0][0]/det
    #inv[0][1]=-XtX[1][0]/det
    #inv[1][0]=-XtX[0][1]/det
    #Encontrando ângulo Beta
    #beta=[0,0]
    return(madj)
x = [[3,0,2],[2,0,-2],[0,1,1]]
det = determinante (x)
if det == 0: print ('Não existe matriz inversa')
else: print ('Matriz inversa possível, determinante = ',det)
inv = matrizinv(x,det)
print (inv)
