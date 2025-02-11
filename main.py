from src.data import *
from src.headers import *

TG = generator("tftg")

TG.addGenerationPort(68)
TG.addOutputPort(5, 160, "100G") #Physical Port, Port ID(D_P), Port bw

TG.addVariance([10000, 90000], [8, 2])
TG.addIP(dst = "10.0.0.2")                #set IP header with destination address

Header = Header(name = "TSN", size = 8) #create a 8 bits cutom header part 1
Header.addField(Field("metadata", 8))        #create a 8 bits cutom header part 1
TG.addHeader(Header)  
	

TG.generate()
