count = 0
print(count, type(count))
range_count = 10
for_count = 0
run = True
while run:
    print('Hello Cycle')
    break
while run:
    print('Step =', count)
    count += 1
    break
while count < range_count:
    print('Step =', count)
    count += 1
    break
while count < range_count:
    print('Step =', count)
    count += 1
    if count == 3:
        print('Step =', count, 'If body')
        break
while run:
    print('Steps =', count)
    count += 1
    if count == range_count:
        print('STOP', count),
        break


