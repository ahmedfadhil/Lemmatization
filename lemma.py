from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("Dog"))
print(lemmatizer.lemmatize("better", pos='a'))
print(lemmatizer.lemmatize("best", pos='a'))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run", 'v'))

sample = gutenberg.raw('bible-kjv.txt')
tok = sent_tokenize(sample)

print(tok[4:10])
