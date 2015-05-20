import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

import matplotlib.pyplot as plt
import pandas as pd

loansData.boxplot(column='Amount.Requested')

plt.show()

loansData.hist(column='Amount.Requested')
plt.show()

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()