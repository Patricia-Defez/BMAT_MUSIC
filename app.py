
import time
timestr = time.strftime("%Y-%m-%d")

from fastapi import FastAPI, File, UploadFile,HTTPException
from fastapi.responses import FileResponse
import uvicorn
import pandas as pd
import os

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get('/')
def read_root():
    return {"Hello": "world!"}

@app.post('/file/upload')
async def upload_file(file: UploadFile):
    chunksize = 20000
    df = pd.read_csv(file.file, chunksize=chunksize, iterator=True)
    new_columns = {'Song':'Song', 'Date': 'Date', 'Number of Plays':'Total Number of Plays for Date'}
    #new_df = df.rename(columns=new_columns)
    new_filename = "{}_{}.csv".format(os.path.splitext(file.filename)[0],timestr)
    outputf = pd.DataFrame(columns=['Song','Date','Total Number of Plays for Date'])
    for chunk in df:
        new_ch =chunk.rename(columns=new_columns)   
        output =  new_ch.groupby(['Song','Date'])['Total Number of Plays for Date'].sum()
        outputf = pd.concat([outputf, output] )
    pip = os.getpid()
    print(pip)
    outputf.to_csv(new_filename)
    return {"filename": new_filename, "PIP": pip}

@app.get("/file/download/{name}")
async def download_file(name: str):

    return FileResponse(path= os.path.join(BASE_DIR,name),filename=name)


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)