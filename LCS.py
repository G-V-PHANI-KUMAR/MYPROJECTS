import os,time

def longestcommonsubstr(str1: str,str2: str,verbose=False):
    a,b=len(str1),len(str2)
    matrix = [[0 for i in range(b+2)] for j in range(a+2)]
    for i in range(len(str1)):
        matrix[i+2][0]=str1[i]
    for j in range(len(str2)):
        matrix[0][j+2]=str2[j]        
    for i in range(2,a+2):
        for j in range(2,b+2):
            if str1[i-2]==str2[j-2]:
                matrix[i][j]=1+matrix[i-1][j-1]
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
            if verbose:
                printmat(matrix)
    return matrix,matrix[a+1][b+1]

def printmat(matrix):
        for i in matrix:
            print(list(map(str,i)))
        time.sleep(2) # change to how slow you want the screen to move!
        os.system('cls' if os.name == 'nt' else 'clear')

def doteffect():
        for _ in range(3):
           print('.',end='')
        print()
        time.sleep(3)

def pathtrav(str1,str2,matrix):
    row,col = len(str1)+1,len(str2)+1
    s=''
    print("Traversing back",end='')
    doteffect()
    while matrix[row][col]!=0:
        if matrix[row-1][col]==matrix[row][col-1] and matrix[row][col]!=matrix[row-1][col]:
            s=s+str1[row-2]
            matrix[row][col]='*'
            row-=1
            col-=1
        else:
            while matrix[row][col]==matrix[row-1][col]:
                matrix[row][col]='*'
                printmat(matrix)
                row-=1
            while matrix[row][col]==matrix[row][col-1]:
                matrix[row][col]='*'
                printmat(matrix)
                col-=1
        printmat(matrix)
    return s[::-1]

str1,str2=input("Enter string 1:"),input("Enter String 2:")
matrix,lcslen=longestcommonsubstr(str1,str2,True)
lcs=pathtrav(str1,str2,matrix)
print(lcs,lcslen)
        