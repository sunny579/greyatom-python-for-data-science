# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)
print(data.columns)
#Code starts here

# Step 1 
#Reading the file
loan_status = data['Loan_Status'].value_counts(ascending = False)
loan_status.plot(kind ='bar')
#Creating a new variable to store the value counts


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind = 'bar',stacked = False)
plt.xlabel('PropertyArea')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)



#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education','Loan_Status'])

education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind = 'bar',stacked = True)

#Changing the x-axis label
plt.xlabel('Education Status')


#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation = 45)

# Step 4 
#Subsetting the dataframe based on 'Education' columngGraduate
graduate = data[data['Education'] == 'Graduate']
#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education'] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate.plot(kind = 'density',label ='Graduate')

#Plotting density plot for 'Graduate'

not_graduate.plot(kind  = 'density',label ='Not Graduate')
#For automatic legend display


# Step 5
#Setting up the subplots
fig , (ax_1,ax_2,ax_3)= plt.subplots(nrows = 3 ,ncols = 1)

#Plotting scatter plot
data.plot.scatter(x='ApplicantIncome' , y='LoanAmount',ax =ax_1)

#Setting the subplot axis title
data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)

#Plotting scatter plot
data['TotalIncome'] = data['ApplicantIncome']+data['CoapplicantIncome']


#Setting the subplot axis title
data.plot.scatter(x='TotalIncome',y='LoanAmount',ax= ax_3)

#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



