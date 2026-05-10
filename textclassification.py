# Practical 9: Text Classification

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

n = int(input("Enter number of training samples: "))

texts = []
labels = []

for i in range(n):

    text = input(f"Enter text {i+1}: ")
    label = input("Enter label (positive/negative): ")

    texts.append(text)
    labels.append(label)

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test prediction
test_text = [input("Enter text for prediction: ")]

test_vector = vectorizer.transform(test_text)

prediction = model.predict(test_vector)

print("\nPredicted Label:", prediction[0])
