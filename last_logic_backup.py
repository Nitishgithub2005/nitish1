import ch_ml as chml
from sklearn.ensemble import RandomForestClassifier 
import Feature_extraction_ff as fex

best_model = RandomForestClassifier(n_estimators=60)
best_model.fit(chml.X, chml.y)
 
print(fex.data_set_list_creation("https://www.google.com"))

new_url_features = fex.data_set_list_creation("https://www.google.com")


new_url_features = [new_url_features]  


prediction = best_model.predict(new_url_features)


if prediction == 1:
    print("The URL  is precdicted as a phishing URL.")
else:
    print("The URL  is predicted as a legitimate URL.")
