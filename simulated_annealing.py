import random
from copy import deepcopy
from dataclasses import dataclass
from typing import override


@dataclass
class Position:
    x: int
    y: int

    def distance_to(self, other: "Position") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self) -> str:
        return f"Position(x={self.x}, y={self.y})"


class City:
    def __init__(self, name: str, pos: Position):
        self.name = name
        self.pos = pos

    def distance_from(self, other: "City") -> float:
        return self.pos.distance_to(other.pos)

    @override
    def __str__(self) -> str:
        return f"City(name={self.name})"


class Route:
    def __init__(self):
        self._cities: list[City] = []

    def add_city(self, city: City):
        self._cities.append(city)

    def swap_neighbours(self) -> "Route":
        ALLOWED_INDEXES = [n for n in range(0, len(self._cities))]
        START = random.randint(0, len(ALLOWED_INDEXES) - 1)
        _ = ALLOWED_INDEXES.pop(START)
        END = ALLOWED_INDEXES[random.randint(0, len(ALLOWED_INDEXES) - 1)]
        new_route = Route()
        new_route._cities = deepcopy(self._cities)
        new_route._cities[START], new_route._cities[END] = (
            new_route._cities[END],
            new_route._cities[START],
        )
        return new_route

    @property
    def total_distance(self) -> int | float:
        total = 0
        cities_max_index = len(self._cities) - 1
        for index, city in enumerate(self._cities):
            if index >= cities_max_index:
                break
            next_city = self._cities[index + 1]
            total += city.distance_from(next_city)
        total += self._cities[-1].distance_from(self._cities[0])
        return total

    def __sub__(self, other: "Route") -> float:
        if not isinstance(other, Route):
            raise TypeError("can only subtract Route objects")
        return self.total_distance - other.total_distance

    def __str__(self) -> str:
        return f"Route(total_distance={self.total_distance})"


def simulated_annealing(
    route: "Route",
    temp: float = 1000,
    min_temp: float = 0.001,
    alpha: float = 0.995,
    max_iter: int = 10000,
) -> "Route":
    current = deepcopy(route)
    best = deepcopy(route)
    for _ in range(max_iter):
        if temp < min_temp:
            break
        candidate = current.swap_neighbours()
        DELTA = candidate - current
        if DELTA < 0 or random.random() < pow(2.71828, -DELTA / temp):
            current = candidate
            if candidate.total_distance < best.total_distance:
                best = deepcopy(candidate)
        temp *= alpha
    return best


route = Route()
route.add_city(City("A", Position(0, 0)))
route.add_city(City("B", Position(3, 10)))
route.add_city(City("C", Position(-3, 10)))
route.add_city(City("D", Position(-1, -10)))
route.add_city(City("E", Position(-2, -11)))
route.add_city(City("F", Position(-7, 90)))
route.add_city(City("G", Position(12, -5)))
route.add_city(City("H", Position(0, 0)))
route.add_city(City("I", Position(3, 11)))
route.add_city(City("J", Position(-3, 8)))
route.add_city(City("K", Position(-1, -3)))
route.add_city(City("L", Position(-2, -4)))
route.add_city(City("M", Position(-7, 6)))
route.add_city(City("N", Position(17, -8)))
route.add_city(City("N", Position(15, 11)))
route.add_city(City("N", Position(99, 13)))
route.add_city(City("N", Position(25, 14)))
route.add_city(City("N", Position(22, 2)))
route.add_city(City("N", Position(21, 1)))
route.add_city(City("N", Position(7, -1)))
route.add_city(City("N", Position(11, -0)))
route.add_city(City("N", Position(1, -2)))


best_route = simulated_annealing(route, alpha=0.95, min_temp=0.01, max_iter=50000)
print("initial route", route)
print("best route", best_route)
