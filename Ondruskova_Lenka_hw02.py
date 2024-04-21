import json


def decade(year):
    return year - (year % 10)


def correctedlist(string):
    if string == "":
        return []
    split = string.split(", ")
    return split


result = []

with open("netflix_titles.tsv", mode="r", encoding="utf-8") as inputfile:
    header = inputfile.readline().strip("\n").split("\t")

    ColumnIndex1 = header.index("PRIMARYTITLE")
    ColumnIndex2 = header.index("DIRECTOR")
    ColumnIndex3 = header.index("CAST")
    ColumnIndex4 = header.index("GENRES")
    ColumnIndex5 = header.index("STARTYEAR")

    for line in inputfile:
        columns = line.split("\t")

        dict = {
            "title": columns[ColumnIndex1],
            "directors": correctedlist(columns[ColumnIndex2]),
            "cast": correctedlist(columns[ColumnIndex3]),
            "genres": columns[ColumnIndex4].split(","),
            "decade": decade(int(columns[ColumnIndex5])),
        }
        result.append(dict)

with open("hw02_output.json", mode="w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
