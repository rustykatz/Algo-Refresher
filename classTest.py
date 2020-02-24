class Alpha():
    def __init__(self):
        self.name = 'Alpha'
        self.gp = 10 

    def Send(self, amount, target):
        self.gp -= amount
        target.gp += amount
        print("ALPHA-> GP Send:", amount, "Total Gp", self.gp)
        print("BETA-> GP Receive:", amount, "Total Gp", target.gp)

    def Rename(self, newName):
        oldName = self.name
        self.name = newName
        print('NAME CHANGE:',oldName, '->', self.name)

class Beta():
    def __init__(self):
        self.name = 'Beta'
        self.gp = 10 

    def Send(self, amount, target):
        self.gp -= amount
        target.gp += amount
        print("BETA-> GP Send:", amount, "Total Gp", self.gp)
        print("ALPHA-> GP Receive:", amount, "Total Gp", target.gp)


class Rules():
    def __init__(self):
        self.nameList = [] 

    
    def Validity(self, nameList, name, fxn):
        pass 

    def BelowThreshold(self, objList):
        pass 

def TransactionTest():
    a = Alpha()
    print(a.name)
    print('\n')
    b = Beta()

    print('Transaction 1')
    a.Send(2,b)
    print('\n')

    print('Transaction 2')
    b.Send(5,a)

    print('\n')
    a.Rename('THETA')

# Returns list 
def GenerateObjectList(objClass, numInstances):
    res = []
    [res.append(objClass) for x in range(numInstances)]
    return res 



def main():
    # TransactionTest()

    # Num of Alpha Objects
    instances = 10

    # Create instances of Alpha Obj and add to iterable list 
    # for i in range(0,instances):
    #     a.append(Alpha())

    x = GenerateObjectList(Alpha(), instances)

    # Print names of all Alpha objects in the list 
    print(x)
    for i in x:
        print(i)

if __name__ == "__main__":
    main()