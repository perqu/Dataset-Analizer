import pandas as pd
import numpy as np
import io

def info(df):
    print("------------DIMENSIONS------------")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("--------------DTYPES--------------")
    columns = df.columns.tolist()
    integers = df.select_dtypes("integer").columns.tolist()
    floats = df.select_dtypes("float").columns.tolist()
    bools = df.select_dtypes("bool").columns.tolist()
    objects = df.select_dtypes("object").columns.tolist()
    dataType = []
    for el in columns:
        if el in integers:
            dataType.append('int')
        if el in floats:
            dataType.append('float')
        if el in bools:
            dataType.append('bool')
        if el in objects:
            dataType.append('object')
    d = {'Column' : columns, 'Type': dataType}
    print(pd.DataFrame(d))

    print("----------MISSING VALUES----------")
    print("Is any value missing? ", np.where(df.isnull().values.any() == False,  "No", "Yes"), "\n")

    buf = io.StringIO()
    df.info(buf=buf)
    info = buf.getvalue().split('\n')[-2].split(":")[1].strip()
    print("----------MEMORY USAGE------------ \n", info)