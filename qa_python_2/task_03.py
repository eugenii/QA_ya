# Задание 3. Классы для спортивных состязаний.
points = 0


class PointsForPlace:
    """Points for place."""

    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        if place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        return 101 - place


class PointsForMeters:
    """Points for meters of throwing."""

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        return meters * 0.5


class TotalPoints(PointsForMeters, PointsForPlace):
    """Work with distance and place."""

    def __init__(self):
        self.points = points

    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(105))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
