#Sherri and Jesse's Circuit Solver

#Get input from user as to what elements are in the circuit







#Set up matrix equation and solve

def solve(component):

    A = np.array([])  #create empty set -- will be matrix with all equations
    b = np.array([])  #create empty set -- will be matrix in eqn Ax=b

    for i in range(len(component)):
        for j in range(len(component)+1):
            A[i][j] = 0                     #fill with zeroes: need number of rows to be number of components (nodes) plus current (in series circuit, current is all the same)
            b[j] = 0
            return A

    A[0][0] = 0                          #make row 1 of A say that Vgrd = 0
    

    for i in range(len(component)):   #length of input should be number of devices
         
                                
        if component[i].type == "b":   #if device is a battery 

            A[i][i] = -1                #negative terminal voltage should be -1 as coeff
            A [i][i+1] = 1              #positive terminal voltage should be 1 as coeff
            
            b[i] = component[i].voltage

        else:

            A[i][i] = -1
            A[i][i+1] = 1
            A[i][len(component)] = -1*component[i].resistance


    return A
    return b
            
            
                        
        
