# identifyTopic.py                                                  #
# QURU ~ Final Year Project 2019                                    #
# Sukkur IBA University                                             #
# Developer: Mohammad Usama                                         #
# Version: Final Script                                             #
#####################################################################

import gensim
from gensim import corpora, models


def get_lda_from_lists_of_words(lists_of_words, **kwargs):

    dictionary = corpora.Dictionary(lists_of_words)  # this dictionary maps terms to integers
    corpus = [dictionary.doc2bow(text) for text in lists_of_words]  # create a bag of words from each document
    # tfidf = models.TfidfModel(
    #     corpus)  # this models the significance of words using term frequency inverse document frequency
    # corpus_tfidf = tfidf[corpus]
    kwargs["id2word"] = dictionary  # set the dictionary
    return models.LdaModel(corpus, **kwargs)  # do the LDA topic modelling


def get_top_terms(lda, num_terms=10):
    txt = []
    num_terms = min([num_terms, lda.num_topics])
    # for i in range(0, num_terms):
    #     terms = [term for term, val in lda.show_topic(i, num_terms)]
    #     txt.append("\t - top {} terms for topic #{}: {}".format(num_terms, i, ' '.join(terms)))
    return lda.show_topic(0, num_terms)


from nltk.tokenize import word_tokenize


def getTopic(docs):
    docs = [word_tokenize(doc.lower()) for doc in docs]

    topicsLda = get_lda_from_lists_of_words([s for s in docs if isinstance(s,list)], num_topics=1, passes=20)
    return get_top_terms(topicsLda)[0][0]




# def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
#     """https://spacy.io/api/annotation"""
#     texts_out = []
#     for sent in texts:
#         doc = nlp(" ".join(sent))
#         texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
#     return texts_out