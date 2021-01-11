
# Software Development Kits (SDKs)
import smartsheet
import os
from datetime import *
from pprint import pprint

from simple_smartsheet import Smartsheet
from simple_smartsheet.models import Sheet, Column, Row, Cell, ColumnType

from tkinter import *

try:
    # Python3
    import tkinter as tk
except ImportError:
    # Python2
    import Tkinter as tk

import plotly.graph_objects as go

import numpy as np
#===============================================
global sDate, eDate
#===============================================
Label_width = "20"          #Width of the label
Font = "Times New Roman"    #The font shown on the GUI
Font_size = "11"            #The font size shown on the GUI
Label_bd = "2"              #Border thickness

Label_height = "1"          #Height of label
#===============================================



# Token
TK = 'hj8lpncr2xthejeb65h2bn24a3';

# Initialize client
smartsheet_client = smartsheet.Smartsheet(TK);

# Make sure we don't miss any errors
smartsheet_client.errors_as_exceptions(True)

# assume user
smartsheet_client.assume_user("wwei@briskheat.com")


#TOKEN = os.getenv('HOME')
#print(TOKEN)
SHEET_NAME = '20210104Test'
smartsheet = Smartsheet(TK)

'''
# create a new Sheet
new_sheet_skeleton = Sheet(
    name = SHEET_NAME,
    columns = [
        Column(primary=True, title="Full Name", type=ColumnType.TEXT_NUMBER),
        Column(title = "Number of read books", type=ColumnType.TEXT_NUMBER),
        Column(title = "Birth date", type=ColumnType.DATE),
        Column(title = "Library member", type=ColumnType.CHECKBOX),
    ],
)
'''

#===========================Functions generating labels
def gen_Label(arg, r, c):

    Label(gui, text = arg, font=(Font, Font_size),
          height = Label_height, width = Label_width, bd=Label_bd,
          relief="groove").grid(row = r, column = c, sticky=NSEW)
#===========================
def FirstYieldingRate():

    FindDataRange()

    EstimatePerCustomer()

#===========================
def FindDataRange():

    dateFormat();
    print(sDate, eDate);

#===========================
def EstimatePerCustomer():
    '''
    In this section, the funciton will sort out the data within Start Date, sDate, and Ending Date, eDate.
    '''


    #pprint(sheet.as_list())

    '''
    i1 = IntVar(); #Reading checkbox of "AMAT" starts with UAPM, APM

    i2 = IntVar(); #Reading check box of "ASM" starts with UASM

    i3 = IntVar(); #Reading check box of "TKBS" starts with UTKE

    i4 = IntVar(); #Reading check box of "LAM" stars with UEBR

    UTET (TEL in India)

    UEGS (Entegris)
    '''
    global Result
    Result = {};

    if (i1.get() == True):
        print('AMAT');
        Result['UAPM'] = sortByPartNum("UAPM");
        Result['APM'] = sortByPartNum("APM");

    if (i2.get() == True):
        print('ASM')
        Result['UASM']  = sortByPartNum("UASM")

    if (i3.get() == True):
        print('TKBS')
        Result['UTKE'] = sortByPartNum("UTKE")

    if (i4.get() == True):
        print('LAM')
        Result['UEBR'] = sortByPartNum("UEBR")

    #print(Result)

    j = 0
    gen_Label('Custmoer', row_ini+11+j, column_ini); #Customer's name
    gen_Label('Passing test count', row_ini+11+j, column_ini+1); # Passing Count
    gen_Label('Total test count', row_ini+11+j, column_ini+2); # Passing Count
    gen_Label('First pass yield rate (%)', row_ini+11+j, column_ini+3); # Passing Count
    j += 1;
    for i in Result.keys():
        print(i);
        gen_Label(i, row_ini+11+j, column_ini); #Customer's name
        gen_Label(Result[i][0], row_ini+11+j, column_ini+1); # Passing Count
        gen_Label(Result[i][1], row_ini+11+j, column_ini+2); # Passing Count
        gen_Label((Result[i][0]/Result[i][1]*100), row_ini+11+j, column_ini+3); # Passing Count
        j += 1;
    #print( len(sheet.rows) );

    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    fig.write_html('first_figure.html', auto_open=True)

#===========================
def sortByPartNum(nameInput):

    sheets = smartsheet.sheets.list();
    #pprint(sheets);
    sheet = smartsheet.sheets.get('UTR - Record20201022')
    #pprint(sheet.__dict__)
    full_PartNum_name_Col = sheet.get_column("Part Number")
    #pprint(full_PartNum_name_Col.__dict__)
    #pprint(type(sheet.rows))

    CountTotal = 0;
    CountSuccess = 0;

    for row in sheet.rows:
        full_name = str( row.get_cell("Part Number").value );
        full_TType = str( row.get_cell("Test Type").value);
        full_Status = str( row.get_cell("Status").value);
        full_PT = str( row.get_cell('Passed 1St Test').value );

        rowDate = ( row.get_cell('Request Date').value );

        #print(str(type(rowDate)))
        if (str(type(rowDate)) == "<class 'datetime.date'>"): #Only process datetime.date type object
            #print('datetime.date')
            if ((rowDate - testsDate).days>0) and ((testeDate - rowDate).days > 0):

                print((rowDate - testsDate).days, (testeDate - rowDate).days)
                if full_Status.startswith("Complete") and full_TType.startswith("Design Validation (AMAT, ASM, TKBS, LAM...)"):
                    if full_name.startswith(nameInput):
                        #print(full_name, nameInput)
                        #print(row.get_cell("Test 1").value)
                        if full_PT.startswith("True"):
                            #print(row.get_cell('Passed 1St Test').value)
                            CountSuccess += 1;

                        CountTotal += 1;

    print('Count of success of {0} is {1}'.format(nameInput, CountSuccess))
    print('Count of {0} is {1}'.format(nameInput, CountTotal))
    return [CountSuccess, CountTotal]

#===========================
def GeneratingCustomerCheckBox():

    global i1, i2, i3, i4;

    i1 = IntVar(); #Reading checkbox of "AMAT"
    i2 = IntVar(); #Reading check box of ASM
    i3 = IntVar(); #Reading check box of TKBS
    i4 = IntVar(); #Reading check box of LAM
    #
    Label(gui, text = '', height = Label_height, bg = "grey", fg = "black",
    bd=Label_bd).grid(row = row_ini + 3, column = column_ini, sticky=NSEW, columnspan=7)

    gen_Label("Customer(s)", row_ini + 4, column_ini)

    c1 = Checkbutton(gui, text = 'AMAT', variable = i1).grid(row = row_ini+5, column = column_ini, sticky=NSEW);
    c2 = Checkbutton(gui, text = 'ASM', variable = i2).grid(row = row_ini+6 , column = column_ini, sticky=NSEW);
    c3 = Checkbutton(gui, text = 'TKBS', variable = i3).grid(row = row_ini+7 , column = column_ini, sticky=NSEW);
    c4 = Checkbutton(gui, text = 'LAM', variable = i4).grid(row = row_ini+8, column = column_ini, sticky=NSEW);

#===========================
def toggle():
    '''
    use
    t_btn.config('text')[-1]
    to get the present state of the toggle button
    '''
    if t_btn.config('text')[-1] == 'True':
        t_btn.config(text='False')
        print ("pressed true")
    else:
        t_btn.config(text='True')

#===========================
def dateFormat():
    global sDate, eDate, testsDate, testeDate;
    #    print(var_gas.get())

    #testsDate = datetime(int(Start_YY.get()), int(Start_MM.get()), int(Start_DD.get()));
    #testeDate = datetime(int(End_YY.get()), int(End_MM.get()), int(End_DD.get()));

    try:
        if (int(Start_YY.get()) > int(End_YY.get())):
            sDate = 'Ending year should be After starting year';
            eDate = 'Ending year should be After starting year';
#            testsDate = sDate;
        #    testeDate = sDate;

        elif (int(Start_YY.get()) == int(End_YY.get())) and (int(Start_MM.get()) > int(End_MM.get())):
            sDate = 'Ending month should be After starting month';
            eDate = 'Ending month should be After starting month';
#            testsDate = sDate;
        #    testeDate = sDate;

        elif (int(Start_YY.get()) == int(End_YY.get())) and (int(Start_MM.get()) == int(End_MM.get())) and (int(Start_DD.get()) > int(End_DD.get())):
            sDate = 'Ending day should be After starting day';
            eDate = 'Ending day should be After starting day';
#            testsDate = sDate;
        #    testeDate = sDate;

        else:
            sDate = str(Start_MM.get()) + '/' + str(Start_DD.get()) + '/' + str(Start_YY.get())[-2:];
            eDate = str(End_MM.get()) + '/' + str(End_DD.get()) + '/' + str(End_YY.get())[-2:];

            testsDate = date(int(Start_YY.get()), int(Start_MM.get()), int(Start_DD.get()));
            testeDate = date(int(End_YY.get()), int(End_MM.get()), int(End_DD.get()));

    except:
        sDate = "Problem occurred! Please send question to Email wwei@briskheat.com";
        eDate = sDate;
        testsDate = sDate;
        #testeDate = sDate;

    Label(gui, text = str(sDate), font=(Font, Font_size), height = Label_height, width = Label_width, bd=Label_bd, relief="groove").grid(row = row_ini + 1, column = column_ini + 4, sticky=NSEW)

    Label(gui, text = str(eDate), font=(Font, Font_size), height = Label_height, width = Label_width, bd=Label_bd, relief="groove").grid(row = row_ini + 2, column = column_ini + 4, sticky=NSEW)

#===========================
def GeneratingDateInput():

    global row_ini, column_ini;
    global Start_YY, Start_MM, Start_DD, End_YY, End_MM, End_DD;

    row_ini = 0;
    column_ini = 0;

    def conv(X):
        return [str(int(X[i])) for i in range(0, len(X))]

    Yi = 2020;
    Ye = 2050;
    YY = conv(np.linspace(Yi, Ye, (Ye-Yi)-1));                                              #List of year
    MM = conv(np.linspace(1, 12, 12));    #List of month
    DD = conv(np.linspace(1, 31, 31))                                                             #List of day

    #=======================
    YY_but = tk.Button(gui, text='Year', font=(Font, Font_size), bd=Label_bd, width = Label_width,
              relief="groove", fg = "black", bg = "light grey", command=''
              ).grid(row = row_ini , column = column_ini + 1, sticky=NSEW)

    MM_but = tk.Button(gui, text='Month', font=(Font, Font_size), bd=Label_bd, width = Label_width,
              relief="groove", fg = "black", bg = "light grey", command=''
              ).grid(row = row_ini , column = column_ini + 2, sticky=NSEW)

    DD_but = tk.Button(gui, text='Day', font=(Font, Font_size), bd=Label_bd, width = Label_width,
                  relief="groove", fg = "black", bg = "light grey", command=''
                  ).grid(row = row_ini , column = column_ini + 3, sticky=NSEW)

    #=======================
    DefaultTime();
    '''
        Today = date.today();
        Pri_90_days = Today - timedelta(days = 90);
    '''
    #=======================
    #Label "Starting date"
    gen_Label("Starting date", row_ini + 1 , column_ini)

    # The drop menu of starting year
    Start_YY = StringVar(gui)                       # Create a Tkinter variable, call the corresponding constructor
    #Start_YY.set( YY[0] )                          # Default year is "2020"
    Start_YY.set( Pri_90_days.year )                # Default year is Prior 90 days
    SYDM = OptionMenu(gui, Start_YY, *YY)           # generate the drop down menu
    SYDM.grid(row = row_ini + 1, column = column_ini + 1, sticky=NSEW)
    SYDM.config(bg = "white", width = Label_width)

    # The drop menu of starting month
    Start_MM = StringVar(gui)                       # Create a Tkinter variable, call the corresponding constructor
    #Start_MM.set( MM[0] )                          # Default month is "1"
    Start_MM.set( Pri_90_days.month )               # Default month
    SMDM = OptionMenu(gui, Start_MM, *MM)           # generate the drop down menu
    SMDM.grid(row = row_ini + 1, column = column_ini + 2, sticky=NSEW)
    SMDM.config(bg = "white", width = Label_width)

    # The drop menu of starting day
    Start_DD = StringVar(gui)                       # Create a Tkinter variable, call the corresponding constructor
    #Start_DD.set( DD[0] )                          # Default date
    Start_DD.set( Pri_90_days.day )                           # Default date
    SDDM = OptionMenu(gui, Start_DD, *DD)           # generate the drop down menu
    SDDM.grid(row = row_ini + 1, column = column_ini + 3, sticky=NSEW)
    SDDM.config(bg = "white", width = Label_width)

    # The format of starting date be
    #===========================Estimate Enthalpy

    gen_Label(" ", row_ini + 1, column_ini + 4)

    #Label "Ending date"
    gen_Label("Ending date", row_ini + 2 , column_ini)

    # The drop menu of ending year
    End_YY = StringVar(gui)                         # Create a Tkinter variable, call the corresponding constructor
    #End_YY.set( YY[0] )                            # Default year is "2020"
    End_YY.set( Today.year )                        # Default year is current year
    EYDM = OptionMenu(gui, End_YY, *YY)             # generate the drop down menu
    EYDM.grid(row = row_ini + 2, column = column_ini + 1, sticky=NSEW)
    EYDM.config(bg = "white", width = Label_width)

    # The drop menu of starting month
    End_MM = StringVar(gui)                         # Create a Tkinter variable, call the corresponding constructor
    #End_MM.set( MM[0] )                            # Default month is "1"
    End_MM.set( Today.month )                       # Default month is current month
    EMDM = OptionMenu(gui, End_MM, *MM)             # generate the drop down menu
    EMDM.grid(row = row_ini + 2, column = column_ini + 2, sticky=NSEW)
    EMDM.config(bg = "white", width = Label_width)

    # The drop menu of end day
    End_DD = StringVar(gui)                         # Create a Tkinter variable, call the corresponding constructor
    #End_DD.set( DD[0] )                             # Default date is "1"
    End_DD.set( Today.day )                             # Default date is "1"
    EDDM = OptionMenu(gui, End_DD, *DD)             # generate the drop down menu
    EDDM.grid(row = row_ini + 2, column = column_ini + 3, sticky=NSEW)
    EDDM.config(bg = "white", width = Label_width)

    #Updating the label "gen_Label(" ", row_ini + 1, column_ini + 4)"
    ED_but = tk.Button(gui, text="Validating starting and ending date", font=(Font, Font_size), bd=Label_bd, width = 30,
    relief="groove", fg = "black", bg = "green", command=dateFormat
    ).grid(row = row_ini , column = column_ini + 4, sticky=NSEW)

    gen_Label(" ", row_ini + 2, column_ini + 4)

#===========================
def DefaultTime():
    global Today, Pri_90_days;

    Today = date.today();
    Pri_90_days = Today - timedelta(days = 90);
    #print(Today.month, Pri_90_days)

if __name__ == "__main__":

    gui = Tk();
    gui.title('Total cases')
    gui.configure(background = "Dark grey");
    wids = gui.winfo_screenwidth();
    heis = gui.winfo_screenheight();
    gui.geometry( "%dx%d+%d+%d" %(wids*0.75, heis, 0, 0))

    #=========================================
    GeneratingDateInput()

    GeneratingCustomerCheckBox()
    #=========================================

    Label(gui, text = '', height = Label_height, bg = "grey", fg = "black",
    bd=Label_bd).grid(row = row_ini + 9, column = column_ini, sticky=NSEW, columnspan=7)

    #Updating the label "gen_Label(" ", row_ini + 1, column_ini + 4)"
    Result_but = tk.Button(gui, text="Yield first pass yield rate", font=(Font, Font_size), bd=Label_bd, width = 30,
    relief="groove", fg = "black", bg = "green", command=FirstYieldingRate
    ).grid(row = row_ini+10 , column = column_ini, sticky=NSEW)

    #toggle of auto-Updating
    #t_btn = tk.Button(text='True', width=12, command=toggle).grid(row = row_ini , column = column_ini+6, sticky=NSEW)
    t_btn = tk.Button(text='Switch Mic On', width=15, command=toggle)
    t_btn.grid(row = row_ini , column = column_ini+6, sticky=NSEW, padx=10)


    gui.mainloop()
