def lt_gt_eq (item1, item2):
    if type(item1) is not int or type(item2) is not int:
        raise TypeError("Arguments must be integers")

    if item1 < item2:
        return "Less Than"
    if item1 > item2:
        return "Greater Than"
    return "Equal"

from os.path import isfile, exists


def populate_directory(path, **kwargs):
    if type(path) is not str:
        raise TypeError("Path argument must be a string")
    if isfile(path):
        raise IOError("Path exists, but is not a directory")
    if not exists(path):
        raise IOError("Directory does not exist")

    for k, v in kwargs.items():
        with open(path+k, mode="w", encoding="utf8") as f:
            f.write(v)



def main():
    print(populate_directory("/etc", name="hello"))
    # print(lt_gt_eq("hi", 2))
    # print(Solution().func())


if __name__ == '__main__':
    main()
