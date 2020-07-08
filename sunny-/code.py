# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

bank = pd.DataFrame(bank_data)

#Code starts here
categorical_var = bank.select_dtypes(include = 'object')
numerical_var = bank.select_dtypes(include = 'number')

#print(categorical_var)
#print(numerical_var)

# 2nd part
bank.drop(['Loan_ID'],inplace =True,axis = 1)
banks = bank

print(banks.isnull().sum())

bank_mode = banks.mode()
banks.fillna(bank_mode)

# 3rd part

avg_loan_amount = pd.pivot_table(banks,index = ['Gender','Married','Self_Employed'],values ='LoanAmount',aggfunc = 'mean')

print(avg_loan_amount)
#4th part

loan_approved_se = len(banks[(banks['Self_Employed'].str.startswith('Y')) & (banks["Loan_Status"].str.startswith('Y'))])
loan_approved_nse = len(banks[(banks['Self_Employed'].str.startswith('N')) &  (banks['Loan_Status'].str.startswith('Y'))])
percentage_se = loan_approved_se*100/614

percentage_nse = loan_approved_nse*100/614



# 5th part

loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan_term = len(loan_term[loan_term > 25])

#6th part

loan_groupby = banks.groupby('Loan_Status')

loan_groupby =loan_groupby[['ApplicantIncome','Credit_History']]

mean_values = loan_groupby.mean()
print(mean_values.iloc[1,0] ,2)









