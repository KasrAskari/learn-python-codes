

car_colors = {1: 'blue', 2: "red", 3: "green", 4: "white", 5: "black"}

def car_color_print():
    message = "car color"
    return message


def car_color_print(num):
    car_color = car_colors[num]
    #message = f"car color: {car_color}"
    #return message
    return f"car color: {car_color}"


def car_color_print(num, intro_txt="Hey You"):
    car_color = car_colors[num]
    return f"{intro_txt}, car color: {car_color}"

print(car_color_print(2))