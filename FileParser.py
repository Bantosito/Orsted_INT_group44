from datetime import datetime, date
from turbineClass import Turbine
import csv #Library used to recognize csv files
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

#creating dictionary of data connected to each Turbine (windmill)
global turbineData
turbineData = {}


#Function for opening

def loadTurbine():
    file = open(filenameTurbine, "r")
    allTurbines = list(csv.reader(file, delimiter = ";"))
    #print(allTurbines)
    rowCount = 0
    global turbineId 
    turbineId = 0
    
    for atribute in allTurbines:
        if rowCount == 0:
            newTurbine = newTurbine = Turbine(date_time = atribute[0],
            active_power = atribute[1],
            wind_speed = atribute[2],
            theoretical_power = atribute[3],
            wind_direction = atribute[4],
            service = atribute[5],
            error = atribute[6],
            faultMsg = atribute[7],
            statusText = atribute[8])
            turbineData[turbineId] = newTurbine
            #print(turbineData)
            rowCount += 1
            turbineId  += 1

        else:
            atribute[1] = str(atribute[1]).replace(",", ".")
            atribute[2] = str(atribute[2]).replace(",", ".")
            atribute[3] = str(atribute[3]).replace(",", ".")
            newTurbine = Turbine(date_time = datetime.strptime(atribute[0], '%d %m %Y %H:%M'),
            active_power = atribute[1],
            wind_speed = atribute[2],
            theoretical_power = atribute[3],
            wind_direction = atribute[4],
            service = atribute[5],
            error = atribute[6],
            faultMsg = atribute[7],
            statusText = atribute[8])
            turbineData[turbineId] = newTurbine
            turbineId  += 1
            

def turbineDifference():
    for key, value in turbineData.items():
        if key == 0:
            pass
        else:
            theoretical = turbineData[key].theoretical_power
            active = turbineData[key].active_power
            
            theoretical = float(theoretical) 
            active = float(active) 
            difference = theoretical - active 
        
            difference = round(difference,2) 
            
            turbineData[key].difference =  difference


def writeTurbine():
    file = open(turbineOutput, "w+")
    writer = csv.writer(file, delimiter = ";")
    
    for key, value in turbineData.items():
        dataList = [value.date_time, value.active_power, value.wind_speed, value.theoretical_power, value.wind_direction,value.service, value.error, value.faultMsg, value.statusText, value.difference]
        writer.writerow(dataList)
        
#def barGraph():
#    for key, value in turbineData.items():
#        if key == 0:
#            pass
#        else:
#            #if turbineData[key].date_time()

#1
df = pd.read_csv(filenameTurbine,delimiter=";",decimal =",", parse_dates = ["Date/Time"])      
#df.info()
#2
df1 = df["Theoretical_Power "].sub(df["Active_Power"]).to_frame("Power_Difference")
dupa = {"FaultMsg" : "str"}
df2 = pd.concat([df, df1], axis = 1).round(2)

#changing datatype for #7
df2["FaultMsg"] = df2["FaultMsg"].astype("object")


#5
df3 = df2.copy().sort_values(by=["Wind_Speed"], ascending = False).reset_index(drop=True)
df3.info()
#6
df3.iloc[1:20].plot(x = "Wind_Speed", y = "Active_Power", rot = 0, kind = "bar",xlabel = "Wind speed (m/s)", ylabel = "Power(kW)" )
plt.title("Wind speed against Active Power")
plt.xticks(rotation = 45)
#plt.show()

#?
print(df3["Wind_Speed"])
#4
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
#plt.show()
#7 taskOutput - can work as task #8
taskEight = df2[df2["Error"] > 3]
taskOutput = taskEight[taskEight["FaultMsg"] == True]

for row in taskOutput.index:
    df2.at[row,"Status Text"] = "Turbine not in operation"
    df2.at[row,"FaultMsg"] = "Required"

#print(list)
print(taskOutput)
#9
taskNine = taskOutput[taskOutput["Error"] > 50]
print(taskNine)
for row in taskNine.index:
    df2 = df2.drop([row])
#3
#printing back to the csv file
df2.to_csv(turbineOutput, index =False)
    
#loadTurbine()
#turbineDifference()
#writeTurbine()
    