import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

print loansData.head ()

# Rename Columns and make them lower case
loansData.columns = loansData.columns.map(lambda x: x.replace('.', '_').lower())

#drop null values from the following rows using .dropna
df = loansData.dropna(subset=['home_ownership', 'interest_rate', 'monthly_income'])

#remove % symbol from interest rate and convert to float. Several different ways to do this:
#loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]
#df['interest_rate'] = df['interest_rate'].apply(lambda x: float(str(x).rstrip('%')))

df['interest_rate'] = df['interest_rate'].apply(lambda x: float(x[:-1]))

#using monthly income (instead of annual) to model interest rates
X = sm.add_constant(df['monthly_income'])
est = sm.OLS(df['interest_rate'], X).fit()

est.summary()

import statsmodels.formula.api as smf

est = smf.ols(formula='interest_rate ~ monthly_income + home_ownership', data=df).fit()

est.summary()

# interaction is what is the relationship with both of the variables are interacting together
est = smf.ols(formula='interest_rate ~ monthly_income * home_ownership', data=df).fit()

est.summary()