def find_visited_cups(start, end, n):
    visited_order = []  # Track cups in the order they were visited
    visited_set = set()  # Track cups that have been visited
    current_position = start  # Start at the defined starting cup

    # Loop until a cup is revisited (when it starts to repeat)
    while current_position not in visited_set:
        visited_order.append(current_position)  # Record the visit order
        visited_set.add(current_position)  # Mark the current cup as visited
        
        # Calculate the new position, wrapping around using modulo
        current_position = start + ((current_position - start + n) % total_cups)
    
    return visited_order


# Function to find cups that were not visited
def find_not_visited(visited_order, start, end):
    total_cups_list = list(range(start, total_cups))  # All cups from start to end
    not_visited = [cup for cup in total_cups_list if cup not in visited_order]  # Cups not visited
    return not_visited


# Function to find in which cup the G-th ball was placed
def find_gth_ball(visited_order, g, total_cups):
    g_position = (g - 1) % len(visited_order)  # The position of the G-th ball
    return visited_order[g_position]


# Example usage:
start = 1  # Define the starting cup (e.g., Cup 1)
end = 1    # Define the ending cup (e.g., Cup 9)
total_cups = 120
n = 5  # Step size: Place a ball in every 6th cup clockwise

# Find the order in which cups were visited
visit_order = find_visited_cups(start, end, n)
print(f"Visited order: {visit_order}")

# Find the cups that were not visited
not_visited = find_not_visited(visit_order, start, end)
print(f"Cups not visited: {not_visited}")

# Find in which cup the G-th ball was placed
g = 11  # Define the G-th ball number
gth_ball_position = find_gth_ball(visit_order, g, total_cups)
print(f"The {g}-th ball was placed in cup {gth_ball_position}")
