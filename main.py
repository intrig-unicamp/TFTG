from src.data import *

TG = generator("tftg") # type: ignore

TG.addGenerationPort(68)
TG.addOutputPort(5, 160, "100G") #Physical Port, Port ID(D_P), Port bw

TG.genarate()