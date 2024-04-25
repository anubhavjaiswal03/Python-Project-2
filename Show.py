from Media import Media


class Show(Media):
    """
    Describes the Show class derived from the Media Class and it's data members and member functions.
    """

    def __init__(self, show_id, show_type, show_title, show_director, cast, average_rating, country_code, date_added,
                 release_year, media_rating, duration, genre, description):
        super().__init__(show_id, show_title, average_rating)
        self.__show_type = show_type
        self.__show_director = show_director
        self.__show_cast = cast
        self.__show_country_code = country_code
        self.__show_date_added = date_added
        self.__show_release_year = release_year
        self.__show_content_rating = media_rating
        self.__show_duration = duration
        self.__show_genre = genre
        self.__show_description = description

    def __str__(self):
        return (f"{self._media_id}, {self.__show_type}, {self._media_title}, {self.__show_director}, "
                f"{self.__show_cast}, {self._media_average_rating}, {self.__show_country_code}, "
                f"{self.__show_date_added}, {self.__show_release_year}, {self.__show_content_rating}, "
                f"{self.__show_duration}, {self.__show_genre}, {self.__show_description}")

    # Accessor/Mutators:
    def get_show_id(self):
        return self.get_id()

    def get_show_title(self):
        return self.get_title()

    def get_show_average_rating(self):
        return self._media_average_rating

    def get_show_type(self):
        return self.__show_type

    def get_show_director(self):
        return self.__show_director

    def get_show_cast(self):
        return self.__show_cast

    def get_show_country_code(self):
        return self.__show_country_code

    def get_show_date_added(self):
        return self.__show_date_added

    def get_show_release_year(self):
        return self.__show_release_year

    def get_show_content_rating(self):
        return self.__show_content_rating

    def get_show_duration(self):
        return self.__show_duration

    def get_show_genre(self):
        return self.__show_genre

    def get_show_description(self):
        return self.__show_description


if __name__ == '__main__':
    test_file = "Input Files/shows10.csv"
    shows_data = []
    with open(test_file) as show_file:
        line = show_file.readline()
        while line:
            temp = Show(*line.strip().split(','))
            shows_data.append(temp)
            line = show_file.readline()

    # shows_data.pop(0)

    for show in shows_data:
        print(show)
