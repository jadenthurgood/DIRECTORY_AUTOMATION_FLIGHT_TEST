import os
import pathlib
import numpy as np
from datetime import date
import time
#Creates a directory for flight test data, media, and backups

#Get Todays date information
todays_date = date.today()
current_year = str(todays_date.year) + "-"
current_month = str(todays_date.month) + "-"
current_day = str(todays_date.day) + "_"

#Create Strings for the folders you are going to create
preflight_folder = "Preflight"
flight_data_folder = "Flight_Data"
Onboard_folder = "ONBOARD"
GCS_folder = "GCS"
Media_folder = "Media"

#Get the programs name
program_name = str(input("\nEnter the name of the program: ")) + "_Flights"

#ask if the user would like to use today's date for the folder naming or if they want to manually input the date
use_todays_date = int(input("\nWould you like to used today's date to name the aircraft folder? (Type 1 for yes and 0 for no): "))

#set the use_date based on if the user is going to manually input a date, or used today's date
if use_todays_date == True: #today's date
    use_year = current_year
    use_month = current_month
    use_day = current_day
else: #manually input a date
    use_year = str(input("\nEnter the year (format: xxxx): ")) + "-"
    use_month = str(input("Enter the month (format: xx): ")) + "-"
    use_day = str(input("Enter the day (format: xx):  ")) + "_"

#Get the drive that the program is being run from
current_directory = str(pathlib.Path().resolve())

#Save the new directories at the directory where the program was run
current_drive = current_directory

#Save the directory at the drive level
""" current_drive = current_directory[0:3] """


#check to see if the directory exists before creating it
path_exists = os.path.isdir(os.path.join(current_drive, program_name))

if path_exists == True:
    new_path = os.path.join(current_drive, program_name)
else:
    #Make the Program Name Folder
    new_path = os.path.join(current_drive, program_name)
    os.makedirs(new_path)

#Ask the user if they would like to set up multiple ships or just one.
single_ship = int(input("\nWould you like to set up 1 directory for one ship? \nOr multiple directories for multiple ships? (Type 1 for one ship and 0 for multiple): "))

if single_ship == False:
    print("\n\nThis part of the program will create multiple directories over a range of aircraft numbers.")
    sequential_ships = int(input("\nAre the ships you are setting up in sequential order (Ex: Ship 01, Ship 02, Ship 03...)?\nType 1 for yes or 0 for no: "))
    
    if sequential_ships == False:
        ships_list = [tail for tail in input("\nPlease enter the ship numbers separated by spaces (Ex: ALE-112 ALE-94 ALE-54): ").split()]
        
        #make a directory for each of the user specified ships
        for i in range(len(ships_list)):
            ship_number = ships_list[i]

            #Make the Date and Ship Folder 
            new_path_2 = os.path.join(new_path,(use_year + use_month + use_day + ship_number))
            os.makedirs(new_path_2)

            #Make the Preflight Folder
            new_path_3 = os.path.join(new_path_2,preflight_folder)
            os.makedirs(new_path_3)

            #Make the Flight Data folder
            new_path_4 = os.path.join(new_path_2,flight_data_folder)
            os.makedirs(new_path_4)

            #Make the ONBOARD folder
            new_path_5 = os.path.join(new_path_4,Onboard_folder)
            os.makedirs(new_path_5)

            #Make the GCS folder
            new_path_6 = os.path.join(new_path_4,GCS_folder)
            os.makedirs(new_path_6)

            #Make the Media folder
            new_path_7 = os.path.join(new_path_4,Media_folder)
            os.makedirs(new_path_7)

            print(ship_number + " directory created")
        pass

    else: #The ship numbers are in sequential order

        print("\nThe user will input the lowest ship number in the range, and the highest\n")

        start_ship_number = int(input("Enter the lowest ship number: "))
        end_ship_number = int(input("Enter the hightest ship number: "))

        for i in np.arange(start_ship_number,end_ship_number + 1):
            ship_number = "Ship" + str(i)
        
            #Make the Date and Ship Folder
            new_path_2 = os.path.join(new_path,(use_year + use_month + use_day + ship_number))
            os.makedirs(new_path_2)

            #Make the Preflight Folder
            new_path_3 = os.path.join(new_path_2,preflight_folder)
            os.makedirs(new_path_3)

            #Make the Flight Data folder
            new_path_4 = os.path.join(new_path_2,flight_data_folder)
            os.makedirs(new_path_4)

            #Make the ONBOARD folder
            new_path_5 = os.path.join(new_path_4,Onboard_folder)
            os.makedirs(new_path_5)

            #Make the GCS folder
            new_path_6 = os.path.join(new_path_4,GCS_folder)
            os.makedirs(new_path_6)

            #Make the Media folder
            new_path_7 = os.path.join(new_path_4,Media_folder)
            os.makedirs(new_path_7)

            print(ship_number + " directory created")

else: #The user just wants to create one ship directory

    ship_number = "Ship" + str(input("\nEnter the ship number: "))

    #Make the Date and Ship Folder
    new_path_2 = os.path.join(new_path,(use_year + use_month + use_day + ship_number))
    os.makedirs(new_path_2)

    #Make the Preflight Folder
    new_path_3 = os.path.join(new_path_2,preflight_folder)
    os.makedirs(new_path_3)

    #Make the Flight Data folder
    new_path_4 = os.path.join(new_path_2,flight_data_folder)
    os.makedirs(new_path_4)

    #Make the ONBOARD folder
    new_path_5 = os.path.join(new_path_4,Onboard_folder)
    os.makedirs(new_path_5)

    #Make the GCS folder
    new_path_6 = os.path.join(new_path_4,GCS_folder)
    os.makedirs(new_path_6)

    #Make the Media folder
    new_path_7 = os.path.join(new_path_4,Media_folder)
    os.makedirs(new_path_7)

    print(ship_number + " directory created")

#make sure their directory is where it should be and let the user know
dir_exists = os.path.isdir(os.path.join(current_drive, program_name))
if dir_exists:
    print("\nYour directory was created in the location this program was run from, and is named: ", program_name)
else:
    pass

#pause the program for 15 seconds to give the user time to read any output messages to the console
print("\nProgram has completed")
time.sleep(15)