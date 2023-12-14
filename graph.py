# legitimate_data = pd.read_csv('legit_structured_ff.csv')
# phishing_data = pd.read_csv('phish_data_ff.csv')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
legitimate_data = pd.read_csv('our_legit.csv')
phishing_data = pd.read_csv('our_phish.csv')


all_data = pd.concat([legitimate_data, phishing_data])

X = all_data.drop(['Label','url'], axis=1) 
y = all_data['Label']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='')
X_train_processed = imputer.fit_transform(X_train_scaled)
X_test_processed = imputer.transform(X_test_scaled)

