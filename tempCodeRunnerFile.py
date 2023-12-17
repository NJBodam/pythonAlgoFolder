# prj-gui.py: GUI

import PySimpleGUI as sg
import regex as re

def getTimeInMin(timestr):
    # checks if timestr is valid time and if True returns a timestamp in min
    # if not 0 is returned
    pattern = r"(2[0-3]|(0|1)?[0-9])\:([0-5]?[0-9])" # group1 and group3
    matchobj = re.match(pattern,timestr)
    if matchobj != None and len(matchobj)>3:
        return int(matchobj.group(1))*60 + int(matchobj.group(3))
    else: return 0
    
def getDateInMin(datestr):
    # checks if datestr is valid date (simplified calendar)
    # and if True returns a timestamp in min else 0 is returned
    pattern = r"([0-9]{2,4})\-(1[0-2]|0?[1-9])\-([1-2][0-9]|3[0-1]|0?[1-9]|)" # groups1-3
    matchobj = re.match(pattern,datestr)
    if matchobj != None and len(matchobj)>2:
        (y,m,d) = int(matchobj.group(1)), int(matchobj.group(2))-1, int(matchobj.group(3))-1
        return 60*24 * (int(d) +30*(int(m)+12*int(y))) 
    else:
        return 0
    
def getTimefromStamp(stamp):
    factor = (1,12,30,24,60)
    timelist = [0]*5 # seq of 5 values for (year, month, day, hour, minute)
    for i in range(len(timelist)-1,-1,-1):
        timelist[i] = stamp % factor[i]
        stamp //= factor[i]
    timelist[1] += 1 # month
    timelist[2] += 1 # day
    timelist[0] = stamp
    return tuple(timelist) #(year, month, day, hour, minute)

def niceDateTimeStr(tmtuple):
    # new alternatives for formatting strings
    # "%"<number of digits or letters><data type of the symbol>  and in the end a % with the tuple of values
    return "%4i-%2i-%2i %2i:%2i" % tmtuple
    
def enterSensors():
    # opens a window to ask for a sensor specification
    # returns a list of the entered sensors  (sensor name, unit, timestep and timestamp)
    
    layout = [
          [
            sg.Text("Name of the sensor: ", size = (35,1)),
            sg.In( enable_events=True, key="-SENSOR-", size = (10,1))
          ],
          [
            sg.Text("Unit of the sensor:    ", size = (35,1)),
            sg.In(enable_events=True, key="-UNIT-",size = (10,1))
          ],
          [ sg.Text("Time intervall (in min.): ", size = (35,1)),
            sg.In(enable_events=True, key="-STEP-",size = (10,1)),
            ],
          [
            sg.Text("Date of the first measurement (yyyy-mm-dd):    ", size = (35,1)),
            sg.In(enable_events=True, key="-DATE-", size=(10, 1)),
          ],
          [
            sg.Text("Time of the first measurement (hh:mm):    ", size = (35,1)),
            sg.In(enable_events=True, key="-TIME-", size=(10, 1)),
          ],
          [sg.Button("Finish"), sg.Button("Add next Sensor")]
        ]
    mywindow = sg.Window("Sensor Data App: Sensor definition", layout)

    sensors = {}
    while True:
        event, values = mywindow.read()
        if event == sg.WIN_CLOSED: # End program if user closes window or
            return sensors
        elif event == "Finish" or event == "Add next Sensor":
            # Store Values in dictionary
            sensorname = values["-SENSOR-"] #
            sensorunit = values["-UNIT-"] #
            sensorstep = int(values["-STEP-"]) # 
            timestamp = getTimeInMin(values["-TIME-"]) + getDateInMin(values["-DATE-"])
            if sensorname != "" :
                sensors[sensorname]=[sensorname,sensorunit,sensorstep,timestamp]
            if event == "Finish":
                mywindow.close()
                break
            else: #Clear the fields
                for key in values:
                    mywindow[key].update('')
    return sensors

def enterMeasurements(sensors):     
    valueList=[]
    names = [v for v in sensors]
    layout = [
          [
            sg.Text("Name of the sensor: "),
            sg.Combo(names, expand_x=True, enable_events=True,  readonly=False, key='-SENSOR-')
          ],
          [
            sg.Text("Observation time:"),
            sg.In("Unknown", key="-TIME-"),
          ],
          [
            sg.Text("value:    "),
            sg.In(enable_events=True, key="-VALUE-", size=(15, 1)),
          ],
        [sg.Button("Finish"),
          sg.Button("Add next Value")]
        ]
    mywindow = sg.Window("Sensor Data App", layout)
    newValue = None
    sensorname= names[0]
    while True:
        event, values = mywindow.read()
        print(event, values)
        if event == sg.WIN_CLOSED: # End program if user closes window or
            return valueList
        elif event == "-SENSOR-": # presses the OK button
            sensorname = values["-SENSOR-"] #
            newTime = getTimefromStamp(sensors[sensorname][3]) # Put sensor time in input window
            mywindow['-TIME-'].update( niceDateTimeStr(newTime))
        elif event == "Finish" or event == "Add next Value":
            # Store Values
            sensorname = values["-SENSOR-"] #
            newTime = getTimefromStamp(sensors[sensorname][3])
            mywindow['-TIME-'].update(newTime)
            # Compute and store the time of the next measurement
            sensors[sensorname][3] += sensors[sensorname][2]
            newValue = int(values["-VALUE-"])
            if newValue != None:
                valueList.append((sensorname, newValue, newTime))
            if event == "Finish":
                mywindow.close()
                break
            else: # prepare for "add new value"
                #This will clear the fields
                for key in values:
                    mywindow[key].update('')
    return valueList

if __name__ == "__main__":
    sg.set_options(font=('Arial Bold', 9))
    sg.theme("BlueMono") # look up themes by calling sg.theme_previewer()

    sensors = enterSensors()
    if sensors !={}:
        values = enterMeasurements(sensors)
