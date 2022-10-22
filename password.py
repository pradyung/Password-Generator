def generatePassword(length = 10, caseSensitive = True, keywords = []):
    import random
    keywords = list(map(
        lambda x: x.replace(" ", ""),
        keywords
    ))

    keywordLens = map(
        lambda x: len(x),
        keywords
    )

    totalKeyLen = sum(keywordLens)
    if totalKeyLen > length:
        keywords = []
    else: 
        length -= totalKeyLen

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if caseSensitive:
        alpha += "abcdefghijklmnopqrstuvwxyz"
    else:
        keywords = list(map(
            lambda x: x.upper(),
            keywords
        ))
    alpha = list(alpha)
    numOfSymbols = len(alpha)

    fillIns = []

    for _ in range(length):
        fillIns.append(alpha[random.randint(0,numOfSymbols-1)])

    if len(keywords) == 0:
        return "".join(fillIns)
    
    password = keywords + fillIns
    random.shuffle(password)

    return "".join(password)

print(generatePassword(length=30, caseSensitive = False, keywords=["Pradyun h", "2708"]))