def decimalToBinary(n):
    return bin(n).replace("0b", "")


def convertIP(ipaddress):
    binary = ""
    try:
        parts = str(ipaddress).split(".")
        for part in parts:
            num = int(part)
            bin = decimalToBinary(num)
            if binary == "":
                binary = str(bin)
            else:
                binary = binary + "." + str(bin)
    except:
        print("Insert 4 digits between 0 and 255, separated by dots")
    return binary


if __name__ == '__main__':
    res = "y"

    while res == "y" or res == "Y":
        ipAddress = input("Insert IP to convert: ")
        ipBinary = convertIP(ipAddress)
        if ipBinary != "":
            print("The IP converted to binary is: " + ipBinary)
        res = input("Convert another IP? (y/n)")
