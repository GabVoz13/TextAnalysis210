
import nltk
from nltk import FreqDist
from nltk.text import Text

# Download required resources (first time only)
nltk.download('punkt')
nltk.download('stopwords')

# --- Helper Functions ---

import os

def load_text(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        exit(1)  # Exit the program if the file is not found
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    words = [word for word in tokens if word.isalpha()]  # remove punctuation/numbers
    return words

def lexical_diversity(words):
    return len(set(words)) / len(words)

def get_most_common(words, n=10):
    return FreqDist(words).most_common(n)

def most_similar_word(target, words):
    text_obj = Text(words)
    print(f"Words similar to '{target}':")
    text_obj.similar(target)

# --- Load and Process Your Texts ---

avatar_words = preprocess(load_text("avatarSpeeches.txt"))
sonnets_words = preprocess(load_text("shakeSonnets.txt"))

# --- Analysis ---

print("🔍 Lexical Diversity:")
print(f"Avatar Speeches: {lexical_diversity(avatar_words):.3f}")
print(f"Shakespeare Sonnets: {lexical_diversity(sonnets_words):.3f}\n")

print("📝 Most Common Words in Avatar Speeches:")
print(get_most_common(avatar_words))
print("\n📝 Most Common Words in Shakespeare Sonnets:")
print(get_most_common(sonnets_words))

print("\n🤖 Similar Words to 'life' in Avatar Speeches:")
most_similar_word('life', avatar_words)
print("\n🎭 Similar Words to 'life' in Shakespeare Sonnets:")
most_similar_word('life', sonnets_words)

fdist_avatar = FreqDist(avatar_words)
fdist_sonnets = FreqDist(sonnets_words)

print("\n❤️ Frequency of 'love' in Avatar Speeches:", fdist_avatar['love'])
print("❤️ Frequency of 'love' in Shakespeare Sonnets:", fdist_sonnets['love'])

