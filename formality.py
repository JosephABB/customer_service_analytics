import textblob, nltk
#nltk.download("averaged_perceptron_tagger")

def forma (handle, data):
        
    # counter for nouns, adjectives, prepositions, determiners
    f = 0

    # counter for pronouns, verbs, adjectives, interjections
    c = 0

    for line in data:
        if line["Company"].lower() == handle:
            blob = textblob.TextBlob(line["Text"])
            for word, tag in blob.tags:
                if "NN" in tag or "JJ" in tag or "IN" in tag or "DT" in tag:
                    f += 1
                elif "PR" in tag or "VB" in tag or "RB" in tag or "UH" in tag:
                    c += 1
                
    
    forma_val = 50 * ((f-c) / (f+c) + 1)
    print(handle + ": " + str(forma_val))
   
                

