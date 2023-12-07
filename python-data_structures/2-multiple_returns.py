def multiple_return(sentence):
    if not sentence:
       return 0, None
    else:
        return(len(sentence), sentence[0])