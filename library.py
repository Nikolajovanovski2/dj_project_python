import nltk

raw = open('example.txt').read()
type(raw)
tokens = nltk.word_tokenize(raw)
type(tokens)
words = [w.lower() for w in tokens]
type(words)
vocab = sorted(set(words))
type(vocab)
type(tokens)
len(tokens)
var = tokens[:5]
print(f"All words with lower cases {words[:5]}")
words = [W.upper() for W in tokens]
type(words)
vocab = sorted(set(words))
type(vocab)
type(tokens)
len(tokens)
var = tokens[:5]
print(f"All words with upper cases {words[:5]}")
text=nltk.Text(tokens)
type(text)
text[100:180]
print(f"The specified range of tokens are {text[100:180]}")

File = open ('example.txt')
lines = File.read()
sentences = nltk.sent_tokenize(lines)
nouns = []
adjective = []
adverb = []
verb = []
len(tokens)
var = tokens[:10]
for sentence in sentences:
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if pos == 'NN'  or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS':
            nouns.append(word)
print(f"The nouns in example are{nouns[:10]}")
for sentence in sentences:
    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if pos == 'JJ' or pos == 'JJR' or pos == 'JJS':
            adjective.append(word)
print(f"The adjectives in example are{adjective[:10]}")
for sentence in sentences:
    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if pos == 'RB'or pos == 'RBR' or pos == 'RBS':
            adverb.append(word)
print(f"The adverbs in example are {adverb[:10]}")
for sentence in sentences:
    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if pos == 'VB' or pos == 'VBG' or pos == 'VBD' or pos == 'VBN'or pos == 'VBP' or pos == 'VBZ':
            verb.append(word)
print(f"The verbs in example are{verb[:10]}")





