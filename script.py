def get_user_input():
    name = input("Enter your user_Name: ")
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    return name, length, width

def calculate_area(length, width):
    return length * width

if __name__ == "__main__":
    print("2")
    user_name, user_length, user_width = get_user_input()
    print("Area of rectangle:", calculate_area(user_length, user_width))