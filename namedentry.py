# Practical 7: Named Entity Recognition

import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

n = int(input("Enter number of headlines: "))

headlines = []

for i in range(n):
    headline = input(f"Enter headline {i+1}: ")
    headlines.append(headline)

for headline in headlines:

    doc = nlp(headline)

    print("\nHeadline:", headline)
    print("Named Entities:")

    for ent in doc.ents:
        print(ent.text, "-", ent.label_)
