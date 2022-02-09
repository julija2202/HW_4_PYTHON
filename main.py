count = 0
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

for item in range(for_count, range_count):
    print('Steps = ', item)

for item in range(0, 30):
    if item == 5:
        print('item = ', item)
    else:
        if item == 10:
            print('item = ', item)
        else:
            if item < 4:
                print('item < ', item)
            else:
                if item >= 27:
                    print('item >= ', item)
                else:
                    print('Steps = ', item)

for item in range(0, range_count+1):
    print('Steps = ', item)
    if item == 7:
        inner_count = 0
        print('--inner_count = ', inner_count)
        for inner_item in range(0, item):
            print('-------- Inner_Step = ', inner_item)
            if inner_item == 5:
                inner_count = inner_item
            else:
                print('-- inner_count =', inner_count)

for item in range(0, 20):
    print('Steps = ', item)
    if item > 7 and item < 12:
        print('If_item =', item)
        continue
print('End_iteration =', item)