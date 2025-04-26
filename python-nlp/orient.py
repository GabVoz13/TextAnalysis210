
import nltk
import nltk.corpus

nltk.download('book')
# The next line lets us do GET requests from remote URLs on the web:
from urllib import request
# The following import lines are for plotting interactive visualizations in Python
import matplotlib
import matplotlib.pyplot as plt
for line in open("avatarSpeeches.txt"):
     for word in line.split():
         if word.endswith('ing'):
             print(word)

