from nltk import FreqDist
from nltk.book import text3 as book_of_genesis

# frequency distribution
fdist = FreqDist(book_of_genesis)
print(fdist)
fdist.most_common(50)  # 50 most common tokens

# cumilative frequency plot
fdist.plot(50, cumulative=True)

# get words longer than 10
minimum_characters = 10
words_set = set(book_of_genesis)  # not interested in duplicates
long_words = [word for word in words_set if len(word) > minimum_characters]
sorted(long_words)  # sorted alphabetically (capital letters first)

# get words longer than 7 that occur more than 7 times
minimum_characters = 7
minimum_frequency = 7
fdist = FreqDist(book_of_genesis)
frequent_long_words = [word for word in words_set
                       if len(word) > minimum_characters and fdist[word] > minimum_frequency]
sorted(frequent_long_words)  # sorted alphabetically (capital letters first)

# frequency of words based on their length
words_length = [len(word) for word in book_of_genesis]
fdist = FreqDist(words_length)
fdist.most_common()
fdist.max()  # most frequent word length
fdist.freq(3)  # frequency of words whose length is 3
