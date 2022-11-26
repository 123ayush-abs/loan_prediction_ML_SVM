import pandas as pd 
import numpy as np 
import seaborn as snb 
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# loading the dataset to pandas DataFrame
loan_dataset = pd.read_csv('loan_data.csv')
loan_dataset.head(2)

# statistical measures
loan_dataset.describe()

# number of missing values in each column
loan_dataset.isnull().sum()

# dropping the missing values
loan_dataset = loan_dataset.dropna()
loan_dataset.isnull().sum()

# label encoding
loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)
loan_dataset.head(2)

# replacing the value of 3+ to 4 in loan dependent columns
loan_dataset = loan_dataset.replace(to_replace='3+', value=4)
# dependent values
loan_dataset['Dependents'].value_counts()
# loan_dataset['Education'].value_counts()

# """Data visulalization using seaborn"""

# education & Loan Status
snb.countplot(x='Education',hue='Loan_Status',data=loan_dataset)

# marital status & Loan Status
snb.countplot(x='Married',hue='Loan_Status',data=loan_dataset)

# convert categorical columns to numerical values
loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

# separating the data and label
X = loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = loan_dataset['Loan_Status']
print(Y)

X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)

# """Training the model using SVM model

# """

classifier = svm.SVC(kernel='linear')

#training the support Vector Macine model
classifier.fit(X_train,Y_train)


# Model evaluation on different paaremetr
# accuracy score on training data
X_train_prediction = classifier.predict(X_train)
training_data_accuray = accuracy_score(X_train_prediction,Y_train)
print(X_train_prediction)

print('Accuracy on training data : ', training_data_accuray)

# accuracy score on training data
X_test_prediction = classifier.predict(X_test)
test_data_accuray = accuracy_score(X_test_prediction,Y_test)
print('Accuracy on test data : ', test_data_accuray)