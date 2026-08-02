# =========================================================
# Task: File Handling, Automation, and Exception Handling
# Author: Rajshree Potphode
# Description: This script demonstrates reading/writing txt and csv
# files, automating file operations (rename, move, delete), and
# handling errors using try-except blocks.
# =========================================================

import os
import shutil
import csv

print("---- STEP 1: Writing a text file ----")
try:
    file = open("sample.txt", "w")
    file.write("Hello, this is my first file!")
    file.close()
    print("sample.txt created and written successfully.\n")
except IOError as e:
    print(f"Error writing file: {e}\n")


print("---- STEP 2: Reading the text file back ----")
try:
    file = open("sample.txt", "r")
    content = file.read()
    print("Contents of sample.txt:")
    print(content, "\n")
    file.close()
except FileNotFoundError:
    print("sample.txt not found.\n")


print("---- STEP 3: Writing a CSV file ----")
try:
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Aman", 21])
        writer.writerow(["Rajshree", 22])
    print("data.csv created and written successfully.\n")
except IOError as e:
    print(f"Error writing CSV file: {e}\n")


print("---- STEP 4: Reading the CSV file back ----")
try:
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        print("Contents of data.csv:")
        for row in reader:
            print(row)
    print()
except FileNotFoundError:
    print("data.csv not found.\n")


print("---- STEP 5: Demonstrating exception handling ----")
try:
    file = open("not_real.txt", "r")
except FileNotFoundError:
    print("Handled error: 'not_real.txt' does not exist. Program did not crash.\n")


print("---- STEP 6: Automating file operations ----")

try:
    os.rename("sample.txt", "renamed_sample.txt")
    print("Renamed 'sample.txt' to 'renamed_sample.txt'.")
except FileNotFoundError:
    print("File to rename not found.")
except PermissionError:
    print("Permission denied while renaming the file.")

try:
    if not os.path.exists("backup"):
        os.mkdir("backup")
    shutil.move("renamed_sample.txt", "backup/renamed_sample.txt")
    print("Moved 'renamed_sample.txt' into the 'backup' folder.")
except FileNotFoundError:
    print("File to move not found.")
except PermissionError:
    print("Permission denied while moving the file.")

try:
    os.remove("data.csv")
    print("Deleted 'data.csv'.")
except FileNotFoundError:
    print("File to delete not found.")
except PermissionError:
    print("Permission denied while deleting the file.")

print("\n---- Script finished successfully ----")
