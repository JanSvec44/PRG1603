import math

def radius_sum(r1, r2):
    return r1 + r2

def euclid_distance(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))

def has_intersection(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    e_distance = euclid_distance(x1,y1,x2,y2)
    r_sum = radius_sum(r1,r2)

    result = {"is_intersection": False, "intersections_count": 0}

    if e_distance == r_sum:
        result["is_intersection"] = True
        result["intersections_count"] = 1
    elif e_distance < r_sum:
        result["is_intersection"] = True
        result["intersections_count"] = 2

    return result

