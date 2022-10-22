# df Create mantually  pd.DataFrame()
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
# Barchart create using matplotlib .plot.bar()
ax = df.plot.bar(x='lab', y='val', rot=0)
plt.show()
