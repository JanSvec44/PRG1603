import pytest

import circle_stats as st


@pytest.mark.parametrize(
    ("circle_1", "circle_2", "expected"),
    [
        ([0, 0, 2], [0, 3, 1], ({"is_intersection": True, "intersections_count": 1})),
        ([0, 0, 2], [3, 0, 1], ({"is_intersection": True, "intersections_count": 1})),
        ([0, 0, 2], [0, 3, 2], ({"is_intersection": True, "intersections_count": 2})),
        ([0, 0, 2], [0, 4, 2], ({"is_intersection": True, "intersections_count": 1})),
        ([2, -1, 1], [1.2, 5, 3], ({"is_intersection": False, "intersections_count": 0})),
    ],
)
def test_has_intersection(circle_1, circle_2, expected):
    assert st.has_intersection(circle_1, circle_2) == expected

@pytest.mark.parametrize(
    ("r1", "r2", "expected"),
    [
        (2, 3, 5),
        (5, 4, 9),
        (3, 4, 7)
    ],
)
def test_radius_sum(r1, r2, expected):
    assert st.radius_sum(r1, r2) == expected