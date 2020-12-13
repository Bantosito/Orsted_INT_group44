from datetime import datetime, date
import os #Library used to acces system data. In here to acces path of Turbine_Latest.csv
import pandas as pd
import matplotlib.pyplot as plt



#fileName
global filenameTurbine
filenameTurbine = os.path.join ( os.path.dirname(os.path.realpath(__file__)), "Turbine_Latest.csv") 
# We use that to assign a path of the Turbine_Latest.CSV so it is not going to show any problem
# conected to being in different location, or to system not recognizing the file


global turbineOutput
turbineOutput = os.path.join ( os.path.dirname(os.path.realpath(__file__)), "Turbine_Output.csv") 

        
#Task #1 Done
def loadCsv():
    global df
    df = pd.read_csv(filenameTurbine,delimiter=";",decimal =",", parse_dates = ["Date/Time"])      
    #df.info()
#Task #2   Done
def powerDifference(): 
    global df   
    global df2 
    df1 = df["Theoretical_Power "].sub(df["Active_Power"]).to_frame("Power_Difference")
    dupa = {"FaultMsg" : "str"}
    df2 = pd.concat([df, df1], axis = 1).round(2)

    #changing datatype for Task#7
    df2["FaultMsg"] = df2["FaultMsg"].astype("object")

def printPowerDifference():
    global df2
    print("Date              Power Difference")

    dat1 = df2["Date/Time"]
    dat2 = df2["Power_Difference"]

    dat3 = pd.concat([dat1,dat2], axis = 1)
    print(dat3.to_string(index=False, header = False))
    
    print("\n\n Press any button and enter to continue")
    input(">")

# Task #4 Done
def plotTheoreticalActivePower(): 
    global df4
    
    index = ["Theoretical_Power ", "Active_Power"]

    afterDate = df["Date/Time"] >= "2018-05-01 04:00"
    beforeDate = df["Date/Time"] <= "2018-05-01 08:00 "
    between = afterDate & beforeDate
    filtered = df.loc[between]
    filtered ["Date/Time"] = filtered["Date/Time"].dt.strftime("%H:%M")


    index = ["Active_Power","Theoretical_Power "]

    filtered.plot(x="Date/Time", y=index ,rot = 0, kind = "bar",xlabel = "Theoretical Power and Active Power readings gathered on 05-01-2018", ylabel = "Power(kW)")
    plt.title("Theoretical Power and Active Power")
    plt.xticks(rotation = 45)
    plt.show()
    


#Task #5 Done
def sortAndPlotWindSpeed():
    global df2
    global df3
    df3 = df2.copy().sort_values(by=["Wind_Speed"], ascending = False).reset_index(drop=True)
    #df3.info()
    
    #task #6
    
    df3.iloc[1:20].plot(x = "Wind_Speed", y = "Active_Power", rot = 0, kind = "bar",xlabel = "Wind speed (m/s)", ylabel = "Power(kW)" )
    plt.title("Wind speed against Active Power")
    plt.xticks(rotation = 45)
    plt.show()
    
    
#?
#print(df3["Wind_Speed"])
    
#Task #7 taskOutput - can work as task #8
def updateStatusText():
    global df2
    global taskOutput
    taskEight = df2[df2["Error"] > 3]
    
    taskOutput = taskEight[taskEight["FaultMsg"] == True] #taskOutput outputs info for excercise 8 (should change the name)

    for row in taskOutput.index:
        df2.at[row,"Status Text"] = "Turbine not in operation"
        df2.at[row,"FaultMsg"] = "Required"

    #Task8 
def TurbinesWithError():
    print("Turbines with Error >3 and FaultMsg = True are:/n")
    print(taskOutput) 
    print("\n\n Press any button and enter to continue")
    input(">")

#Task #9
def dropRowsOverFifty():
    global taskOutput
    global df2
    taskNine = taskOutput[taskOutput["Error"] > 50]
    for row in taskNine.index:
        df2 = df2.drop([row])
#Task #u3
#printing back to the csv file]

def printToCsv():
    global df2
    df2.to_csv(turbineOutput, index =False,sep=";")
    