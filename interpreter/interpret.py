# 0 is success
# -1 is end
# -255 is dnf
# Scope:
# [[[ (System call names) ],[ (System calls) ]],[ (Program variable scope (scope:0 is stdin),(scope:1 is stdout)) ],[[Variable name map],[Corresponding vars]]]



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
    # Gets the input from scope[2] and outputs to scope[1] (returns to)
    scope[1][1] = input(scope[1][2])
    return scope,0

def add(scope):
    scope[1][0] = str(float(scope[1][3]) + float(scope[1][4]))
    return scope, 0

def sub(scope):
    scope[1][0] = str(float(scope[1][4]) - float(scope[1][3]))
    return scope, 0    

def mul(scope):
    scope[1][0] = str(float(scope[1][3]) * float(scope[1][4]))
    return scope, 0

def div(scope):
    scope[1][0] = str(float(scope[1][4]) / float(scope[1][3]))
    return scope, 0

def f(scope):
    if scope[1][0] == scope[1][1]:
        scope = exec_module(scope[1][2],scope)
    return scope,0

def end(scope):
    import sys
    sys.exit(0)

#-1: End                - Kills the program
# 0: If                 - Checks if data in scope[1][0] is equal to scope[1][1] and if so, jump to another program in scope[1][2]
# 1: Print              - Prints stuff in scope[1][0]
# 2: Input              - Inputs stuff in scope[1][1] with prompt scope[1][2]
# 3: Add                - Adds values in scope[1][3] and scope[1][4] and outputs to scope[1][0]
# 4: Subtract           - Subtracts scope[1][4] to scope[1][3] (scope4 - scope3) and outputs to scope[1][0]
# 5: Multiply           - Multiplys scope[1][4]and scope[1][3] and outputs to scope[1][0]
# 6: Divide             - Divides scope[1][4] by scope[1][3] (scope4 / scope3) and outputs to scope[1][0]


calls = [[-1,0,1,2,3,4,5,6],[end,f,prints,inputs,add,sub,mul,div]]


system_calls = calls






def syscall_translator(sysc,scope):
    try:
        sysc = int(sysc)
    except:
        for system_call_name in scope[0][0]:
            if system_call_name == sysc:
                sysc = int(scope[0][1][scope[0][0].index(system_call_name)])
    for system_call in system_calls[0]:
        if system_call == sysc:
            scope, ret = system_calls[1][system_calls[0].index(sysc)](scope)
            return scope, ret
        

def interpret(command,scope=[[[],[]],[],[]]):
    if command == ";;":
        return scope, -1
    if command.startswith("#") or command.startswith("//"):
        return scope, 0
    if command == "":
        return scope, 0
    if command.split(" ")[0] == "sysc":
        scope, ret = syscall_translator(command.split(" ")[1],scope)
        return scope, ret
    if command.split(" ")[0] == "setv":
        try:
            index = int(command.split(" ")[1])
        except:
            for varmap in scope[2][0]:
                if varmap == command.split(" ")[1]:
                    index = int(scope[2][1][scope[2][0].index(varmap)])
        try:
            value = command.split('"')[1].strip('"')
        except:
            value = scope[1][int(command.split(" ")[2])]
        scope[1][index] = value
        return scope, 0
    if command.split(" ")[0] == "map":
        number_to_map = int(command.split(" ")[1])
        var_to_map_to = command.split(" ")[2]
        if var_to_map_to in scope[2][0]:
            scope[2][1][scope[2][0].index(var_to_map_to)] = number_to_map
            return scope, 0
        scope[2][0].append(var_to_map_to)
        scope[2][1].append(number_to_map)
        return scope, 0

    if command.split(" ")[0] == "trans":
        syscall = int(command.split(" ")[1])
        name = command.split('"')[1].strip('"')
        scope[0][0].append(name)
        scope[0][1].append(syscall)
        return scope, 0
    if command == "scope":
        print(scope)
        return scope, 0
    if command.split(" ")[0] == "module":
        name = command.split('"')[1].strip('"')
        scope = exec_module(name, scope)
        return scope, 0
    if command == "exec":
        scope,ret = interpret(scope[1][9],scope) # Executes the code in the 9th slot
        return scope, ret
    return scope, 255
    
    

def repl():
    counter = 0
    scope = [[[],[]],[[],[]],[[],[]]]

    while counter < 100:
        scope[1].append(" ")
        counter += 1
    while True:
        #x = input("? ")
        x = 'module "main"'
        scope, ret = interpret(x, scope)
        print(ret)
        
        return
        if ret == -1:
            return
        

if __name__ == "__main__":
    repl()
        