# calculates avg sentiment polarity across company's tweets
import nltk, textblob

def pol (handle, data):

    # polarity list
    pol_list = []

    for line in data:
        if line["Company"].lower() == handle:
            pol_value = textblob.TextBlob(line["Text"]).polarity
            pol_list.append(pol_value)

    average = sum(pol_list)/len(pol_list)
    
    print(handle + ": " + str(average))
