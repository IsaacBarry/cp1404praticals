"""
Hex Colours
"""

colours_1 = {"black": "#000000", "blue1": "#0000ff", "blueviolet": "#8a2be2", "brown": "#a52a2a", "coral": "#ff7f50"}
colours_2 = {"cyan1": "#00ffff", "darkgreen": "#006400", "darkorange": "#ff8c00", "darkorchid": "#9932cc"}

colour_name = input("Enter Colour Name: ").lower()

while colour_name != " ":
    if colour_name in colours_1:
        print(colour_name, " code is ", colours_1[colour_name])
    elif colour_name in colours_2:
        print(colour_name, " code is ", colours_2[colour_name])
    else:
        print("Enter Valid Name. ")
    colour_name = input("Enter Colour Name: ").lower()
