def find_common_participants(partic1, partic2, separator=','):
    particlist_1 = partic1.split(separator)
    particlist_2 = partic2.split(separator)

    same_partic = list(set(particlist_1).intersection(set(particlist_2)))
    same_partic.sort()

    return same_partic


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

partic = find_common_participants(participants_first_group, participants_second_group)
print('Одинаковые люди по алфавиту:', partic)
# TODO Провеьте работу функции с разделителем отличным от запятой
