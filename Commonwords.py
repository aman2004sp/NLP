# Practical 3: Most Common Words Frequency

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')

text = input("Enter text: ")

# Lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenize
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word not in stop_words]

# Frequency count
freq = Counter(filtered)

print("\nMost Common Words:")
for word, count in freq.most_common():
    print(word, ":", count)
