def get_user_input():
    name = input("Enter your username: ")
    length = float(input("Enter rectangle Length: "))
    width = float(input("Enter rectangle Width: "))
    return name, length, width

if __name__ == "__main__":
    user_name, user_length, user_width = get_user_input()
    print("Area of rectangle:", calculate_area(1, 3))