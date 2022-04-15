# Amplience QA Engineer Technical Test Response

## Instructions

Git clone this repository to your local machine. 

Use any appropriate IDE of your choice (eg: Visual Studio, PyCharm) and open the folder containing the repo contents.

### **Prerequisites:**

Install below python packages:

```bash
pip install requests 
pip install pytest 
pip install selenium
```

Chrome is the chosen browser for the UI testing in this exercise. 

For selenium to interface with the Chrome browser an appropriate driver must be installed - you can find different versions of chromedriver.exe here: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

Please install the driver version compatible with your Chrome version.

In the python script (inside the test folder) please set the appropriate chromedriver.exe path before running the tests.

```bash
## set chromedriver.exe path
chromedriver_exe_path =  '../chromedriver'
```

### Running tests

To execute the tests - run below command in the terminal inside this folder.

```bash
py.test -v
```

**Please Note:** In Part 2 - unable to visually locate the web UI element corresponding to public_gists. This check was ignored in my automation tests.
