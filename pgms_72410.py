def solution(new_id):
    able_string = ['-', '_', '.']
    able_string.extend([chr(i) for i in range(97, 123)])
    able_string.extend([str(i) for i in range(0, 10)])
    answer = ''

    new_id = new_id.lower()

    for ch in new_id:
        if ch in able_string:
            if not answer or not ch == '.' == answer[-1]:
                answer += ch

    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]

    if not answer:
        answer = 'a'
    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer



print(solution("z-+.^."))
