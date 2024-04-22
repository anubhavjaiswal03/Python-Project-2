class Media:

    def __init__(self, media_id, media_title, media_rating):
        self._id = media_id
        self._title = media_title
        self._average_rating = media_rating

    def get_id(self):
        """

        :return:
        """
        return self._id

    def get_title(self):
        """

        :return:
        """
        return self._title

    def get_rating(self):
        """

        :return:
        """
        return self._average_rating

    def set_id(self, new_id) -> None:
        """

        :param new_id:
        """
        self._id = new_id

    def set_title(self, new_title) -> None:
        """

        :param new_title:
        """
        self._title = new_title

    def set_rating(self, new_rating) -> None:
        """

        :param new_rating:
        :return:
        """
        self._average_rating = new_rating
