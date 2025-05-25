from src.data import *

TG = generator("tftg") # type: ignore

TG.addGenerationPort(68)
TG.addOutputPort(1, 134, "10G") #Physical Port, Port ID(D_P), Port bw
TG.addOutputPort(2, 134, "10G") #Physical Port, Port ID(D_P), Port bw
#TG.histogram("histogram", "histogram.txt", 3) #DelayMode: 1 = normal, 2 = random, 3 = interval

TG.addFlow("flow1", fixedDelay=10000, outputPort=134)

TG.addFlow("flow2", fixedDelay=100000, outputPort=134)


TG.generate()