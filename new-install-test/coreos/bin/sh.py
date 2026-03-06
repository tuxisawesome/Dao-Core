#0.1

repo_root = "https://raw.githubusercontent.com/tuxisawesome/DaoDownloader/refs/heads/main/"

def init(drivers, drivernames, configmgr, drivermgr,kernel):


    debug = True




    
    config = configmgr.readconfig("config.cfg")
    interactive = configmgr.getvalue(config, "interactive")
    display = drivers[drivernames.index("display")]
    imp = drivers[drivernames.index("input")]
    if interactive == "0": interactive = False 
    else: interactive = True
    kernel_arguments = kernel.args
    if "interactive=false" in kernel_arguments: interactive = False
    if interactive:
        firstrun(drivers, drivernames, configmgr, drivermgr,kernel)
    else:
        display.printline("!   Not an interactive shell, skipping...")


def firstrun(drivers, drivernames, configmgr, drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    imp = drivers[drivernames.index("input")]
    system = drivers[drivernames.index("sys")]
    display.printline("Welcome to the Dao Installation Program!")
    display.printline("We will now update your system to make sure it is running the latest software.")
    display.printline("Would you like to: [i]nstall the latest updates, [a]ccess network options, or [e]xit the installer?")
    x = imp.getinput("[i/a/e]: ")
    if x == "i":
        display.printline("Installing updates...")
        system_update(drivers,drivernames,configmgr,drivermgr,kernel)
        display.printline("Updates installed successfully!")
        display.printline("Signing core system files...")
        sign(drivers,drivernames,configmgr,drivermgr,kernel)
        display.printline("Core system files signed successfully!")
        display.printline("Rebooting system to apply updates...")
        return
    elif x == "a":
        display.printline("Accessing network options...")
        display.printline("[s]: Scan for networks")
        display.printline("[c]: Connect to a network")
        display.printline("[g]: Get network status")
        x = imp.getinput("[scg]: ")
        if x == "s":
            display.printline("Scanning for nearby networks...")
            ssidlist = network.scan_networks(kernel)
            if len(ssidlist) == 0:
                display.printline("No networks found.")
                return
            display.printline("Nearby Networks:")
            display.printline("================")
            for ssid in ssidlist:
                display.printline(ssid[0].decode("utf-8") + "  Strength: " + str(ssid[2]))
        elif x == "g":
            display.printline("Getting network information...")
            info = network.network_info(kernel)
            if info is None:
                display.printline("Not connected to a network.")
                return
            display.printline("IP Address: " + info[0])
            display.printline("Subnet Mask: " + info[1])
            display.printline("Gateway: " + info[2])
            display.printline("DNS: " + info[3])
        elif x == "c":
            # Here you would add code to show advanced options, such as partitioning the disk, configuring the network, etc.
            netconnect(drivers,drivernames,configmgr,drivermgr,kernel)
            display.printline("Network configured successfully!")
        firstrun(drivers,drivernames,configmgr,drivermgr,kernel)
    elif x == "e":
        display.printline("Exiting installer. Goodbye!")
        return
    else:
        display.printline("Invalid option selected.")
        firstrun(drivers, drivernames, configmgr, drivermgr,kernel)




def sign(drivers,drivernames,configmgr,drivermgr,kernel):
    def sha256(data: str) -> str:
        """
        Computes the SHA-256 hash of the input data.

        This function implements the SHA-256 algorithm from scratch as specified
        in FIPS 180-4. It takes a string as input and returns its SHA-256
        hash as a 64-character hexadecimal string. No external modules are required.

        Args:
            data: The input string to be hashed.

        Returns:
            The SHA-256 hash of the data as a lowercase hexadecimal string.
        """
        # -----------------------------------------------------------------------------
        # Section 1: Helper Functions & Bitwise Operations
        # -----------------------------------------------------------------------------
        # These are the core bitwise operations used in the SHA-256 algorithm.
        # All operations are performed on 32-bit unsigned integers. The `& 0xFFFFFFFF`
        # mask is used to ensure results remain within the 32-bit boundary.

        def rotr(x, n):
            """Circular right rotate a 32-bit integer x by n bits."""
            return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

        def shr(x, n):
            """Right shift a 32-bit integer x by n bits."""
            return (x >> n) & 0xFFFFFFFF

        # Logical functions as defined in the FIPS 180-4 standard
        ch = lambda x, y, z: (x & y) ^ (~x & z)
        maj = lambda x, y, z: (x & y) ^ (x & z) ^ (y & z)
        sigma0 = lambda x: rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
        sigma1 = lambda x: rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
        gamma0 = lambda x: rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)
        gamma1 = lambda x: rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

        # -----------------------------------------------------------------------------
        # Section 2: SHA-256 Constants
        # -----------------------------------------------------------------------------
        # These constants are defined in the SHA-256 standard.

        # K: Round constants - first 32 bits of the fractional parts of the
        # cube roots of the first 64 prime numbers.
        K = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

        # H: Initial hash values - first 32 bits of the fractional parts of the
        # square roots of the first 8 prime numbers.
        H = [
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
        ]

        # -----------------------------------------------------------------------------
        # Section 3: Pre-processing and Padding
        # -----------------------------------------------------------------------------
        # The input data must be padded to be a multiple of 512 bits.

        # 1. Convert the input string to a sequence of bytes.
        message_bytes = data.encode('utf-8')
        original_len_bits = len(message_bytes) * 8

        # 2. Append the '1' bit (0x80 byte).
        padded_message = message_bytes + b'\x80'

        # 3. Append '0' bits (null bytes) until message length in bits is congruent
        #    to 448 (mod 512). This means len(bytes) % 64 == 56.
        while len(padded_message) % 64 != 56:
            padded_message += b'\x00'

        # 4. Append the original message length in bits as a 64-bit big-endian integer.
        padded_message += original_len_bits.to_bytes(8, 'big')

        # -----------------------------------------------------------------------------
        # Section 4: Process the Message in 512-bit (64-byte) Chunks
        # -----------------------------------------------------------------------------
        # The main loop of the algorithm.

        # Iterate over the padded message in 64-byte chunks.
        for i in range(0, len(padded_message), 64):
            chunk = padded_message[i:i+64]

            # a. Create the message schedule (w)
            w = [0] * 64
            # First 16 words are from the chunk directly (big-endian).
            for j in range(16):
                w[j] = int.from_bytes(chunk[j*4:j*4+4], 'big')

            # Extend the first 16 words into the remaining 48 words of the schedule.
            for j in range(16, 64):
                w[j] = (gamma1(w[j-2]) + w[j-7] + gamma0(w[j-15]) + w[j-16]) & 0xFFFFFFFF

            # b. Initialize working variables with current hash values.
            a, b, c, d, e, f, g, h = H

            # c. Compression function main loop.
            for j in range(64):
                t1 = (h + sigma1(e) + ch(e, f, g) + K[j] + w[j]) & 0xFFFFFFFF
                t2 = (sigma0(a) + maj(a, b, c)) & 0xFFFFFFFF
                h = g
                g = f
                f = e
                e = (d + t1) & 0xFFFFFFFF
                d = c
                c = b
                b = a
                a = (t1 + t2) & 0xFFFFFFFF

            # d. Update hash values with the compressed chunk.
            H[0] = (H[0] + a) & 0xFFFFFFFF
            H[1] = (H[1] + b) & 0xFFFFFFFF
            H[2] = (H[2] + c) & 0xFFFFFFFF
            H[3] = (H[3] + d) & 0xFFFFFFFF
            H[4] = (H[4] + e) & 0xFFFFFFFF
            H[5] = (H[5] + f) & 0xFFFFFFFF
            H[6] = (H[6] + g) & 0xFFFFFFFF
            H[7] = (H[7] + h) & 0xFFFFFFFF

        # -----------------------------------------------------------------------------
        # Section 5: Produce the Final Hash
        # -----------------------------------------------------------------------------
        # Concatenate the final hash values and format as a hex string.

        final_hash = ''.join(f'{val:08x}' for val in H)
        return final_hash
    display = drivers[drivernames.index("display")]
    display.printline("Bootsign")
    conf = configmgr.readconfig("verifiedboot.cfg")
    sid = configmgr.getkeys(conf)
    for s in sid:
        with open(s, 'r') as x:
            p = x.readlines()
            z = ""
            for line in p:
                z = z + line
            filehash = sha256(z)
            conf = configmgr.setvalue(conf, s, filehash)
            x.close()
        display.printline("*   Signed " + s + " with hash " + str(filehash))
    configmgr.writeconfig("verifiedboot.cfg",conf)
    display.printline("Done!")



def system_update(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    net = drivers[drivernames.index("net-connect")]
    interactive = drivers[drivernames.index("input")]
    sysctl = drivers[drivernames.index("sys")]
    packagekit = drivers[drivernames.index("packagekit")]
    packagekit.configuration.repo_root = repo_root

    display.printline("System update")
    if True:
        x = packagekit.system_update_backend(repo_root + "system/",net,sysctl,kernel,display)
        if x == -255:
            display.printline("No internet.")
        if x == -1:
            display.printline("Server down.")
        if x == 0:
            display.printline("Please now run 'bootsign' in case any core system files changed.")


def netconnect(drivers,drivernames,configmgr,drivermgr,kernel):
    display = drivers[drivernames.index("display")]
    display.printline("Net-Connect")
    display.printline("Checking for a valid network driver...")
    try:
        network = drivers[drivernames.index("net-connect")]
    except:    
        display.printline("!   No network driver found. Please install a network driver to use this application.")
        return
    interactive = drivers[drivernames.index("input")]
    display.printline("Please enter the SSID of the network you wish to connect to:")
    ssid = interactive.getinput("SSID: ")
    password = interactive.getinput("Password (leave blank for open networks): ")
    display.printline("Attempting to connect to " + ssid + "...")
    network.connect(display,kernel,ssid, password)