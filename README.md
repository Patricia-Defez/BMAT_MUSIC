# BMAT_MUSIC

## Description:
The proyect is a small REST API with tow end points which takes a CSV file of the following format as its input, 
processes it and generates the output CSV file.<br/>
Input CSV file: “Song”, “Date”, “Number of Plays”.<br/> 
There will be many records for each song within each day. Input is not sorted.<br/>
Output CSV file: “Song”, “Date, “Total Number of Plays for Date”.<br/>
Both input and output CSV files can be larger than available memory.<br/>
Python version is 3.10.11<br/>
Fastapi version is 0.103.1<br/>

### Create a virtual env:
After cloning the project, it is recommended to create a virtual env.<br/>
- To create the virtual env, got to the project root in a terminal and write:<br/>
  ```python3 -m venv env```<br/>
- To activate it:
  In Windows:
  ```source env/bin/activate```<br/>
  In Unix/macOS:
  ```.\env\Scripts\activate```<br/>
- To leave it:
  ```deactivate```<br/><br/>
For more information: [Python gide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

### Installations:
It is necessary to have Python3 installed, but also, some dependencies are necessary.<br/>
With the venv activate:
```
   pip install fastapi uvicorn python-multipart pandas
   
```

### Start server
```uvicorn app:app --reload```<br/>
Uvicorn running on http://127.0.0.1:8000<br/>
The Swagger will be in http://localhost:8000/docs
