import numpy as np
import pandas as pd
import string
import nltk
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
# nltk.download('punkt') # one time execution
import re
from nltk.tokenize import sent_tokenize
import networkx as nx
import loadGlove


def tokenize_sentences(text):
    sentences = sent_tokenize(text)

    # Removing punctuation
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

    # Remove Emails
    # data = [re.sub('\S*@\S*\s?', '', sent) for sent in data]

    # make alphabets lowercase
    clean_sentences = [s.lower() for s in clean_sentences]

    clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

    dirty_Sentences = sentences;

    sentences = []

    # Removing citations
    for sentence in dirty_Sentences:

        sentences.append(re.sub(r'\[([a-z0-9])*\]', "", sentence).strip())
    # for i in range(len(sentences)):
    #     print("     Original: "+sentences[i])
    #     print("      Cleaned: "+clean_sentences[i])

    word_embeddings = load_glove()
    # loadGlove.gloveDict = word_embeddings

    sentence_vectors = []

    for i in clean_sentences:
        if len(i) != 0:
            v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()]) / (len(i.split()))
        else:
            v = np.zeros((100,))
        sentence_vectors.append(v)

    sim_mat = np.zeros([len(sentences), len(sentences)])

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1, 100), sentence_vectors[j].reshape(1, 100))[0, 0]



    nx_graph = nx.from_numpy_array(sim_mat)
    scores = nx.pagerank(nx_graph)

    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    ranked_raw_sentences = sorted(((scores[i], s) for i, s in enumerate(clean_sentences)), reverse=True)

    graded_sen=[]
    graded_raw_sen = []
    for i in range(len(ranked_sentences)):
        graded_sen.append(ranked_sentences[i][1])
        graded_raw_sen.append(ranked_raw_sentences[i][1])

    return graded_sen,graded_raw_sen,word_embeddings

def remove_stopwords(sen):
    stop_words = stopwords.words('english')
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

def load_glove():
    f = open('glove.6B.100d.txt', encoding='utf-8')
    word_embeddings = {}

    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        word_embeddings[word] = coefs

    f.close()

    return word_embeddings