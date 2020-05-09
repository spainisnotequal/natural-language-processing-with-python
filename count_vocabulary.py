from nltk.book import text3 as book_of_genesis

number_of_tokens = len(book_of_genesis)
unique_tokens = set(book_of_genesis)
unique_tokens_sorted = sorted(unique_tokens)


def lexical_diversity(text):
    "A mesaure of the lexical diversity (or richness) of a text."
    return len(set(text)) / len(text)


print("lexical diversity:",
      round(lexical_diversity(book_of_genesis) * 100, 2), "%")
