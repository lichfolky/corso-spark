### Eseguire un file python in python
"""
exec(open("spark-examples/hello_spark.py").read())
"""

### grafici in python

import matplotlib.pyplot as plt
plt.style.use('ggplot')
myplot = df_pandas.plot(kind='barh', x='occupation', y='plus_50k')
