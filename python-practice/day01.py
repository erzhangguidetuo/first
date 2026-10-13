# print("-------------------------------------------------------")

# a = "hello"
# print(a)

# print("-------------------------------------------------------")

# score = float(input("请输入你的成绩："))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("D")

# print("-------------------------------------------------------")

# age = int(input("请输入你的年龄："))
# if age <= 6:
#     print("儿童")
# elif age <= 18:
#     print("青少年")
# elif age <=60:
#     print("成年人")
# else:
#     print("老年人")

# print("-------------------------------------------------------")

# num = 1
# while num <= 100:
#     print(num)
#     num += 1

# print("-------------------------------------------------------")

# for num1 in range(1,101):
#     print(num1)

# print("-------------------------------------------------------")

# num2 = 0
# for num3 in range(1,101):
#     num2 += num3
# print(num2)
# print("-------------------------------------------------------")

# j = 1
# while j <= 9:
#     i = 1
#     while i <= j:
#         print(f"{i}*{j}={i*j}", end="\t")
#         i += 1
#     print()
#     j += 1

# print("-------------------------------------------------------")

# print("学生成绩管理系统")
# print("-------------------------------------------")
# student_number = int(input("请输入学生人数："))
# i = student_number
# avg_list = []
# avg_name = []
# all_avg_aocre = 0
# while i < 2*student_number:
#     student_nmae = str(input("学生姓名："))
#     chinese_socre = int(input("语文成绩："))
#     math_socre = int(input("数学成绩："))
#     english_socre = int(input("英语成绩："))
#     avg_socre = (chinese_socre + math_socre + english_socre)/3
#     avg_list.append(avg_socre)
#     avg_name.append(student_nmae)
#     i += 1 
# print("=====================================================")
# for avg in range(len(avg_name)):
#     print(f"{avg_name[avg]}的平均分为：{avg_list[avg]}")   
# print("=====================================================")
# for index in avg_list:
#     all_avg_aocre += index 
# print(f"全班平均分为：{all_avg_aocre/3}")
# max_avg_socre = max(avg_list)
# j = avg_list.index(max_avg_socre)
# print(f"{avg_name[j]}的平均分最高为：{max_avg_socre}")






# print("学生管理系统")
# print("==========================================================")
# def avg(chinese,math,english):
#     return (chinese + math + english)/3
# num = int(input("请输入有几个学生："))
# i = num
# name_list=[]
# score_list = []
# hege_num = 0
# buhege_num = 0
# all_avg = 0

# while i < num * 2:
#     name = input("请输入学生姓名：")
#     chinese = int(input("请输入语文成绩："))
#     math = int(input("请输入数学成绩："))
#     english = int(input("请输入英语成绩："))
#     name_list.append(name)
#     avg_score = avg(chinese,math,english)
#     score_list.append(avg_score)
#     i += 1

# for index in range(len(name_list)):
#     if score_list[index] >= 60:
#         hege_num += 1
#     else:
#         buhege_num += 1
# print(f"及格人数为：{hege_num}")
# print(f"不合格人数为：{buhege_num}")
           

# max_score = max(score_list)
# index1 = score_list.index(max_score)
# print(f"{name_list[index1]}是平均最高的：{max_score}分")

# min_score = min(score_list)
# index2 = score_list.index(min_score)
# print(f"{name_list[index2]}是平均最低的：{min_score}分")

# for i in score_list:
#     all_avg += i
# print(f"全班平均分为：{all_avg/3}")








# student_informations = {"name":"tom",
#                         "age" : 18,
#                         "python" : 95}
# print(student_informations["name"])
# print(student_informations["python"])
# student_informations["python"] = 100
# student_informations["city"] = "BeiJing"
# print(student_informations)

# student = {}
# name = input("请输入姓名：")
# chinese = int(input("请输入语文成绩："))
# math = int(input("请输入数学成绩："))
# english = int(input("请输入英语成绩："))
# student["name"] = name
# student["chinese"] = chinese
# student["math"] = math
# student["english"] = english
# def avg(chinese,math,english):
#     return (chinese + math + english)/3
# avg_score = avg(chinese,math,english)
# student["avg_score"] = avg_score
# print(student)







# students=[{
#                 "name":"tom",
#                 "python":95
#             },
#             {
#                 "name":"jerry",
#                 "python":88
#             },
#             {
#                 "name":"jack",
#                 "python":76
#             }
#             {
#                 "name":"mary",
#                 "python":91
#             }
#         ]
# max_score = 0
# max_name = None
# second_score = 0
# second_name = None
# for student in students:
#     if max_score < student["python"]:
#         max_score = students[0]["python"]
#         max_name = students[0]["name"]
        







students =[]
with open("student,txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        stu={
            "name" : line[0],
            "python" : line[1],
            "english" : line[2],
            "math" : line[3]
            }
        students.append(stu)



def add_student(name,python,english,math):
    student = {}
    student["name"] = name
    student["python"] = python
    student["english"] = english
    student["math"] = math
    students.append(student)

def all_student():
    for stu in students:
        print("==================================")
        print(f"姓名为：{stu["name"]}")
        print(f"python成绩是：{stu["python"]}")
        print(f"英语成绩为：{stu["english"]}")
        print(f"数学成绩是：{stu["math"]}")
        print("==================================")

def find_students(name):
    find = 0
    for stu in students:
        if  name == stu["name"]:
            find = 1
            if find == 1:
                print("================================")
                print(f"姓名：{stu["name"]}")
                print(f"python：{stu["python"]}")
                print(f"英语：{stu["english"]}")
                print(f"数学：{stu["math"]}")
                break
    if find == 0:
        print("没找到这个人！")

def change_students(change_name,change_prj,change_sco):
    find = 0
    for stu in students:
        if change_name == stu["name"]:
            find = 1
            if find == 1:
                if change_prj == "python":
                    stu["python"] = change_sco
                    break
                if change_prj == "english":
                    stu["english"] = change_sco
                    break
                if change_prj == "math":
                    stu["math"] = change_sco
                    break
                if change_prj != "python" or "english" or "math":
                    print("没有这个科目！")
                    break
        with open("student.txt","w",encoding="utf-8") as f:
            for line in f:
                if line[0] == change_name:
                    line[1] == 
    if find == 0:
        print("没有这个科目！")

def del_students(del_student):
    find = 0
    for stu in students:
        if del_student == stu["name"]:
            find = 1
            if find == 1:
                students.remove(stu)
                break
    if find == 0:
        print("没有这个学生！")

while True:
    print("==========学生管理系统==========")
    print("1.添加学生")
    print("2.查看所有学生")
    print("3.查询学生")
    print("4.修改成绩")
    print("5.删除学生")
    print("0.退出")

    choice = int(input("请选择："))
    if choice == 0:
        break

    elif choice == 1:
        name = input("请输入姓名：")
        python = int(input("请输入python成绩："))
        english = int(input("请输入英语成绩："))
        math = int(input("请输入数学成绩："))
        add_student(name,python,english,math)

    elif choice == 2:
       all_student()

    elif choice == 3:
        find_student = input("请输入要查询的学生：")
        find_students(find_student)

    elif choice == 4:
        change_name = input("你要修改的学生：")
        change_prj = input("你要修改的科目：")
        change_sco = input("你要修改的分数：")
        change_students(change_name,change_prj,change_sco)

    elif choice == 5:
        del_student = input("输入要删除的学生：")
        del_students(del_student)



    