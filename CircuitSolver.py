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
        new_row = []                #assumption that input looks like (battery or resistor, positive terminal, negative terminal, value)
        
                                
        if in_put[i][0] == battery:   #if device is a battery (can change exact way of knowing if it's a battery)
            for i in range(2*len(in_put)-2):   ##put in all zeroes except 2: for the two voltages
                new_row.append(0)
                return new_row
            if i == 0:
                new_row.insert(i, 1)                #a 1 for the voltage at the positive terminal
                new_row.insert(len(in_put), -1)     # -1 for the voltage at the negative terminal (if signs are wrong, will be corrected in voltage value)
            else:
                new_row.insert(i,1)
                new_row.insert(i+1, -1)
                
            A.append(new_row)
            b.append(in_put[i].voltage)

        else:
            for i in range(2*len(in_put)-3):        #3 other spots to be filled
                new_row.append(0)                   
                return new_row

            new_row.insert(i-1, 1)
            new_row.insert(i, -1)

            if in_put[i].direction == True:         #Give resistors attribute to show direction. True = + to -; false = - to +
                new_row.insert(len(in_put)+i, -1 * in_put[i].resistance)
            else:
                new_row.insert(len(in_put)+i, in_put[i].resistance)

            
            
                        
        
