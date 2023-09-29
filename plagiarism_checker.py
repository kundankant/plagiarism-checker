import re
from collections import Counter

# Sample documents (replace with your own)
document1 = "This is a sample document."
document2 = "This is another document, similar but not identical."
document3 = "This is a completely unrelated document."

# Tokenize and preprocess text
def preprocess(text):
    text = text.lower()
    # Remove punctuation and split into words
    words = re.findall(r'\w+', text)
    return set(words)

# Preprocess the documents
set1 = preprocess(document1)
set2 = preprocess(document2)
set3 = preprocess(document3)

# Function to calculate Jaccard similarity
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union

# Define a similarity threshold
similarity_threshold = 0.5

# Check for plagiarism
similarity1_to_2 = jaccard_similarity(set1, set2)
similarity1_to_3 = jaccard_similarity(set1, set3)

if similarity1_to_2 >= similarity_threshold:
    print(f"Document 1 is similar to Document 2 (Jaccard Similarity: {similarity1_to_2:.2f})")

if similarity1_to_3 >= similarity_threshold:
    print(f"Document 1 is similar to Document 3 (Jaccard Similarity: {similarity1_to_3:.2f})")

