"""The common module contains common functions and classes used by the other modules.
"""

import numpy as np

def Create_25_Random_points():
    """ Returns a random 25 points between 1 and 31.

    Returns:
        list: 25 Random(Integer) points between 1 and 31.

    """

    # Each points are far from >3
    def is_far_enough(new_point, existing_points, min_distance=3):
        for point in existing_points:
            if np.sqrt((new_point[0] - point[0])**2 + (new_point[1] - point[1])**2) < min_distance:
                return False
        return True

    np.random.seed(0) 
    num_points = 25
    unique_points = set()

    while len(unique_points) < num_points:
        x = np.random.randint(1, 31)
        y = np.random.randint(1, 31)
        new_point = (x, y)

        if is_far_enough(new_point, unique_points):
            unique_points.add(new_point)
    # print
    points = unique_points_list
    print(points)
    return points

def hello_world():
    """Prints "Hello World!" to the console.
    """
    print("Hello World!")


def get_version():
    """Returns the version of the geowanhee package.

    Returns:
        str: The version of the geowanhee package.
    """
    return "0.0.1"

