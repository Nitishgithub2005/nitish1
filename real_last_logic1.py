import ch_ml as chml
from sklearn.ensemble import RandomForestClassifier 
import Feature_extraction_ff as fex

best_model = RandomForestClassifier(n_estimators=60)
best_model.fit(chml.X, chml.y)

def detect_phishing(domain):
    def get_url_from_domain(domain, protocol="http"):
        return f"{protocol}://{domain}"
    list_200 = []
    domain_name = domain
    protocols = [ "https", "http","ftp", "smtp", "tcp", ]
    for protocol in protocols:
        try:
            url = get_url_from_domain(domain_name, protocol)
            response = requests.get(url, timeout=3)
            list_200.append(url)
        except Exception as e:
            pass
    if len(list_200)>0:
            print(fex.data_set_list_creation(list_200[0]))

            new_url_features = fex.data_set_list_creation(list_200[0])


            new_url_features = [new_url_features]  


            prediction = best_model.predict(new_url_features)


            if prediction == 1:
                return "The URL  is precdicted as a phishing URL."
            else:
                return "The URL  is predicted as a legitimate URL."
    else:
        return "Not found"