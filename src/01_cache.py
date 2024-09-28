from itertools import permutations
use_cache_input = input('Use cache [Y/n]: ') 
use_cache = not use_cache_input or use_cache_input.lower() == 'y'
n = int(input('Stack size? '))
stack = goal = tuple(range(1, n + 1))
pancake_num = 0
total = hit = miss = 0

def is_sorted(pancakes, goal):
    return pancakes == goal

def flip(pancakes, flip_point):
    return pancakes[:flip_point][::-1] + pancakes[flip_point:]

def get_next_state(pancakes):
    for flip_point in range(2, len(pancakes) + 1):
        yield flip(pancakes, flip_point)

def find_min_flips(pancakes):
    global total 
    queue = [(pancakes, 0)]

    while queue:
        total += 1
        current_stack, flips = queue.pop(0)

        if is_sorted(current_stack, goal):
            return flips

        for next_state in get_next_state(current_stack):
            queue.append((next_state, flips + 1))

    return None

def find_min_flips_cache(pancakes):
    global total, hit, miss
    visited = set()
    queue = [(pancakes, 0)]

    while queue:
        total += 1
        current_stack, flips = queue.pop(0)

        if is_sorted(current_stack, goal):
            return flips

        for next_state in get_next_state(current_stack):
            if next_state not in visited:
                miss += 1
                visited.add(next_state)
                queue.append((next_state, flips + 1))
            hit += 1

    return None

# Choose cached or non-cached function based on user input
find_min_flips_fn = find_min_flips_cache if use_cache else find_min_flips

for p in permutations(stack):
    pancake_num = max(pancake_num, find_min_flips_fn(p))

print(f"pancake number: {pancake_num}")
print(f"Total states evaluated: {total}")
if use_cache:
    print(f"Repeated states not added to queue: {hit}")
    print(f"First-time states added to queue: {miss}")
