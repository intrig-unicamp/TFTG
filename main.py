from data import *

TG = generator("tftg")

TG.addGenerationPort(68)
TG.addOutputPort(5, 160, "100G") #Physical Port, Port ID(D_P), Port bw
