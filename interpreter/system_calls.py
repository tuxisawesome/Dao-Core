
def exec_module(name,scope):
    new_scope = scope
    x = []
    with open(name + ".hm","r") as d:
        x = d.readlines()
        d.close()
    for line in x:
        new_scope, ret = interpret(line.strip("\n"),new_scope)
        if ret == -1:
            return new_scope
    return new_scope





def prints(scope):
    if scope[1][0].endswith("\\n") or scope[1][0].endswith("\n"):
        print(scope[1][0].strip("\\n"))
    else: print(scope[1][0],end="")

    return scope, 0

def inputs(scope):
    # Gets the input from scope[0] and outputs to scope[1] (returns to)
    scope[1][1] = input(scope[1][0])
    return scope,0

def add(scope):
    scope[1][0] = str(float(scope[1][1]) + float(scope[1][2]))
    return scope, 0

def sub(scope):
    scope[1][0] = str(float(scope[1][2]) - float(scope[1][1]))
    return scope, 0    

def mul(scope):
    scope[1][0] = str(float(scope[1][1]) * float(scope[1][2]))
    return scope, 0

def div(scope):
    scope[1][0] = str(float(scope[1][2]) / float(scope[1][1]))
    return scope, 0

def f(scope):
    if scope[1][0] > 0:
        exec_module(scope[1][1],scope)
    return scope,0
# 0: If                 - Checks if data in scope[1][0] is greater than 0 and if so, jump to another program in scope[1][1]
# 1: Print              - Prints stuff in scope[1][0]
# 2: Input              - Inputs stuff in scope[1][1] with prompt scope[1][0]
# 3: Add                - Adds values in scope[1][1] and scope[1][2] and outputs to scope[1][0]
# 4: Subtract           - Subtracts scope[1][2] to scope[1][1] (scope2 - scope1) and outputs to scope[1][0]
# 5: Multiply           - Multiplys scope[1][1]and scope[1][2] and outputs to scope[1][0]
# 6: Divide             - Divides scope[1][2] by scope[1][1] (scope2 / scope1) and outputs to scope[1][0]


calls = [[0,1,2,3,4,5],[f,prints,inputs,add,sub,mul]]

