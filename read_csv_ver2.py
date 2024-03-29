import pandas as pd
from datetime import datetime
from input_class import *


#filepath = userdata.get_filepath()  #"./list.csv"
#data = pd.read_csv(filepath, thousands=",", index_col=0, names=['col1','col2','col3'], encoding='utf-8')
#data = pd.read_csv(filepath, sep="," , dtype="unicode")

glb_code = ""
glb_price = ""
glb_cate  = ""

def read_file():
    global data, glb_code, glb_price, glb_cate

    #glb_code = data['상품코드'].values.tolist()
    #glb_price = data['대분류'].values.tolist()
    #glb_cate = data['중분류'].values.tolist()
##############

def get_count_data():
    global glb_code
    ud = Userdata()
    filepath = ud.get_filepath()
    print('----123123----', ud.username)
    print('-----in get count data--------')
    print(filepath)
    print('-------------')
    data = pd.read_csv(filepath, sep="," , dtype="unicode")
    return len(data)
###############

def setState(idx , state, price , cateType):
    global glb_code
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    txt = f' {time}:: {glb_code[idx]} :: {price} :: {cateType}| :: {state}\n\n'
    f = open("log.txt", 'a',encoding='utf8')
    f.write(txt)
    f.close()

def get_data(n):
    global glb_code, glb_price, glb_cate
    value = [glb_code[n] , glb_price[n], glb_cate[n]]
    return value
    #print(glb_code[n] , "\n", glb_price[n] , "\n", glb_cate[n])
###############