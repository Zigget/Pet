'''
All code was assembled by myself, Samuel Sidzyik.
I pulled bits and pieces from various sources but not one line of this file was written by anyone other than myself.

sources referenced
https://www.pysimplegui.org/en/latest/cookbook/
https://github.com/PySimpleGUI/PySimpleGUI/issues/2298
https://github.com/PySimpleGUI/PySimpleGUI/issues/721
'''
# -- -- imports for GUI, and functions from 'connected.py' -- --
import PySimpleGUI as sg
from connected import *
import os

# -- -- Visual Theme to GUI -- --
# https://icon-icons.com/download/89239/ICO/32/
sg.set_options(icon=r"C:\Users\Owner.P200219L\Desktop\C2C\Final\pawprint.ico",text_color='black')

# -- -- Function to create Home window with navigation nested within -- --
def startwindow():
    # -- -- Lays out the Home window -- --
    layout = [[sg.Text('''Sam\'s Doggo
    Life Insurance''',font='Lucinda 20',size=(20,2),justification='c')],
            [sg.Button('Login',key='login',size=(15,1),font='Lucinda 12'),sg.Button('Get a Quote',key='quote',size=(15,1),font='Lucinda 12')],
            [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Home',layout)

    # -- -- intiates the window -- --
    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return 'close'
        
        # -- -- Lays out and initiates Quote Window -- --
        elif event == 'quote':
            window.Close
            quotewindow()

        # -- -- New Window to Login -- --
        elif event == 'login':
            layoutlogin = [[sg.Text('Username',key='user',size=(15,1),font='Lucinda 12'),sg.Input(key='userinput',font='Lucinda 12',size=(15,1))],
            [sg.Text('Password',key='pass',size=(15,1),font='Lucinda 12'),sg.Input(key='passinput',font='Lucinda 12',size=(15,1))],
            [sg.Text('',key='space',size=(15,1),font='Lucinda 12'),sg.Text(key='error',font='Lucinda 12',size=(15,1))],
            [sg.Button('Login',key='login',font='Lucinda 12'),sg.Button('Back',key='back',font='Lucinda 12'),sg.Button('Forgot Password',key='forgot',font='Lucinda 12',pad=(35,0))],
            [sg.Button('Exit',font='Lucinda 12')]]
            window2 = sg.Window('Log in',layoutlogin,alpha_channel=0).finalize()
            window2.SetAlpha(1)
            window.Close()
            window = window2
            while True:
                event,values = window.read()
                if event == 'Exit' or event == sg.WIN_CLOSED:
                    return 'close'
                elif event == 'login':
                    pass
                elif event == 'back':
                    # -- -- Closes login and reopens Home window -- --
                    window.Close()
                    startwindow()

def quotewindow():
    layoutquote = [[sg.Text('Doggo Name',key='dname',size=(15,1),font='Lucinda 12'),sg.Input(key='userinput',font='Lucinda 12',size=(15,1))],
    [sg.Text('Doggo Breed',key='pass',size=(15,1),font='Lucinda 12'),sg.Combo(['Mixed Breed under 15lbs.','Mixed Breed under 30 lbs.','Mixed Breed under 65lbs.','Mixed Breed under 110lbs.','Mixed Breed over 110lbs.'],key='kind',font='Lucinda 12',size=(15,1))],
    [sg.Text('Doggo Age',key='age',size=(15,1),font='Lucinda 12'),sg.Input(key='ageinput',font='Lucinda 12',size=(15,1))],
    [sg.Text('',key='space',size=(40,2),font='Lucinda 12',visible=False)],
    [sg.Button('Quote me',key='quote',font='Lucinda 12'),sg.Button('Back',key='back',font='Lucinda 12'),sg.Button('Apply for this policy!',key='approved',font='Lucinda 12',visible=False)],
    [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Log in',layoutquote,alpha_channel=0).finalize()
    window.SetAlpha(1)
    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            return 'close'

        # -- -- Actual Functionality -- --
        elif event == 'quote':
            cost = guiinsurability(values['kind'],int(values['ageinput']))
            window['space'].update('Your Doggo is eligible for life insurance!\nA policy is available for as low as ${:.2f} per year!'.format(cost),visible=True)
            window['approved'].update(visible=True)
        elif event == 'back':
            window.Close()
            startwindow()
        elif event == 'approved':
            pass

# Keeps windows open until exit or [X] pressed
while True:
    if startwindow() == 'close':
        break


# menu = [['File',['New File','Open File','Save','Save as...']],['Edit',['Undo','Redo','Copy','Cut','Paste']]]
# layout = [[sg.Menu(menu,key='menu',font='Luinda 12')],[
#         sg.Multiline(size=(90,20),key='multi')]]
# window = sg.Window('Python Notepad',layout,return_keyboard_events=True)

# while True:
#     event,values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     else:
#         if event == 'Open File':
#         #Open File
#             layout2 = [[sg.Text('Open',font='Lucinda 12')],
#                     [sg.Input(key='input',size=(25,1)),sg.FilesBrowse(key='file',target='IN')],
#                     [sg.Ok(font='Lucinda 12',key='ok'),sg.Exit(key='Exit',font='Lucinda 12')]]
#             browse_window = sg.Window('File Browse',layout2)
#             event,values = browse_window.read()

#             filename = values['file']
#             file_name = os.path.join(os.path.dirname(__file__),filename)

#             with open(filename,'r') as read_file:
#                 rf = read_file.read()
#             window['multi'].update(value=rf)