def diff_ans(data):
    return sum(len(set(group.replace("\n", ""))) for group in data.split("\n\n"))

def same_ans(data):
    return sum(len(set.intersection(*map(set, group.splitlines()))) for group in data.split("\n\n"))

f = open('advent6.txt', 'r').read()

print(diff_ans(f))
print(same_ans(f))