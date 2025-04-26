import nltk
from nltk import FreqDist

nltk.download('punkt')

def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def save_output(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

avatar_text = load_text('../Webscrape/scraped_links.txt')

tokens = nltk.word_tokenize(avatar_text)

freq_dist = FreqDist(tokens)

most_common_words = freq_dist.most_common(30)

output = ""
for word, count in most_common_words:
    output += f"{word}: {count}\n"

save_output('common_words_output.txt', output)

print("Finished analyzing! Output saved.")
