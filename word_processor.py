import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn

query = "The bruises along his rib cage and left arm, though, he did not"

def word_form_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def word_form_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def word_form_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def word_form_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def pen_to_wn(tag):
    if word_form_adjective(tag):
        return wn.ADJ
    elif word_form_noun(tag):
        return wn.NOUN
    elif word_form_adverb(tag):
        return wn.ADV
    elif word_form_verb(tag):
        return wn.VERB
    return wn.NOUN


tags = nltk.pos_tag(word_tokenize(query))
for tag in tags:
    wn_tag = pen_to_wn(tag[1])
    print(tag[0] + "---> " + WordNetLemmatizer().lemmatize(tag[0], wn_tag))
