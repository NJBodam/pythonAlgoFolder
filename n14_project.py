# Step Three - Analyze Your Data
# Brainstorm some questions you could answer using the data set you chose, then start answering those questions. Here are some ideas to get you started:

# Titanic Data
# What factors made people more likely to survive?
# Baseball Data
# What is the relationship between different performance metrics? Do any have a strong negative or positive relationship?
# What are the characteristics of baseball players with the highest salaries?
# Make sure you use NumPy and Pandas where they are appropriate!


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = '/Users/mac/Documents/pythonLearning/pythonAlgo/Data Spreadsheet/titanic_data.csv'
titanic_df = pd.read_csv(filename)

# plt.hist(data, bins=20) 

# Plot a graph
# plt.plot(x_values, y_values)

# Display the graph
# plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

filename = '/Users/mac/Documents/pythonLearning/pythonAlgo/Data Spreadsheet/titanic_data.csv'
df = pd.read_csv(filename)

if True:
    print(titanic_df[:10])
    
#     grouped_data = titanic_df.groupby('Sex')
    
    # You can take one or more columns from the result DataFrame
#     print(grouped_data.groups)
    
    print('\n') # Blank line to separate results
    
#     first_even = titanic_df.groupby('Survived', as_index=False).first()
#     print(first_even)
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
#     print(grouped_data['Survived'].sum())
    print(df.isnull().sum())
    print(df.dtypes)


# %%
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df['Age'] = df['Age'].fillna(df['Age'].mean())

    print(df.isnull().sum())
    
    embarked = df['Embarked'].unique()
    for embark in embarked:
        print(embark)
    
    df['Embarked'] = df['Embarked'].fillna('N')
    df['Embarked'] = df['Embarked'].map({'Q': 0,'S':1,'C':2, 'N':3}).astype(int)
    df['Sex'] = df['Sex'].map({'female': 0,'male':1}).astype(int)
    df['Age'] = df['Age'].astype(int)
    df['Fare'] = df['Fare'].astype(int)
    
    print(df.dtypes)
    print(df.isnull().sum())


    

# %%
print(df.head())
data = df.drop(['PassengerId','Name','Cabin','Ticket'], axis =1, inplace=True)


# %%
fig = plt.figure(figsize =(10, 7))
plt.hist(x = [df[df['Survived']==1]['Age'], df[df['Survived']==0]['Age']],stacked=True, color = ['g','r'],label = ['Survived','Not survived'])
plt.title('Age Histogram with Survival')
plt.xlabel('Age')
plt.ylabel('No of passengers')
plt.legend()

# fig = plt.figure(figsize = (7, 5))
# plt.hist(x = [df[df['Survived']==1]['Sex'], df[df['Survived']==0]['Sex']], stacked=True, color = ['blue', 'red'], label = ['Survived', 'Not survived'])
# plt.title('Sex Histogram with Survival')
# plt.xlabel('Sex')
# plt.ylabel('No of passengers')
# plt.legend()

survival_counts = df['Survived'].value_counts()
survival_counts.plot(kind='bar', rot=3)
plt.title('Survival by Sex')
plt.ylabel('No of passengers')
plt.xlabel('Sex')

fig = plt.figure(figsize = (5, 5))
plt.hist(x = [df[df['Survived']==1]['Fare'], df[df['Survived']==0]['Fare']], stacked=True, label = ['Survived', 'Not survived'])
plt.title('Fare Histogram with Survival')
plt.xlabel('Fare')
plt.ylabel('No of passengers')
plt.legend()




# %%
# Survival Count

column = 'Survived'

# Create a bar chart
survival_counts = df[column].value_counts()
survival_counts.plot(kind='bar', rot=0)

# Adding labels and title
plt.xlabel('Survived')
plt.ylabel('Count')
plt.title('Survival Count (0 = No, 1 = Yes)')

# Show the plot
plt.show()



# %%
Train = df.drop(['Survived'], axis=1)
Test = df.iloc[:,1]
print(Train)
print(Test)
x_train, x_test, y_train, y_test = train_test_split(Train, Test, test_size = 0.2, random_state = 1)

LR = LogisticRegression(solver='liblinear', max_iter=200)
LR.fit(x_train, y_train)
y_pred = LR.predict(x_test)
LRAcc = accuracy_score(y_pred,y_test)
print('Logistic regression accuracy: {:.2f}%'.format(LRAcc*100))

# %%

age_groups = pd.cut(df['Age'], bins=range(0, 100, 10), include_lowest=True)
pd.crosstab(age_groups, df.Survived).plot(kind='bar')

plt.ylabel('No.of Passengers')
plt.title('Age over Survival')
plt.grid(color="red", linestyle="--", alpha=0.5)
# print(age_groups)


def convert_sex(column):
    return pd.qcut(column, [0, 1], labels=['Female', 'Male'])
# sex_class = df.Sex.apply(convert_sex)

# df['Sex'] = df['Sex'].map({0: 'Female',1:'Male'}).astype(object)

print(df.Sex)
pd.crosstab(df.Sex, df.Survived).plot(kind='bar')
plt.ylabel('No of Passengers')
plt.title('Sex of Survival')
plt.grid(color='red', linestyle=':', alpha=0.5)

# %%
from sklearn.preprocessing import LabelEncoder
obj=LabelEncoder()
df['Sex']=obj.fit_transform(df['Sex'])
df.head(4)

# %%
# from sklearn import tree
# from sklearn.model_selection import train_test_split

# model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)

# x_train, x_test, y_train, y_test = train_test_split(df, df['Survived'], test_size=0.3)
# model.fit(x_train,y_train)

survived_df=df['Survived'].value_counts()
survived_df.plot(kind='pie',autopct='%1.1f%%',title='Survival Distribution')

# %%
df.groupby('Pclass').count()
print(df[df['Survived']==1].groupby('Pclass')['Survived'].count())
print(df[df['Survived']==0].groupby('Pclass')['Survived'].count())
print(df.groupby('Pclass')['Survived'].mean()*100)



# %%
#To Predict Your Survival You can use. Pclass=[1 or 2 or 3] Sex=[male=1,female=0], Age=[Your_Age], Fare[0-512]

# %%




