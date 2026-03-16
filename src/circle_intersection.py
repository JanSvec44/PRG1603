from circle_stats import has_intersection
from circles_intersection_draw import draw_data

circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}

print(has_intersection(circle_1, circle_2))
draw_data(circle_1, circle_2)

