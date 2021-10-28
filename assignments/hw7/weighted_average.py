"""
Name: <Christopher Hamilton, II>
<weighted_average>.py

Problem: This program calculates a weighted average

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name,out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    total_class = 0
    count = 0
    for lines in infile:
        w_total = 0
        acc = 0
        name, numbers = lines.split(": ")
        numbers = numbers.split(" ")
        weight = numbers[::2]
        grade = numbers[1::2]
        for c in range(len(weight)):
            int_w = int(weight[c])
            int_g = int(grade[c % len(grade)])
            w_total = w_total + int_w
            acc = acc + (int_w * int_g)
        if w_total == 100:
            average = acc / 100
            total_class = total_class + average
            count = count + 1
            outfile.write(str(name) + "'s average: " + str(round(average, 1)) + "\n")
        elif w_total > 100:
            outfile.write(str(name) + "'s average: Error: The weights are more than 100." + "\n")
        else:
            outfile.write(str(name) + "'s average: Error: The weights are less than 100." + "\n")
    tc_average = round((total_class / count), 1)
    outfile.write("Class average: " + str(tc_average))
    infile.close()
    outfile.close()


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == "__main__":
    main()
