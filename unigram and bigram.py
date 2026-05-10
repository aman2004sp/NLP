# Practical 5: Unigram and Bigram Language Model

from collections import defaultdict
import nltk

nltk.download('punkt')

text = input("Enter training text: ")

tokens = nltk.word_tokenize(text.lower())

# Unigrams
unigrams = tokens

# Bigrams
bigrams = list(nltk.bigrams(tokens))

# Vocabulary size
vocab = set(tokens)
V = len(vocab)

# Count frequencies
unigram_counts = defaultdict(int)
bigram_counts = defaultdict(int)

for word in unigrams:
    unigram_counts[word] += 1

for bg in bigrams:
    bigram_counts[bg] += 1

# Add-one smoothing
def bigram_probability(w1, w2):
    return (bigram_counts[(w1, w2)] + 1) / (unigram_counts[w1] + V)

sentence = input("Enter sentence to calculate probability: ")

sentence_tokens = nltk.word_tokenize(sentence.lower())

probability = 1

for i in range(len(sentence_tokens) - 1):
    probability *= bigram_probability(
        sentence_tokens[i],
        sentence_tokens[i + 1]
    )

print("\nSentence Probability:", probability)
