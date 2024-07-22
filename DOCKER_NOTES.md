installa estensioni:
- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)


Installa Docker

Attiva opzione:
"Add the *.docker.internal names to the host's /etc/hosts file (Requires password)"


### pySpark con Docker 
Usiamo l'immagine docker ufficiale di pyspark:
```
docker run -it -p 4040:4040 --hostname localhost --rm spark:python3 /opt/spark/bin/pyspark
```

### pySpark e jupyter con Docker

```
docker run -it -p 8888:8888 --hostname localhost jupyter/pyspark-notebook
```

### per usare gli esercizi
```
docker build . -t spark-demo 
docker run -it -p 4040:4040 --hostname localhost --rm spark-demo /opt/spark/bin/pyspark  
```
## Altro
### Attaccare shell container

```
docker ps

docker exec -it <mycontainer> bash
```

### To create/change a root password in a running container

docker exec -itu 0 {container} passwd

### environment variables
https://github.com/apache/spark-docker/blob/master/OVERVIEW.md#environment-variable