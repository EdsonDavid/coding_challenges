#Task

#Given the names and grades for each student in a class of  students,
#store them in a nested list and print the name(s) of any student(s)
#having the second lowest grade.

#Input Format

# The first line contains an integer "N" the number of students.
# The  subsequent "2N" lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

#Constraints

# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

#Output Format

#Print the name(s) of any student(s) having the second lowest grade in.
#If there are multiple students, order their names alphabetically and
#print each one on a new line.

if __name__ == '__main__':
    N = int(input())
    while N < 2 or N > 5:
        N = int(input())
    name_score = [[None for _ in range(2)] for _ in range(N)]
    for _ in range(N):
        for i in range (2):
            if i == 0:
                name_score[_][i] = input()
            elif i == 1:
                name_score[_][i] = float(input())
    name_score.sort(key=lambda x: x[1], reverse=False)

    fst_low_grade = 1
    for _ in range(N):
        if name_score[_][1] == name_score[_+1][1]:
            fst_low_grade += 1
        else:
            break

    sec_low_grade = 1
    if fst_low_grade == len(name_score)-1:
        for _ in range(N-fst_low_grade):
            if name_score[_+fst_low_grade-1][1] == name_score[_+fst_low_grade][1]:
                sec_low_grade += 1
            else:
                break
    elif N-fst_low_grade == 2:
        print(fst_low_grade)
        for _ in range(N-fst_low_grade):
            if name_score[_+fst_low_grade][1] == name_score[_+fst_low_grade+1][1]:
                sec_low_grade += 1
                if _+fst_low_grade == N-2:
                    break
            else:
                break
    else:
        for _ in range(N - fst_low_grade):
            if name_score[_ + fst_low_grade][1] == name_score[_ + fst_low_grade+1][1]:
                sec_low_grade += 1
            else:
                break

    sorted_names = [None] * sec_low_grade
    for _ in range(sec_low_grade):
        sorted_names[_] = name_score[_+fst_low_grade][0]
    sorted_names.sort(reverse=False)
    for names in sorted_names:
        print(names)

