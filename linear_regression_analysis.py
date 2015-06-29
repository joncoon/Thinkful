import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#remove % symbol from interest rate and convert to float
#loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]

loansData['Interest.Rate'] = loansData['Interest.Rate'].apply(lambda x: float(x[:-1]))

#remove "month" at the end of loan length and convert to integer
#loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]

loansData['Loan.Length'] = loansData['Loan.Length'].apply(lambda x: x[:-6])

#create a new column called Fico Score with lower limit value
#loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]

# = operating on this list, assign this name, do this to this name
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda val: int(val.split('-')[0]))


loansData['Interest.Rate'][0:5] # first 5 rows of Interest.Rate
# 81174     8.90%
# 99592    12.12%
# 80059    21.98%
# 15825     9.99%
# 33182    11.71%
# Name: Interest.Rate, dtype: object

loansData['Loan.Length'][0:5] # first 5 rows of Loan.Length
# 81174    36 months
# 99592    36 months
# 80059    60 months
# 15825    36 months
# 33182    36 months
# Name: Loan.Length, dtype: object

loansData['FICO.Range'][0:5] # first 5 rows of FICO.Range
# 81174    735-739
# 99592    715-719
# 80059    690-694
# 15825    695-699
# 33182    695-699
# Name: FICO.Range, dtype: object

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Now you want to put the two columns together to create an input matrix (with one column for each independent variable)
x = np.column_stack([x1,x2])

#Now we create a linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

#And output the results summary
print f.summary()