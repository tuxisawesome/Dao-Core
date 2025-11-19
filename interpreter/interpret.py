# 0 is success
# -1 is end
# -255 is dnf
# Scope:
# [[[ (System call names) ],[ (System calls) ]],[ (Program variable scope (scope:0 is stdin),(scope:1 is stdout)) ]]

import system_calls as syscall


system_calls = syscall.calls






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
        

def interpret(command,scope=[[[],[]],[]]):
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
        index = int(command.split(" ")[1])
        try:
            value = command.split('"')[1].strip('"')
        except:
            value = scope[1][int(command.split(" ")[2])]
        scope[1][index] = value
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
    return scope, 255
    
    

def repl():
    counter = 0
    scope = [[[],[]],[]]

    while counter < 100:
        scope[1].append(" ")
        counter += 1
    while True:
        x = input("? ")
        scope, ret = interpret(x, scope)
        print(ret)
        if ret == -1:
            return
        

if __name__ == "__main__":
    repl()
        