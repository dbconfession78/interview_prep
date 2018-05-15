class Solution:
    # this version uses stack
    def get_importance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        if employees == [] or employees is None:
            return 0
        emp_dict = {}
        stack = []
        retval = 0
        employees = build_tree(employees)
        for emp in employees:
            emp_dict[emp.id] = emp

        stack.append(emp_dict.get(id))
        while stack:
            top = stack.pop()
            if top is None:
                continue
            retval += top.importance
            for sub_id in top.subordinates:
                stack.append(emp_dict.get(sub_id))
        return retval

    # this version uses recursion
    def get_importance_2(self, employees, id):
        emp_dict = {}
        if employees == [] or employees is None:
            return 0
        employees = build_tree(employees)
        for emp in employees:
            emp_dict[emp.id] = emp

        return self.get_imp_helper(emp_dict, id, 0)

    def get_imp_helper(self, emp_dict, id, ret):
        emp = emp_dict.get(id)
        subs = [emp_dict.get(x) for x in emp.subordinates]
        ret += emp.importance
        for sub in subs:
            ret = self.get_imp_helper(emp_dict, sub.id, ret)
        return ret

def main():
    print(Solution().get_importance([[1, 2, [2]], [2, 3, []]], 2))
    print(Solution().get_importance([], 1))
    print(Solution().get_importance([[1,5,[2,3]],[2,3,[]],[3,3,[]]], 1))
    print(Solution().get_importance([[1,5,[2,3]],[2,3,[]],[3,3,[]], [3,3, [4]], [4, 1, []]], 1))


def build_tree(node_list):
    list = []
    for node in node_list:
        list.append(Employee(node[0], node[1], node[2]))
    return list


class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# LC input
# [[1,2,[2]], [2,3,[]]]
# 2
# []
# 1
# [[1,5,[2,3]],[2,3,[]],[3,3,[]], [3,3, [4]], [4, 1, []]]
# 1
# [[1,5,[2,3]],[2,3,[]],[3,3,[]], [3,3, [4]], [4, 1, []]]
# 1



if __name__ == '__main__':
    main()


# Instructions
"""
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.

"""