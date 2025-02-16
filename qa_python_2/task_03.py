# Задание 3. Классы для спортивных состязаний.

class PointsForPlace:
    """Points for place."""

    def __init__(self):
        self.points = 0

    def get_points_for_place(self, place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return self.points
        if place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return self.points
        self.points = 101 - place
        return self.points


class PointsForMeters:
    """Points for meters of throwing."""

    def __init__(self):
        self.points = 0

    def get_points_for_meters(self, meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return self.points
        self.points *= 0.5
        return self.points


class TotalPoints(PointsForMeters, PointsForPlace):
    """Work with distance and place."""

    def get_total_points(self, meters, place):
        ...


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
