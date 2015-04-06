########################################
##Title: DC Circuit Solver                
##Filename: Circuit_Solver.py
##Authors: Sherri Green and Jesse Chang
##Most Recent Edit: 4/6/15
##Last Editor: Sherri Green
########################################

import numpy as np

class R:                                                            #Create Resistor Class
    def __init__(self, name, posnode, negnode, resistance):  #(self, name of device (eg. "b1"), name of positive node, name of negative node, resistance value, empty dictionary)
        self.name = name
        self.posnode = posnode
        self.negnode = negnode
        self.resistance = float(abs(resistance))
        self.ref = {self.posnode:1, self.negnode: -1, 'current': -self.resistance, "c" : 0}
        

class B:
    def __init__(self, name, posnode, negnode, voltage):
       self.name = name
       self.posnode = posnode
       self.negnode = negnode
       self.voltage = float(voltage)
       self.ref = {self.posnode: 1, self.negnode:-1, "current": 0, "c" : self.voltage}   #current isn't acutally 0 -- but we don't have a -IR term, so we make it 0


def get_nodes(components):                                              #function to get list of nodes (nodes are strings) from list of components
    unk_nodes = []
    for i in components:
        if unk_nodes.count(i.posnode) == 0:                             #if the number of times the string for posnode appears in the unknown nodes list = 0
            unk_nodes.append(i.posnode)

        if unk_nodes.count(i.negnode) == 0:
            unk_nodes.append(i.negnode)
    return unk_nodes

def solve (components):                                                 #list of components that user inputs
    nodes = get_nodes(components)                                       #get list of nodes from the list of components
    
    n = len(nodes)+len(components)                                      #number of rows in matrix A
    x = nodes+components                                                #concatenate lists of nodes and components (for order)
    A = np.zeros(n)
    A[nodes.index("gnd")] =1
    b = np.array([0])                                                   #ground
    for i in components:                                                #Voltages at nodes
        temp = np.zeros(n)                                              #row to be added to A
        temp[nodes.index(i.posnode)] = i.ref[i.posnode]                #take value from dictionary associated with posnode and put it in the temporary row in column associated with that node 
        temp[nodes.index(i.negnode)] = i.ref[i.negnode]
        temp[x.index(i)] = i.ref["current"]                             #for resistors
        A = np.vstack((A,temp))
        b = np.vstack((b, [i.ref["c"]]))

    for i in nodes:                                                     #currents through devices (junction rule)
        if i != "gnd":
            temp = np.zeros(n)
            for j in components:
                if i == j.posnode:                                      #posnodes flowing out
                    temp[x.index(j)] = -1
                if i == j.negnode:                                      #negnodes flowing in
                    temp[x.index(j)] = 1
            A = np.vstack((A, temp))
            b = np.vstack((b, [0]))
 
        
    #print "A =", A
    #print "b = ", b
    solved = np.linalg.solve(A,b)                                       #Ax=b. this gives x
    solutions = {}
    #print x, solved
    for i in range(len(nodes)):
        solutions[nodes[i]] = solved[i]                                 #puts node into dictionary with voltage (as an array) as reference
        print "the voltage at ", nodes[i], " is " , solved[i]
    for i in range(len(components)):
        solutions[components[i].name] = solved[len(nodes)+i]            #puts component into dictionary with current (as array) as reference
        print "the current across ", components[i].name, " is ", solved[len(nodes)+i]
    return solutions

    
##Testing
        
r1 = R("r1", "e1", "e0", -4)
b1 = B("b1", "e0", "gnd", -7)
r2 = R("r2", "e1", "gnd", 2)
r3 = R("r3", "e1", "gnd", 6)
b2 = B ("b2", "e1", "gnd", 3)
components = [r1, b1, r2, r3, b2]
components_dict = {"r1":r1,"r2":r2,"r3":r3,"b1":b1,"b2":b2}
sol = solve(components)
##print sol
