## Install JDK 
https://www.oracle.com/java/technologies/downloads/

## Installazione Windows di Spark

Scarica da:  
https://spark.apache.org/downloads.html

Estrai la cartella compressa, rinominala in `Spark` e spostala in `C:\`

## Hadoop

Salva `winutils.exe` da https://github.com/cdarlint/winutils
nella cartella Hadoop/bin 

https://phoenixnap.com/kb/install-spark-on-windows-10

### Configura le variabili di sistema

Cerca `Variabili di ambiente`

Crea variabile `SPARK_HOME` con valore `C:\Spark`  
Alla variabile Path, aggiungi `%SPARK_HOME%\bin`

Crea variabile `HADOOP_HOME` con valore `C:\HADOOP`  
Alla variabile Path, aggiungi `%HADOOP_HOME%\bin`

## Python

https://www.python.org/downloads/

Installa python, assicurati di selezionare `ADD to PATH`


## Installa pyspark in un venv
Crea un nuova cartella per il tuo progetto, poi spostati nella cartella con il terminale


```
python -m venv .pyspark-env
```
Ora attiva l'venv:

**Windows**

In PowerShell:
```
.pyspark-env\Scripts\Activate.ps1
```
Se in cmd.exe:
```
.pyspark-env\Scripts\activate.bat
```  
**Se ci sono errori di permessi, dovrebbe bastare questo comando:**
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

**Linux and MacOS**
```
source myvenv/bin/activate
```

### PySpark

Installa con pip:
```
pip install pyspark
pip install findspark
pip install jupyterlab
```

## Altro

### ERROR ShutdownHookManager: Exception while deleting Spark temp dir:

The issue is in the ShutdownHook that tries to delete the temp files but fails. Though you cannot solve the issue, you can simply hide the exceptions by adding the following 2 lines to your log4j.properties file in %SPARK_HOME%\conf. If the file does not exist, copy the log4j.properties.template and rename it.

logger.shutdownhookmanager.name = org.apache.spark.util.ShutdownHookManager
logger.shutdownhookmanager.level = OFF

logger.sparkenv.name = org.apache.spark.SparkEnv
logger.sparkenv.level = ERROR

### Scala

https://get-coursier.io/docs/cli-installation

sbt
~run

https://docs.scala-lang.org/scala3/book/introduction.html
https://docs.scala-lang.org/tour/tour-of-scala.html