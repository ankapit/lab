import csv
import json

INPUT_FILENAME = "input_new.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, 'r', newline= "\n") as file:
        reader = csv.DictReader(file, delimiter= ",")
        for row in reader:
            data.append(row)

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=True)




if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")