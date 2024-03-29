class Movie:
    def __init__(self, title, rating):
        self.title = title
        # below is a non-public attribute
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if 1 <= new_rating <= 5:
            self._rating = new_rating
        else:
            print("Please enter a valid rating.")

# Testing instance
my_movie = Movie("Hello", 4.5)
my_movie.rating = 6
print(my_movie.rating)