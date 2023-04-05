# calculates company's avg subjectivity across tweets
import nltk, textblob

def sub (handle, data):

    # polarity list
    pol_list = []

    for line in data:
        if line["Company"].lower() == handle:
            pol_value = textblob.TextBlob(line["Text"]).subjectivity
            pol_list.append(pol_value)

    average = sum(pol_list)/len(pol_list)
    
    print(handle + ": " + str(average))