"""
https://interviewing.io/questions/employee-hierarchy
Given an array of employee IDs including who they report to, write a function to calculate the score for a given employee.
The employee score for an employee equals "Total number of direct and indirect employees report to that employee, then plus 1."
The “plus one" here means adding the employee itself as self-reporting.
An employee without any other employees reporting to it, will have employee score 1.
Each employee has a unique eid (employee_id).
Given a direct report map, where key is an eid, value is an array of eids who directly report to key.
This map should contain all employees. The map could contain cycles.
Here is an example of direct report map: {123: [234, 345], 234: [456, 789], 345:[], 456:[], 789:[]}
Your solution should have better runtime when called multiple times.
"""


class Node:
    def __init__(self, id):
        self.id = id
        self.children = {}


point_map = {}


def count_points(key, report_map):
    # iterate through the map and get the employee and reportees
    # If employee has no reportees, store 1 to point_map
    # If the employee has reportees, recursively count point of reportees.

    # base case
    if not report_map:
        return 0

    # check if reportees are present, memoize
    if len(report_map[key]) == 0:
        point_map[key] = 1
        return 1

    # If already memoized, return the val
    if point_map.get(key):
        return point_map[key]

    # Calculate the score recursively for if reportees are present
    score = 0
    for emp in report_map[key]:
        score += count_points(emp, report_map)

    # Add self score
    score += 1

    # memoize
    point_map[key] = score
    return score


report_map = {123: [234, 345], 234: [456, 789], 345: [], 456: [], 789: []}
count_points(123, report_map)
print(point_map)
