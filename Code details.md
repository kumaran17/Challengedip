+ This file provides few details regarding my test script from the **_Repository Challenge Dip_**.

+ I use **_Visual Studio Code_** for writing my **Selenium Test Scripts** in _Python_

+ **Screenshots** are programmed to be saved on my `C:\Users\dhamilton\Desktop\Selenium project\output` with separate sub folders corresponding to each functionality on the website.

* I have made use of **_datetime module_** to save screenshots on folders with current date and time as its name. This makes it easier for reviewing output.

   `save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\login\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")`

   From the above line of code it can be seen that `+datetime.now()` is used to get **_current date and time_** from the system and the **_datetime format_** is specified using the code `.strftime("%d-%m-%Y %I-%M %p")`

+ **_new directory_** is created using the code `os.mkdir(save_dir)` so that for each instance of the test  run a new folder is created with current date and time as its name. 

* Since there are several test cases and and the **_need to save all the screenshots within the same directory_** the following code is applied for every test case that needs to save screenshot

   `os.path.join(Login.save_dir, 'screenshotname.png')`

* Each **_class_** has its own **_separete sub folder to save screenshot_** which can be seen within them. `os.path.join` joins the location path from `.save_dir` with `screenshot.png` file so that the screenshot is saved in the location of `save_dir`

There are 3 separate main folders to save screenshots under the main directory output for now

> Currently Selenium takes 77.61 Seconds for to run 9 tests via Visual Studio Code Terminal
