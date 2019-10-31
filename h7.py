## Name :
## People you worked with :

from bs4 import BeautifulSoup
import requests
import unittest


# Task 1: The function takes the BeautifulSoup object as input.
# It finds and returns a list with all the <tr> tags that contain movie information.
def getAllMovieRows(s):
    pass


# Task 2: The function takes as input the list returned by the previous function.
# It goes through the list, finds all the movie names, and returns a list of the top 250 movie names.
def getAllMovies(movie_rows):
    pass

# Task 3: The function takes as input the list return by by the getAllMovieRows() function.
# It goes through the list, and creates a dictionary where the keys are years and values are list of movies released in that year.
def getMovieByYears(movie_rows):
    pass

# Task 4: The function takes as input the list returned by the getAllMovieRows() function.
# It goes through the list, finds all the directors, and returns a list of director names.
# The list will not have any repeat names, all names are unique.
def getAllDirectors(movie_rows):
    pass


# Task 5: The IMDB Top 250 webpage displays a list of genres on the right (see instructions document for image).
# The function takes as input the BeautifulSoup object and returns a list of those genres.
def getAllGenres(s):
    pass


# Extra Credit: Writes the 250 movies to a file called ''movies.txt''.
# The movies are sorted alphabetically before they are written.
# Each movie is written on a separate line.
# Closes the file after writing the movies.
# The function doesn't return anything!
def saveMovieNames(movies,filename):
    pass

# ====================================== PLEASE DO NOT EDIT ANYTHING BELOW THIS LINE ================================== #
# ====================================== AGAIN, DO NOT EDIT ANYTHING BELOW THIS LINE! ================================== #

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://www.imdb.com/chart/top').text, 'html.parser')

    def test_len_movie_list(self):
        self.assertEqual(len(getAllMovieRows(self.soup)), 250)
        self.assertEqual(len(getAllMovies(getAllMovieRows(self.soup))), 250)

    def test_years_dictionary(self):
        dictionary_years = getMovieByYears(getAllMovieRows(self.soup))
        self.assertTrue('1994' in dictionary_years)
        allYearLists = [dictionary_years[i] for i in dictionary_years]
        allMovies = [movie for mList in allYearLists for movie in mList]
        self.assertEqual(len(allMovies),250)

    def test_director_list_is_unique(self):
        self.assertEqual(len(getAllDirectors(getAllMovieRows(self.soup))), len(set(getAllDirectors(getAllMovieRows(self.soup)))))

    def test_total_movie_genres(self):
        self.assertEqual(len(getAllGenres(self.soup)), 21)

    def test_file_has_250_movies(self):
        f = open('movies.txt')
        movie_list = [m.strip() for m in f.readlines()]
        f.close()
        self.assertEqual(len(movie_list),250)
        self.assertEqual(sorted(movie_list),movie_list)

def main():
    # Creating a Beautiful Soup Object
    url = 'https://www.imdb.com/chart/top'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    all_rows = getAllMovieRows(soup)

    all_movies = getAllMovies(all_rows)
    print("======================== IMDB Top 250 Movies ========================")
    print(all_movies)
    print("\n")

    years_and_movies = getMovieByYears(all_rows)
    print("======================== IMDB Top 250 Movies By Year ========================")
    if years_and_movies:
        for year in years_and_movies:
            print("{}: {}".format(year, str(years_and_movies[year])))
    print("\n")

    all_directors = getAllDirectors(all_rows)
    print("======================== IMDB Top Directors ========================")
    print(all_directors)
    print("\n")

    all_genres = getAllGenres(soup)
    print("======================== IMDB Movie Genres ========================")
    print(all_genres)
    print("\n")

    filename = "movies.txt"
    saveMovieNames(all_movies,filename)


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)
