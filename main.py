import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Defining a Class
class GraphVisualization:

    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()


df = pd.read_csv()

for index, row of df.itterrows();


