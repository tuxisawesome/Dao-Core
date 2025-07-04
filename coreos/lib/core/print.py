def init(drivers, drivernames, configmgr, drivermgr):
    import os
    try:
        columns, rows = os.get_terminal_size()
        
    except OSError:
        columns = None
        rows = None
    if columns and rows:
        print("Loaded with " + str(columns) + " columns and " + str(rows) + " rows.")
    else:
        print("Could not determine terminal width.")

def printline(text):
    print(text)

def clear():
    import os
    os.system("clear||cls")