# Practical 2: Regex Extraction with User Input

import re

text = input("Enter text: ")

# Extract usernames from emails
usernames = re.findall(r'([a-zA-Z0-9._%+-]+)@', text)

# Extract hashtags
hashtags = re.findall(r'#\w+', text)

# Extract dates
dates = re.findall(r'\b\d{1,2}/\d{1,2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b', text)

# Extract phone numbers
phones = re.findall(r'(?:\+91[- ]?)?\d{10}', text)

print("\nUsernames:", usernames)
print("Hashtags:", hashtags)
print("Dates:", dates)
print("Phone Numbers:", phones)
