# -*- coding: utf-8 -*-
import networkx as nx

# 创建有向图
G = nx.DiGraph()
# 有向图之间边的关系
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
for edge in edges:
    G.add_edge(edge[0], edge[1])
pageRank_list = nx.pagerank(G, alpha=1)
print("pageRank值是：", pageRank_list)