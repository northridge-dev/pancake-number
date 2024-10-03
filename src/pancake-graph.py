from itertools import permutations

def flip(pancakes, flip_point):
    return pancakes[:flip_point][::-1] + pancakes[flip_point:]

def get_next_state(pancakes):
    for flip_point in range(2, len(pancakes) + 1):
        yield flip(pancakes, flip_point)

def find_min_flips(stack_size):
    stack = goal = tuple(range(1, stack_size + 1))
    mins = []
    cache_hit = 0
    cache_miss = 0
    visited = set()
    queue = [(pancakes, 0)]

    while queue:
        current_stack, flips = queue.pop(0)

        for next_state in get_next_state(current_stack):
            if next_state not in visited:
                cache_miss += 1
                visited.add(next_state)
                mins.append(flips + 1)
                queue.append((next_state, flips + 1))
            cache_hit += 1



n = int(input('Stack size? '))
find_min_flips(stack)

print(f"pancake number: {max(mins)}")
print(f"cache hits: {cache_hit}")
print(f"cache miss: {cache_miss}")
