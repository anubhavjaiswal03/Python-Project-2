from Media import Media


class Show(Media):

    def __init__(self, show_id, show_type, show_title, director, cast, average_rating, country_code, date_added,
                 release_year, media_rating, duration, genre, description):
        Media(show_id, show_title, average_rating)
        self.__show_type = show_type
        self.__show_director = director
        self.__show_cast = cast
        self.__show_country = country_code
        self.__show_date_added = date_added
        self.__show_release_year = release_year
        self.__show_media_rating = media_rating
        self.__show_duration = duration
        self.__show_genre = genre
        self.__show_description = description

    # Accessor/Mutators: