def average(sequence):
    return sum(sequence) / len(sequence)


def avg(seq): return sum(seq) / len(seq)


def total(seq): return sum(seq)


def top(seq): return max(seq)


students = {
    {'name': 'Rolf', 'grades': (67, 90, 95, 100)},
    {'name': 'Bob', 'grades': (56, 78, 80, 90)},
    {'name': 'Jen', 'grades': (98, 90, 95, 99)},
    {'name': 'Anne', 'grades': (100, 100, 95, 100)}
}

for student in students:
    print(average(student['grades']))
