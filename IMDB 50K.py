# Practical 8: IMDB Movie Review Sentiment Classification

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
# Make sure IMDB Dataset.csv is in same folder

df = pd.read_csv("IMDB Dataset.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Check dataset size
print("\nDataset Shape:")
print(df.shape)

# Features and labels
X = df['review']
y = df['sentiment']

# Convert text into TF-IDF vectors
vectorizer = TfidfVectorizer(
    stop_words='english',
    max_features=5000
)

X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# User input prediction
while True:

    review = input("\nEnter movie review (or type exit): ")

    if review.lower() == "exit":
        break

    review_vector = vectorizer.transform([review])

    prediction = model.predict(review_vector)

    print("Predicted Sentiment:", prediction[0])
