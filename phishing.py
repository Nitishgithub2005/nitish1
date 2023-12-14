def detect_phishing(url):
    # Check if the URL contains "phishing" as a substring
    if "phishing" in url.lower():
        return "Phishing Detected"
    else:
        return "No Phishing Detected"