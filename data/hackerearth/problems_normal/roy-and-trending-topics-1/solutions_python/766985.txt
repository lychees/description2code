from operator import itemgetter

N = [int(x) for x in raw_input().split()][0]

top_five = []


def update_top_five(new_topic):
    global top_five
    if top_five.__len__() != 5:
        top_five.append(new_topic)
        top_five = sorted(top_five, key=itemgetter(6, 0), reverse=True)
    else:
        if top_five[4][6] < new_topic[6] or (top_five[4][6] == new_topic[6] and top_five[4][0] < new_topic[0]):
            top_five[4] = new_topic
            top_five = sorted(top_five, key=itemgetter(6, 0), reverse=True)


while N > 0:
    N -= 1
    topic = [int(x) for x in raw_input().split()]
    new_z_score = topic[2] * 50 + topic[3] * 5 + topic[4] * 10 + topic[5] * 20
    topic.append(new_z_score - topic[1])
    update_top_five(topic)

for topic in top_five:
    print topic[0], topic[6] + topic[1]