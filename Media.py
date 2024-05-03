# Description: This file contains the Media class, containing member variables to store ID, title, and an average rating
# This file also contains constructor function taking in an ID, a title, and an average rating as parameters and assigns
# those values to the appropriate member variables and appropriate accessor/mutator functions.
class Media:
    """
    Base Class for the classes: Show and Book, defining id, title and average_rating Data Members along with their
    respective accessors and mutators.
    """

    def __init__(self, media_id, media_title, media_average_rating):
        '''
        Constructor Function taking ID,title and average rating as parameters and assigning those values to the
        appropriate member variables.
        '''
        self._media_id = media_id
        self._media_title = media_title
        self._media_average_rating = float(media_average_rating)

    def get_id(self) -> str:
        """
        Getter/Accessor for the Media id, Eg, book if, TV Show Id, or even film id.
        :return: Media ID
        """
        return self._media_id

    def get_title(self) -> str:
        """
        Getter/Accessor for the Media title, e.g. the title of a Book or Show or Film.
        :return: Media Title.
        """
        return self._media_title

    def get_rating(self) -> float:
        """
        Getter/Accessor for the Average Media Rating, like the Average rating of a book, show or film.
        :return:
        """
        return self._media_average_rating

    def set_id(self, new_id) -> None:
        """
        Setter/Mutator for the Media ID, e.g. changing the book ID, Show ID or Film ID.
        :param new_id: The new media ID to replace to older one.
        """
        self._media_id = new_id

    def set_title(self, new_title) -> None:
        """
        Setter/Mutator for the Media Title, e.g. changing the title of a book, title of a Show or Film.
        :param new_title: The new title to replace to older one.
        """
        self._media_title = new_title

    def set_rating(self, new_rating) -> None:
        """
        Setter/Mutator for the Media Average Rating, e.g. changing the Average rating of a book, or a Show or a Film.
        :param new_rating: The new Media Average Rating.
        """
        self._media_average_rating = new_rating
