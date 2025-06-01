import sys
def load(name, path_in_lib):
    sys.path.append("lib/" + path_in_lib)    
    return __import__(name.strip("\n"))

def defload(name, path):
    sys.path.append(path)    
    return __import__(name.strip("\n"))

def unload(name):
    del name