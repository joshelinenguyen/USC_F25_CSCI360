import numpy as np
import heapq

# Directions for moving in the grid (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Define terrain costs
TERRAIN_COSTS = {
    'R': (1, 2),  # (normal_battery_cost, low_battery_cost)
    'H': (3, 4),
    'C': (5, 10),
    'E': (2, 2),
    'S': (1, 2),
    'G': (1, 2)
}

# added in heuristic helper function
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, K=1):
    """
    Implement A* Search for the Autonomous Delivery Robot problem.

    Args:
        grid (List[List[str]]): 2D grid map containing:
            'S' - Start
            'G' - Goal
            'R' - Road
            'H' - Highway
            'C' - Construction Zone
            'E' - Charging Station
            'X' - Blocked / Impassable
        K (int): battery consumption per move

    Returns:
        path (List[Tuple[int, int]]): sequence of coordinates from S to G (inclusive)
        total_cost (float): total traversal cost of the found path
    """
    n = len(grid)

    # Locate Start (S) and Goal (G)
    sx, sy = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 'S'][0]
    gx, gy = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 'G'][0]

    # ----- WRITE YOUR CODE BELOW -----
    # create a priority queue with f = g + h, (x, y) coordinates, and then battery and path so far
    queue =[]
    
    # starting point
    heapq.heappush(queue, (0, 0, sx, sy, 100, [(sx, sy)]))
    
    # to keep track of costs
    cost = {(sx, sy, 100):0}

    while queue:
        # pop the first
        f, g, x, y, battery, path = heapq.heappop(queue)

        # check if the goal has been reached yet
        if (x, y) == (gx, gy):
            return path, g

        # checking neighboring spots
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            # check within bounds
            if not ( 0 <= nx < n and 0 <= ny < n):
                continue

            current = grid[nx][ny]

            # blocked
            if current == 'X':
                continue

            # decrease battery life with each move
            battery_life = battery - K

            # when battery is depleted
            if battery_life <= 0:
                continue

            # battery cost is normal when above 50
            normal_cost = battery >= 50
            terrain_cost = TERRAIN_COSTS.get(current, (float('inf'), float('inf')))
            if normal_cost == True:
                move_cost = terrain_cost[0]
            else:
                move_cost = terrain_cost[1]

            # Charging stations
            if current == 'E':
                move_cost += 2
                battery_life = 100

            # Update cost and state
            new_cost = g + move_cost
            state = (nx, ny, battery_life)

            # if this path is cheaper, add to the heap
            if state not in cost or new_cost < cost[state]:
                cost[state] = new_cost

                # compute heuristic function (gets the distance)
                h = heuristic((nx, ny), (gx, gy))
                f = new_cost + h

                heapq.pushheap(queue, (f, new_cost, nx, ny, battery_life, path + [(nx, ny)]))
                                        
    # ----- WRITE YOUR CODE ABOVE -----
    
    # If the open list becomes empty and the goal was not reached, no path exists.
    return [], float('inf')


if __name__ == "__main__":
    grid = [
        ['S','R','R','R','X','R'],
        ['C','X','E','R','C','R'],
        ['R','R','H','R','X','E'],
        ['X','C','R','H','R','R'],
        ['E','X','R','C','R','R'],
        ['R','R','R','X','H','G']
    ]

    path1, cost1 = a_star_search(grid, K=1)
    print("\nCase 1 (K=1):")
    if path1:
        print("  Optimal Path:", path1)
        print("  Minimum Cost:", cost1)
    else:
        print("  No path found.")

    path2, cost2 = a_star_search(grid, K=10)
    print("\nCase 2 (K=10):")
    if path2:
        print("  Optimal Path:", path2)
        print("  Minimum Cost:", cost2)
    else:
        print("  No path found.")

    path3, cost3 = a_star_search(grid, K=20)
    print("\nCase 3 (K=20):")
    if path3:
        print("  Optimal Path:", path3)
        print("  Minimum Cost:", cost3)
    else:
        print("  No path found.")
