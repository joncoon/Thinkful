import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

print loansData.head ()

# Rename Columns and make them lower case
loansData.columns = loansData.columns.map(lambda x: x.replace('.', '_').lower())

#drop null values from the following rows using .dropna
df = loansData.dropna(subset=['home_ownership', 'interest_rate', 'monthly_income'])

print loansData.head ()

#remove % symbol from interest rate and convert to float. Several different ways to do this:
#loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]
#df['interest_rate'] = df['interest_rate'].apply(lambda x: float(str(x).rstrip('%')))

loansData['interest.rate'] = loansData['interestrate'].apply(lambda x: float(x[:-1]))

print loansData.head ()

loansData['interest_rate'] = loansData['interest_rate'].apply(lambda x: float(str(x).rstrip('%')))

print loansData.head ()


X = sm.add_constant(loansData['monthly_income'])
est = sm.OLS(loansData['interest_rate'], X).fit()

est.summary()