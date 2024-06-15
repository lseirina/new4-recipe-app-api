def some(seats, students):
    seats.sort()
    students.sort()
    res = []
    for seat, student in zip(seats, students):
        res.append(abs(seat - student))
    return sum(res)
    # seats.sort()
    # students.sort()
    # return sum(abs(seat - student) for seat, student in zip(seats, students))


print(some([4,1,5,9], [1,3,2,6]))