# ExtractKeywords.py                                                #
# QURU ~ Final Year Project 2019                                    #
# Sukkur IBA University                                             #
# Developer: Mohammad Usama                                         #
# Version: Final Script                                             #
#####################################################################

# import rake
import random

from rake_nltk import Rake
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk



def getKeyWords(text_runs,raw_text):
    # rake = Rake(min_length=1, max_length=2)
    text = ""
    r_text = ""
    for i in range(len(text_runs)):
        text+=" "+text_runs[i]
        r_text+= " "+raw_text[i]


    # Get most frequent words and their count beside Stop Words to avoid those words as keywords for blanks such as topic of paragraph
    frequent_list = sortFreqDict(wordListToFreqDict(word_tokenize(r_text)))[:2]
    print(frequent_list)

    # Store Frequent words in frequent_words list
    frequent_words=[]
    for tupple in frequent_list:
        frequent_words.append(tupple[1])

    # Tokeninzing text to extratxt text as words
    tokenized_text = word_tokenize(r_text)

    # Part of speech Tagging to each extracted word
    tokens = nltk.pos_tag(tokenized_text)

    properNouns = {}
    numbers = {}
    adjectives = {}
    nouns = {}

    # Extracting ProperNouns Numbers Adjectives and nouns as dictionary for possible keywords
    for token  in tokens:
        if token[1] == "NNP" and token[0] not in properNouns.keys() and token[0].lower() not in frequent_words:
            properNouns[token[0]] = token[1]
        if token[1] == "CD"  and token[0] not in numbers.keys() and token[0].lower() not in frequent_words:
            numbers[token[0]] = token[1]
        if token[1] == "JJ"  and token[0] not in adjectives.keys() and token[0].lower() not in frequent_words:
            adjectives[token[0]] = token[1]
        if (token[1] == "NN" or token[1] == "NNS" ) and token[0] not in nouns.keys() and token[0].lower() not in frequent_words:
            nouns[token[0]] = token[1]

    # print(properNouns)
    # print(numbers)
    # print(adjectives)
    # print(nouns)

    # Extracting key_words from Keyword Dictionary against each sentence
    key_words = []
    priorityCandidate = numbers
    priorityCandidate.update(properNouns)
    priorityCandidate.update(adjectives)

    for text in text_runs:
        isFound = 1
        key_word = []

        text_tokens = word_tokenize(text)
        priorityKeys = list(priorityCandidate.keys())
        random.shuffle(priorityKeys)



        for candidate in priorityKeys:
            if candidate in text_tokens:
                key_word.append(candidate)
                key_word.append(priorityCandidate[candidate])
                # key_words[number] = numbers[number]
                isFound = 0
                break

        # for number in numbers.keys():
        #     if number in text_tokens:
        #         key_word.append(number)
        #         key_word.append(numbers[number])
        #         # key_words[number] = numbers[number]
        #         isFound = 0
        #         break
        # if isFound:
        #     for proper_noun in properNouns.keys():
        #         if proper_noun in text_tokens:
        #             key_word.append(proper_noun)
        #             key_word.append(properNouns[proper_noun])
        #             # key_words[proper_noun] = properNouns[proper_noun]
        #             isFound = 0
        #             break
        if isFound:
            for noun in nouns.keys():
                if noun in text_tokens:
                    key_word.append(noun)
                    key_word.append(nouns[noun])
                    # key_words[noun] = nouns[noun]
                    isFound = 0
                    break
        # if isFound:
        #     for adjective in adjectives.keys():
        #         if adjective in text_tokens:
        #             key_word.append(adjective)
        #             key_word.append(adjectives[adjective])
        #             # key_words[adjective] = adjectives[adjective]
        #             isFound = 0
        #             break
        if isFound:
            key_word.append("null")
            key_word.append("null")

        key_words.append(key_word)

    # print(key_words)
    return key_words


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

def getKeyWordss(text_runs):
    rake = Rake(min_length=1, max_length=2)

    print("Generating Key Words . . .")

    all_keywords=[]

    for line in text_runs:

        # myText = text_runs[0][0]
        rake.extract_keywords_from_text(line)
        if len(rake.get_ranked_phrases())>0:
            all_keywords.append(rake.get_ranked_phrases()[0])
        else:
            all_keywords.append("null")

    # using average perceptron Tagger pos
    print("Keywords Extracted")
    print(all_keywords)
    print("Cleaning Extracted Key Words . . .")

    print("Keyword Generated")
    return all_keywords


