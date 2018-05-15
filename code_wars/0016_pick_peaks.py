"""
In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

Have fun!

"""

class Solution():
    def pick_peaks(self, arr):
        retdct = {}
        hi = 0
        hi_idx = None
        i = 0
        pos = []
        peaks = []
        plat = False
        peak_positions = set()

        while i < len(arr):
            if i > 0:
                if arr[i] > arr[i - 1]:
                    hi = arr[i]
                    hi_idx = i

                if arr[i] < arr[i - 1]:
                    if plat:
                        plat = False

                        if hi_idx and hi_idx not in peak_positions:
                            pos.append(hi_idx)
                            peaks.append(hi)
                            peak_positions.add(hi_idx)

                    elif (i - 1) == hi_idx:
                        if hi_idx and hi_idx not in peak_positions:
                            pos.append(hi_idx)
                            peaks.append(hi)
                            peak_positions.add(hi_idx)

                if arr[i] == arr[i-1]:
                    plat = True

            i += 1
        retdct["pos"] = pos
        retdct["peaks"] = peaks

        return retdct


def main():
    # {"pos":[3,7], "peaks":[6,3]}
    print(Solution().pick_peaks([1,2,3,6,4,1,2,3,2,1]))

    # {"pos":[3,7], "peaks":[6,3]}
    print(Solution().pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))

    # {"pos":[3,7,10], "peaks":[6,3,2]})
    print(Solution().pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))

    # {"pos":[2,4], "peaks":[3,2]}
    print(Solution().pick_peaks([2,1,3,1,2,2,2,2,1]))

    # {"pos":[7], "peaks":[4]}
    print(Solution().pick_peaks([1,2,3,3,3,3,3,4,3,3,3,3,3,3,2]))

    # {"pos":[], "peaks":[]}
    print(Solution().pick_peaks([19,3,3,-2,-1]))






if __name__ == '__main__':
    main()