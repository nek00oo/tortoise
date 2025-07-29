def get_user_input():
    name = input("Enter username: ")
    length = float(input("Enter rectangle Length: "))
    width = float(input("Enter rectangle Width: "))
    return name, length, width

def calculate_area(length, width):
    return length * width

if __name__ == "__main__":
    user_name, user_length, user_width = get_user_input()
    print("Area of rectangle:", calculate_area(6, 3))
    print("Area of rectangle:", calculate_area(user_length, user_width))