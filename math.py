def find_visited_cups(start, end, n):
    visited_order = []  # Track cups in the order they were visited
    visited_set = set()  # Track cups that have been visited
    current_position = start  # Start at the defined starting cup

    while current_position not in visited_set:
        visited_order.append(current_position)  # Record the visit order
        visited_set.add(current_position)  # Mark the current cup as visited
        
        # Calculate the new position, wrapping around using modulo
        current_position = start + ((current_position - start + n) % total_cups)
    
    return visited_order

# Example usage:
start = 1  # Define the starting cup (e.g., Cup 3)
end = 1   # Define the ending cup (e.g., Cup 10)
total_cups = 9
n = 6      # Place a ball in every 3rd cup clockwise

visit_order = find_visited_cups(start, end, n)
print(visit_order)
