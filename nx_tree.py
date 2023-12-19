import matplotlib.pyplot as plt
import networkx as nx
import random

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None): 
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

            
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def TOUCH(line,plru):  # check if line is miss or hit
    if line not in valid_inputs:
        print("Invalid line!")
        return
    for i in range(8,16):
    # hit
        if line == G.nodes[i]['state']:  
            traverseal = nx.shortest_path(G, source=1, target=i)
            print("Hit!")
            # print("Path:", traverseal)
            if (G.nodes[traverseal[0]]['state'] == 0 and i in [8,9,10,11]) or (G.nodes[traverseal[0]]['state'] == 1 and i in [12,13,14,15]):
                G.nodes[traverseal[0]]['state'] = 1 - G.nodes[traverseal[0]]['state'] # toggle root state
            if (G.nodes[traverseal[1]]['state'] == 0 and i in [8,9,12,13]) or (G.nodes[traverseal[1]]['state'] == 1 and i in [10,11,14,15]):
                G.nodes[traverseal[1]]['state'] = 1 - G.nodes[traverseal[1]]['state'] # toggle level2 state
            if (G.nodes[traverseal[2]]['state'] == 0 and i%2==0 ) or (G.nodes[traverseal[2]]['state'] == 1 and i%2==1):
                G.nodes[traverseal[2]]['state'] = 1 - G.nodes[traverseal[2]]['state'] # toggle level3 state
            return  
    # miss
    print("Miss!")
    G.nodes[plru]['state'] = line
    traverseal = nx.shortest_path(G, source=1, target=plru)
    for i in traverseal[:-1]:
        G.nodes[i]['state'] = 1 - G.nodes[i]['state'] # toggle state
    return
        
# 0 is left, 1 is right, PLRU returns PLRU line (8,9,10,11,12,13,14,15)
# def PLRU():
#     plru = 1                     # start at root
#     state = G.nodes[plru]['state']
#     if state == 0:               # left
#         plru = 2
#         if state == 0:           # left.left
#             plru = 4
#             if state == 0:       # left.left.left    A
#                 plru = 8
#                 return plru
#             elif state == 1:     # left.left.right   B
#                 plru = 9
#                 return plru
#         elif state == 1:         # left.right
#             plru = 5
#             if state == 0:       # left.right.left   C
#                 plru = 10
#                 return plru
#             elif state == 1:     # left.right.right  D
#                 plru = 11
#                 return plru
#     elif state == 1:             # right
#         plru = 3
#         if state == 0:           # right.left
#             plru = 6
#             if state == 0:       # right.left.left   E
#                 plru = 12
#                 return plru
#             elif state == 1:     # right.left.right  F
#                 plru = 13
#                 return plru
#         elif state == 1:         # right.right
#             plru = 7
#             if state == 0:       # right.right.left  G
#                 plru = 14
#                 return plru
#             elif state == 1:     # right.right.right H
#                 plru = 15
#                 return plru
def color():
    node = 1
    if G.nodes[node]['state'] == 0:
        G[node][node+1]['color'] = 'red'
        node+=1
        if G.nodes[node]['state'] == 0:
            G[node][node+2]['color'] = 'red'
            node+=2
            if G.nodes[node]['state'] == 0:
                G[node][node+4]['color'] = 'red'
                plru = node+4
                return plru
            elif G.nodes[node]['state'] == 1:
                G[node][node+5]['color'] = 'red'
                plru = node+5
                return plru
        elif G.nodes[node]['state'] == 1:
            G[node][node+3]['color'] = 'red'
            node+=3
            if G.nodes[node]['state'] == 0:
                G[node][node+5]['color'] = 'red'
                plru = node+5
                return plru
            elif G.nodes[node]['state'] == 1:
                G[node][node+6]['color'] = 'red'
                plru = node+6
                return plru
    elif G.nodes[node]['state'] == 1:
        G[node][node+2]['color'] = 'red'
        node+=2
        if G.nodes[node]['state'] == 0:
            G[node][node+3]['color'] = 'red'
            node+=3
            if G.nodes[node]['state'] == 0:
                G[node][node+6]['color'] = 'red'
                plru = node+6
                return plru
            elif G.nodes[node]['state'] == 1:
                G[node][node+7]['color'] = 'red'
                plru = node+7
                return plru
        elif G.nodes[node]['state'] == 1:
            G[node][node+4]['color'] = 'red'
            node+=4
            if G.nodes[node]['state'] == 0:
                G[node][node+7]['color'] = 'red'
                plru = node+7
                return plru
            elif G.nodes[node]['state'] == 1:
                G[node][node+8]['color'] = 'red'
                plru = node+8
                return plru
            
if __name__ == "__main__":
        
    G=nx.Graph()
    G.add_edges_from([(1,2), (1,3), (2,4), (2,5), (3,6), (3,7), (4,8), (4,9),
                    (5,10), (5,11), (6,12), (6,13), (7,14), (7,15)])

    PLRU_bits = [1,2,3,4,5,6,7]          # 1, 2, 3, 4, 5, 6, 7 state nodes
    lines = [8,9,10,11,12,13,14,15] # A, B, C, D, E, F, G, H
    valid_inputs = ['A','B','C','D','E','F','G','H','X','Y','Z']

    # state assignment
    for i in PLRU_bits:
        G.nodes[i]['state']=0
    for i,j in zip(lines,['A','B','C','D','E','F','G','H']):
        G.nodes[i]['state']=j
    #first coloring
    for i in G.edges():
        G[i[0]][i[1]]['color'] = 'black'
    plru = color()
    ##### Run touch sequence in format {line1 line2 line3 ...}#####  touch only lines in valid_inputs
    print("Choose a line to touch:")

    line_seq = input().split(' ')
    for line in line_seq:
        TOUCH(line,plru)
        plru = color()
        
    # color edges
    for i in G.edges():
        G[i[0]][i[1]]['color'] = 'black'
    color()
    edge_colors = [G[u][v]['color'] if 'color' in G[u][v] else 'black' for u, v in G.edges()]
    node_states = {i: G.nodes[i]['state'] for i in G.nodes}
    pos = hierarchy_pos(G,1)
    nx.draw(G, pos=pos, labels=node_states,font_size=22,with_labels=True, node_size=1200, edge_color=edge_colors)
    plt.savefig('PLRU_DT.png')

