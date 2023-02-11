import matplotlib.pyplot as plt
import networkx as nx
from tkinter import *

# koru code
root = Tk()
root.title("CGT PROJECT")


def onClick():

    global vertexCount
    vertexCount = int(textField.get())

    newWindow()


def displayData(leaf, vertex1, vertex2, weight):

    printLabel = Label(leaf, text="(" + str(vertex1) + " , " +
                       str(vertex2) + ")" + "  ->  " + "(" + weight + ")")
    printLabel.pack()


def nextButtonClick(leaf, firstField, secondField, weightField):

    vertex1 = firstField.get()
    vertex2 = secondField.get()
    weight = weightField.get()

    displayData(leaf, vertex1, vertex2, weight)

    firstField.delete(0, END)
    secondField.delete(0, END)
    weightField.delete(0, END)


def stopButtonClick(leaf, label2, label3, firstField, secondField, weightField, nextButton, stopButton):

    label2.destroy()
    label3.destroy()

    firstField.destroy()
    secondField.destroy()
    weightField.destroy()

    nextButton.destroy()
    stopButton.destroy()


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

    stopButton = Button(leaf, text="DONE", command=lambda: stopButtonClick(
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
# koru code
count = 0


class GraphVisualization:
    def __init__(self):
        global count
        count += 1
        self.visual = []
        self.weight = []

    def addEdge(self, a, b, w):
        temp = (str(a), str(b), w)
        self.visual.append(temp)
        self.weight.append(w)

    def visualize(self):
        G = nx.Graph()

        for i in range(len(self.visual)):
            G.add_edge(self.visual[i][0], self.visual[i]
                       [1], weight=self.visual[i][2])

        pos = nx.spring_layout9(G, seed=7)

        nx.draw_networkx_nodes(G, pos, node_size=270, node_color='y')

        nx.draw_networkx_edges(G, pos, edgelist=self.visual, width=2)

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels, font_size=6, font_family="sans-serif")
        nx.draw_networkx_labels(G, pos, font_size=8, font_color='g')

        ax = plt.gca()
        ax.margins = 0.08
        plt.axis("off")
        plt.tight_layout()
        plt.show()
        plt.savefig(f"g{count}.png")
        plt.clf()


a = [0, 1, 2, 3]
mat = [[0, 3, 0, 0, 4], [3, 0, 2, 0, 5], [
    0, 2, 0, 6, 1], [0, 0, 6, 0, 0], [4, 5, 1, 0, 0]]


def feeder(a, x):
    #x = GraphVisualization()
    for i in range(len(a)-1):
        G.addEdge(a[i], a[i+1], mat[a[i]][a[i+1]])


#feeder(a, G)
G = GraphVisualization()
G.addEdge(0, 2, 1)
G.addEdge(1, 2, 3)
G.addEdge(1, 3, 5)

G.visualize()


""" G = GraphVisualization()
G.addEdge(0, 3, 11)
G.addEdge(1, 2, 32)
G.addEdge(1, 0, 5)

G.visualize() """

""" G1 = GraphVisualization()
G1.addEdge(0, 2, 9)
G1.addEdge(1, 2, 1)
G1.addEdge(1, 3, 2)
G1.addEdge(5, 3, 4)
G1.addEdge(3, 4, 4)
G1.addEdge(1, 0, 3)
G1.visualize() """

#G1 = GraphVisualization()
mat = [[0, 3, 0, 0, 4], [3, 0, 2, 0, 5], [
    0, 2, 0, 6, 1], [0, 0, 6, 0, 0], [4, 5, 1, 0, 0]]
v = 5
count = 0
#mat = [[0, 3, 2, 0], [3, 0, 0, 4], [2, 0, 0, 5], [0, 4, 5, 0]]


def printPathUtil(u, d, visited, path, pi, count):
    #print("entered path util")
    visited[u] = 1
    path.append(u)
    pi += 1

    if (u == d):
        print("path length :", count)
        print(path)
        feeder(path)
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
#printPath(0, 3)

n = 4
matrix = [[0 for i in range(n)] for j in range(n)]


def matConstructor(a, b, w):
    matrix[a][b] = w
    matrix[b][a] = w
