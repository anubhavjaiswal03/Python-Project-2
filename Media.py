class Media:
    """
    Base Class for the classes: Show and Book, defining id, title and average_rating Data Members along with their
    respective accessors and mutators
    """
    def __init__(self, media_id, media_title, media_average_rating):
        self._media_id = media_id
        self._media_title = media_title
        self._media_average_rating = media_average_rating

    def get_id(self):
        """

        :return:
        """
        return self._media_id

    def get_title(self):
        """

        :return:
        """
        return self._media_title

    def get_rating(self):
        """

        :return:
        """
        return self._media_average_rating

    def set_id(self, new_id) -> None:
        """

        :param new_id:
        """
        self._media_id = new_id

    def set_title(self, new_title) -> None:
        """

        :param new_title:
        """
        self._media_title = new_title

    def set_rating(self, new_rating) -> None:
        """

        :param new_rating:
        :return:
        """
        self._media_average_rating = new_rating
