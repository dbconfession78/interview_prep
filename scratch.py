"""
Module 7-github_commits - list 10 commits (from the most recent to oldest) of
                          the repository “rails” by the user “rails” using the
                          Github API.
                          (https://developer.github.com/v3/repos/commits/)
"""
"""
100-github_commits.py
"""
import requests
import sys


def request_to_github(the_url):
    """makes a request for commits from input url"""
    r = requests.get(the_url)
    the_json = r.json()
    c_range = 10 if len(the_json) >= 10 else len(the_json)
    for i in range(c_range):
        c = the_json[i]
        c_sha = c.get('sha')
        c_author = c.get('commit').get('author').get('name')
        print('{}: {}'.format(c_sha, c_author))
#
# if __name__ == "__main__":
#     """MAIN APP"""
#     the_url = ('https://api.github.com/repos/{}/{}/commits'
#                .format(sys.argv[2], sys.argv[1]))
#     request_to_github(the_url)


def main():
    import requests
    import sys

    # repo = sys.argv[1]
    # owner = sys.argv[2]
    repo = "rails"
    owner = "rails"

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    j = r.json()
    if j == []:
        print("No result")
    else:
        if len(j) >= 10:
            limit = 10
        else:
            limit = len(j);
        for i in range(limit):
            elem = j[i]
            sha = elem.get('sha')
            author = elem.get('commit').get('author').get('name')
            item = "{}: {}".format(sha, author)
            print(item)

if __name__ == "__main__":
    main()