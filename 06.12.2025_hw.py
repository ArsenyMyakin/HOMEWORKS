#Задача 1
# with open("text.txt", "w", encoding="utf-8") as file:
#     file.write("Привет\nКак дела\n")
# with open("text.txt", "a", encoding="utf-8") as file:
#     file.write("Как погода?\n")
# with open("text.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())

#Задача 2
# dict={"A":10, "B":20, "C":30}
# import random
# new_dict = {random.randint(100, 1000): value for key, value in dict.items()}
# # print(new_dict)
# with open("text.txt", "w", encoding="utf-8") as file:
#     file.write(str(new_dict))
#     print(new_dict)

#Задача 3
import random
with open("text.txt", "w", encoding="utf-8") as file:
    for i in range(50):
        file.write(random.randint(1, 100))
with open("text.txt", "a", encoding="utf-8") as file:





