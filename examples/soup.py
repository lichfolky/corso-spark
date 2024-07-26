from bs4 import BeautifulSoup
from pyspark.sql import SparkSession, Column, DataFrame
from pyspark.sql.functions import substr, substring
import requests

request = requests.get("https://www.wikipedia.com", verify=False)
soup = BeautifulSoup(request.content, "html.parser")
# print(soup.title.string)
# print(soup.a["href"])

links = soup.find_all("a")
# urls = [*map(lambda link: link["href"], links)]
# urls = list(map(lambda link: link["href"], links))
urls = [(link["href"], 3) for link in links]
# print(urls)

spark = SparkSession.builder.appName("soup-spark").getOrCreate()

df = spark.createDataFrame(urls, ["url", "count"])

df = df.withColumn("url", substr("url", "count"))
df = df.select(["url"]).withColumn("domain", substring("url", 0, 16))
df = df.groupby("domain").count()

df.show()

## df = df[df["domain"] == "en.wikipedia.org"]
## df.show()
# btrim(str[, trim])
