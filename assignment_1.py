
with open('twitter.txt') as f:                          //reading file
    x = f.read()
slurs = ['nake','fuck','sexy']                          //an array of some racial slurs
w=''
count=0     //number of slurs
word=0      //total number of word in a sentence
dop=0       //degree of profanity
for i in range(len(x)):
    if(x[i]!=" "):
        w=w+x[i] // w take each letter
        for j in range(len(slurs)):
            if(w==slurs[j]): //check word in a senetence as racial slurs
                w=''
                count=count+1
                word=word+1
                if(i==len(x)-1):
                    continue
    if(x[i]==" "):
        if(w!=''):
            word=word+1
        w=''   
dop = (count/word) // calculate degree of profanity
print(dop)          //display degree of profanity

