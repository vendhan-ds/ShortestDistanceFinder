mat = [[0, 3, 0, 0, 4], [3, 0, 2, 0, 5], [
    0, 2, 0, 6, 1], [0, 0, 6, 0, 0], [4, 5, 1, 0, 0]]
v = 5
count = 0


def printPathUtil(u, d, visited, path, pi, count):
    #print("entered path util")
    visited[u] = 1
    path.append(u)
    pi += 1

    if (u == d):
        print("path length :", count)
        print(path)
        """ for j in range(pi):
            print(path[j]) """
    else:
        temp = mat[u]
        # print(temp)
        for k in range(v):
            temp2 = temp[k]
            if ((temp2 != 0) & (visited[k] == 0)):
                count = count+temp2
                printPathUtil(k, d, visited, path, pi, count)
                count = count-temp2
    path.pop()
    pi = pi-1
    visited[u] = 0


def printPath(s, d):
    # console.log("entered driver")print("entered printpath")
    count = 0
    visited = [0]*v
    path = []
    pi = 0
    print("enterd printpath")
    # print(path)
    printPathUtil(s, d, visited, path, pi, count)


print("hi")
printPath(0, 3)
