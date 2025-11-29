import joblib
import urllib.parse

MODEL_PATH = "random_forest_model.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return model, vectorizer
    except Exception as e:
        print(f"[ERROR] Failed to load model or vectorizer: {e}")
        print("Make sure you have run `python3 script_main.py` successfully.")
        exit(1)

def classify_url(url: str):
    model, vectorizer = load_artifacts()

    # Decode URL-encoded characters like %20 etc.
    decoded_url = urllib.parse.unquote(url)

    # Vectorize
    X = vectorizer.transform([decoded_url])

    # Predict
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]  # probability of being malicious (class 1)

    if pred == 1:
        label = "MALICIOUS"
    else:
        label = "SAFE"

    print(f"\nURL: {url}")
    print(f"Decoded: {decoded_url}")
    print(f"Prediction: {label}")
    print(f"Malicious probability: {prob:.4f}")

if __name__ == "__main__":
    print("=== URLKnight CLI Web Application Firewall ===")
    print("Type a URL to classify (or 'q' to quit)\n")

    while True:
        url = input("Enter URL: ").strip()
        if url.lower() in ("q", "quit", "exit"):
            print("Exiting...")
            break
        if not url:
            print("Please enter a non-empty URL.")
            continue

        classify_url(url)
        print()

