# <u>Web Application Firewall for Malicious Request Detection Using Machine Learning</u>

This project implements a Machine Learning–based Web Application Firewall (WAF) designed to classify incoming web requests as **malicious** or **safe**.  
By analyzing URL patterns using TF-IDF vectorization and a Random Forest classifier, the system helps detect harmful requests such as **SQL Injection (SQLi)**, **Cross-Site Scripting (XSS)**, and other injection-based attacks.

The project includes both a **Command-Line Interface (CLI)** for universal use and an optional **Tkinter GUI**.

---

## ✨ Features

- Real-time malicious URL detection  
- Random Forest–based classification  
- Character-level TF-IDF feature extraction  
- CLI (fully OS-compatible)  
- GUI using Tkinter (optional)  
- Easy dataset and model customization  

---

## 📁 Folder Structure

Web-Application-Firewall-ML/
│
├── badqueries.txt # Dataset: malicious URLs
├── goodqueries.txt # Dataset: safe URLs
├── script_main.py # Model training script
├── cli.py # Command-line URL classifier
├── gui.py # Tkinter GUI for URL classification (optional)
├── requirements.txt # Dependencies list
├── random_forest_model.pkl # Saved ML model (auto-created)
├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer (auto-created)
├── LICENSE # MIT License
└── README.md # Documentation

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Web-Application-Firewall-ML.git
cd Web-Application-Firewall-ML

2️⃣ Create a virtual environment

macOS/Linux
python3 -m venv venv
source venv/bin/activate
Windows
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt
🧠 Training the Machine Learning Model
Run the training script:
python3 script_main.py
This will:
Load and clean dataset files
Vectorize URLs using TF-IDF (1–3 character n-grams)
Train a Random Forest model
Evaluate performance
Save:
random_forest_model.pkl
tfidf_vectorizer.pkl
These files are used for prediction.
🖥️ Running the CLI Firewall (Recommended)
The CLI version is compatible with all operating systems, including macOS where Tkinter may not work.
python3 cli.py
Example:
Enter URL: http://example.com/test.php?id=1' OR '1'='1

🛑 Result: MALICIOUS

To exit:
Enter URL: q
🖼️ Running the GUI (Optional)
python3 gui.py

⚠️ Note:

Tkinter may not run on older macOS versions due to framework linking issues.
If GUI fails, use the CLI version instead.
🧩 Customization Options
Extend datasets (badqueries.txt, goodqueries.txt)
Improve ML model (try SVM, Logistic Regression, XGBoost)
Tune Random Forest hyperparameters
Deploy as a REST API using Flask/FastAPI
Build a full web dashboard
Integrate with existing WAF systems

🏁 Project Summary

This project demonstrates how Machine Learning enhances web security by detecting malicious web requests before they reach the server.
Using TF-IDF feature extraction and a Random Forest classifier, this system achieves robust and explainable detection performance suitable for:
Academic research
Web security demonstrations
Real-world security prototypes
ML-based URL filtering mechanisms

📜 License

This project is licensed under the MIT License.
You are free to modify, distribute, and use this project, provided that the original license file remains included.