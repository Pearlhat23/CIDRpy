def binInc(bin):
 #takes an array of "1"s and "0"s which represents a binary value
 #iterates backwards across the array generating an output and carry value for each bit
 #output is carry xor input (calculated here as a similarity comparison); carry is carry and input
 #this simulates a series of half adders
 carry="1"
 out=["0"]*len(bin)
 for i in range(len(bin)-1,-1,-1):
  if(carry!=bin[i]):
   out[i]="1"
  if(carry=="1" and bin[i]=="1"):
   carry="1"
  else:
   carry="0"
 return out
def binDec(bin):
 #takes an array of "1"s and "0"s which represents a binary value
 #iterates backwards across the array generating an output and carry value for each bit
 #output is carry xor input (calculated here as a similarity comparison); carry is carry and not input
 #this simulates a series of half subtracters
 carry="1"
 out=["0"]*len(bin)
 for i in range(len(bin)-1,-1,-1):
  if(carry!=bin[i]):
   out[i]="1"
  if(carry=="1" and bin[i]=="0"):
   carry="1"
  else:
   carry="0"
 return out

def netcalc(ip,cidr):
 ipstr=""
 mskstr=""
 idstr=""
 brdcststr=""
 rngstr=["",""] #these are the values which will be returned
 quaddot=[] #will hold the parsed ip
 ipstr=ip+"/"+str(cidr) #creates the string form of the ip
 for num in ip.split('.'): #iterates across sections of the string seperated by '.'
  quaddot.append(int(num)) #adds the section to quaddot as an integer
 clss="Unknown" #initialized to "Unknown" to handle exceptions
 clssranges=[(1,126,"A"),(128,191,"B"),(192,223,"C"),(224,239,"D"),(240,254,"E")] #lists class ranges
 for low,high,res in clssranges: #iterates across class ranges
  if(int(quaddot[0])>=low and int(quaddot[0])<=high): #tests if ip is in the current range
   clss=res #saves the class current class
 ipbin=["0"]*32  #initializes the binary form of the ip
 for quadind in range(4): #iterates across the ip array
  for bit in range(8): #iterates across the bits in each section of the ip
   ipbin[(8*quadind)+bit]=str(quaddot[quadind]//(2**(7-bit))) #sets the current value of the ip binary to "1" if that power of two is present and "0" if not
   quaddot[quadind]%=2**(7-bit) #reduces the current ip value by the current power of 2 if present to keep track; does mean that the decimal ip is lost
 submsk=["0"]*32 #initializes the binary form of the subnet mask
 for i in range(cidr): #sets the first "cidr" digits to "1" acquiring the subnet mask
  submsk[i]="1"
 submskint=[0,0,0,0] #initializes the decimal form of the subnet mask
 for i in range(4): #iterates across the subnet mask integer array
  for j in range(8): #iterates across the bits in each segment of the subnet mask binary
   submskint[i]+=(int(submsk[(8*i)+j]))*(2**(7-j)) #increases the current value in submskint by the current power of two if  the current bit is "1"
  if i>0: #if it isn't on the first round adds a "." to the output string
   mskstr+="."
  mskstr+=str(submskint[i]) #adds the current value to the string
 netidbin=["0"]*32 #same process as before on lines 47-61 applied to the Network ID except as noted
 for i in range(32):
  if ipbin[i]=="1" and submsk[i]=="1": #puts the ip and subnet mask through an AND gate to generate the ID
   netidbin[i]="1"
 netid=[0,0,0,0]
 for i in range(32):
  netid[i//8]+=(int(netidbin[i]))*(2**(7-(i%8)))
 for i in range(4):
  if i>0:
   idstr+="."
  idstr+=str(netid[i])
 brdbin=["0"]*32 #same process as before on lines 47-61 applied to the Broadcast Address except as noted
 for i in range(32):
  if ipbin[i]=="1" or submsk[i]=="0": #puts the ip and the inverse of the subnet mask through an OR gate to generate the Address
   brdbin[i]="1"
 brdcst=[0,0,0,0]
 for i in range(32):
  brdcst[i//8]+=(int(brdbin[i]))*(2**(7-(i%8)))
 for i in range(4):
  if i>0:
   brdcststr+="."
  brdcststr+=str(brdcst[i])
 rngmaxbin=binDec(brdbin) #generates the max on the range by decrementing the broadcast address binary by one
 rngminbin=binInc(netidbin) #generates the max on the range by incrementing the network id binary by one
 rngmax=[0,0,0,0] #same process as before on lines 55-61 applied to the upper and lower bounds on the ip range except as noted
 rngmin=[0,0,0,0]
 for i in range(32):
  rngmax[i//8]+=(int(rngmaxbin[i]))*(2**(7-(i%8)))
  rngmin[i//8]+=(int(rngminbin[i]))*(2**(7-(i%8)))
 for i in range(4):
  if i>0:
   rngstr[0]+="."
   rngstr[1]+="."
  rngstr[0]+=str(rngmin[i])
  rngstr[1]+=str(rngmax[i])
 return ipstr,clss,mskstr,idstr,brdcststr,rngstr #returns the output strings

if __name__=='__main__':
 import sys
 fullip=sys.argv[1] #gets the command line argument
 arrfullip=fullip.split('/') #seperates the ip from the cidr
 ipstr,clss,mskstr,idstr,brdcststr,rngstr=netcalc(arrfullip[0],int(arrfullip[1])) #gets the values from the function
 print("IP: ",ipstr,"\nClass: ",clss,"\nNet-Mask: ",mskstr,"\nNet-ID: ",idstr,"\nBroadcast-Address: ",brdcststr,"\nRange: ",rngstr[0],"-",rngstr[1],sep="") #prints values to the console
