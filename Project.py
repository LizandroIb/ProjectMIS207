max_capacity = 50
current_members = 0

print("Welcome to the theater!")

while current_members < max_capacity:
    # Calculate the available seats
    available_seats = max_capacity - current_members
    
    print(f"\nCurrent number of audience members: {current_members}")
    print(f"Available seats: {available_seats}")
    
    try:
        action = input("Enter 'enter' for a group entering or 'leave' for a group leaving (or 'quit' to exit): ").lower()

        if action == 'quit':
            break
        elif action == 'enter':
            group_size = int(input("Enter the size of the group entering: "))
            if group_size <= available_seats:
                current_members += group_size
            else:
                print(f"Sorry, there are only {available_seats} available seats. The group cannot enter.")
        elif action == 'leave':
            group_size = int(input("Enter the size of the group leaving: "))
            if group_size <= current_members:
                current_members -= group_size
            else:
                print(f"Invalid input. The group cannot leave more members than are currently inside.")
        else:
            print("Invalid input. Please enter 'enter', 'leave', or 'quit'.")
    except ValueError:
        print("Invalid input. Please enter a valid group size.")
    
if current_members == maximum_capacity:
     print("\nThe theater is now full!")
else:
    print("\nExiting the program.")