from collections import deque

def water_jug(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()

    # Start with both jugs empty
    start = (0, 0)
    queue.append((start, [start]))

    while queue:
        current, path = queue.popleft()
        jug1 = current[0]
        jug2 = current[1]

        # Check if we reached the target
        if jug1 == target or jug2 == target:
            print("Solution Found:")
            for state in path:
                print("Jug1:", state[0], "Jug2:", state[1])
            return

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # All possible next moves
        next_states = []

        # Fill Jug1
        next_states.append((jug1_capacity, jug2))

        # Fill Jug2
        next_states.append((jug1, jug2_capacity))

        # Empty Jug1
        next_states.append((0, jug2))

        # Empty Jug2
        next_states.append((jug1, 0))

        # Pour Jug1 -> Jug2
        pour = min(jug1, jug2_capacity - jug2)
        next_states.append((jug1 - pour, jug2 + pour))

        # Pour Jug2 -> Jug1
        pour = min(jug2, jug1_capacity - jug1)
        next_states.append((jug1 + pour, jug2 - pour))

        # Add next states to the queue
        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))

    print("No solution possible.")

# Example usage
water_jug(5, 3, 0)
