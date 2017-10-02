def loopMain():
    word = input('write your word')
    wordname = word.split()
    print(wordname)
    for x in wordname:
        print(x[0].upper())
loopMain()

