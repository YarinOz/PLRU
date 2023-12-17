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

def TOUCH(line):  # check if line is miss or hit
    if line not in valid_inputs:
        print("Invalid line!")
        return
    #hit = False
    for i in range(8,16):
    # hit
        if line == G.nodes[i]['state']:  
            traverseal = nx.shortest_path(G, source=1, target=i)
            print("Hit!", traverseal)
            for i in traverseal[:-1]:
                G.nodes[i]['state'] = 1 - G.nodes[i]['state'] # toggle state
            return
    # miss
    plru = PLRU()
    print("Miss!", plru)
    G.nodes[plru]['state'] = line
    traverseal = nx.shortest_path(G, source=1, target=plru)
    for i in traverseal[:-1]:
        G.nodes[i]['state'] = 1 - G.nodes[i]['state'] # toggle state
    return
        
# 0 is left, 1 is right, PLRU returns PLRU line (8,9,10,11,12,13,14,15)
def PLRU():
    plru = 1                     # start at root
    state = G.nodes[plru]['state']
    if state == 0:               # left
        plru = 2
        if state == 0:           # left.left
            plru = 4
            if state == 0:       # left.left.left    A
                plru = 8
                return plru
            elif state == 1:     # left.left.right   B
                plru = 9
                return plru
        elif state == 1:         # left.right
            plru = 5
            if state == 0:       # left.right.left   C
                plru = 10
                return plru
            elif state == 1:     # left.right.right  D
                plru = 11
                return plru
    elif state == 1:             # right
        plru = 3
        if state == 0:           # right.left
            plru = 6
            if state == 0:       # right.left.left   E
                plru = 12
                return plru
            elif state == 1:     # right.left.right  F
                plru = 13
                return plru
        elif state == 1:         # right.right
            plru = 7
            if state == 0:       # right.right.left  G
                plru = 14
                return plru
            elif state == 1:     # right.right.right H
                plru = 15
                return plru
        
G=nx.Graph()
G.add_edges_from([(1,2), (1,3), (2,4), (2,5), (3,6), (3,7), (4,8), (4,9),
                  (5,10), (5,11), (6,12), (6,13), (7,14), (7,15)])

PLRU_bits = [1,2,3,4,5,6,7]          # 1, 2, 3, 4, 5, 6, 7 state nodes
lines = [8,9,10,11,12,13,14,15] # A, B, C, D, E, F, G, H
valid_inputs = ['A','B','C','D','E','F','G','H','X','Y','Z']

for i in PLRU_bits:
    G.nodes[i]['state']=0
for i,j in zip(lines,['A','B','C','D','E','F','G','H']):
    G.nodes[i]['state']=j

##### Run touch sequence #####  touch only lines in valid_inputs
print("Choose a line to touch:")
line = TOUCH(input())


node_states = {i: G.nodes[i]['state'] for i in G.nodes}
pos = hierarchy_pos(G,1)
nx.draw(G, pos=pos, labels=node_states,font_size=22,with_labels=True, node_size=1200)
plt.savefig('PLRU_DT.png')
