# 1 ############################

import os
os.chdir("DZ_files")

def domains_point_free(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip()[1:] for line in file.readlines()]
    except FileNotFoundError as error:
        return f"No file {error}"

print(domains_point_free("domains.txt"))

# 2 ############################

def surnames(filename):
    with open(filename, "r") as file:
        return [line.split("\t")[1] for line in file.readlines()]


print(surnames("names.txt"))

# 3 #############################

from datetime import datetime

def dates(filename):

    result = []
    with open(filename, "r") as file:
        for line in file.readlines():
            my_line = line.split(" - ")
            if len(my_line) > 1:
                date = my_line[0]
                day, month, year = date.split()
                my_date = datetime.strptime(f"{day[:-2]} {month} {year}", "%d %B %Y")
                result.append(
                    {
                        "date_original": date,
                        "date_modified": datetime.strftime(my_date, "%d/%m/%Y"),
                    }
                )
    return result


print(dates("authors.txt"))