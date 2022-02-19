import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def find_list(m, selected_elements, remained_list):
    if len(selected_elements) == m:
        return [selected_elements]
    possible_list = []
    for remained_element in remained_list:
        appended_selected_elements = selected_elements.copy()
        appended_selected_elements.append(remained_element)
        removed_remained_list = remained_list.copy()
        removed_remained_list.remove(remained_element)
        my_list = find_list(m, appended_selected_elements, removed_remained_list)
        possible_list.extend(my_list)
    return possible_list


candidate_list = [i+1 for i in range(n)]
result = find_list(m, [], candidate_list)
for i in result:
    print(' '.join(map(str ,i)))