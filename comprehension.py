"""
Filename: comprehension.py

This program uses list comprehension to iterate through a csv file and create a ist of dictionaries of people
who have heart disease, meaning their 'target' value is 1.0.

Programmer: Jacob Merki
"""
from typing import List, Text, Dict
import csv


def read_csv(filename: Text) -> List[Dict]:
    """
    Reads a csv file, creating a list of dictionaries representing row data from the csv.  Each dictionary should
    contain a key for each column header and the value for that particular row.  You may assume all values will be
    stored as floats.

    :param filename: name of csv file to be processed
    :return: list of dictionaries representing the rows of the csv
    """
    data = []
    with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
        rows = csv.DictReader(csv_file)
        for row in rows:
            subject = dict(row)
            for category in subject:
                subject[category] = float(subject[category])
            data.append(subject)
    return data


def heart_disease(data: List[Dict]) -> List[Dict]:
    result = [subject for subject in data if subject['target'] == 1]
    return result


def main():
    data = read_csv("heart_small.csv")
    result = heart_disease(data)
    for patient in result:
        print(patient)


main()
