# TFTG: Time Fidelity Traffic Generation through P4/Tofino Programmable Hardware

Repository of paper NETWORK-24-00606 submitted for IEEE Network Magazine special issue of Deterministic, Reliable, Resilient and Programmable Networks for 6G.

## Overview

Overview da ferramenta, alguma figurinha


## Available features



## How to install

### Requirements

## How to use


## Available commands

### Setup commands

#### Add output port
Add the output port for the configurated traffic
Parameters: P_ID of output port (Tofino P-ID)

Usage:
```python
#addGenerationPort(P_ID)
Gen.addGenerationPort(68)
```

<!-- Isso é um comentário e não será exibido no GitHub 

from src.data import *
from src.headers import *

Gerador = generator("pipo")


###############################################
#### Packet generator Case 1
Gerador.addGenerationPort(68)
Gerador.genMode("") # histogram, computed (pega histograma.xml como no DETERMINISTIC6G, ou através de parametros) 
Gerador.histogram("histogram.xml") # Caminho pro histograma
Gerador.distribution(meanInt = 1000, stdDevInt = 100, pktSize=1000) # intervalo medio de produção de pacotes (ns), desvio padrao da produção (ideia, poe ser outra forma de variar), tamanho do pacote
Gerador.addOutputPort(5, 160, "100G") #Physical Port, Port ID(D_P), Port bw
Gerador.addEth(eth_dst="10.2.2.2", Eth_src = "10.2.2.1") # ?
#### TAS Case 2
Gerador.addFlow("name", 1, 150) # nome (para identificar), Priority (0-7), size (B)
Gerador.setGclPriPort(5, 160, 1, 100, 900, 0) #Physical Port, Port ID(D_P), priority (0-7), Time Open (ns), Time Closed (ns), Offset (ns)
Gerador.setGB(True) # Se verdadeiro deve computar a guardband (pkt_size/throughput) para n mandar pacotes mesmo q com o gate aberto antes do fim do intervalo
#### ATS Case 3
#### FRER Case 4
#### PREOF Case 4
#### Reordering Case 5
Gerador.reodering(False)
Gerador.reoderingLayer(2) # 2 FREF (TSN), 3 PREOF (DETNET)
#### gPTP Case 6
Gerador.setSyncPort(5,160) #Physical Port, Port ID(D_P)
Gerador.setGptpParams(syncInt = 125, correctField = 0, rateRatio = 1) # intervalo de sincronização (ms), valor setado pro correctionField (ns), valor setado pro rateRatio 


Gerador.generate()

-->


### Generation commands




## Examples




## Team
