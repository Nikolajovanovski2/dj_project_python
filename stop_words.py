
from nltk.corpus import stopwords


stopList = stopwords.words('english')
additional_stopwords = """case juge judgment court"""

stopList += additional_stopwords.split()


fileF = open('example.txt')
text = fileF.read()
clean = {word for word in text.split() if word not in stopList}
print(clean)
