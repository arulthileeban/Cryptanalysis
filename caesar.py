import re
from math import log10
from pycipher import Caesar

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        self.ngrams = {}
        for line in file(ngramfile):
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.itervalues())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        #Computing score of a text
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in xrange(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score
       

fitness = ngram_score('quadgrams.txt')
      
def cryptanalysis(ctext):
    # Cleaned Text
    ctext = re.sub('[^A-Z]','',ctext.upper())
    scores = []
    for i in range(26):
        scores.append((fitness.score(Caesar(i).decipher(ctext)),i))
    return max(scores)

print "Enter text and key:"    
input_text = raw_input()
key_val = input()
ctext = Caesar(key=key_val).encipher(input_text)#'YMJHFJXFWHNUMJWNXTSJTKYMJJFWQNJXYPSTBSFSIXNRUQJXYHNUMJWX'
print "Ciphered Text:"+ctext
max_key = cryptanalysis(ctext)

print 'Solution: '+str(max_key[1])
print Caesar(max_key[1]).decipher(ctext)
