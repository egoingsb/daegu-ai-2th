# members = [
#     ['egoing', 'Seoul', 'Web'],
#     ['leezhe', 'Jeju', 'Design']
# ]
# print(members[0][1])
# for member in members:
#     print(member[0], member[1], member[2])
members = [
    {'city':'Seoul', 'job':'WEB', 'name':'egoing'},
    {'city':'Jeju', 'job':'Design', 'name':'leezche'}
]
print(members[0]['city'])
for member in members:
    print(member['name'], member['city'], member['job'])