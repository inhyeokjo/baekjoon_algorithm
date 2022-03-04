def solution(id_list, report, k):
    dic_repo = {id: [] for id in id_list}
    answer = [0] * len(id_list)

    temp = report[0].split(' ')
    print(temp[1], 'chch')
    print(dic_repo[temp[1]], 'test1')
    print(dic_repo['frodo'], 'test2')
    print(temp[1], )

    # for repo in set(report):
    #     repo = repo.split(' ')
    #     dic_repo[repo[1]].append(repo[0])
    #     dic_repo['neo'].append(repo[0])
    #
    # for key, values in dic_repo.items():
    #     if len(values) >= k:
    #         for v in values:
    #             answer[id_list.index(v)] += 1
    # print(dic_repo)
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
print(solution(id_list, report, k))
