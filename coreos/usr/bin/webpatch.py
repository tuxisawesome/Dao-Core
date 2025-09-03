def init(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    net = drivers[drivernames.index("net-connect")]
    interactive = drivers[drivernames.index("input")]
    sysctl = drivers[drivernames.index("sys")]
    argv = configmgr.getvalue(configmgr.readconfig("env.cfg"), "argv")
    if argv == "-R" or argv == "-r":
        display.printline("!!! REMOVAL MODE !!!")
        removal_mode = True
    else:
        removal_mode = False
    website_root = "https://raw.githubusercontent.com/tuxisawesome/DaoDownloader/refs/heads/main/"
    #response_code,response_data = net.get_web_data(website_root + "README.txt",kernel)
    app = interactive.getinput("Please enter the app: ")
    directory = "usr/bin/"
    if not removal_mode:
        x = download_file(website_root + "apps/" + app + ".py", directory, app + ".py",net,kernel)
        if x == 404:
            display.printline("This application does not exist, or the server is down.")
            return
        elif x == -255:
            display.printline("The network is not connected.")
        elif x == -1:
            display.printline("The system encounterred a strange error code.")
        elif x == -2:
            display.printline("The repository name is incorrect.")
        else:
            display.printline("The application " + app + " was installed successfully.")
    else:
        sysctl.rmfile(directory + app + ".py")
        display.printline("Application Removed.")


def download_file(website,directory,filename,net,kernel):
    print(website)
    if not website.startswith("http:") and not website.startswith("https:"):
        return -2
    response_code, response_content = net.get_web_data(website,kernel)
    if response_code != 200:
        if response_code == -255:
            return -255
        elif response_code == "404":
            return 404
        return -1
    with open(directory + "/" + filename, "wb") as file:
        file.write(response_content)
        file.close()
    return 0
