#Sherri and Jesse's Circuit Solver

#Get input from user as to what elements are in the circuit







#Set up matrix equation and solve

def solve(in_put):

    A = np.array([])  #create empty set -- will be matrix with all equations
    b = np.array([])  #create empty set -- will be matrix in eqn Ax=b

    row1 = [1]                          #make row 1 of A say that Vgrd = 0
    for i in range(2*len(in_put)-1):   #add 1 less than 2*number of devices of zeroes to the first row
        row1.append(0)
        return row1

    A.append(row1)
    b.append(0)

    for i in range(len(in_put)):   #length of input should be number of devices
                                    #assumption that input looks like (battery or resistor, positive terminal, negative terminal, value)
        if in_put[i][0] == battery:   #if device is a battery (can change exact way of knowing if it's a battery)
            new_row = []
            new_row.insert(i, 1)
            
                        
        
