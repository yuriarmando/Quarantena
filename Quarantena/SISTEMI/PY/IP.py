import numpy as np

def addressCheck(string):
    field=string.split(".")
    ip=[]
    for index,_ in enumerate(field):
        try:
            ip.append(int(field[index]))
        except:
            print("\n ----------------------------------------------")
            print("\n WARNING")
            print("\n the number entered is not valid")
            print("\n ----------------------------------------------")
    for index,_ in enumerate(ip):
        if ip[index] < 0:
            ip[index] = 0
        if ip[index] > 255:
            ip[index] = 255
    while len(ip) > 4:
        ip.pop(len(ip)-1)
    while len(ip) < 4:
        ip.append(0)
    return ip

def maskCheck(string):
    try:
        mask=int(string)
    except:
        print("\n ----------------------------------------------")
        print("\n WARNING")
        print("\n the number entered is not valid")
        print("\n ----------------------------------------------")
        mask=24
    if (mask < 1):
        mask = 1
    if (mask > 31):
        mask=31
    return mask

def findIP(binaryIP, mask):
    n_host = hostNumber(mask)
    binaryIP = resetHostIpPart(binaryIP, mask)
    ip=[]
    ip.append(list(np.repeat(binaryIP, 1)))
    while(n_host != 0):
        ip.append(IncreaseIP(list(np.repeat(ip[-1], 1))))
        n_host-=1
    return ip

def hostNumber(mask):
    number=(2 ** (32-mask)) - 2
    return number

def resetHostIpPart(binaryIP, mask):
    for index in range(mask,32):
        binaryIP[index]=0
    return binaryIP

def IncreaseIP(binaryIP):
    increase=1
    index=1
    while (increase==1):
        if binaryIP[-index] == 1:
            binaryIP[-index] = 0
            index += 1
        else:
            binaryIP[-index] = 1
            increase = 0
        if index >= (len(binaryIP)-1):
            increase = 0
    return binaryIP
    
def binaryAddress(decimalIP):
    ip=[]
    for index,_ in enumerate(decimalIP):
        num=decimalIP[index]
        cont = 0
        ip_temp=[]
        for _,_ in enumerate(ip_temp):
            ip_temp.pop()
        while cont < 8:
            if num > 0:
                if num%2==0:
                    ip_temp.append(0)
                    num=num/2
                else:
                    ip_temp.append(1)
                    num=(num-1)/2
            else:
                ip.append(0)
            cont += 1
        ip += ip_temp
    return ip

def decimalAddress(binaryIP):
    string=["","","",""]
    ip=[]
    for index,_ in enumerate(binaryIP):
        pos=int(index/8)
        string[pos]+=str(binaryIP[index])
    for index,_ in enumerate(string):
        ip.append(int(string[index], 2))
    return ip
        
def main():
    string=input ("enter ip address (decimal mode) \n")
    ip_d=addressCheck(string)
    ip_b=binaryAddress(ip_d)
    string=input ("enter ip mask (only number) \n")
    mask=maskCheck(string)
    list_b_ip=findIP(ip_b,mask)
    list_d_ip=[]
    for index,_ in enumerate(list_b_ip):
        list_d_ip.append(decimalAddress(list_b_ip[index]))
        print(list_d_ip[index])

    


    

#this function is used to convert the program into a library in case you want to use it in that way
if __name__ == "__main__":
    main()