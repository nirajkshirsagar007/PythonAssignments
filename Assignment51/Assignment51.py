
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# PART 1 – LOAD AND PREPROCESS DATA
# -----------------------------------------------------------

# Load datasets
fake = pd.read_csv("fake.csv")
true = pd.read_csv("true.csv")

# Add labels
fake['label'] = 0   # Fake news
true['label'] = 1   # Real news

# Combine datasets
df = pd.concat([fake, true], axis=0).reset_index(drop=True)

# Use only 'text' column (you can also combine 'title' + 'text')
df = df[['text', 'label']]

# Drop null values
df.dropna(inplace=True)

# Separate features & target
X = df['text']
y = df['label']

# -----------------------------------------------------------
# PART 2 – FEATURE EXTRACTION (TF-IDF)
# -----------------------------------------------------------

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vectors = vectorizer.fit_transform(X)

# -----------------------------------------------------------
# PART 3 – TRAIN TEST SPLIT
# -----------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_vectors, y, test_size=0.2, random_state=42
)

# -----------------------------------------------------------
# PART 4 – TRAIN MODELS
# -----------------------------------------------------------

# Logistic Regression
log_model = LogisticRegression()
log_model.fit(X_train, y_train)

# Decision Tree
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)

# Voting Classifier
voting_hard = VotingClassifier(
    estimators=[('lr', log_model), ('dt', tree_model)],
    voting='hard'
)

voting_soft = VotingClassifier(
    estimators=[('lr', log_model), ('dt', tree_model)],
    voting='soft'
)

voting_hard.fit(X_train, y_train)
voting_soft.fit(X_train, y_train)

# -----------------------------------------------------------
# PART 5 – EVALUATION
# -----------------------------------------------------------

def evaluate(model, name):
    print("\n==============================")
    print(f"MODEL: {name}")
    print("==============================")

    y_pred = model.predict(X_test)
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(f"Confusion Matrix - {name}")
    plt.show()

# Evaluate individual & ensemble models
evaluate(log_model, "Logistic Regression")
evaluate(tree_model, "Decision Tree Classifier")
evaluate(voting_hard, "Voting Classifier – Hard Voting")
evaluate(voting_soft, "Voting Classifier – Soft Voting")