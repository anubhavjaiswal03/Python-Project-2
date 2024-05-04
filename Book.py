from Media import Media


class Book(Media):
    """
    Describes the Book class derived from the Media Class and it's data members and member functions.
    """

    def __init__(self, book_id, book_title, book_authors, book_average_rating, isbn_number, isbn13_number,
                 language_code, pages_count,
                 ratings_count, publication_date, publisher):
        super().__init__(media_id=book_id, media_title=book_title, media_average_rating=book_average_rating)
        self.__book_authors = book_authors
        self.__book_isbn_number = isbn_number
        self.__book_isbn13_number = isbn13_number
        self.__book_language_code = language_code
        self.__book_page_count = int(pages_count)
        self.__book_rating_count = int(ratings_count)
        self.__book_publication_date = publication_date
        self.__book_publisher = publisher

    def __str__(self):
        return (f"{self._media_id}, {self._media_title}, {self.__book_authors}, {self._media_average_rating},"
                f"{self.__book_isbn_number}, {self.__book_isbn13_number}, {self.__book_language_code}, "
                f"{self.__book_page_count},{self.__book_rating_count}, {self.__book_publication_date}, "
                f"{self.__book_publisher}")

    # Accessor/Mutators:
    def get_book_author(self):
        return self.__book_authors

    def get_book_isbn_number(self):
        return self.__book_isbn_number

    def get_book_isbn13_number(self):
        return self.__book_isbn13_number

    def get_book_language_code(self):
        return self.__book_language_code

    def get_book_page_count(self):
        return self.__book_page_count

    def get_book_rating_count(self):
        return self.__book_rating_count

    def get_book_publication_date(self):
        return self.__book_publication_date

    def get_book_publisher(self):
        return self.__book_publisher

    def get_details(self) -> str:
        """
        Helper function that returns a nice block of string that could be used in Recommendations Tab.
        """
        return (f"Title: {self.get_title()}\nAuthor: {self.__book_authors}\nAverage Rating: {self.get_rating()}"
                f"\nISBN: {self.__book_isbn_number}\nISBN13: {self.__book_isbn13_number}"
                f"\nLanguage Code:{self.__book_language_code}"
                f"\nPages: {self.__book_page_count}"
                f"\nRating Count: {self.__book_rating_count}"
                f"\nPublication Date: {self.__book_publication_date}"
                f"\nPublisher: {self.__book_publisher}")


if __name__ == '__main__':
    test_file = "Input Files/books1000.csv"
    books_data = []
    with open(test_file) as book_file:
        line = book_file.readline()
        while line:
            temp = Book(*line.strip().split(','))
            books_data.append(temp)
            line = book_file.readline()

    for book in books_data:
        print(book, flush=True)
