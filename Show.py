# Authors: Anubhav Jaiswal, Prayash Das
# Description: This program inherits from the Media class, containing member variables to store the show type, directors
# , actors, country code, date the show was added, the year it was released, the rating, the duration, genres, and a
# description. It also has appropriate constructor taking in an ID, a title, average rating, show type, directors,
# actors, country code, date show was added, year the show was released , rating, duration, genres, and a description as
# parameters and assigns those values to appropriate member variables and has appropriate accessor/mutator functions.

from Media import Media


class Show(Media):
    """
    Describes the Show class derived from the Media Class and it's data members and member functions.
    """

    def __init__(self, show_id, show_type, show_title, show_director, cast, average_rating, country_code, date_added,
                 release_year, media_rating, duration, genre, description):
        '''
        Constructor Function taking the required parameters
        '''
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
        '''
        str function for formatting the output of the class as required
        '''
        return (f"{self._media_id}, {self.__show_type}, {self._media_title}, {self.__show_director}, "
                f"{self.__show_cast}, {self.get_rating()}, {self.__show_country_code}, "
                f"{self.__show_date_added}, {self.__show_release_year}, {self.__show_content_rating}, "
                f"{self.get_show_duration_str()}, {self.__show_genre}, {self.__show_description}")

    # Accessor/Mutators:
    def get_show_type(self):
        '''
        Getter/Accessor for Show Type
        :return: Show Type
        '''
        return self.__show_type

    def get_show_director(self):
        '''
        Getter/Accessor for Show Director
        :return: Show Director
        '''
        return self.__show_director

    def get_show_cast(self):
        '''
        Getter/Accessor for the Show Cast
        :return: Show Cast
        '''
        return self.__show_cast

    def get_show_country_code(self):
        '''
        Getter/Accessor for country code of the show
        :return: Country Code
        '''
        return self.__show_country_code

    def get_show_date_added(self):
        '''
        Getter/Accessor for the date of the show added
        :return: Date of the show added
        '''
        return self.__show_date_added

    def get_show_release_year(self):
        '''
        Getter/Accessor for the release year of the show
        :return: Year the show was released
        '''
        return self.__show_release_year

    def get_show_content_rating(self):
        '''
        Getter/Accessor for the content rating of the show
        :return: Content Rating
        '''
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
        '''
        Getter/Accessor for the Show genre
        :return: Show genre
        '''
        return self.__show_genre

    def get_show_description(self):
        '''
        Getter/Accessor for the Show Description
        :return: Description of the show
        '''
        return self.__show_description

    def get_details(self):
        """
        Helper function that returns a nice block of string that could be used in Recommendations Tab.
        """
        return (f"Title: {self.get_title()}Type: {self.__show_type}\nDirector: {self.__show_director}"
                f"\nCsst: {self.get_rating()}"
                f"\nAverage Rating: {self.get_rating()}\nCountry Code: {self.__show_country_code}"
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
