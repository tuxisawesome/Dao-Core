def init(drivers, drivernames, configmgr, drivermgr,kernel):
    config = configmgr.readconfig("config.cfg")
    interactive = configmgr.getvalue(config, "interactive")
    display = drivers[drivernames.index("display")]
    if interactive == "0": interactive = False 
    else: interactive = True
    if interactive:
        continues = True
        while continues:
            x = drivers[drivernames.index("input")].getinput("$ ")
            if x == "": continue

            if x == "exit":
                continue

            if x == "poweroff":
                sys = drivers[drivernames.index("sys")]
                display.printline("*   This system is going down for shutdown NOW!")
                return
            
            
            if x == "env-reload":    
                kernel.reload_env()
                continue
                        
            if x == "help": 
                display.printline("WalterOS Shell")
                continue
            try:
                args = x.split(" ")
                if len(args) > 1:
                    newenv = configmgr.setvalue(configmgr.readconfig("env.cfg"), "argv", args[1])
                    configmgr.writeconfig("env.cfg",newenv)
                else:
                    newenv = configmgr.setvalue(configmgr.readconfig("env.cfg"), "argv", "null")
                    configmgr.writeconfig("env.cfg",newenv)
                try:
                    y = drivermgr.defload(args[0], "bin/")
                except:
                    try:
                        y = drivermgr.defload(args[0], "usr/bin/")
                    except:
                        display.printline("File not found!")
                        continue
            except:
                display.printline("ERROR!")
                continue
            try:
                x = y.init(drivers, drivernames, configmgr, drivermgr,kernel)
                if x == "quit":
                    break
                else:
                    continue
            except:
                display.printline("File may be corrupted!\nPlease check the arguments the file is taking.")
                continue
            
    else:
        display.printline("!   Not an interactive shell, skipping...")

