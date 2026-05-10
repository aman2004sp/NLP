# Practical 6: POS Tagging

import nltk
from collections import Counter

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = input("Enter text: ")

# Tokenize
tokens = nltk.word_tokenize(text)

# POS tagging
pos_tags = nltk.pos_tag(tokens)

print("\nPOS Tags:")
print(pos_tags)

# Extract nouns
nouns = [word for word, pos in pos_tags if pos.startswith('NN')]

print("\nNouns:")
print(nouns)

# POS frequency
pos_freq = Counter(tag for word, tag in pos_tags)

print("\nPOS Frequency Dictionary:")
print(dict(pos_freq))
