import requests, json, nltk, textblob
import polarity, subjectivity, formality, cont_loop, fkgl

response = requests.get("https://dgoldberg.sdsu.edu/515/customer_service_tweets_full.json")

if response:
    print("Welcome to the customer service analyzer!")

    # initiates loop
    cont = True

    # load the data
    data = json.loads(response.text)

    while cont:

        # receive user input
        analysis = input("\nWhich analysis would you like to perform (polarity/subjectivity/formality/FKGL)? ")
        handle = input("\nWhich Twitter handle would you like to analyze? ")

        # converts user input to lowercase
        analysis = analysis.lower()
        handle = handle.lower()

        if analysis == "polarity":
            polarity.pol(handle, data)
            cont = cont_loop.con()
        elif analysis == "subjectivity":
            subjectivity.sub(handle, data)
            cont = cont_loop.con()
        elif analysis == "formality":
            formality.forma(handle, data)
            cont = cont_loop.con()
        elif analysis == "fkgl":
            fkgl.fk(handle, data)
            cont = cont_loop.con()
        else:
            print("unsupported mode")


else:
    print("connection error")