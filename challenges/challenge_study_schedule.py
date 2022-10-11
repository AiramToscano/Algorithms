
def study_schedule(permanence_period, target_time):
    cont = 0
    try:
        for i in permanence_period:
            if (int(i[0]) <= target_time <= int(i[1])):
                cont += 1
        return cont
    except Exception:
        return None
