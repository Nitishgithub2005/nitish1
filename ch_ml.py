import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier

# Load legitimate and phishing datasets
legitimate_df = pd.read_csv('our_legit.csv')
phishing_df = pd.read_csv('our_phish.csv')


# Combine both datasets
data = pd.concat([legitimate_df, phishing_df])

# Check for non-numeric values in columns
non_numeric_cols = data.select_dtypes(exclude=['number']).columns.tolist()
# print("Non-numeric columns:", non_numeric_cols)

# Replace or handle non-numeric values before converting to numeric
# For example, you can replace non-numeric values with NaN
data[non_numeric_cols] = data[non_numeric_cols].apply(pd.to_numeric, errors='coerce')

# Drop rows with NaN values if needed
data.dropna(inplace=True)

# Separate features and target
X = data.drop('Label', axis=1)
y = data['Label']
# Initialize models (same as before)
models = {
    'Decision Tree': DecisionTreeClassifier(),
    'Gaussian Naive Bayes': GaussianNB(),
    'Random Forest': RandomForestClassifier(n_estimators=60),
    'K-Neighbours Classifier': KNeighborsClassifier(),
    'Multilayer Perceptron': MLPClassifier(hidden_layer_sizes=(100,), max_iter=100, alpha=1),
    # 'SVM': SVC(kernel='linear'),
    'AdaBoost': AdaBoostClassifier(),
    'Neural Network': MLPClassifier(alpha=1),
    # 'Gaussian Process': GaussianProcessClassifier(1.0 * RBF(1.0)),
}

# Evaluate models
for model_name, model in models.items():
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    # Print evaluation metrics
    print(f"------ {model_name} ------")
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print("\n")

# K-Fold cross-validation to find the best model
best_model = None
best_score = 0

for model_name, model in models.items():
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
    mean_score = scores.mean()

    if mean_score > best_score:
        best_score = mean_score
        best_model = model_name

# print(f"Best Model: {best_model} with Accuracy: {best_score}")
