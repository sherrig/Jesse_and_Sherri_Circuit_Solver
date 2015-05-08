#################################
# Title: Project Part 1 Solution#
# Lesson: DC Circuits           #
# Filename: part_1.py	        #
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/17/2014	#
# Last Editor: Joe Griffin	#
#################################

# Relevant Classes: 6.01, 6.002, 6.005

# We will assemble a set of components by naming their leads identical names, and we will
#   create a list of equations based on the device equations and Kirchoff's Current Law.

##TO-DO LIST:
##    List currents and nodes together in a convenient format (dictionary)
##    Create set of equations as numpy array, by extracting data from device
##        equations and by extracting equations from nodes/currents listing
##    Solve equations and re-associate the solution vector with the variable
##        names



import numpy as np

class onePort:
    def __init__(self, e2, e1, i):                      # Node connections and device current
        self.e1 = e1                                    #   are attributes, passed as strings
        self.e2 = e2
        self.i = i

class Resistor(onePort):
    def __init__(self, r, e2, e1, i):                   # Device characteristics are passed
        self.r = r                                      #   as values.
        self.e1 = e1
        self.e2 = e2
        self.i = i
        self.eq = [(1, self.e2),
                   (-1, self.e1),
                   (-self.r, self.i)
                   ]                                      # self.eq is the device law
                                                          # written as a list of tuples. The tuples contain (coefficient,
                                                          #variable) pairs, where coefficient is a number and variable
                                                          #is a string such that the sum of all the terms in the list
                                                          #is zero.  This gives e2-e1-ir=0 

class Battery(onePort):
    def __init__(self, v0, e2, e1, i):                  
        self.v0 = v0
        self.e1 = e1
        self.e2 = e2
        self.i = i
        self.eq = [(1, self.e2),
                   (-1, self.e1),
                   (-self.v0, None)                    # Device law If the variable is the value `None`, the coefficient term
                                                          #is assumed to be a constant.
                   ]

def sortCurrents(deviceList):                           # Returns a dictionary listing nodes and
    currents = {}                                       #   in/out currents
    for device in deviceList:
        if not device.e1 in currents:
            currents[device.e1] = [(1, device.i)]
        else:
            currents[device.e1].append((1, device.i))
        if not device.e2 in currents:
            currents[device.e2] = [(-1, device.i)]
        else:
            currents[device.e2].append((-1, device.i))
    return currents

def createEquations(deviceList, currentDict, GND):      # Returns a pair of numpy arrays A, b
    Vars = []                                           #   and a list of variable names that
    for device in deviceList:                           #   together represent the circuit's
        if not device.e1 in Vars:                       #   governing equations in the matrix
            Vars.append(device.e1)                      #   form Ax=b
        if not device.e2 in Vars:
            Vars.append(device.e2)
        if not device.i in Vars:
            Vars.append(device.i)
    A = np.zeros((len(Vars), len(Vars)))
    b = np.zeros(len(Vars))
    for devInd in xrange(len(deviceList)):              # First, we add the device equations
        for term in deviceList[devInd].eq:
            if not term[1] == None:                     # Not a constant term, devInd gives eq
                A[devInd][Vars.index(term[1])] = term[0]#   var.index(term[1]) gives variable
            else:
                b[devInd] = -term[0]                    # Constant term, place into correct eq

    numDevices = len(deviceList)
    nodeRowInd = 0
    for node in currentDict:                            # Next, we add junction rule equations
        eq = numDevices + nodeRowInd
        if not node == GND:
            for term in currentDict[node]:
                A[eq][Vars.index(term[1])] = term[0]
        else:
            A[eq][Vars.index(node)] = 1
        nodeRowInd += 1

    return (A, b, Vars)

def getSensitivity(A):                                  # Returns condition number of a matrix
    return np.linalg.cond(A)                            #   which indicates error sensitivity

def solveEqs(A, b, varList):                            # Returns a dictionary of variables
    if not np.linalg.det(A):
        return 'No solution'
    x = np.linalg.solve(A, b)
    sol = {}
    for index in xrange(len(varList)):
        sol[varList[index]] = x[index]
    return sol

def solveCircuit(deviceList, GND):
    currentDict = sortCurrents(deviceList)
    (A, b, varList) = createEquations(deviceList, currentDict, GND)
    return solveEqs(A, b, varList)
