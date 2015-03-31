#Sherri and Jesse's Circuit Solver

#Get input from user as to what elements are in the circuit

class Resistor:
    def __init__(self,resistance):
        self.resistance = resistance
        self.type = "r"
    def __str__(self):
        return 'a'
class Battery:
    def __init__(self,voltage):
        self.voltage = voltage
        self.type = "b"





#Set up matrix equation and solve
import numpy as np


def solve(component):

    A = np.zeros((len(component)+1, len(component)+1))  #create empty set -- will be matrix with all equations
    b = np.zeros((len(component)+1,1))  #create empty set -- will be matrix in eqn Ax=b

    A[0][0] = 1                         #make row 1 of A say that Vgrd = 0
    

    for i in range(len(component)-1):   #length of input should be number of devices
         
                                
        if component[i].type == "b":   #if device is a battery 

            A[i+1][i] = 1                #negative terminal voltage should be -1 as coeff
            A [i+1][i+1] = -1              #positive terminal voltage should be 1 as coeff
            
            b[i] = component[i].voltage

        else:

            A[i+1][i] = -1
            A[i+1][i+1] = 1
            A[i+1][len(component)] = -1*component[i].resistance

    if component[len(component)-1].type == "b":
        A[len(component)][0] = -1
        A[len(component)][len(component)-1] = 1

        b[len(component)] = component[len(component)-1].voltage

    else:
        A[len(component)][0] = -1
        A[len(component)-1][len(component)-1] = 1
        A[len(component)-1][len(component)] = -1*component[len(component)].resistance


    return A, b
    #return b
 #   x = np.linalg.solve(A,b)
    #return x
    
            
r1 = Resistor(4)
r2 = Resistor(5)
b1 = Battery(6)
b2 = Battery(7)
circuit = np.array([r1, r2, b1, b2])
print solve(circuit)           
                        
        
