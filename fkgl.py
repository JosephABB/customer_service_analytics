# function to perform Flesch-Kincaid Grade Level
import syllables, textblob, nltk

def fk (handle, data):

    # syllabus per tweet
    syl = 0

    # words per tweet
    words = 0

    #sentences per tweet 
    sent = 0

    # score per tweet
    fkgl_list = []

    for line in data:
        if line["Company"].lower() == handle:
            syl = syllables.estimate(line["Text"])
            blob = textblob.TextBlob(line["Text"])
            for word in blob.words:
                words += 1
            for sentence in blob.sentences:
                sent += 1

            fkgl_val = (0.39 * (words / sent)) + (11.8 * (syl / words)) - 15.59
            fkgl_list.append(fkgl_val)
        words = 0
        sent = 0

    avg = sum(fkgl_list)/len(fkgl_list)
    print(handle + ": " + str(avg))
            