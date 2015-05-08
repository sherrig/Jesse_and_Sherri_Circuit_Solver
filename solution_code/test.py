# Test Circuit Joe
components = [Battery(2, 'hot', 'gnd', 'b1'),
              Resistor(10, 'hot', 'left', 'r1'),
              Battery(4, 'hot', 'right', 'b2'),
              Resistor(30, 'right', 'left', 'r2'),
              Resistor(1, 'left', 'gnd', 'r3'),
              Resistor(50, 'right', 'gnd', 'r4')
              ]
solveCircuit(components, 'gnd')
# Sherri/Jesse Solver
components = [B('b1', 'hot', 'gnd', 2),
              R('r1', 'hot', 'left', 10),
              B('b2', 'hot', 'right', 4),
              R('r2', 'right', 'left', 30),
              R('r3', 'left', 'gnd', 1),
              R('r4', 'right', 'gnd', 50)
              ]
solve(components)
