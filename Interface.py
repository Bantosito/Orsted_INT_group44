import os #library used for cls() function

import FileParser as fp #we are loading other file containing the rest of thecode as FP so it will be called as "fp." in the future

# Cls is a function that uses clear command in terminal which wipes the contents leaving the comand prompt blank (clearing terminal window)
def cls():
    os.system('cls' if os.name=='nt' else 'clear') # Easy if statement recognising the system you are using and applying appropriate command (cks for windows/clear for "linux/macos")
cls()

cmdPrompt = ">"

#executing functions that correspond to different tasks, those happend first after starting the program

fp.loadCsv()  #task 1 function loads csv
fp.powerDifference() #task 2 counting power difference and creating corresponding collumn
fp.updateStatusText() # task 7 updates status of turbines with error >3  and FaultMsg = true
fp.dropRowsOverFifty() #task 9 deletes rows where error > 50

#mainMenu fuction leads back to menu and waits for user input 
def mainMenu(): 
    
    #drawing
    print("==========================================")        
    print("              CHOOSE AN OPTION            ")
    print("--------------------------------------------")
    print("Enter the number to select the function you want to perform")
    print("_________________________________________")                    
    print("1: Print the Power_Difference. "
    + "\n2: Plot the bar graph of Theoretical and Active Power"
    + "\n3: Plot a graph of Wind Speed and Active Power"
    + "\n4: Print all the information of Turbines with Error >3 and FaultMsg True\n"
    + "\n0: Exit the application and update the 'Turbine_Output.csv' file with new data")
    print("============================================")

    userInput = input(cmdPrompt)
    # Based on userInput we determine what to do next
                    
    if userInput == "1": 
        fp.printPowerDifference() #self explanatory
        cls()
        mainMenu()
    elif userInput == "2": 
        fp.plotTheoreticalActivePower() #self explanatory
        cls()
        mainMenu()
    elif userInput == "3":
        fp.sortAndPlotWindSpeed() #self explanatory
        cls()
        mainMenu()
    elif userInput == "4":
        fp.TurbinesWithError() #self explanatory
        cls()
        mainMenu()
    elif userInput == "q" or userInput == "0" : # Exit the loop and save the changes to the TURBINE_OUTPUT.CSV file
        fp.printToCsv()
        cls()
        exit()
    else:
        cls()
        print("Unexpected input.")
        mainMenu()
        # Loops here so if the userInput is unexpected(wrong), it will ask again.
        
        
        
print("\n======================================")
print("       Files Loaded correctly \n")
print("       Power_Difference collumn created \n")
print("       Cells of turbines with errors updated\n")
print("       Turbines with Error > 50 deleted")
print("======================================\n")

#execute MainMenu Function
mainMenu() 
