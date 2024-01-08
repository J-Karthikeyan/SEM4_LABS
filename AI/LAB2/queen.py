count = 0
for i in range(8):
    for j in range(8):
        matrix = [[0 for _ in range(8)] for _ in range(8)]
        for k in range(8):
            for l in range(8):
                if k==i or l==j or abs(i-k) == abs(j-l):
                    continue
                else:
                    matrix[k][l] = 1
        for x in range(8):
            for y in range(8):
                if matrix[x][y]:
                    count+=1

print(count/2)
