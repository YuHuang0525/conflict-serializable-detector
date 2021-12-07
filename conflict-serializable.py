import LinkedList
import re

#s = 'r1(A) r4(D) w3(C) r2(B) w2(A) r1(C) w3(B)' -- false
#s = 'r2(A) r1(B) w2(A) r2(B) r3(A) w1(B) w3(A) w2(B)' -- false
#s = 'r2(A) r1(B) w2(A) r3(A) w1(B) w3(A) r2(B) w2(B)' -- true
#s = 'R1(A), W2(B), R3(C), W3(A), R3(D), R4(B), W4(D), W2(C)' -- true
#s = 'r1(A)w1(A)r2(A)w2(A)r1(B)w1(B)r2(B)w2(B)' -- true

s = input('please type in your schedules:')
nums = set(re.findall('[0-9]', s))
temp = []
for x in nums:
    temp.append(int(x))

nums = sorted(temp)

def find_num_behind(temp_list, original_s):
    result = []
    for x in temp_list:
        single_schedule = original_s[x[0]:x[1]]
        temp_num = single_schedule[1]
        read_write = single_schedule[0]
        attribute = single_schedule[-2]
        if read_write == 'r':
            temp = re.findall('w[^{0}]\({1}\)'.format(temp_num, attribute), original_s[x[1]:])
            if len(temp) != 0:
                for y in temp:
                    temp_num = re.findall('[0-9]',y)
                    result.append(int(temp_num[0]))
            else:
                continue
        elif read_write == 'w':
            temp = re.findall('r[^{0}]\({1}\)'.format(temp_num, attribute), original_s[x[1]:])
            if len(temp) != 0:
                for y in temp:
                    temp_num = re.findall('[0-9]', y)
                    result.append(int(temp_num[0]))
            else:
                continue
    return result


l1 = LinkedList.sLinkedList()
cur_node = LinkedList.Node()
l1.head = cur_node

break_counter = 0

for x in nums:
    if break_counter == 1:
        break
    temp_list = [m.span() for m in re.finditer('[a-z]{}\s*\([a-zA-Z]\)'.format(x), s)]
    num_behind = find_num_behind(temp_list, s)
    #print(x)
    #print('----')
    #print(temp_list)
    #print(set(num_behind))
    if cur_node.val == 0:
        cur_node = LinkedList.Node(x)
        cur_node.next = None
        l1.head = cur_node
    #l1.print_list()
    #print(l1.detect_loop())
    for num in set(num_behind):
        if l1.detect_loop() == 'loop_detected':
            print('\n')
            print('This is cyclic and thus NOT conflict-serializable')
            break_counter = 1
            break
        temp_all_nodes = l1.find_all_nodes()
        if num in temp_all_nodes.values():
            temp_node = l1.find_node(num)
            cur_node.next = temp_node
            cur_node = cur_node.next
            continue
        temp_node = LinkedList.Node(num)
        temp_node.next = None
        cur_node.next = temp_node
        cur_node = cur_node.next

if not break_counter and l1.detect_loop() == 'no_loop_detected':
    print('\n')
    print('This is acyclic and thus conflict-serializable')
    print('\n')
    print('Check is done')

# this checks whether we have loops in our schedules after the very last step of inserting into LinkedList
elif break_counter:
    print('\n')
    print('Check is done')

elif l1.detect_loop() == 'loop_detected':
    print('\n')
    print('This is cyclic and thus NOT conflict-serializable')
    print('\n')
    print('Check is done')
