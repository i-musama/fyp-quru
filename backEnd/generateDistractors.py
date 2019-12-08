# generateDistractors.py                                            #
# QURU ~ Final Year Project 2019                                    #
# Sukkur IBA University                                             #
# Developer: Mohammad Usama                                         #
# Version: Final Script                                             #
#####################################################################

import random

import nltk
# nltk.download('wordnet')
from sklearn.metrics.pairwise import cosine_similarity
import threading
import numpy as np
from scipy.spatial import distance
import timeit
from nltk.stem import PorterStemmer

from nltk.corpus import wordnet   #Import wordnet from the NLTK



def getDistractors_By_Glove(keywords,glove):
	start = timeit.default_timer()
	# word_embeddings = load_glove()
	word_embeddings = glove
	loading_time = timeit.default_timer() - start
	print("Glove Loading Time: {}".format(loading_time))
	stemmer = PorterStemmer()
	options = []
	for keyword in keywords:
		word = keyword[0].lower()
		word_vector = word_embeddings.get(word, np.zeros((100,)))
		print(word_vector)
		if 0 in word_vector:
			print("Vector not Found")
		distractors_dict = {}
		start = timeit.default_timer()
		i = 0
		for key in word_embeddings.keys():
                        # if key != word and stemmer.stem(word) != stemmer.stem(key):
			if key != word:
				distractors_dict[key] = distance.euclidean(word_vector.reshape(1, 100),word_embeddings.get(key).reshape(1, 100))
				# distractors_dict[key] = cosine_similarity(word_vector.reshape(1, 50), word_embeddings.get(key).reshape(1, 50))[0,0]
		comparison_time = timeit.default_timer() - start
		print("Comparison Time: {}".format(comparison_time))

		sorted_dict = sorted(distractors_dict.items(), key=lambda x: x[1])
		distractors = []

		for item in sorted_dict:
                        if len(distractors) ==3:
                                break
                        if stemmer.stem(word) != stemmer.stem(item[0]):
                                distractors.append(item[0])
              
		distractors.append(word)
		random.shuffle(distractors)
		print(distractors)
		options.append(distractors)
	return options


def ignoregetDistractors_By_Glove(keywords,glove):
	start = timeit.default_timer()
	# word_embeddings = load_glove()
	global word_embeddings
	word_embeddings = glove
	loading_time = timeit.default_timer() - start
	print("Glove Loading Time: {}".format(loading_time))

	Threads = []
	for keyword in keywords:
		thread = threading.Thread(target=calculateDistractor,args=(keyword,))
		Threads.append(thread)

	for thread in Threads:
		thread.start()

	for thread in Threads:
		thread.join()


def calculateDistractor(keyword):
	word = keyword[0].lower()
	word_vector = word_embeddings.get(word, np.zeros((100,)))
	print(word_vector)
	if 0 in word_vector:
		print("Vector not Found")
	distractors_dict = {}
	start = timeit.default_timer()
	i = 0
	for key in word_embeddings.keys():
		if key != word:
			distractors_dict[key] = distance.euclidean(word_vector.reshape(1, 100),
													   word_embeddings.get(key).reshape(1, 100))
	# distractors_dict[key] = cosine_similarity(word_vector.reshape(1, 50), word_embeddings.get(key).reshape(1, 50))[0,0]
	comparison_time = timeit.default_timer() - start
	print("Comparison Time: {}".format(comparison_time))

	sorted_dict = sorted(distractors_dict.items(), key=lambda x: x[1])

	for item in sorted_dict[:3]:
		print(item)

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

def getDistractors(word):
    syn = list()
    ant = list()

    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            syn.append(lemma.name())    #add the synonyms
            if lemma.antonyms():    #When antonyms are available, add them into the list
                ant.append(lemma.antonyms()[0].name())

    print('Synonyms: ' + str(syn))
    print('Antonyms: ' + str(ant))
