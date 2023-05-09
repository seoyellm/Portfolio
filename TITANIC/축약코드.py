import numpy as np
import pandas as pd

df = pd.read_csv("train.csv")
print(df.info())

print(df.isna().sum())
# Cabin          687  --> drop
# Embarked         2  --> S
# Age            177  --> mean()

# ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
print(df.select_dtypes("object").columns)

# drop : PassengerId,Name,Ticket,Fare,Cabin
# Survived,Pclass,Age(mean),SibSp,Parch,'Embarked(S -> 0,1,2)', 'Sex(1,0)'

df = df.drop(['PassengerId','Name','Ticket','Fare','Cabin'], axis=1)

df['Age']      =  df['Age'].fillna(df['Age'].mean())
df['Embarked'] =  df['Embarked'].fillna('S')
df['Embarked'] = df['Embarked'].replace(['S','C','Q'],[0,1,2])
df['Sex']      = df['Sex'].replace(['male','female'],[1,0])

print(df.info())
print(df.head(2))

#====================================================
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# ---------------------------------------------------------------------
# 1. X(문제지), y(답안지) 분리
# 2. 위에것을 8:2 비율로 train, test용으로 분리
#      문제지80,문제지20, 답안지80,답안지20 = train_test_split(문제지, 답안지)
# 3. 모델선택
#                     모델.fit(문제지80, 답안지80)
#           예측답안20 = 모델.predict(문제지20)
# 4. 점수확인 : *score(답안지20, 예측답안20)
# ---------------------------------------------------------------------
# 데이터프레임 : object X, 결측 X
# X,y분리 --> 8:2 --> 모델 --> fit --> predict  --> score --> 평가검증
# ---------------------------------------------------------------------
답안지891 = df['Survived']
문제지891 = df.drop('Survived', axis=1)

문제지80,                문제지20______, 답안지80,답안지20____ = train_test_split(문제지891, 답안지891, test_size=0.2, random_state=111)
모델 = DecisionTreeClassifier()
모델.fit(문제지80, 답안지80)
예측답안20 = 모델.predict(문제지20______)
s = accuracy_score(                            답안지20____, 예측답안20)
print(s)







