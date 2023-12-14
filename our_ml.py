import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier

# Read data
legitimate_df = pd.read_csv("our_legit.csv", low_memory=False)
phishing_df = pd.read_csv("our_phish.csv", low_memory=False)
df = pd.concat([legitimate_df, phishing_df], axis=0)

df = df.sample(frac=1).drop('url', axis=1).drop_duplicates()
# Extract features and target
X = df.drop('Label', axis=1)
Y = df['Label']
# Initialization of models
models = {
    'Decision Tree': DecisionTreeClassifier(),  # 1
    'Gaussian Naive Bayes': GaussianNB(),  # 2
    'Random Forest': RandomForestClassifier(n_estimators=60),  # 3
    'K-Neighbours Classifier': KNeighborsClassifier(),  # 4
    'Multilayer Perceptron': MLPClassifier(hidden_layer_sizes=(100,), max_iter=100, alpha=1),  # 5
    'SVM': SVC(kernel='linear'),  # 6
    'AdaBoost': AdaBoostClassifier(),  # 7
    'Neural Network': MLPClassifier(alpha=1),  # a
    'Gaussian Process': GaussianProcessClassifier(1.0 * RBF(1.0)),  # b
}

# Performance evaluation for each model
for model_name, model in models.items():
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)
    accuracy_list = cross_val_score(model, X, Y, cv=kfold, scoring='accuracy')
    precision_list = cross_val_score(model, X, Y, cv=kfold, scoring='precision')
    recall_list = cross_val_score(model, X, Y, cv=kfold, scoring='recall')

    print("\n-------", model_name, "-------")
    print(f"accuracy ==> {accuracy_list.mean()}")
    print(f"precision ==> {precision_list.mean()}")
    print(f"recall ==> {recall_list.mean()}")

# Overall average calculation
def calculate_average(metric_list):
    return sum(metric_list) / len(metric_list)

accuracy_avg = []
precision_avg = []
recall_avg = []

for model_name, model in models.items():
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)
    accuracy_avg.append(cross_val_score(model, X, Y, cv=kfold, scoring='accuracy').mean())
    precision_avg.append(cross_val_score(model, X, Y, cv=kfold, scoring='precision').mean())
    recall_avg.append(cross_val_score(model, X, Y, cv=kfold, scoring='recall').mean())

print("Overall average accuracy:", calculate_average(accuracy_avg))
print("Overall average precision:", calculate_average(precision_avg))
print("Overall average recall:", calculate_average(recall_avg))
