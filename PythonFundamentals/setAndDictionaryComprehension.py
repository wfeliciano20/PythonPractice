# set comprehension
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']


friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}

print(present_friends)

# dictionary Comprehension

friends2 = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 11]

# using zip function
long_timers2 = dict(zip(friends2, time_since_seen))

# using dictionary comprehension
long_timers = {
    friends2[i]: time_since_seen[i]
    for i in range(len(friends2))
    # if time_since_seen[i] > 5
}

print(long_timers)
print(long_timers2)
