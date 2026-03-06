#0.1


def init(drivers,drivernames,configmgr,drivermgr,kernel):
    

def sign():
    
    import kernel as configmgr

    conf = configmgr.readconfig("verifiedboot.cfg")
    sid = configmgr.getkeys(conf)
    for s in sid:
        with open(s, 'r') as x:
            p = x.readlines()
            z = ""
            for line in p:
                z = z + line
            filehash = sha256(z)
            print(filehash)
            conf = configmgr.setvalue(conf, s, filehash)
            x.close()
    configmgr.writeconfig("verifiedboot.cfg",conf)
    print("Done!")

if __name__ == "__main__":
    sign()