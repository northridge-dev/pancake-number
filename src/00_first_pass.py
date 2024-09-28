from itertools import permutations
n = int(input('Stack size? '))
stack = goal = tuple(range(1, n + 1))
pancake_num = 0

def is_sorted(pancakes, goal):
    return pancakes == goal

def flip(pancakes, flip_point):
    return pancakes[:flip_point][::-1] + pancakes[flip_point:]

def get_next_state(pancakes):
    for flip_point in range(2, len(pancakes) + 1):
        yield flip(pancakes, flip_point)

def find_min_flips(pancakes):
    queue = [(pancakes, 0)]

    while queue:
        current_stack, flips = queue.pop(0)

        if is_sorted(current_stack, goal):
            return flips

        for next_state in get_next_state(current_stack):
            queue.append((next_state, flips + 1))

    return None



for p in permutations(stack):
    pancake_num = max(pancake_num, find_min_flips(p))

print(f"pancake number: {pancake_num}")
