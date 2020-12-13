import os
import FileParser as fp #we are loading other file containing the rest of code as FP so it will be called as "fp." in the future

# Cls is a function that uses clear command in terminal which wipes the contents leaving the comand prompt blank
def cls():
    os.system('cls' if os.name=='nt' else 'clear') # Easy if statement recognising the system you are using and applying appropriate command (cks for windows/clear for "linux/macos")
cls()

cmdPrompt = ">"

#loading csv File
fp.loadCsv()
fp.powerDifference()
fp.updateStatusText()

def mainMenu():
    print("==========================================")        
    print("              CHOOSE AN OPTION            ")
    print("--------------------------------------------")
    print("Enter the number to select the function you want to perform")
    print("_________________________________________")
                    # Loop here so that if the userInput is unexpected, it will ask again.
                    # The loop will exit using 'return' statements.
    print("1: Print the Power_Difference. "
    + "\n2: Plot the bar graph of Theoretical and Active Power"
    + "\n3: Plot a graph of Wind Speed and Active Power"
    + "\n4: Print all the information of Turbines with Error >3 and FaultMsg True\n"
    + "\n0: Exit the application and update the 'Turbine_Output.csv' file")
    print("============================================")

    userInput = input(cmdPrompt)
                    # Based on userInput we determine what to do next
    #cls()
    if userInput == "1": # Choose from menu
                        # Returning a method means that we are ending what left in this
                        #  method and continuing it with the following
        fp.printPowerDifference()
        cls()
        mainMenu()
    elif userInput == "2": 
        fp.plotTheoreticalActivePower()
        cls()
        mainMenu()
    elif userInput == "3":
        fp.sortAndPlotWindSpeed()
        cls()
        mainMenu()
    elif userInput == "4":
        fp.TurbinesWithError()
        cls()
        mainMenu()
    elif userInput == "q" or userInput == "0" : # Exit the loop
        fp.printToCsv()
        cls()
        exit()
    else:
        cls()
        print("Unexpected input.")
        mainMenu()
        
        
        
print("\n======================================\n")
print("       Files Loaded correctly \n")
print("======================================\n\n")
mainMenu()