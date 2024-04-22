from Media import Media


class Book(Media):

    # bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, publication_date, publisher
    def __init__(self, book_id, book_title, book_authors, book_average_rating, isbn_number, isbn13_number,
                 language_code, pages_count,
                 ratings_count, publication_date, publisher):
        super().__init__(book_id, book_title, book_average_rating)
        self.__book_authors = book_authors
        self.__book_isbn_number = isbn_number
        self.__book_isbn13_number = isbn13_number
        self.__book_language_code = language_code
        self.__book_page_count = pages_count
        self.__book_rating_count = ratings_count
        self.__book_publication_date = publication_date
        self.__book_publisher = publisher

    # Accessor/Mutators:
