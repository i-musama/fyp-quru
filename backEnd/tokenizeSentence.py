
from nltk import tokenize

def getSentencec():
    file = open("input.txt",'r')
    print("Generating Sentences")
    fileText = file.read()
    # print(fileText)
    questions = tokenize.sent_tokenize(fileText)

    return questions