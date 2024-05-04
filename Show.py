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
        self.__show_duration = int(duration.split(" ")[0])
        self.__show_duration_unit = duration.split(" ")[1]
        self.__show_genre = genre
        self.__show_description = description

    def __str__(self):
        return (f"{self._media_id}, {self.__show_type}, {self._media_title}, {self.__show_director}, "
                f"{self.__show_cast}, {self.get_rating()}, {self.__show_country_code}, "
                f"{self.__show_date_added}, {self.__show_release_year}, {self.__show_content_rating}, "
                f"{self.get_show_duration_str()}, {self.__show_genre}, {self.__show_description}")

    # Accessor/Mutators:
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

    def get_show_duration_str(self):
        """Returns the durations as String constructing from the show duration and duration unit (min or Season)"""
        return f"{self.__show_duration} {self.__show_duration_unit}"

    def get_show_duration(self):
        """
        Returns the Number of minutes or seasons as int.
        """
        return self.__show_duration

    def get_show_genre(self):
        return self.__show_genre

    def get_show_description(self):
        return self.__show_description

    def get_show_details(self):
        """
        Helper function that returns a nice block of string that could be used in Recommendations Tab.
        """
        return (f"Title: {self.get_title()}Type: {self.__show_type}\nDirector: {self.__show_director}"
                f"\nCsst: {self.get_rating()}"
                f"\nAverage Rating: {self.a}\nCountry Code: {self.__show_country_code}"
                f"\nDate Added:{self.__show_date_added}"
                f"\nRelease Year: {self.__show_release_year}"
                f"\nMedia Rating: {self.__show_content_rating}"
                f"\nDuration: {self.get_show_duration_str()}"
                f"\nGenre: {self.__show_genre}"
                f"\nDescription: {self.__show_description}")


if __name__ == '__main__':
    test_file = "Input Files/shows100.csv"

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
