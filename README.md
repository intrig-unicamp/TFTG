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
# addGenerationPort(P_ID) Adiciona a porta de geração de trafego
Gerador.addGenerationPort(68)

# Adiciona a porta de saida do equipamento
Gerador.addOutputPort(5, 160, "100G") #Physical Port, Port ID(D_P), Port bw
```


<!-- Isso é um comentário e não será exibido no GitHub 

Gerador = generator("pipo")


# Adiciona os endereços de fonte e destino do pacote
Gerador.addIP(IP_dst="10.2.2.2", IP_src = "10.2.2.1") # ?
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

#### Add a packet flow
Add a new flow of packets to be generated. The optional parameters have default values

Mandatory parameters: 

  Name of the flow (for later identification)

Optional parameter
 - MODE of generation (could be by histograms or using numerical parameters)
 - PCP, indicating the priority of the flow (0-7)
 - PktLen, with the packet size in bytes
 - Eth_src and  Eth_dest, indicating the MAC source and destination
 - IP_src and  IP_dest, indicating the IP source and destination
  
```python
Gerador.addFlow(name,mode="computed",PCP=0,PktLen=654,Eth_src="10.2.2.2",Eth_dest="10.2.2.3",IP_src="198.168.1.0",IP_dest="198.168.1.1")
```

The Optional parameters can be set later in the code

```python
Gerador.genMode("histogram")
# histogram(file) Recebe o caminho para o arquivo de histograma
Gerador.histogram("histogram.xml")
```

```python
Gerador.genMode("computed")
# distribution(sendInt, intStdDev, pktLen) recebe o intervalo de produção (ns), o desvio padrão do envio de pacotes, e o tamanhode cada pacote (B)
Gerador.distribution(sendInt = 100, intStdDev = 0, pktlen = 64)
```



## Examples




## Team
