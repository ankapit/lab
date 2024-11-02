# TODO Напишите функцию find_common_participants

def find_common_participants(list1, list2, spliter = ","):
    names1 = set(list1.split(spliter))
    names2 = set(list2.split(spliter))
    common = list(names1.intersection(names2))
    common.sort()
    return common
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))