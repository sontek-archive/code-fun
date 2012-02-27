length = int(raw_input())

swap = {
    'bc': 'a',
    'ac': 'b',
    'ab': 'c',
}

for index in range(1, length+1):
    test = raw_input()

    def solve(t, best_match):
        if len(t) < best_match:
            best_match = len(t)

        for index, s in enumerate(t):
            # if we aren't at the end of the string
            if index != len(t)-1:
                # if the 2 characters next to each other don't match
                if s != t[index+1]:
                    match = s + t[index+1]

                    for key in swap.keys():
                        # check which letter to swap the match with
                        if match == key or match == key[::-1]:
                            # replace the first occurance of the match
                            result = t.replace(match, swap[key], 1)
                            current_len = len(result)

                            if current_len < best_match:
                                best_match = current_len

                            # our current match is better than current best_match
                            # return this match
                            new_len = solve(result, best_match)

                            if new_len < best_match:
                                best_match = new_len
                                return best_match

        return best_match

    print solve(test, 99)
