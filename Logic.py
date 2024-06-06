def Message(message):
    print("\n The result: ", message,"\n")

def Add(a, b):
    return float(a)+float(b)
def Subtract(a, b):
    return float(a)-float(b)
def Multiply(a, b):
    return float(a)*float(b)
def Divide (a,b):
    return float(a)/float(b)

def Power(a,x):
    return Power(a,x)

def Operate(var, oper):
    match oper:
        case "+":
            return Add(var[0], var[1])
        case "-":
            return Subtract(var[0], var[1])
        case "/":
            return Divide(var[0], var[1])
        case "*":
            return Multiply(var[0], var[1])

def OperWeight(Table):
    weigh=[]
    for x in range(len(Table)):
        if Table[x]=="*" or Table[x]=="/":
            weigh.append(2)
        else:
            weigh.append(1)
    return weigh

def Calculate(var, oper):
    print("CALCULATION")
    operWeigh=OperWeight(oper)
    y=len(oper)
    for x in range(len(oper)):
        print(len(oper))
        if x<y-1:
            if operWeigh[0] >= operWeigh[1]:
                result = Operate([var[0], var[1]], oper[0])
                del var[0]
                del oper[0]
                del operWeigh[0]
                var[0] = result
            else:
                result = Operate([var[1], var[2]], oper[1])
                del var[1]
                del oper[1]
                del operWeigh[1]
                var[1] = result
        else:
            var[0] = Operate([var[0], var[1]], oper[0])
    return var[0]