import pickle
import re
import time
import warnings
warnings.filterwarnings('ignore')

text = input("Enter your review: ")

start = time.perf_counter() 

loaded_model = pickle.load(open("model.sav", 'rb'))

def cleanText(raw_text, remove_stopwords=False, stemming=False, split_text=False):
    letters_only = re.sub("[^a-zA-Z]", " ", raw_text)  # remove non-character
    words = letters_only.lower().split() # convert to lower case 
    
    if remove_stopwords: # remove stopword
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
        
    if stemming==True: # stemming
        #stemmer = PorterStemmer()
        stemmer = SnowballStemmer('english') 
        words = [stemmer.stem(w) for w in words]
        
    if split_text==True:  # split text
        return (words)
    
    return( " ".join(words))

fin = cleanText(text)

result = loaded_model.predict([fin])

if result==1:
    prediction = "Positive"
else:
    prediction = "Negative"



end = time.perf_counter()  