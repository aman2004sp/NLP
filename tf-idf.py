# Practical 4: TF-IDF Matrix

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

n = int(input("Enter number of documents: "))

documents = []

for i in range(n):
    doc = input(f"Enter document {i+1}: ")
    documents.append(doc)

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=vectorizer.get_feature_names_out()
)

print("\nTF-IDF Matrix:")
print(df)
