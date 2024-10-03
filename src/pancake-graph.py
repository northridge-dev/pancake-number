from itertools import permutations

def flip(pancakes, flip_point):
    return pancakes[:flip_point][::-1] + pancakes[flip_point:]

def get_next_state(pancakes):
    for flip_point in range(2, len(pancakes) + 1):
        yield flip(pancakes, flip_point)

def find_min_flips(stack_size):
    goal = tuple(range(1, stack_size + 1))
    pancake_num = 0
    cache_hit = 0
    cache_miss = 0
    visited = set()
    queue = [(goal, 0)]

    while queue:
        current_stack, flips = queue.pop(0)

        for next_state in get_next_state(current_stack):
            if next_state not in visited:
                cache_miss += 1
                visited.add(next_state)
                if pancake_num < flips + 1:
                    pancake_num = flips + 1
                queue.append((next_state, flips + 1))
            cache_hit += 1
    print(f"cache hits: {cache_hit}")
    print(f"cache miss: {cache_miss}")

    return pancake_num 


n = int(input('Stack size? '))

print(f"pancake number: {find_min_flips(n)}")
