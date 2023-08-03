no_of_test_cases = int(raw_input())

for i in range(no_of_test_cases):
    total_nodes = int(raw_input())
    nodes = [int(x) for x in raw_input().split()]
    if total_nodes == 1:
        print nodes[0]
        continue
    j = total_nodes - 1
    max_sum_per_sub_tree = [0] * total_nodes
    while j >= 2:
        root_index = j / 2 - 1
        max_sum_per_sub_tree[root_index] = nodes[j] + nodes[j - 1] + nodes[root_index]
        if j >= total_nodes / 2:
            max_sum_per_sub_tree[j] = nodes[j]
            max_sum_per_sub_tree[j - 1] = nodes[j - 1]
        nodes[root_index] += max(nodes[j], nodes[j - 1])
        j -= 2

    print max(max_sum_per_sub_tree)