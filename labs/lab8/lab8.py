"""
Name: <Christopher Hamilton, II>
<lab8>.py
"""
from encryption import encode,encode_better


def main():
    # add other function calls here
    number_words("Walrus.txt", "Walrus_output.txt")
    hourly_wages("hourly_wages.txt", "hourly_wages_out.txt")
    x = calc_check_sum("0072946520")
    print(x)
    send_message("message.txt", "jojo")
    send_safe_message("secret_message.txt", "dio", 1)
    send_uncrackable_message("safest_message.txt", "king_crimson", "pad.txt")



def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "r")
    i = 1
    for line in infile:
        words = line.split()
        for words in words:
            outfile.write(str(i) + " " + words + "\n")
            i += 1
    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "r")
    for line in infile:
        split = line.split()
        wage = float(split[2])
        wage += 1.65
        wage = wage * int(split[3])
        outfile.write(split[0] + " " + split[1] + " " + str(wage) + "\n")
    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - 1
        acc += int(isbn[i]) * pos
        return acc


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "wt")
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "wt")
    for line in infile:
        outfile.write(encode(line, key))
    infile.close()
    outfile.close()


def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "wt")
    padfile = open(pad, "r")
    k = padfile.read()
    for line in infile:
        outfile.write(encode_better(line, k))
    infile.close()
    outfile.close()


main()
