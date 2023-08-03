N = int(raw_input())

while N > 0:
    result = ''
    input_line = raw_input()
    C, tree_seq = input_line.split()

    index = 0
    stack = []
    if int(C) == 0:
        result += tree_seq[0]
    for ch in tree_seq:
        if ch.isalpha() or ch == '.':
            if stack and type(stack[-1]) is tuple:
                index = stack[-1][1] + 2
            stack.append((ch, index))
        if ch == '(':
            stack.append('(')
            index -= 1
        if ch == ')':
            node1 = stack.pop()
            node2 = stack.pop()
            stack.pop()
            if node2[1] == int(C) and node2[0] != '.':
                result += node2[0]
            if node1[1] == int(C) and node1[0] != '.':
                result += node1[0]
    if result:
        print ''.join(sorted(result))
    else:
        print 'Common Gandhijee!'
    N -= 1