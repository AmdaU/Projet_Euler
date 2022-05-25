from num2words import num2words
from collections import Counter

sum([len(num2words(i).replace(" ","").replace("-","")) for i in range(1,1001)])
