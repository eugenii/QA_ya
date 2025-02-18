# Task 5. Competitions results.

class Results:
    """Calculate results."""

    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Footbal(Results):
    """Footbal results methods."""

    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return f'Футбольных побед: {self.victories}'

    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draws}'

    def number_of_losses(self):
        return f'Футбольных поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков: {3 * self.victories + self.draws}'


class Hockey(Results):
    """Hockey results methods."""

    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return f'Хокейных побед: {self.victories}'

    def number_of_draws(self):
        return f'Хокейных ничьих: {self.draws}'

    def number_of_losses(self):
        return f'Хокейных поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков: {2 * self.victories + self.draws}'


footbal_team = Footbal(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (footbal_team, hockey_team):
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())