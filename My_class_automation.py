from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
import time
import pip
import calendar
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from apscheduler.schedulers.blocking import BlockingScheduler
from dhooks import Webhook
webhook = Webhook("https://discord.com/api/webhooks/910720477427798026/3KAIFgmjpKP5tWp9QZyOSNF2J5OQQu0-JpIIcbvatiRevLqXQQ5wu4-y3si6l4Z_I71u")
#webhook link of a discord channel
datetime_now=datetime.now()
#gets the date and time of current day

test_root = Tk()
test_root.iconbitmap("lpu_logo.ico")
test_root.geometry("948x632")
test_root.minsize(948,632)
test_root.maxsize(948,632)
test_root.title("My Class Automation Control Center")
img = ImageTk.PhotoImage(Image.open("background.png"))
panel = Label(test_root, image=img)
panel.place(x=-5, y=-5)

myFont = font.Font(family='Helvetica', size=10, weight='bold')
btn = Button(test_root, text="Exit", command=test_root.destroy, font=myFont,bg="#456ada")
btn.place(x=880, y=580)

def check_system():
    
    def installing():
       package1='selenium'
       package2='apscheduler'
       package3='dhooks'
       pip.main(['install',package1])
       pip.main(['install',package2])
       pip.main(['install',package3])
    def check():
        try:
            import selenium
            import apscheduler
            import dhooks
            final_message=Label(text="Sucessfully Installed : )")
            final_message.pack()
            
        except ModuleNotFoundError:
            final_message=Label(text="Installation Failed : )")
            final_message.pack()
    installing()
    check()

btn_2= Button(test_root, text="---> Click Here To Install All Necessary Components <---",
            command=check_system,font=myFont,fg="white", bg="#3488EF")
btn_2.place(x=37, y=30)
check_instruction_1=Label(text="Only One Time Required",font=('roboto', 12, 'bold'),bg="#a58460").place(x=40, y=70)
writtenby=Label(text="Written By Yaswanth",font=('roboto',12,'bold')).place(x=20, y=350)

var1= StringVar()
var2=StringVar()

x, y="", ""
def get_value():
   global x, y
   x= var1.get()
   y= var2.get()
   test_root.destroy()
   automation()

user_name = Label(text="Registration Number :",font=('roboto', 10, 'bold'),bg="#af8b66").place(x=560,y=60)
user_password = Label(text="Password :",font=('roboto', 10, 'bold'),bg="#af8b66").place(x=560,y=100)
user_name_input_area = Entry(test_root,textvariable=var1).place(x=710,y=60)
user_password_entry_area = Entry(test_root,textvariable=var2,show="*").place(x=710,y=100)
submit_button = Button(text="Submit",font=('roboto', 12, 'bold'),fg="white", bg="#3488EF",command= get_value).place(x=720,y=135)

def automation():
    username_input = x
    password_input = y

    def login(Id):
        web = webdriver.Chrome()  # chrome webdriver
        web.get("https://myclass.lpu.in")  # opens myclass website
        time.sleep(1)  # waits 1 sec
        web.maximize_window()  # maximizes the chrome window
        username = web.find_element(By.XPATH, "/html/body/div[2]/div/form/div[6]/input[1]")  # locates username field
        username.send_keys(username_input)  # enters registration number in username field
        time.sleep(1)  # waits 1 sec
        password = web.find_element(By.XPATH, "/html/body/div[2]/div/form/div[6]/input[2]")  # locates password field
        password.send_keys(password_input)  # enters password in password field
        time.sleep(1)  # waits 1 sec
        login = web.find_element(By.XPATH, "/html/body/div[2]/div/form/div[7]/button")  # locates login button
        login.click()  # clicks login button
        webhook.send("Login Success :)")  # sends "login Success :)" notification to discord channel
        time.sleep(1)  # waits 1 sec
        View_classes = web.find_element(By.XPATH, "/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a")
        # locates view_classes container
        View_classes.click()  # Clicks View Classees Button
        time.sleep(1)  # waits 1 sec
        class_elements = web.find_element(By.XPATH,"/html/body/div[1]/div[6]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[{}]".format(Id))
        # Locates the class container respectively according to time
        class_elements.click()  # clicks that class container
        time.sleep(1)  # waits 1 sec
        try:
            join_button = WebDriverWait(web, 150).until(EC.presence_of_element_located((By.XPATH, '//*[@id="meetingSummary"]/div/div/a/i')))
            # waits for 150 sec until the join button appears
            join_button.click()  # clicks the join button once it appears
            webhook.send("Joining The Class :)")  # sends "Joining The Class :)" notification to discord channel
        except:
            webhook.send("Joining class failed :(")  # if the join button does'nt appear in 150sec then
            # sends "Joining class failed :(" notification to discord channel
        try:
            time.sleep(5)  # waits 5 sec
            web.switch_to.frame(web.find_element(By.ID, "frame"))  # finds the frame by id and switch to it
            listen_only_button = WebDriverWait(web, 150).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i')))
            # waits for 150 sec until the listen_only button appears
            listen_only_button.click()  # clicks listen_only button once it appears
            webhook.send("Joining Class Succes :)")  # sends "Joining Class Succes :)" notification to discord channel
        except:
            webhook.send("Not able to Join class :(")  # if the listen_only button does'nt appear in 150sec then
            # sends "Not able to Join class :(" notification to discord channel
        # chatbox-------------------------------------------------------------------------------------------------------
        time_now = datetime_now.strftime("%H:%M:%S")  # gets current time in hours,minutes,seconds format
        if time_now >= "12:00:00":  # checks if the current time is greater or equal to 12:00:00
            chat = ("Good Afternoon")  # if true then "Good Afternoon" value is given to chat variable
        else:
            chat = ("Good Morning")  # if false then "Good Morning" value is given to chat variable
        try:
            public_chat = WebDriverWait(web, 60).until(EC.presence_of_element_located((By.ID, 'chat-toggle-button')))
            # waits for 30 sec until the public-chat container appears
            public_chat.click()  # clicks public-chat container once it appears
        except:  # if the public-chat container does'nt appear in 60sec then
            pass  # nothing happends
        try:
            greeting = WebDriverWait(web, 60).until(EC.presence_of_element_located((By.ID, 'message-input')))
            # waits for 30 sec until the chat-box appears
            greeting.send_keys(chat)  # enters value present in chat variable in chat-box
            greeting.send_keys(Keys.RETURN)  # presses enter key
        except:  # if the chat-box does'nt appear in 60sec then
            pass  # nothing happends
        # chatbox-------------------------------------------------------------------------------------------------------
        try:
            class_ended_button = WebDriverWait(web, 7200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div/button/span')))
            # waits for 7200 sec until the class-ended by teacher page appears
            class_ended_button.click()  # clicks ok
            web.close()  # closes the chrome window
            webhook.send("Left the Class")  # sends "Left the Class" notification to discord channel
        except:  # if the class-ended by teacher page does'nt appear in 7200sec then
            pass  # nothing happends
        time.sleep(5)  # waits 5 sec

    total_time_now = datetime_now.strftime("%H")  # gets the hour value from current time
    if total_time_now > "17":  # checks if the current time hour value is greater 17
        message_root = Tk()
        message_root.geometry("420x60")
        message_root.resizable(width=False, height=False)
        message_root.title("Wizard")
        exit_button = Button(message_root, text="Close", command=message_root.destroy)
        exit_button.pack(side="bottom")
        final_message = Label(text="Classes done for today : )")
        final_message.pack()
        message_root.mainloop()

        print("Classes done for today : )")
        webhook.send("Classes done for today : )")
        quit()  # if it is true then exits the program

    def join(WEEK):
        sched = BlockingScheduler()  # BlockingScheduler
        Year, Month, Day = datetime_now.year, datetime_now.month, datetime_now.day
        # Year variable is assigned with current year,
        # Month variable is assigned with current Month,
        # Day variable is assigned with current Day.
        for i, Id in zip(WEEK.values(), WEEK.keys()):
            # i variable is assigned with values of dictionary which matches with current weekday
            # Id variable is assigned with keys of dictionary which matches with current weekday
            print(i, Id)  # prints i and Id
            x = i.split(":")  # splits dictionary values
            sched.add_job(login, run_date=datetime(Year, Month, Day, int(x[0]), int(x[1]), int(x[2])), args=Id)
            # does this job at specific time mentioned in the dictionary
        sched.start()  # starts the BlockingScheduler

    # Time Table entered as dictionary-------------------------------------------------
    MON  = {"1":"9:00:00","2":"10:00:00","3":"12:00:00","4":"13:00:00","5":"15:00:00"}
    TUE  = {"1":"9:00:00","2":"12:00:00","3":"13:00:00","4":"15:00:00","5":"16:00:00"}
    WED  = {}
    THUR = {"1":"9:00:00","2":"12:00:00","3":"13:00:00","4":"15:00:00","5":"16:00:00"}
    FRI  = {"1":"9:00:00","2":"12:00:00","3":"13:00:00","4":"15:00:00"}
    SAT  = {"1":"10:00:00","2":"12:00:00","3":"15:00:00"}
    # Time Table entered as dictionary-------------------------------------------------
    week_day = calendar.day_name[datetime_now.weekday()]  # gets the weekday name
    # Assigns the corresponding dictionary according to current weekday
    if week_day == "Monday":
        join(MON)
    elif week_day == "Tuesday":
        join(TUE)
    elif week_day == "Wednesday":
        print("Enjoy Your Wednesday No classes Today")
        webhook.send("Enjoy Your Wednesday No classes Today")
    elif week_day == "Thursday":
        join(THUR)
    elif week_day == "Friday":
        join(FRI)
    elif week_day == "Saturday":
        join(SAT)
    else:
        print("Enjoy Your Sunday No classes Today")
        webhook.send("Enjoy Your Sunday No classes Today")
test_root.mainloop()
