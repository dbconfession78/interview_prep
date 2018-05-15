"""
On Quora, a question can have a variety of user-submitted answers. These questions are assigned topic tags to improve discoverability, and views are tracked at the answer level to identify the top answers and surface them in the the feed and search results.

More specifically:

A user can write an answer to a question;
A question can have multiple answers;
A question can be assigned multiple topics;
For example, the question "How many software engineers work at Google as of 2017?" is tagged with the topics "Silicon Valley", "Google", and "Software Engineering".
An answer can get views.
The Most-Viewed Writers for a given topic are the top 10 Quora users whose answers to questions tagged with that topic are viewed the most. (When fewer than 10 users have submitted answers to questions tagged with a particular topic, the Most-Viewed Writers for that topic would include all the users who have contributed answers, regardless of whether or not their answers have any views.) An answer must belong to a question that is tagged with a given topic to be considered to be within that topic.

Given this system, compute the Most Viewed Writers for each topic, ordered from the smallest topic_id to the largest one. If two users have the same number of views, the user with the smaller user_id should come first.

For a specific topic_id, the set of Most-Viewed Writers should be returned in the following format:

<user_id_1> <views_1>
<user_id_2> <views_2>
...
<user_id_N> <views_N>
where:

user_id_i is the ID of the ith user in the set;
views_i is the total number of views the user gets across all their answers in that topic;
Note that views_i may be equal to 0. If a user posted an answer that didn't get any views, they can still be included in the Most Viewed Writers list if there are fewer than 10 users who have contributed answers for that topic;
N is the number of Most Viewed Writers for the topic topic_id.
Example

For topicIds = [[1, 2, 3], [2, 3, 4], [1, 4], [2, 3]],
answerIds = [[6, 4], [1, 2], [5], [3]] and
views = [[2, 1, 2], [6, 3, 5], [3, 3, 0], [5, 1, 1], [4, 2, 3], [1, 4, 2]], the output should be

mostViewedWriters(topicIds, answerIds, views) = [
    [[3, 5], [2, 3], [1, 1]],
    [[3, 5], [2, 3], [1, 2], [4, 2]],
    [[3, 5], [2, 3], [1, 2], [4, 2]],
    [[1, 3], [4, 2]]
]
In this example, we have 4 different topic IDs: 1, 2, 3, and 4. Let's find the Most Viewed Writers for each of them.

For topic_id = 1:
    As we can see in the topicIds array, topic 1 is tagged to questions 0 and 2.
    We can see in the answerIds array that the answers corresponding to this topic are 6, 4, and 5.
    Now let's look at the views array and find all such views[i] that views[i][0] is one of the answer IDs from the last line:
    views[1][0] = 6, so we add views[1][2] = 5 views to the user with ID views[1][1] = 3;
    views[3][0] = 5, so we add views[3][2] = 1 views to the user with ID views[3][1] = 1;
    views[4][0] = 4, so we add views[4][2] = 3 views to the user with ID views[4][1] = 2.
    To recap, for topic_id = 1 we have 3 Most Viewed Writers: the user with ID 3 has 5 views, the user with ID 2 has 3 views, and the user with ID 1 has 1 view.

For topic_id = 2:
    As we can see in the topicIds array, topic 2 is tagged to questions 0, 1, and 3.
    We can see in the answerIds array that the answers corresponding to this topic are 6, 4, 1, 2, and 3.
    Now let's look at the views array and find all such views[i] that views[i][0] is one of our answer IDs:
    views[1][0] = 6, so we add views[1][2] = 5 views to the user with ID views[1][1] = 3;
    views[4][0] = 4, so we add views[4][2] = 3 views to the user with ID views[4][1] = 2;
    views[5][0] = 1, so we add views[5][2] = 2 views to the user with ID views[5][1] = 4;
    views[0][0] = 2, so we add views[0][2] = 2 views to the user with ID views[4][1] = 1;
    views[2][0] = 3, so we add views[3][2] = 0 views to the user with ID views[3][1] = 3.
    To recap, for topic_id = 2 we have 4 Most Viewed Writers: the user with ID 3 has 5 views, the user with ID 2 has 3 views, the user with ID 1 has 2 views, and the user with ID 4 has 2 views. The last two users are ordered as they are because the user with the smaller ID comes first.

For topic_id = 3:
    This topic is tagged to the same questions as topic_id = 2 is, so its Most Viewed Writers is also the same.

For topic_id = 4:
    As we can see in the topicId array, this topic is tagged to questions 1 and 2.
    We can see in the answerId array that the answers corresponding to this topic are 1, 2, and 5.
    Now let's look at the views array and find all such views[i] that views[i][0] is one of our above answer IDs:
    views[5][0] = 1, so we add views[5][2] = 2 views to the user with ID views[5][1] = 4;
    views[0][0] = 2, so we add views[0][2] = 2 views to the user with ID views[0][1] = 1;
    views[3][0] = 5, so we add views[3][2] = 1 views to the user with ID views[3][1] = 1.
    To recap, for topic_id = 4 we have 2 Most Viewed Writers: the user with ID 1 has 3 views, and the user with ID 4 has 2 views.
    Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer topicIds

topicIds[i] contains the topic IDs for the ith question. A question may have no topics.

Guaranteed constraints:
1 ≤ topicIds.length ≤ 5,
0 ≤ topicIds[i].length ≤ 4,
1 ≤ topicIds[i][j] ≤ 1000.

[input] array.array.integer answerIds

answerIds[i] contains the answer IDs for the ith question. A question may have no answers.

Guaranteed constraints:
answerIds.length = topicIds.length,
1 ≤ answerIds[i][j] ≤ 1000.

[input] array.array.integer views

For each valid i, views[i] contains informations about answer views:

views[i][0] is answer_id, the ID of the answer. It is guaranteed that this ID is contained in at least one answerIds[i] list, and that for each answer ID from answerIds there's a corresponding element in views;
views[i][1] is user_id, the ID of the user who submitted the answer;
views[i][2] is views, the number of views the answer answer_id has.
Guaranteed constraints:
1 ≤ views.length ≤ 15,
views[i].length = 3,
0 ≤ views[i][j] ≤ 1000.

[output] array.array.array.integer

An array, containing the Most Viewed Writers for each topic, ordered from the smallest topic_id to the largest one.
"""
from collections import defaultdict
from bisect import bisect
from operator import itemgetter
def mostViewedWriters(topicIds, answerIds, views):
    dct = defaultdict(list)
    dct2 = defaultdict(list)
    retval = []
    for i, arr in enumerate(topicIds):
        for j, elem in enumerate(arr):
            dct[elem].append(i)

    for i, arr in enumerate(views):
        answer = arr[0]
        user = arr[1]
        views = arr[2]
        dct2[answer] = {"user": user, "views": views}

    for topic, quests in dct.items():
        lst1 = []
        lst2 = []
        for quest in quests:
            answers = answerIds[quest]
            lst1 += answers

        view_counts = defaultdict(list)
        views_by_user = defaultdict(int)
        for elem in lst1:
            lst3 = []
            vws = dct2[elem]["views"]
            usr = dct2[elem]["user"]
            views_by_user[usr] += vws
            if vws > 0:
                lst3.append(usr)
                lst3.append(vws)
                if view_counts[vws]:
                    idx = bisect(view_counts[vws], usr)
                    view_counts[vws].insert(idx, usr)
                else:
                    view_counts[vws].append(usr)

        seen_users = set()
        # print(views_by_user)
        user_by_views = {}

        for k, v in views_by_user.items():
            if k not in seen_users:
                if len(view_counts[v]) > 1:
                    for u in view_counts[v]:
                        if u in seen_users:
                            if
                        seen_users.add(u)
                        lst2.append([u, views_by_user[u]])
                else:
                    lst2.append([k, v])
                    seen_users.add(k)
        lst2 = sorted(lst2, key=itemgetter(1), reverse=True)
        retval.append(lst2)
    return retval


# # [
# #   [    [3,5],[2,3],[1,1]    ],
# #   [    [3,5],[2,3],[1,2],[4,2]    ],
# #   [    [3,5],[2,3],[1,2],[4,2]    ],
# #   [    [1,3],[4,2]    ]
# # ]
# ret = mostViewedWriters(
#     [
#         [1,2,3],
#         [2,3,4],
#         [1,4],
#         [2,3]
#     ],
#     [
#         [6,4],
#         [1,2],
#         [5],
#         [3]
#     ],
#     [
#         [2,1,2],
#         [6,3,5],
#         [3,3,0],
#         [5,1,1],
#         [4,2,3],
#         [1,4,2]
#     ]
# )
# for elem in ret:
#     print(elem)
# print()
#
# # [
# #   [   [5,3]   ],
# #   [   [5,3]   ],
# #   [   [5,3]   ]
# # ]
# ret = mostViewedWriters(
#     [[1,2,3]],
#     [[1]],
#     [[1,5,3]]
# )
# for elem in ret:
#     print(elem)
# print()
#
# # [
# #   [   [3,2],[1,1],[10,1]  ],
# #   [   [10,11],[3,2],[1,1] ],
# #   [   [10,10],[1,0]   ]
# # ]
# ret = mostViewedWriters([[],
#  [],
#  [1,2],
#  [],
#  [2,3]], [[],
#  [4],
#  [6,7,8],
#  [3],
#  [1,2]], [[7,3,2],
#  [3,1,10],
#  [1,10,10],
#  [4,8,3],
#  [6,1,1],
#  [2,1,0],
#  [8,10,1]])
#
# for elem in ret:
#     print(elem)
# print()


# [
#   [   [23,37] ],
#   [   [23,37] ],
#   [   [23,37],[1,23],[7,20],[18,18]   ],
#   [   [18,6],[239,1]  ],
#   [   [1,23],[7,20],[18,18]   ],
#   [   [18,6],[239,1]  ],
#   [   [18,6],[239,1]  ],
#   [   [1,23],[7,20],[18,18]   ]
# ]
ret = mostViewedWriters(
    [
        [555,666,777],
        [8,1,239],
        [239,566,1000]
    ],
    [
        [1,2,3],
        [239,567],
        [566,30,8]],
    [
        [1,18,5],
        [239,23,37],
        [567,23,0],
        [566,1,23],
        [30,18,18],
        [8,7,20],
        [3,239,1],
        [2,18,1]
    ])

for elem in ret:
    print(elem)
print()