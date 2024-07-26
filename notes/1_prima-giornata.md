1 
---
D: Cos'è big data?

cosa vuol dire fare analisi big data:
- Grandi dataset distribuiti

V dei bigdata:
volume
velocità
varietà
valore
validità

Ssempio sensori realtime

Spark è un sistema di calcolo ditribuito per processare big data 

high speed e in-memory processing

- batch processing
- tempo reale, detto anche streaming

Spark è veloce perché distribuisce i dati in clusters e li processa in parallelo e in memory è un modello di calcolo distribuito

Perchè usare spark:
- molto robusto, fault tolerant
- in memory processing
- librerie per l'analisi e il processing
- api per java, scala, python e R
- compatibile con vari data framework e data sources

2 
---
Origini: hadoop map reduce e articolo scientifico google


3
---
distributed computing

anche una sola macchina con multipli thread / processi

un cluster di computers

Strutture immutabili:

tupla = (1, 2)
testo = "ciao"
testo[2] = "c" # errore
tupla[2] = "c" # errore

non sono modificabili, se non creando una nuova copia

differenza tra Map e for
iterazioni isolate, eseguite non necessariamente in ordine e sullo stesso core.

immutabile è anche, spazio in memoria fisso

RDD resilient ditributed dataset - immutable, non tabulare, non ha schema nè datatype vengono usati internamente

tar -xf archive.zip
