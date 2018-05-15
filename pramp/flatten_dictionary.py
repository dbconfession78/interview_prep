"""
Flatten a Dictionary

A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).

Example:

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.

Constraints:

[time limit] 5000ms
[input] Dictionary dict
[output] Dictionary
"""
test_no = 1
# def flatten_dictionary_PRACTICE(dictionary):
def flatten_dictionary(dictionary):
    return {}

def flatten_dictionary_PASSED(dictionary):
# def flatten_dictionary(dictionary):
    def helper(dictionary, prev_key):
        retval = {}
        for k, v in dictionary.items():
            if type(v) is dict:
                retval.update(helper(v, prev_key+"."+k))
            else:
                ret = prev_key
                if ret.startswith("."):
                    ret = ret[1:]
                if k != "":
                    if ret != "":
                        ret += "."
                    ret += "{}".format(k)
                retval[ret] = v
        return retval

    retval = {}
    for k,v in dictionary.items():
        if type(v) is dict:
            retval.update(helper(v, k))
        else:
            retval[k] = v
    return retval

def test(sol, retval):
    global test_no
    print("{}. ".format(test_no), end="")
    test_no += 1
    if retval != sol:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print(" - sol: {},  ret: {}".format(sol, retval))


def main():
    ######### TESTS ############
    test({"Key1": "1", "Key2.a": "2", "Key2.b": "3", "Key2.c.d": "3", "Key2.c.e": "1"}, flatten_dictionary({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}}))
    test({"Key.a":"2","Key.b":"3"}, flatten_dictionary({"Key":{"a":"2","b":"3"}}))
    test({"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"}, flatten_dictionary({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}}))
    test({"a":"1","b":"3"}, flatten_dictionary({"":{"a":"1"},"b":"3"}))
    test({"a.b.c.d.e.f":"pramp"}, flatten_dictionary({"a":{"b":{"c":{"d":{"e":{"f":{"":"pramp"}}}}}}}))
    test({"a":"1"}, flatten_dictionary({"a":"1"}))

if __name__ == "__main__":
    main()

