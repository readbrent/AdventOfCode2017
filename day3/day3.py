import math

def get_smallest_odd_square_greater(target):
    current_square = 3
    while True:
        squared = current_square ** 2
        if squared > target:
            return squared
        current_square += 2

def get_manhattan_distance(target):
    if target == 1:
        return 0

    ring_corner = get_smallest_odd_square_greater(target)

    # Iterate counterclockwise until we hit the target
    ring_size = int(math.sqrt(ring_corner))
    x_dist = (ring_size - 1) / 2
    y_dist = (ring_size - 1) / 2

    # Walk left
    current_val = ring_corner

    if current_val == target:
        return abs(x_dist) + abs(y_dist)

    for _ in range(ring_size - 1):
        current_val -= 1
        x_dist -= 1

        if current_val == target:
            return abs(x_dist) + abs(y_dist)

    # Walk up
    for _ in range(ring_size - 1):
        current_val -= 1
        y_dist -= 1

        if current_val == target:
            return abs(x_dist) + abs(y_dist)

    # Walk right
    for _ in range(ring_size - 1):
        current_val -= 1
        x_dist += 1

        if current_val == target:
            return abs(x_dist) + abs(y_dist)

    # Walk down
    for _ in range(ring_size - 1):
        current_val -= 1
        y_dist += 1

        if current_val == target:
            return abs(x_dist) + abs(y_dist)

    # Error!
    return -1

def run_manhattan_distance_tests():
    assert get_manhattan_distance(1) == 0
    assert get_manhattan_distance(12) == 3
    assert get_manhattan_distance(1024) == 31

def run_tests():
    run_manhattan_distance_tests()

    print (get_manhattan_distance(361527))

def main():
    run_tests()

if __name__ == "__main__":
    main()
