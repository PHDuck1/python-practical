def filterBible(scripture, book, chapter):
    return [i for i in scripture if i.startswith(book+chapter)]