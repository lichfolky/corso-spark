data = [("Mattia", 10), ("Arturo", 20), ("Barbara", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
