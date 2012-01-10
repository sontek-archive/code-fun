def p(text, num):
    print '%d - %s' % (num, text)

for i in range(1,101):
    by_3 = i % 3
    by_5 = i % 5

    if by_3 == 0 and by_5 == 0:
        p('fizzbuzz', i)
    elif by_3 == 0:
        p('fizz', i)
    elif by_5 == 0:
        p('buzz', i)
