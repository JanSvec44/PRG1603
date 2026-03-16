import pytest

import circle_stats


@pytest.mark.parametrize(
    ("circle_1", "circle_2", "expected"),
    [
        ([0, 0, 2], [0, 3, 1], (True, 1)),
        ([0, 0, 2], [3, 0, 1], (True, 1)),
        ([0, 0, 2], [0, 3, 2], (True, 2)),
        ([0, 0, 2], [0, 4, 2], (True, 2)),
        ([2, -1, 1], [1.2, 5, 3], (False, 0)),
    ],
)
def test_has_intersection(circle_1, circle_2, expected):
    assert has_intersection(circle_1, circle_2) == expected

@pytest.mark.parametrize(
    ("r1", "r2", "expected"),
    [
        (2, 3, 5),
        (5, 4, 9),
        (3, 4, 7)
    ],
)
def test_radius_sum(r1, r2, expected):
    assert radius_sum(r1, r2) == expected