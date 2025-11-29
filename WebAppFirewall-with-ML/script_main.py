from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import os
import urllib.parse
import joblib
import random

def loadFile(name):
    directory = str(os.getcwd())
    filepath = os.path.join(directory, name)
    with open(filepath, 'r', encoding="utf8") as f:
        data = f.readlines()
    data = list(set(data))  # remove duplicates
    result = []
    for d in data:
        d = str(urllib.parse.unquote(d.strip()))  # strip newline + decode
        if d:  # skip empty lines
            result.append(d)
    return result

# Load data
badQueries = loadFile('badqueries.txt')
goodQueries = loadFile('goodqueries.txt')

badQueries = list(set(badQueries))
goodQueries = list(set(goodQueries))

# 🔹 OPTIONAL: downsample to speed up training if dataset is huge
MAX_SAMPLES_PER_CLASS = 10000  # you can reduce to 5000 if still slow

if len(badQueries) > MAX_SAMPLES_PER_CLASS:
    badQueries = random.sample(badQueries, MAX_SAMPLES_PER_CLASS)

if len(goodQueries) > MAX_SAMPLES_PER_CLASS:
    goodQueries = random.sample(goodQueries, MAX_SAMPLES_PER_CLASS)

allQueries = badQueries + goodQueries
yBad = [1 for _ in range(len(badQueries))]
yGood = [0 for _ in range(len(goodQueries))]
y = yBad + yGood
queries = allQueries

# 🔹 Make TF-IDF a bit lighter (fewer features)
vectorizer = TfidfVectorizer(
    min_df=2,              # ignore super-rare patterns
    analyzer="char",
    sublinear_tf=True,
    ngram_range=(1, 2)     # use 1-2 char ngrams instead of 1-3
)

X = vectorizer.fit_transform(queries)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

badCount = len(badQueries)
goodCount = len(goodQueries)

# 🔹 Faster Random Forest (less trees, limited depth, use all CPU cores)
rf = RandomForestClassifier(
    class_weight={1: 2 * goodCount / badCount, 0: 1.0},
    n_estimators=50,       # was 100
    max_depth=20,          # limit tree depth
    n_jobs=-1,             # use all CPU cores
    random_state=42
)

print("Training RandomForest, this may take a few moments...")
rf.fit(X_train, y_train)

# Save model + vectorizer
joblib.dump(rf, 'random_forest_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

# Evaluation
predicted = rf.predict(X_test)
fpr, tpr, _ = metrics.roc_curve(y_test, (rf.predict_proba(X_test)[:, 1]))
auc = metrics.auc(fpr, tpr)

print("Bad samples: %d" % badCount)
print("Good samples: %d" % goodCount)
print("Baseline Constant negative: %.6f" % (goodCount / (goodCount + badCount)))
print("------------")
print("Accuracy: %f" % rf.score(X_test, y_test))
print("Precision: %f" % metrics.precision_score(y_test, predicted))
print("Recall: %f" % metrics.recall_score(y_test, predicted))
print("F1-Score: %f" % metrics.f1_score(y_test, predicted))
print("AUC: %f" % auc)
