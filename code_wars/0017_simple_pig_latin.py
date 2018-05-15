"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !


"""
from string import punctuation
class Solution():
    def pig_it(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word not in punctuation:
                word = list(word)
                word.append(word.pop(0))
                word = "".join(word)
                word += "ay"
                words[i] = word
        return " ".join(words)


def main():
    print(Solution().pig_it("Pig latin is cool"))   # # igPay atinlay siay oolcay
    print(Solution().pig_it("Hello world !"))       # igPay atinlay siay oolcay





if __name__ == '__main__':
    main()