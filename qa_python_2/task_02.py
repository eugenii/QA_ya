# Задание 2. Создание иерархии фильмов.

class Movies:
    """Родительский класс."""

    def __init__(self):
        self.movies = list()

    def add_movie(self, movie):
        self.movies.append(movie)


class Drama(Movies):
    """Дочерний класс для Movies - только драмы."""

    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Драмы: {self.movies}'


class Comedy(Movies):
    """Дочерний класс для Movies - только комедии."""

    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}'


comedy = Comedy()
print(comedy.add_movie('Большой куш'))
drama = Drama()
print(drama.add_movie('Оружейный барон'))
