# coding = utf-8

wordstring = '''I never saw a Moor-I never saw the Sea.
                Yet know I how the Heather looks.
                And what a Billow be.
                I never spoke with God.
                Nor visited in Heaven.
                Yet certain am I of the spot.
                As if the Checks were given.'''

wordstring = wordstring.replace('.', '')
wordlist = wordstring.split()
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

d = dict(zip(wordlist,wordfreq))
print(d)
