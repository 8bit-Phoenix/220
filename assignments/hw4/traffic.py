"""
Name: <Christopher Hamilton, II>
<traffic>.py

Problem: This program calculates entered traffic patterns

Certification of Authenticity:
I certify that this is entirely my own work
"""


def main():
    road = int(input("How many roads were surveyed? "))
    acc = 0
    for i in range(1, road + 1):
        days = int(input("How many days was road " + str(i) + " surveyed: "))
        acc2 = 0
        for _ in range(1, days + 1):
            cars = int(input("How many cars traveled on day " + str(_) + ": "))
            acc2 = cars + acc2
        acc = acc + acc2
        road_average = acc2 / days
        print("Road " + str(i) + " average vehicles per day:", round(road_average, 2))
    average_overall = acc / road
    print("Total number of vehicles traveled on all roads:", acc)
    print("Average number of vehicles per road:", round(average_overall, 2))


if __name__ == "__main__":
    main()
