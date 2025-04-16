#CIS-117 Lab4
#This module/python codes takes the CSV file "country_full.csv" and separates countries
#by region and generates one CSV file for each region (e.g. Asia, Europe, Oceania).
#Jason Chan
#I worked by myself for Partner Lab 3


import csv

def country_csv(file_name):
    """This function takes a CSV file input and does the following:
    1. Reads the CSV file (with headers) and splits the data into their own individual dictionaries.
    2. Generates and writes a CSV file for each dictionary, generating a file per region."""

    try:
        #create a blank dictionary "countries" containing one key (name) and one value (region).
        #note that some names (e.g. Antarctica) don't have a region specified. Assign value as "none".
        countries = {}
        Asia = {}
        Europe = {}
        Africa = {}
        Oceania = {}
        Americas = {}
        No_region_specified = {}

        header = ["name", "region"]

        with open("country_full.csv", mode = "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row["region"] != "":
                    region = row["region"]
                    name = row["name"]
                    countries[name] = region
                elif row["region"] == "":
                    region = "none"
                    name = row["name"]
                    countries[name] = region

#Use a for-loop to iterate over the "country" dictionary and store the name in respective
#regions dictionary (e.g. Afghanistan = Asia >>> Should be placed in dictionary "Asia")
        for key, value in countries.items():
            if value == "Asia":
                Asia[key] = value
            elif value == "Europe":
                Europe[key] = value
            elif value == "Africa":
                Africa[key] = value
            elif value == "Oceania":
                Oceania[key] = value
            elif value == "Americas":
                Americas[key] = value
            else:
                No_region_specified[key] = value

#use the csv writer module to convert each created dictionary (e.g. Asia, Oceania, Americas, etc)
#into its own CSV file.

        with open("Asia.csv", mode = "w", newline = "") as Asia_file:
            Asia_writer = csv.writer(Asia_file)
            Asia_writer.writerow(header)
            for key, value in Asia.items():
                Asia_writer.writerow([key, value])

        with open("Europe.csv", mode = "w", newline = "") as Europe_file:
            Europe_writer = csv.writer(Europe_file)
            Europe_writer.writerow(header)
            for key, value in Europe.items():
                Europe_writer.writerow([key, value])

        with open("Africa.csv", mode = "w", newline = "") as Africa_file:
            Africa_writer = csv.writer(Africa_file)
            Africa_writer.writerow(header)
            for key, value in Africa.items():
                Africa_writer.writerow([key, value])

        with open("Oceania.csv", mode = "w", newline = "") as Oceania_file:
            Oceania_writer = csv.writer(Oceania_file)
            Oceania_writer.writerow(header)
            for key, value in Oceania.items():
                Oceania_writer.writerow([key, value])

        with open("Americas.csv", mode = "w", newline = "") as Americas_file:
            Americas_writer = csv.writer(Americas_file)
            Americas_writer.writerow(header)
            for key, value in Americas.items():
                Americas_writer.writerow([key, value])

        with open("No_Region_Specified.csv", mode = "w", newline = "") as No_region_specified_file:
            No_region_specified_writer = csv.writer(No_region_specified_file)
            No_region_specified_writer.writerow(header)
            for key, value in No_region_specified.items():
                No_region_specified_writer.writerow([key, value])

    except IOError as e:
        print(f"An I/O error occured: {e}")

    except FileNotFoundError as e:
        print(f"An error occurred: {e}")

    except PermissionError as e:
        print(f"You do not have permission to read the file: {e}")


print(country_csv("country_full.csv"))
