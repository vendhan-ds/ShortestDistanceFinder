import networkx as nx
import matplotlib.pyplot as plt
import random
from tkinter import *

v = 0
count = 0


arr = []
start = 0
end = 0


l = [i for i in range(v)]

allpaths = []


class GraphVisualization:
    def __init__(self):
        self.visual = []
        self.wowt = []

    def addEdge(self, a, b, w):
        temp = (str(a), str(b), w)
        temp1 = (str(a), str(b))
        self.visual.append(temp)
        self.wowt.append(temp1)

    def visualize(self):
        G = nx.Graph()
        for i in range(len(self.visual)):
            G.add_edge(self.visual[i][0], self.visual[i]
                       [1], weight=self.visual[i][2])

        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size=450, node_color='b')

        nx.draw_networkx_edges(G, pos, edgelist=self.visual, width=2)

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels, font_size=6, font_family="sans-serif")
        nx.draw_networkx_labels(G, pos, font_size=8, font_color='w')

        ax = plt.gca()
        ax.margins = 0.08
        plt.axis("off")
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(8)
        plt.close()
        plt.clf()

    def dRAW(self, path, list_of_tuples):
        G = nx.Graph()
        for i in range(len(self.visual)):
            G.add_edge(self.visual[i][0], self.visual[i]
                       [1], weight=self.visual[i][2])

        einpath = [(str(u), str(v)) for (u, v, w) in list_of_tuples]
        eninpath = []
        for item in self.wowt:
            if (item not in list_of_tuples):
                eninpath.append(item)

        pos = nx.spring_layout(G, seed=7)
        color = ["#"+''.join([random.choice('0123456789ABCDEF')
                             for j in range(6)]) for i in range(10)]
        nx.draw_networkx_nodes(
            G, pos, node_color=f'{random.choice(color)}', node_size=450)
        pos = nx.spring_layout(G, seed=7)

        nx.draw_networkx_edges(G, pos, edgelist=einpath,
                               width=6, style="dashed", edge_color='b')
        nx.draw_networkx_edges(G, pos, edgelist=eninpath, width=1)

        nx.draw_networkx_labels(G, pos, font_size=8, font_color='w')

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels, font_size=6, font_family="sans-serif", font_color='g')

        weight = 0
        for i in range(len(list_of_tuples)):
            weight += list_of_tuples[i][2]

        ax = plt.gca()
        ax.margins = 0.08
        plt.axis("off")
        plt.tight_layout()
        plt.title(f"Path Length : {weight}")
        plt.show(block=False)
        plt.pause(6)
        plt.close()
        plt.clf()

# algo for finding all paths


def getpath(start, destination):
    weight = 0
    visited = [0]*v
    pathonly = []
    helper(start, destination, visited, pathonly, weight)


def helper(start, destination, visited, pathonly, weight):
    visited[start] = 1
    pathonly.append(start)

    if (start == destination):
        visited[start] = 0
        a = []
        for i in range(len(pathonly)):
            a.append(pathonly[i])
        allpaths.append(a)
        pathonly.pop()
        return

    for i in range(v):
        if ((arr[start][i] != 0) & (visited[i] == 0)):
            weight += arr[start][i]
            helper(i, destination, visited, pathonly, weight)
            weight -= arr[start][i]

    pathonly.pop()
    visited[start] = 0


def getedgewithwt(path):
    lot = [(path[i], path[i + 1], arr[path[i]][path[i + 1]])
           for i in range(len(path) - 1)]
    return lot


def getnodes(path):
    lot = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    return lot


#getpath(0, 3)


##############################
""" v = 5
    mat = [[0, 3, 2, 0], [3, 0, 0, 4], [2, 0, 0, 5], [0, 4, 5, 0]]
    def printPathUtil(u, d, visited, path, pi, count):
    #print("entered path util")
    visited[u] = 1
    path.append(u)
    pi += 1

    if (u == d):
        print("path length :", count)
        print(path)
        # feeder(path)
        for j in range(pi):
            print(path[j]) 
    else:
        temp = matrix[u]
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
    print(s, d, matrix)
    count = 0
    visited = [0]*v
    path = []
    pi = 0
    print("enterd printpath")
    # print(path)
    printPathUtil(s, d, visited, path, pi, count)


print("hi")
printPath(0, 3)
 """


def construct(n):
    global arr
    arr = [[0 for i in range(n)] for j in range(n)]


def matConstructor(a, b, w):
    arr[a][b] = w
    arr[b][a] = w


root = Tk()
root.title("CGT PROJECT")


def onClick():
    global v
    global vertexCount
    vertexCount = int(textField.get())
    v = vertexCount
    construct(vertexCount)

    newWindow()


def displayData(leaf, vertex1, vertex2, weight):

    printLabel = Label(leaf, text="(" + str(vertex1) + " , " +
                       str(vertex2) + ")" + "  ->  " + "(" + weight + ")")
    printLabel.pack()


def nextButtonClick(leaf, firstField, secondField, weightField):

    vertex1 = firstField.get()
    vertex2 = secondField.get()
    weight = weightField.get()

    matConstructor(int(vertex1), int(vertex2), int(weight))
    # print(matrix)
    displayData(leaf, vertex1, vertex2, weight)

    firstField.delete(0, END)
    secondField.delete(0, END)
    weightField.delete(0, END)


def endButtonClick(a, b, c, e, f):
    a.destroy()
    b.destroy()
    getpath(int(c.get()), int(e.get()))

    G = GraphVisualization()


# print original graph
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (arr[i][j] != 0):
                G.addEdge(i, j, arr[i][j])
    G.visualize()
# print paths
    for path in allpaths:
        leng = 0
        e_w_wt = getedgewithwt(path)
        for a in e_w_wt:
            leng = leng+a[2]
        print("path :", path, ",weight :", leng)
        G.dRAW(path, e_w_wt)


def stopButtonClick(leaf, label2, label3, firstField, secondField, weightField, nextButton, stopButton):
    print(arr)
    label2.destroy()
    label3.destroy()

    firstField.destroy()
    secondField.destroy()
    weightField.destroy()

    nextButton.destroy()
    stopButton.destroy()
    # leaflet=Tk()
    label20 = Label(leaf, text="start point : ")
    label20.pack()
    label21 = Label(leaf, text="destination point : ")
    label21.pack()
    start = Entry(leaf, width=10, borderwidth=3)
    end = Entry(leaf, width=10, borderwidth=3)
    start.pack()
    end.pack()
    endButton = Button(leaf, text="DONE", command=lambda: endButtonClick(
        label20, label21, start, end, endButton))
    endButton.pack()


def newWindow():

    root.destroy()

    leaf = Tk()
    leaf.title("ENTER DATA")

    label2 = Label(leaf, text="Enter vertices and their weights below")
    label2.pack()

    label3 = Label(leaf, text="Format: vertex1 vertex2 weight12")
    label3.pack()

    firstField = Entry(leaf, width=10, borderwidth=3)
    firstField.pack()

    secondField = Entry(leaf, width=10, borderwidth=3)
    secondField.pack()

    weightField = Entry(leaf, width=10, borderwidth=5)
    weightField.pack()

    nextButton = Button(leaf, text="Next", command=lambda: nextButtonClick(
        leaf, firstField, secondField, weightField))
    nextButton.pack()

    stopButton = Button(leaf, text="enter start and destination", command=lambda: stopButtonClick(
        leaf, label2, label3, firstField, secondField, weightField, nextButton, stopButton))
    stopButton.pack()

    leaf.mainloop()


label = Label(root, text="Total number of vertices in your Graph : ")
label.pack()

textField = Entry(root, width=50, borderwidth=5)
textField.pack()

textFieldButton = Button(root, text="OK", command=onClick)
textFieldButton.pack()

root.mainloop()
################################
