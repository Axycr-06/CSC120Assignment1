def vowelCheck(letter):
    if letter in "aeiouAEIOU":
        return True
    else:
        return False

def cv_match(sentence, pattern):
    sentenceList = str.split(sentence)
    returnList = []

    for word in sentenceList:
        patternCheck = ''
        for letter in word:
            if vowelCheck(letter):
                patternCheck += 'v'
            else:
                patternCheck += 'c'

        if patternCheck == pattern:
            returnList.append(word)

    return returnList