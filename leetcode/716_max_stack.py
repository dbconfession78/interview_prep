"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""
from collections import defaultdict

class MaxStack(list):
    def push(self, x):
        if self:
            m = max(x, self[-1][1])
        else:
            m = x
        # m = max(x, self[-1][1] if self else None)
        self.append((x, m))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0]

    def peekMax(self):
        return self[-1][1]

    def popMax(self):
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        map(self.push, reversed(b))
        return m

    def run(self, actions, values, expected):
        dct1 = {"push": self.push}
        dct2 = {"pop": self.pop, "popMax": self.popMax, "peekMax": self.peekMax,
                "top": self.top}
        exp_idx = 0
        for i, act in enumerate(actions):
            if act != "MaxStack":
                val = values[i]
                if val:
                    val = val[0]
                    fn = dct1[act]
                    fn(val)
                    print("{}: {}{}".format(act, "\t\t", val))
                else:
                    fn = dct2[act]
                    ret = fn()
                    exp = expected[exp_idx]
                    if ret != exp:
                        # raise Exception(f"Fail:\n act: {act}\n val: {val if val else None} ")
                        pass
                    else:
                        tab_count = 1
                        if act != "peekMax" and act != "popMax":
                            tab_count += 1
                        # self.output_count += 1
                        print("{}: {}{} <<".format(act, "\t" * tab_count, ret))
                    exp_idx += 1

class MaxStack_(list):

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stk = []
    #     self.idx = -1
    #     self.idxs = []
    #     self.max_lst = []
    #     self.output_count = 0
    #     self.val_idxs = defaultdict(int)

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m = max(x, self[-1][1] if self else None)
        # if self.stk:
        #     m = max(x, self.stk[-1][1])
        # else:
        #     m = x
        self.append((x, m))
        # self.idx += 1
        # self.idxs.append(self.idx)
        # if self.max_lst == []:
        #     self.max_lst = [self.idx]
        # else:
        #     if x >= self.stk[self.max_lst[-1]]:
        #         self.max_lst.append(self.idx)

    def pop(self):
        """
        :rtype: int
        """
        return self.pop()[0]
        # if self.stk:
        #     if self.stk[-1] == self.stk[self.max_lst[-1]]:
        #         ret = self.popMax()
        #     else:
        #         ret = self.stk.pop()
        #         self.idxs.pop()
        #         self.idx -= 1
        #         if self.stk[-1] > self.stk[self.max_lst[-1]]:
        #             self.max_lst.append(self.idx)
        #     return ret


    def top(self):
        """
        :rtype: int
        """
        return self[-1][0]
        # return self.stk[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self[-1][1]
        # if self.max_lst:
        #     return self.stk[self.max_lst[-1]]

    def popMax(self):
        """
        :rtype: int
        """
        _max = self[-1][1]
        tmp = []
        while self[-1][0] != _max:
            tmp.insert(0, self.pop())

        ret = self.pop()[0]
        self += tmp
        return ret
        # if self.max_lst != []:
        #     max_idx = self.max_lst.pop()
        #     max_val = self.stk[max_idx]
        #     if self.max_lst and len(self.stk)-1 > max_idx and self.stk[max_idx+1] >= self.stk[self.max_lst[-1]]:
        #         self.max_lst.append(max_idx)
        #     ret = self.stk.pop(max_idx)
        #     if self.max_lst:
        #         if self.stk[self.max_lst[-1]] <= self.stk[-1]:
        #             if self.max_lst[-1] != self.stk.index(self.stk[-1]):
        #                 self.max_lst.append(len(self.stk)-1)
        #     self.idxs.pop()
        #     if not self.max_lst and self.stk:
        #         self.max_lst.append(0)
        #     self.idx -= 1
        #     return ret

    def run(self, actions, values, expected):
        dct1 = {"push": self.push}
        dct2 = {"pop": self.pop, "popMax": self.popMax, "peekMax": self.peekMax,
                "top": self.top}
        exp_idx = 0
        for i, act in enumerate(actions):
            if act != "MaxStack":
                val = values[i]
                if val:
                    val = val[0]
                    fn = dct1[act]
                    fn(val)
                    print("{}: {}{}".format(act, "\t\t", val))
                else:
                    fn = dct2[act]
                    ret = fn()
                    exp = expected[exp_idx]
                    if ret != exp:
                        raise Exception (f"Fail:\n act: {act}\n val: {val if val else None} ")
                    else:
                        tab_count = 1
                        if act != "peekMax" and act != "popMax":
                            tab_count += 1
                        self.output_count += 1
                        print("{}: {}{} <<".format(act, "\t" * tab_count, ret))
                    exp_idx += 1






def main():
    ms = MaxStack()
    acts = ["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]
    vals = [[],[5],[1],[5],[],[],[],[],[],[]]
    ms.run(acts, vals, [5, 5, 1, 5, 1, 5])
    print()
    #
    # ms = MaxStack()
    # acts = ["MaxStack","push","push","push","popMax","popMax","top"]
    # vals = [[],[5],[1],[-5],[],[],[]]
    # ms.run(acts, vals, [5, 1, -5])
    # print()
    #
    # ms = MaxStack()
    # acts = ["MaxStack","push","popMax","push","push","push","pop","peekMax","push","pop","pop","push","peekMax","peekMax","push","peekMax","push","peekMax"]
    # vals = [[],[-2],[],[-45],[-82],[29],[],[],[40],[],[],[66],[],[],[-61],[],[98],[]]
    # expected = [-2, 29, -45, 40, -82, 66, 66, 66, 98]
    # ms.run(acts, vals, expected)
    # print()
    #
    # ms = MaxStack()
    # acts = ["MaxStack","push","popMax","push","push","top","push","peekMax","popMax","popMax","top","push","push","push","peekMax","pop","pop","push","popMax","push","push"]
    # vals = [[],[-29],[],[-65],[70],[],[-72],[],[],[],[],[-18],[80],[73],[],[],[],[-86],[],[38],[10]]
    # expected = [-29, 70, 70, 70, -65, -72, 80, 73, 80, -18]
    # ms.run(acts, vals, expected)
    # print()
    #
    # ms = MaxStack()
    # acts = ["MaxStack","push","peekMax","push","popMax","push","push","push","top","push","peekMax","push","popMax","peekMax"]
    # vals = [[],[-23],[],[-74],[],[-4],[20],[68],[],[83],[],[73],[],[]]
    # expected = [-23,-23,68,83,83,73]
    # ms.run(acts, vals, expected)
    # print()
    #
    # ms = MaxStack()
    # acts = ["MaxStack","push","push","popMax","popMax"]
    # vals = [[],[5],[5],[],[]]
    # expected = [5, 5]
    # ms.run(acts, vals, expected)
    # print()

    actions = ["MaxStack","push","pop","push","popMax","push","popMax","push","pop","push","peekMax","push","popMax","top","push","peekMax","popMax","top","popMax","push","push","top","push","push","popMax","push","push","push","push","popMax","push","top","push","push","push","popMax","popMax","push","popMax","push","popMax","push","pop","top","push","push","push","pop","push","pop","peekMax","push","peekMax","popMax","top","pop","top","push","top","push","pop","push","top","popMax","peekMax","peekMax","push","push","popMax","push","push","push","push","push","peekMax","peekMax","push","push","peekMax","push","push","popMax","pop","top","pop","popMax","pop","peekMax","popMax","push","push","push","push","popMax","push","top","peekMax","popMax","pop","pop","pop","push","top","push","push","pop","push","peekMax","push","push","peekMax","push","push","popMax","top","push","push","top","pop","push","top","push","push","popMax","push","pop","push","pop","push","push","pop","pop","popMax","push","peekMax","top","push","top","push","top","top","popMax","top","push","pop","pop","top","push","push","push","popMax","push","push","push","popMax","push","push","push","push","push","top","pop","push","push","popMax","peekMax","popMax","push","peekMax","top","peekMax","push","top","peekMax","top","peekMax","push","push","push","popMax","push","top","top","popMax","push","pop","push","peekMax","push","pop","push","top","pop","push","popMax","push","push","push","top","push","peekMax","peekMax","push","popMax","peekMax","push","pop","pop","peekMax","popMax","popMax","popMax","top","push","peekMax","peekMax","popMax","push","push","push","push","push","popMax","peekMax","pop","pop","top","push","peekMax","peekMax","pop","push","peekMax","top","push","pop","pop","top","top","pop","popMax","push","top","popMax","popMax","peekMax","push","push","pop","pop","push","push","push","popMax","pop","push","top","popMax","popMax","popMax","push","pop","push","push","push","push","push","push","pop","push","pop","pop","top","push","push","top","popMax","push","pop","peekMax","popMax","top","push","top","push","popMax","peekMax","push","top","push","top","top","top","top","pop","push","push","top","pop","top","popMax","popMax","push","peekMax","push","top","pop","push","push","push","push","pop","popMax","top","peekMax","pop","top","push","pop","pop","pop","pop","popMax","peekMax","pop","push","push","top","push","peekMax","push","top","popMax","push","push","push","popMax","top","pop","pop","push","pop","push","top","pop","push","pop","push","push","push","top","peekMax","top","push","popMax","popMax","top","popMax","popMax","push","popMax","top","push","peekMax","push","popMax","push","top","top","pop","peekMax","top","popMax","push","push","push","peekMax","push","popMax","push","top","pop","peekMax","push","push","peekMax","popMax","push","push","push","pop","popMax","top","push","push","push","pop","push","peekMax","popMax","top","popMax","popMax","top","peekMax","peekMax","peekMax","top","push","popMax","top","top","top","top","push","pop","push","popMax","push","top","pop","peekMax","top","pop","push","popMax","peekMax","peekMax","push","popMax","push","push","push","peekMax","push","push","push","top","push","pop","push","popMax","top","pop","push","push","push","push","top","push","peekMax","popMax","push","top","popMax","push","pop","pop","peekMax","peekMax","peekMax","push","pop","peekMax","peekMax","popMax","pop","push","popMax","pop","push","top","pop","push","push","push","push","push","pop","top","popMax","push","top","push","pop","push","push","top","push","top","pop","push","push","popMax","pop","push","push","push","popMax","peekMax","push","top","popMax","popMax","push","push","top","pop","push","push","push","pop","popMax","pop","push","push","push","push","push","pop","push","popMax","push","push","top","pop","peekMax","push","popMax","push","push","push","pop","push","push","push","popMax","push","push","peekMax","push","top","pop","top","popMax","popMax","pop","pop","pop","push","push","push","push","push","push","push","push","push","top","popMax","push","popMax","top","push","top","popMax","pop","popMax","pop","popMax","push","pop","push","push","push","pop","pop","peekMax","push","top","push","peekMax","push","popMax","push"]
    values = [[],[70],[],[73],[],[76],[],[-13],[],[-7],[],[50],[],[],[89],[],[],[],[],[18],[12],[],[-64],[95],[],[-81],[64],[-39],[12],[],[-13],[],[-93],[54],[51],[],[],[31],[],[3],[],[72],[],[],[68],[-84],[39],[],[-25],[],[],[-89],[],[],[],[],[],[65],[],[15],[],[61],[],[],[],[],[54],[-43],[],[95],[-24],[-66],[36],[-40],[],[],[39],[-3],[],[28],[70],[],[],[],[],[],[],[],[],[-8],[-85],[60],[65],[],[100],[],[],[],[],[],[],[-69],[],[-37],[-23],[],[-100],[],[-94],[13],[],[88],[-77],[],[],[-67],[-23],[],[],[-100],[],[4],[25],[],[-4],[],[-38],[],[-42],[54],[],[],[],[-48],[],[],[-34],[],[-1],[],[],[],[],[32],[],[],[],[86],[-97],[94],[],[-27],[-52],[88],[],[54],[-49],[-24],[39],[-85],[],[],[-66],[-21],[],[],[],[-62],[],[],[],[30],[],[],[],[],[24],[99],[36],[],[63],[],[],[],[66],[],[-48],[],[7],[],[23],[],[],[72],[],[95],[46],[55],[],[98],[],[],[-63],[],[],[-10],[],[],[],[],[],[],[],[-2],[],[],[],[-45],[14],[-72],[1],[-78],[],[],[],[],[],[-35],[],[],[],[-26],[],[],[80],[],[],[],[],[],[],[-76],[],[],[],[],[15],[-3],[],[],[-97],[26],[74],[],[],[9],[],[],[],[],[-52],[],[98],[13],[-89],[-83],[31],[-90],[],[27],[],[],[],[-49],[-83],[],[],[77],[],[],[],[],[89],[],[-62],[],[],[19],[],[-79],[],[],[],[],[],[37],[37],[],[],[],[],[],[-66],[],[1],[],[],[-54],[-4],[66],[56],[],[],[],[],[],[],[30],[],[],[],[],[],[],[],[12],[-53],[],[57],[],[-41],[],[],[-58],[-56],[-59],[],[],[],[],[23],[],[87],[],[],[-58],[],[-25],[-100],[-89],[],[],[],[-78],[],[],[],[],[],[71],[],[],[-57],[],[27],[],[-34],[],[],[],[],[],[],[-93],[58],[50],[],[92],[],[84],[],[],[],[13],[18],[],[],[92],[66],[42],[],[],[],[-2],[50],[-65],[],[9],[],[],[],[],[],[],[],[],[],[],[53],[],[],[],[],[],[-78],[],[5],[],[-53],[],[],[],[],[],[9],[],[],[],[-23],[],[-24],[-97],[-92],[],[-16],[76],[81],[],[94],[],[41],[],[],[],[88],[89],[-73],[4],[],[-47],[],[],[-24],[],[],[-98],[],[],[],[],[],[2],[],[],[],[],[],[-70],[],[],[-61],[],[],[83],[-77],[28],[62],[51],[],[],[],[-98],[],[40],[],[-54],[-84],[],[61],[],[],[56],[-3],[],[],[15],[53],[50],[],[],[99],[],[],[],[4],[-78],[],[],[-67],[-96],[63],[],[],[],[36],[83],[49],[9],[46],[],[71],[],[69],[36],[],[],[],[-46],[],[1],[24],[-35],[],[-1],[-83],[-42],[],[56],[-83],[],[-27],[],[],[],[],[],[],[],[],[-71],[32],[100],[33],[-91],[-50],[-15],[-98],[-74],[],[],[21],[],[],[48],[],[],[],[],[],[],[96],[],[23],[45],[38],[],[],[],[-100],[],[-34],[],[-68],[],[-46]]
    expected = [70,73,76,-13,-7,50,-7,89,89,-7,-7,12,95,64,-13,54,51,31,18,72,3,39,-25,68,68,68,-89,-89,-84,65,15,61,65,61,61,61,95,95,95,95,70,28,28,54,-3,39,39,65,100,100,100,60,-85,-8,-69,-23,36,36,88,-77,-23,-23,-100,36,-4,-38,54,-42,25,13,-48,-34,-1,-1,13,-1,32,-1,-34,94,88,-85,-85,86,54,54,39,-62,39,30,39,30,39,99,63,63,63,66,39,7,23,23,72,55,98,98,98,95,-10,-63,95,95,55,46,-48,39,39,39,36,30,-78,1,-72,30,30,-35,30,-26,80,-26,-72,-72,-72,30,-76,24,14,12,-3,15,74,26,9,12,12,9,-52,-90,27,31,-83,-83,98,77,13,13,-83,89,89,4,19,-79,-79,-79,-79,-79,37,37,37,37,19,4,1,1,56,66,-4,4,-4,-54,30,-54,-66,-62,4,3,-83,-53,57,-41,57,12,-59,-59,-56,23,87,87,-58,-89,3,-89,3,-2,-78,-13,-21,71,-78,-24,27,-34,-34,-34,-24,-57,-24,58,92,84,84,58,58,58,42,92,66,-65,66,66,9,50,50,9,18,18,18,9,53,9,9,9,9,-78,18,-53,-53,13,5,5,13,9,9,9,9,81,94,81,41,41,4,89,89,-24,88,-98,-24,76,76,76,2,76,76,76,-47,9,-70,-61,-61,51,62,83,-98,40,-84,61,61,62,-3,56,53,99,99,53,-78,-78,63,50,-96,46,83,36,36,71,71,-35,69,56,-27,-27,-83,56,49,-83,-42,-83,-74,100,36,21,48,48,21,33,-74,32,96,38,45,28,-100,28,28]
    ms = MaxStack()
    ms.run(actions, values, expected)
    print()


# LC input
# ["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]
# [[],[5],[1],[5],[],[],[],[],[],[]]
# ["MaxStack","push","push","push","popMax","popMax","top"]
# [[],[5],[1],[-5],[],[],[]]
# ["MaxStack","push","popMax","push","push","push","pop","peekMax","push","pop","pop","push","peekMax","peekMax","push","peekMax","push","peekMax"]
# [[],[-2],[],[-45],[-82],[29],[],[],[40],[],[],[66],[],[],[-61],[],[98],[]]
# ["MaxStack","push","popMax","push","push","top","push","peekMax","popMax","popMax","top","push","push","push","peekMax","pop","pop","push","popMax","push","push"]
# [[],[-29],[],[-65],[70],[],[-72],[],[],[],[],[-18],[80],[73],[],[],[],[-86],[],[38],[10]]
# ["MaxStack","push","peekMax","push","popMax","push","push","push","top","push","peekMax","push","popMax","peekMax"]
# [[],[-23],[],[-74],[],[-4],[20],[68],[],[83],[],[73],[],[]]
# ["MaxStack","push","push","popMax","popMax"]
# [[],[5],[5],[],[]]
# ["MaxStack","push","pop","push","popMax","push","popMax","push","pop","push","peekMax","push","popMax","top","push","peekMax","popMax","top","popMax","push","push","top","push","push","popMax","push","push","push","push","popMax","push","top","push","push","push","popMax","popMax","push","popMax","push","popMax","push","pop","top","push","push","push","pop","push","pop","peekMax","push","peekMax","popMax","top","pop","top","push","top","push","pop","push","top","popMax","peekMax","peekMax","push","push","popMax","push","push","push","push","push","peekMax","peekMax","push","push","peekMax","push","push","popMax","pop","top","pop","popMax","pop","peekMax","popMax","push","push","push","push","popMax","push","top","peekMax","popMax","pop","pop","pop","push","top","push","push","pop","push","peekMax","push","push","peekMax","push","push","popMax","top","push","push","top","pop","push","top","push","push","popMax","push","pop","push","pop","push","push","pop","pop","popMax","push","peekMax","top","push","top","push","top","top","popMax","top","push","pop","pop","top","push","push","push","popMax","push","push","push","popMax","push","push","push","push","push","top","pop","push","push","popMax","peekMax","popMax","push","peekMax","top","peekMax","push","top","peekMax","top","peekMax","push","push","push","popMax","push","top","top","popMax","push","pop","push","peekMax","push","pop","push","top","pop","push","popMax","push","push","push","top","push","peekMax","peekMax","push","popMax","peekMax","push","pop","pop","peekMax","popMax","popMax","popMax","top","push","peekMax","peekMax","popMax","push","push","push","push","push","popMax","peekMax","pop","pop","top","push","peekMax","peekMax","pop","push","peekMax","top","push","pop","pop","top","top","pop","popMax","push","top","popMax","popMax","peekMax","push","push","pop","pop","push","push","push","popMax","pop","push","top","popMax","popMax","popMax","push","pop","push","push","push","push","push","push","pop","push","pop","pop","top","push","push","top","popMax","push","pop","peekMax","popMax","top","push","top","push","popMax","peekMax","push","top","push","top","top","top","top","pop","push","push","top","pop","top","popMax","popMax","push","peekMax","push","top","pop","push","push","push","push","pop","popMax","top","peekMax","pop","top","push","pop","pop","pop","pop","popMax","peekMax","pop","push","push","top","push","peekMax","push","top","popMax","push","push","push","popMax","top","pop","pop","push","pop","push","top","pop","push","pop","push","push","push","top","peekMax","top","push","popMax","popMax","top","popMax","popMax","push","popMax","top","push","peekMax","push","popMax","push","top","top","pop","peekMax","top","popMax","push","push","push","peekMax","push","popMax","push","top","pop","peekMax","push","push","peekMax","popMax","push","push","push","pop","popMax","top","push","push","push","pop","push","peekMax","popMax","top","popMax","popMax","top","peekMax","peekMax","peekMax","top","push","popMax","top","top","top","top","push","pop","push","popMax","push","top","pop","peekMax","top","pop","push","popMax","peekMax","peekMax","push","popMax","push","push","push","peekMax","push","push","push","top","push","pop","push","popMax","top","pop","push","push","push","push","top","push","peekMax","popMax","push","top","popMax","push","pop","pop","peekMax","peekMax","peekMax","push","pop","peekMax","peekMax","popMax","pop","push","popMax","pop","push","top","pop","push","push","push","push","push","pop","top","popMax","push","top","push","pop","push","push","top","push","top","pop","push","push","popMax","pop","push","push","push","popMax","peekMax","push","top","popMax","popMax","push","push","top","pop","push","push","push","pop","popMax","pop","push","push","push","push","push","pop","push","popMax","push","push","top","pop","peekMax","push","popMax","push","push","push","pop","push","push","push","popMax","push","push","peekMax","push","top","pop","top","popMax","popMax","pop","pop","pop","push","push","push","push","push","push","push","push","push","top","popMax","push","popMax","top","push","top","popMax","pop","popMax","pop","popMax","push","pop","push","push","push","pop","pop","peekMax","push","top","push","peekMax","push","popMax","push"]
# [[],[70],[],[73],[],[76],[],[-13],[],[-7],[],[50],[],[],[89],[],[],[],[],[18],[12],[],[-64],[95],[],[-81],[64],[-39],[12],[],[-13],[],[-93],[54],[51],[],[],[31],[],[3],[],[72],[],[],[68],[-84],[39],[],[-25],[],[],[-89],[],[],[],[],[],[65],[],[15],[],[61],[],[],[],[],[54],[-43],[],[95],[-24],[-66],[36],[-40],[],[],[39],[-3],[],[28],[70],[],[],[],[],[],[],[],[],[-8],[-85],[60],[65],[],[100],[],[],[],[],[],[],[-69],[],[-37],[-23],[],[-100],[],[-94],[13],[],[88],[-77],[],[],[-67],[-23],[],[],[-100],[],[4],[25],[],[-4],[],[-38],[],[-42],[54],[],[],[],[-48],[],[],[-34],[],[-1],[],[],[],[],[32],[],[],[],[86],[-97],[94],[],[-27],[-52],[88],[],[54],[-49],[-24],[39],[-85],[],[],[-66],[-21],[],[],[],[-62],[],[],[],[30],[],[],[],[],[24],[99],[36],[],[63],[],[],[],[66],[],[-48],[],[7],[],[23],[],[],[72],[],[95],[46],[55],[],[98],[],[],[-63],[],[],[-10],[],[],[],[],[],[],[],[-2],[],[],[],[-45],[14],[-72],[1],[-78],[],[],[],[],[],[-35],[],[],[],[-26],[],[],[80],[],[],[],[],[],[],[-76],[],[],[],[],[15],[-3],[],[],[-97],[26],[74],[],[],[9],[],[],[],[],[-52],[],[98],[13],[-89],[-83],[31],[-90],[],[27],[],[],[],[-49],[-83],[],[],[77],[],[],[],[],[89],[],[-62],[],[],[19],[],[-79],[],[],[],[],[],[37],[37],[],[],[],[],[],[-66],[],[1],[],[],[-54],[-4],[66],[56],[],[],[],[],[],[],[30],[],[],[],[],[],[],[],[12],[-53],[],[57],[],[-41],[],[],[-58],[-56],[-59],[],[],[],[],[23],[],[87],[],[],[-58],[],[-25],[-100],[-89],[],[],[],[-78],[],[],[],[],[],[71],[],[],[-57],[],[27],[],[-34],[],[],[],[],[],[],[-93],[58],[50],[],[92],[],[84],[],[],[],[13],[18],[],[],[92],[66],[42],[],[],[],[-2],[50],[-65],[],[9],[],[],[],[],[],[],[],[],[],[],[53],[],[],[],[],[],[-78],[],[5],[],[-53],[],[],[],[],[],[9],[],[],[],[-23],[],[-24],[-97],[-92],[],[-16],[76],[81],[],[94],[],[41],[],[],[],[88],[89],[-73],[4],[],[-47],[],[],[-24],[],[],[-98],[],[],[],[],[],[2],[],[],[],[],[],[-70],[],[],[-61],[],[],[83],[-77],[28],[62],[51],[],[],[],[-98],[],[40],[],[-54],[-84],[],[61],[],[],[56],[-3],[],[],[15],[53],[50],[],[],[99],[],[],[],[4],[-78],[],[],[-67],[-96],[63],[],[],[],[36],[83],[49],[9],[46],[],[71],[],[69],[36],[],[],[],[-46],[],[1],[24],[-35],[],[-1],[-83],[-42],[],[56],[-83],[],[-27],[],[],[],[],[],[],[],[],[-71],[32],[100],[33],[-91],[-50],[-15],[-98],[-74],[],[],[21],[],[],[48],[],[],[],[],[],[],[96],[],[23],[45],[38],[],[],[],[-100],[],[-34],[],[-68],[],[-46]]



if __name__ == '__main__':
    main()# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()