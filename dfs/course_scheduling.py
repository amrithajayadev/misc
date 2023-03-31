# prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
# num_courses = 5

prerequisites = [[0, 1], [1,0]]
num_courses = 2


def dfs(course, pre, visited, premap):
    if course in visited:
        return False
    if not pre:
        visited.remove(course)
        return True
    visited.add(course)
    for p in pre:
        return dfs(p, premap[p], visited, premap)
    return True


def is_course_scheduling_possible(prerequisites, num_courses):
    premap = {i: [] for i in range(num_courses)}
    visited = set()
    for course, pre in prerequisites:
        premap[course].append(pre)

    for course, pre in premap.items():
        return dfs(course, pre, visited, premap)
    return True

if is_course_scheduling_possible(prerequisites, num_courses):
    print("true")
else:
    print("false")