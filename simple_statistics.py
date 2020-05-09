from nltk import FreqDist
from nltk.book import text3 as book_of_genesis

# frequency distribution
fdist = FreqDist(book_of_genesis)
print(fdist)
fdist.most_common(50)  # 50 most common tokens

# cumilative frequency plot
fdist.plot(50, cumulative=True)
