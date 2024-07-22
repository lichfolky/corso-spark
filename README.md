## Appunti per corso introduttivo a Spark

Per provare gli esercizi nella cartella `exercises`

Installare Docker, scaricandolo da qui:  


### pySpark con Docker 
Usiamo l'immagine docker ufficiale di pyspark:
```
docker run -it -p 4040:4040 --hostname localhost --rm spark:python3 /opt/spark/bin/pyspark
```


### pySpark e jupyter con Docker 
docker run -it -p 8888:8888 --hostname localhost jupyter/pyspark-notebook