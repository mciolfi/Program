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
        if i == 0:
            a = 1
        else:
            a = 0
        if i == 2:
            b = 1
        else:
            b = 2
        linha = []
        for j in range(len(x)):
            if j == 0:
                c = 1
            else:
                c = 0
            if j == 2:
                d = 1
            else:
                d = 2
            if (i+j)%2 == 0:
                calc = (x[a][c]*x[b][d]-x[a][d]*x[b][c])/int(det)
            else:
                calc = -(x[a][c]*x[b][d]-x[a][d]*x[b][c])/int(det)
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
x = [[1,1,0],[0,1,1],[1,0,2]]
inv = matrizinv(x,'3')
print (inv)
from numpy import matrix
from numpy import linalg
A = matrix (x)
print (A.T)
print (A*x)
print (A.I) 
