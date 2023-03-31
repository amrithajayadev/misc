prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
num_courses = 5

def dfs(course, pre, visited, pre_map):
    if course in visited:
        return
    visited.append(course)
    for p in pre:
        dfs(p, pre_map[p], visited, pre_map)
    return

def course_scheudle_order(prerequisites, num_courses):
    pre_map = {i:[] for i in range(num_courses)}
    order = []
    for course, pre in prerequisites:
        pre_map[course].append(pre)
    visited = list()

    for course, pre in pre_map.items():
        dfs(course, pre, visited, pre_map)
    print(visited[::-1])
    return order

course_scheudle_order(prerequisites, num_courses)