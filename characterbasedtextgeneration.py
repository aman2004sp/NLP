# Practical 10: Character-Based Text Generation

from collections import defaultdict
import random

text = input("Enter training text: ")

# Create transitions
transitions = defaultdict(list)

for i in range(len(text) - 1):

    current_char = text[i]
    next_char = text[i + 1]

    transitions[current_char].append(next_char)

start = input("Enter starting character: ")

generated = start

length = int(input("Enter generation length: "))

for _ in range(length):

    last_char = generated[-1]

    if last_char in transitions:

        next_char = random.choice(transitions[last_char])

        generated += next_char

    else:
        break

print("\nGenerated Text:")
print(generated)
