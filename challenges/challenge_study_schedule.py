

def study_schedule(permanence_period, target_time):
    cont = 0
    if (target_time == '' or target_time is None):
        return None
    for i in permanence_period:
        if (type(i[0]) != int or type(i[1]) != int):
            return None
        if (i[0] <= target_time <= i[1]):
            cont += 1
    return cont


# permanence_period = [(2, 2), (1, 2), (2, 2), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_period ,2))
