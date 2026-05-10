# Natural Language Processing Practicals

This repository contains Python programs for NLP practicals based on the syllabus guidelines.

---

# Practicals Included

1. Text Preprocessing
2. Regex Pattern Extraction
3. Most Common Word Frequency
4. TF-IDF Matrix Generation
5. Unigram and Bigram Language Model
6. POS Tagging and Noun Extraction
7. Named Entity Recognition (NER)
8. IMDB Movie Review Sentiment Classification
9. Text Classification
10. Character-Based Text Generation

---

# Requirements

- Python 3.9 or above
- pip package manager

---

# Install All Dependencies (Single Command)

## Windows

```bash
pip install nltk spacy scikit-learn pandas numpy
```

If pip does not work:

```bash
python -m pip install nltk spacy scikit-learn pandas numpy
```

---

## Linux / Ubuntu

```bash
pip3 install nltk spacy scikit-learn pandas numpy
```

If pip3 does not work:

```bash
python3 -m pip install nltk spacy scikit-learn pandas numpy
```

---

# Fixing pip Issues

Sometimes you may get errors like:

```text
'pip' is not recognized as an internal or external command
```

or

```text
No module named pip
```

Follow the steps below.

---

# Windows pip Fix

## Step 1 — Check Python Installation

```bash
python --version
```

If Python version appears, continue.

If not:

Download Python from:

https://www.python.org/downloads/

IMPORTANT:

During installation check:

```text
☑ Add Python to PATH
```

---

## Step 2 — Check pip

```bash
pip --version
```

---

## Step 3 — If pip is not recognized

Try:

```bash
python -m pip --version
```

Then install packages using:

```bash
python -m pip install nltk spacy scikit-learn pandas numpy
```

---

## Step 4 — Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# Linux / Ubuntu pip Fix

## Update system

```bash
sudo apt update
```

---

## Install Python and pip

```bash
sudo apt install python3 python3-pip -y
```

---

## Verify Installation

```bash
python3 --version
pip3 --version
```

---

## Install Dependencies

```bash
pip3 install nltk spacy scikit-learn pandas numpy
```

---

# If Permission Denied Error Comes

Windows:

```bash
pip install --user nltk spacy scikit-learn pandas numpy
```

Linux:

```bash
pip3 install --user nltk spacy scikit-learn pandas numpy
```

---

# If SSL Error Comes

Upgrade pip first:

```bash
python -m pip install --upgrade pip
```

Then retry installation.

---

# Download Required NLTK Resources

Run Python shell:

```bash
python
```

Then execute:

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

Exit Python:

```python
exit()
```

---

# Download spaCy English Model

Windows:

```bash
python -m spacy download en_core_web_sm
```

Linux:

```bash
python3 -m spacy download en_core_web_sm
```

---

# Verify Installation

Run:

```bash
python
```

Then:

```python
import nltk
import spacy
import sklearn
import pandas

print("All libraries installed successfully!")
```

If no error appears, setup is complete.

---

# Practical Overview

---

## Practical 1 — Text Preprocessing

### Features

- Lowercase conversion
- Tokenization
- Stopword removal
- Stemming
- Lemmatization

### Libraries Used

- NLTK

---

## Practical 2 — Regex Extraction

### Features

- Extract usernames
- Extract hashtags
- Extract dates
- Extract phone numbers

### Libraries Used

- re (Regular Expressions)

---

## Practical 3 — Most Common Words

### Features

- Word tokenization
- Stopword filtering
- Frequency counting

### Libraries Used

- NLTK
- collections.Counter

---

## Practical 4 — TF-IDF Matrix

### Features

- Text vectorization
- TF-IDF matrix generation

### Libraries Used

- scikit-learn
- pandas

---

## Practical 5 — Language Model

### Features

- Unigram model
- Bigram model
- Add-one smoothing
- Sentence probability calculation

### Libraries Used

- NLTK

---

## Practical 6 — POS Tagging

### Features

- POS tagging
- Noun extraction
- POS frequency dictionary

### Libraries Used

- NLTK

---

## Practical 7 — Named Entity Recognition

### Features

- Detect:
  - Person names
  - Organizations
  - Locations
  - Dates

### Libraries Used

- spaCy

---

## Practical 8 — IMDB Sentiment Analysis

### Features

- IMDB movie review classification
- Positive/Negative prediction
- TF-IDF vectorization
- Naive Bayes classifier

### Dataset

- IMDB Dataset.csv

### Libraries Used

- pandas
- scikit-learn

---

## Practical 9 — Text Classification

### Features

- Train custom text classifier
- Predict labels

### Libraries Used

- scikit-learn

---

## Practical 10 — Character-Based Text Generation

### Features

- Character transition learning
- Next character prediction
- Random text generation

### Libraries Used

- collections
- random

---

# Running the Programs

Example:

```bash
python practical1.py
```

Linux:

```bash
python3 practical1.py
```

---

# IMDB Dataset Instructions

1. Download dataset from Kaggle
2. Extract zip file
3. Place:

```text
IMDB Dataset.csv
```

in the same folder as the Python scripts.

---

