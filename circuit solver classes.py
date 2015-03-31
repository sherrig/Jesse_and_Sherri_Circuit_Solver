class Resistor:
    def __init__(self,resistance):
        self.resistance = resistance
        self.type = "r"
    def __str__(self):
        return "resistor " + str(self.resistance)
class Battery:
    def __init__(self,voltage):
        self.voltage = voltage
        self.type = "b"
    def __str__(self):
        return "battery " + str(self.voltage)

################################################
component = []
print "Please enter the components in your circuit."
print "If you have no more to enter, please type \"none\""
takingInputs = True
while takingInputs:
    inp = raw_input("resistor or battery?")
    if (inp == "resistor"):
        value = float(raw_input("what is the resistance?"))
        component.append(Resistor(value))
    elif(inp == "battery"):
        value = float(raw_input("what is the voltage?"))
        component.append(Battery(value))
    elif(inp == "none"):
        takingInputs = False
    else:
        print("please try again, input not accepted")


for i in range(len(component)):
    print component[i]
