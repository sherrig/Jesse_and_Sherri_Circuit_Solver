import numpy as np

class R:
    def __init__(self, name, posnode, negnode, resistance, ref):
        self.name = name
        self.posnode = posnode
        self.negnode = negnode
        self.resistance = float(resistance)
        self.ref = {self.posnode:1, self.negnode: -1, 'current': -self.resistance, "c" : 0}
        

class B:
    def __init__(self, name, posnode, negnode, voltage, ref):
       self.name = name
       self.posnode = posnode
       self.negnode = negnode
       self.voltage = float(voltage)
       self.ref = {self.posnode: 1, self.negnode:-1, "current": 0, "c" : self.voltage}


def get_nodes(components):
    unk_nodes = []
    for i in components:
        if unk_nodes.count(i.posnode) == 0:
            unk_nodes.append(i.posnode)

        if unk_nodes.count(i.negnode) == 0:
            unk_nodes.append(i.negnode)
    return unk_nodes

def solve (components):
    nodes = get_nodes(components)
    
    n = len(nodes)+len(components)
    x = nodes+components
    A = np.zeros(n)
    A[nodes.index("gnd")] =1
    b = np.array([0]) #ground
    for i in components:
        temp = np.zeros(n)
        temp[nodes.index(i.posnode)] = i.ref[i.posnode]
        temp[nodes.index(i.negnode)] = i.ref[i.negnode]
        temp[x.index(i)] = i.ref["current"]
        A = np.vstack((A,temp))
        b = np.vstack((b, [i.ref["c"]]))

    for i in nodes:
        if i != "gnd":
            temp = np.zeros(n)
            for j in components:
                if i == j.posnode:
                    temp[x.index(j)] = -1
                if i == j.negnode:
                    temp[x.index(j)] = 1
            A = np.vstack((A, temp))
            b = np.vstack((b, [0]))
 
        
    #print "A =", A
    #print "b = ", b
    solved = np.linalg.solve(A,b)
    #print x, solved
    for i in range(len(nodes)):
        print "the voltage at ", nodes[i], " is " , solved[i]
    for i in range(len(components)):
        print "the current across ", components[i].name, " is ", solved[len(nodes)+i]

    

##r1 = R("r1", "e1", "e0", 4, {})
##b1 = B("b1", "e0", "gnd", 7, {})
##r2 = R("r2", "e1", "gnd", 2, {})
##r3 = R("r3", "e1", "gnd", 6, {})
##b2 = B ("b2", "e1", "gnd", 3, {})
##components = [r1, b1, r2, r3, b2]
##components_dict = {"r1":r1,"r2":r2,"r3":r3,"b1":b1,"b2":b2}
##solve(components)
