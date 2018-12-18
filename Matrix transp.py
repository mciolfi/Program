def transp (matrix):
    mt = []
    for i in range(len(matrix[0])): mt.append([float(matrix[j][i]) for j in range(len(matrix))])
    return (mt)
matrix = [[1,2],[3,4],[5,6]]
mt = transp (matrix)
print (mt)
