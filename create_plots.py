# to run, execute this command in the command line:
# python create_plots.py pagecounts-20160802-150000.txt pagecounts-20160803-150000.txt
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
filename1 = sys.argv[1]
filename2 = sys.argv[2]

data1 = pd.read_table(filename1, sep=' ', header=None, index_col=1,
        names=['lang', 'page', 'views', 'bytes'])

data1_sort = data1.sort_values(by=['views'], ascending=False)
# print(data1_sort)

data2 = pd.read_table(filename2, sep=' ', header=None, index_col=1,
        names=['lang', 'page', 'views', 'bytes'])

data2_sort = data2.sort_values(by=['views'], ascending=False)
data1_sort['views2'] = data2_sort['views']

# print (data1_sort)
# print (data2_sort)

plt.figure(figsize=(10, 5)) # change the size to something sensible
plt.subplot(1, 2, 1) # subplots in 1 row, 2 columns, select the first
plt.plot(data1_sort['views'].values)
plt.title('Popularity Distribution')
plt.xlabel('Rank')
plt.ylabel('Views')

plt.subplot(1, 2, 2) # ... and then select the second
plt.scatter(data1_sort['views'].values, data1_sort['views2'].values)
plt.title('Daily Correlation')
plt.xlabel('Day 1 views')
plt.ylabel('Day 2 views')
plt.xscale('log')
plt.yscale('log')
plt.show()
plt.savefig('wikipedia_Tom.png')


