from datetime import datetime, date
import os #Library used to acces system data. In here to acces path of Turbine_Latest.csv
import pandas as pd #Main library used for manipulating the data through the Data frame object makes everythink easy! Also great for working with CSV files
import matplotlib.pyplot as plt #Library used for drawing graphs


#fileName
global filenameTurbine
filenameTurbine = os.path.join ( os.path.dirname(os.path.realpath(__file__)), "Turbine_Latest.csv") 
# We use that to assign a path of the Turbine_Latest.CSV so it is not going to show any problem
# conected to being in different location, or to system not recognizing the file

#same as above but for the output file
global turbineOutput
turbineOutput = os.path.join ( os.path.dirname(os.path.realpath(__file__)), "Turbine_Output.csv") 

        
#Task #1 We load the file and assign it as a Data frame
def loadCsv():
    global df
    df = pd.read_csv(filenameTurbine,delimiter=";",decimal =",", parse_dates = ["Date/Time"],error_bad_lines=False).dropna()      
    
#Task #2   We create new Dataframe df1 where we subtract Active_Power from theoretical power and add it to the new power difference class
def powerDifference(): 
    global df   
    global df2 
    df1 = df["Theoretical_Power "].sub(df["Active_Power"]).to_frame("Power_Difference")
    dupa = {"FaultMsg" : "str"}
    df2 = pd.concat([df, df1], axis = 1).round(2)

    #changing datatype for Task#7
    df2["FaultMsg"] = df2["FaultMsg"].astype("object")

    #print out power difference for every readings
def printPowerDifference():
    global df2
    print("Date              Power Difference")

    dat1 = df2["Date/Time"]
    dat2 = df2["Power_Difference"]

    dat3 = pd.concat([dat1,dat2], axis = 1) # connects 2 dataframes into 1. One made from Dates and other from Power Difference
    print(dat3.to_string(index=False, header = False))
    
    print("\n\n Press any button and enter to continue")
    input(">")

# Task #4 Done
def plotTheoreticalActivePower(): 
    global df4
    
    index = ["Theoretical_Power ", "Active_Power"]
    
    #filtrate dates
    afterDate = df["Date/Time"] >= "2018-05-01 04:00"
    beforeDate = df["Date/Time"] <= "2018-05-01 08:00 "
    between = afterDate & beforeDate
    #localize the readings from that date bracket
    filtered = df.loc[between]
    filtered ["Date/Time"] = filtered["Date/Time"].dt.strftime("%H:%M")


    index = ["Active_Power","Theoretical_Power "]
    
    #Set up diagram
    filtered.plot(x="Date/Time", y=index ,rot = 0, kind = "bar",xlabel = "Theoretical Power and Active Power readings gathered on 05-01-2018", ylabel = "Power(kW)")
    plt.title("Theoretical Power and Active Power")
    plt.xticks(rotation = 45)
    #plot the diagram
    plt.show()
    


#Task #5 Plots sorted wind speeds
def sortAndPlotWindSpeed():
    global df2
    global df3
    df3 = df2.copy().sort_values(by=["Wind_Speed"], ascending = False).reset_index(drop=True) #sort value function sorts the wind speeed descending as ascending = false
    
    #task #6 iloc function used for using only 20 strongest winds
    df3.iloc[1:20].plot(x = "Wind_Speed", y = "Active_Power", rot = 0, kind = "bar",xlabel = "Wind speed (m/s)", ylabel = "Power(kW)" )
    plt.title("Wind speed against Active Power")
    plt.xticks(rotation = 45)
    plt.show()
    
    
#Task #7 taskOutput - can work as task #8
def updateStatusText():
    global df2
    global taskOutput
    global taskEight
    
    # First step of filtration, solves requirement number 1 and outputs it to a new dataframe
    taskEight = df2[df2["Error"] > 3]
    
    #Second step of filtration "faultMsg -- true", gets output to taskoutput dataframe
    taskOutput = taskEight[taskEight["FaultMsg"] == True] #taskOutput outputs info for excercise 8 (should change the name)
    
        #For every row from Dataframe of filtrated reading change Status_Text and FaultMsg contents
    for row in taskOutput.index:
        df2.at[row,"Status Text"] = "Turbine not in operation"
        df2.at[row,"FaultMsg"] = "Required"

    #Task8 #prints turbine from filtrated data frame
def TurbinesWithError():
    print("\nTurbines with Error >3 and FaultMsg = True are: \n")
    print(taskOutput) 
    print("\n\n Press any button and enter to continue")
    input(">")

#Task #9 Deleting rows where error exceeeds 50
def dropRowsOverFifty():
    global taskOutput
    global df2
    #filtration
    taskNine = taskEight[taskEight["Error"] > 50]
    #for each index number from that dateFrame delete row number...
    for row in taskNine.index:
        df2 = df2.drop([row])

#paste the most current version of Df2 dataframe to the Turbine_Output.file
def printToCsv():
    global df2
    df2.to_csv(turbineOutput, index =False,sep=";")
    