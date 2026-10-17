words = ['words','are','beautiful','but','not','as','u']
for w in words[:]:
    if len(w) > 6:
        x = w
        words.insert(0,w)
        words.remove(w)
        print(words)
    else:
        words.insert(len(words)+1,w)
        words.remove(w)
        print(words)


    