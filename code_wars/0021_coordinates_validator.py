"""
You need to create a function that will validate if given parameters are valid geographical coordinates.

Valid coordinates look like the following: "23.32353342, -32.543534534". The return value should be either true or false.

Latitude (which is first float) can be between 0 and 90, positive or negative. Longitude (which is second float) can be between 0 and 180, positive or negative.

Coordinates can only contain digits, or one of the following symbols (including space after comma) -, .

There should be no space between the minus "-" sign and the digit after it.

Here are some valid coordinates:

-23, 25
24.53525235, 23.45235
04, -23.234235
43.91343345, 143
4, -3
And some invalid ones:

23.234, - 23.4234
2342.43536, 34.324236
N23.43345, E32.6457
99.234, 12.324
6.325624, 43.34345.345
0, 1,2
0.342q0832, 1.2324
"""
class Solution():
    def is_valid_coordinates(self, coordinates):
        coords = coordinates.split(", ")

        x = coords[0].strip("-")
        x_split = x.split(".")
        if len(x_split) > 2 or any([not str.isnumeric() for str in x_split]):
            return False

        y = coords[1].strip("-")
        y_split = y.split(".")
        if len(y_split) > 2 or any([not str.isnumeric() for str in y_split]):
            return False

        x = float(x)
        y = float(y)
        return False if (x < 0 or x > 90) or (y < 0 or y > 180) else True


def main():
    valid_coordinates = [
        "-23, 25",
        "4, -3",
        "24.53525235, 23.45235",
        "04, -23.234235",
        "43.91343345, 143"
    ]

    invalid_coordinates = [
        "23.234, - 23.4234",
        "2342.43536, 34.324236",
        "N23.43345, E32.6457",
        "99.234, 12.324",
        "6.325624, 43.34345.345",
        "0, 1,2",
        "0.342q0832, 1.2324",
        "23.245, 1e1"
    ]

    for coord in valid_coordinates:
        print(Solution().is_valid_coordinates(coord))

    for coord in invalid_coordinates:
        print(Solution().is_valid_coordinates(coord))


if __name__ == '__main__':
    main()
