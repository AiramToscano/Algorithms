def study_schedule(permanence_period, target_time):
    cont = 0
    try:
        for i in permanence_period:
            if (int(i[0]) <= target_time <= int(i[1])):
                cont += 1
        return cont
    except Exception:
        return None


# permanence_period = [(2, 2), (1, 2), (2, 2), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_period, ''))
