# input5-nmask-netid-bcast.py
def calcbcast(nmask,bcast,netid):
	for i in range(0,4):
		subnmask = ~nmask[i]&255
		bcast[i] = netid[i]^subnmask
	return bcast
	
def calcnetid(ipv4,nmask,netid):
	for i in range(0,4):
		netid[i] = int(ipv4[i]) & int(nmask[i]) 
	return netid

def getnmask(cidr,nmask):
	cidr = int(cidr)
	if cidr == 31:
		nmask = [255,255,255,255]
	if cidr == 30:
		nmask = [255,255,255,254]
	if cidr == 29:
		nmask = [255,255,255,252]
	if cidr == 28:
		nmask = [255,255,255,248]
	if cidr == 27:
		nmask = [255,255,255,240]
	if cidr == 26:
		namsk = [255,255,255,224]
	if cidr == 25:
		nmask = [255,255,255,192]
	if cidr == 24:
		nmask = [255,255,255,128]
	if cidr == 23:
		nmask = [255,255,255,0]
	if cidr == 22:
		nmask = [255,255,254,0]
	if cidr == 21:
		nmask = [255,255,252,0]
	if cidr == 20:
		nmask = [255,255,248,0]
	if cidr == 19:
		nmask = [255,255,240,0]
	if cidr == 18:
		nmask = [255,255,224,0]
	if cidr == 17:
		nmask = [255,255,192,0]
	if cidr == 16:
		nmask = [255,255,128,0]
	if cidr == 15:
		nmask = [255,255,0,0]
	if cidr == 14:
		nmask = [255,252,0,0]
	if cidr == 13:
		nmask = [255,248,0,0]
	if cidr == 12:
		nmask = [255,240,0,0]
	if cidr == 11:
		nmask = [255,224,0,0]
	if cidr == 10:
		nmask = [255,192,0,0]
	if cidr == 9:
		nmask = [255,128,0,0]
	if cidr == 8:
		nmask = [255,0,0,0]
	if cidr == 7:
		nmask = [254,0,0,0]
	if cidr == 6:
		nmask = [252,0,0,0]
	if cidr == 5:
		nmask = [248,0,0,0]
	if cidr == 4:
		nmask = [240,0,0,0]
	if cidr == 3:
		nmask = [224,0,0,0]
	if cidr == 2:
		nmask = [192,0,0,0]
	if cidr == 1:
		nmask = [128,0,0,0]
	if cidr == 0:
		nmask = [0,0,0,0]
	return nmask


def main():
	cidr = -1
	ipv4 = [-1,-1,-1,-1]
	nmask =  [-1,-1,-1,-1]
	netid = [-1,-1,-1,-1]
	bcast = [-1,-1,-1,-1]
	startingip = [-1,-1,-1,-1]
	endingip = [-1,-1,-1,-1]
	
	print ('Input an IP and CIDR with 5 inputs.')
	o1 = input("OCTET 1: ")
	o2 = input("OCTET 2: ")
	o3 = input("OCTET 3: ")
	o4 = input("OCTET 4: ")
	cidr = input("CIDR: ")
	print (o1,".",o2,".",o3,".",o4, "/", cidr,sep="")
	ipv4[0] = o1; ipv4[1] = o2; ipv4[2] = o3; ipv4[3] = o4;   
	nmask = getnmask(cidr,nmask)
	netid = calcnetid(ipv4,nmask,netid)
	bcast = calcbcast(nmask,bcast,netid)
	#clean up the output
	#calculte the starting ip and the ending ip
	#print(ipv4,cidr,nmask,bcast)
	#print("IP: ",ipv4)
	print("IP: ",o1,".",o2,".",o3,".",o4,sep="")
	print("NET-MASK: ",nmask)
	print("NETWORK ID: ",netid)
	print("BROADCAST: ",bcast)
main()
