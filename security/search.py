import numpy as np
from dataclasses import dataclass
import time

#スプレッドシートの情報設定
import gspread
import json

from google.oauth2.service_account import Credentials

# 認証のjsoファイルのパス
secret_credentials_json_oath = '/Users/nagahashikirara/Desktop/実験4ファイル/client_secret.json' 

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    secret_credentials_json_oath,
    scopes=scopes
)

gc = gspread.authorize(credentials)

workbook = gc.open_by_key('1D2hnjFB_-hpkBtv4oQopIEeQMiOn96dDBNEWcZwDza8')
worksheet = workbook.get_worksheet(0)

#ディバイスの作成
@dataclass
class device:
    Name_d : str
    Function_d : str
    data_d : str
    Number_d : str
    IP_d : str

#ここはまだ変更する予定
@dataclass
class GW:
    IP_gw:str #変更するかも
    data_gw:str #データを格納するもの

#パケット用意
dtype = [ ("Sender","U12"),("Middle","U12") ,("Receiver","U12"), ("data","U12"), ("Number","i2") ]
packetD1_D2 = np.zeros(1 , dtype = dtype)
packetD1_GW = np.zeros(1 , dtype = dtype)

#GWのIPアドレスとデータ設定
#ここは何も変えないので固定
hostdata = GW('123.456.7.8','none')

#ディバイス情報の登録
device1 = device('カメラ','写真を撮影','none','DEVICE_101','192.168.1.2')
device2 = device('テレビ','投影','none','DEVICE_1234','192.168.1.3')
#不正ディバイスを誰かが作成した.
device3 = device('不正ディバイス','none','none','DEVICE_35617','192.168.1.45')
#ディバイス名と番号を取得した場合
device4 = device('カメラ','不正データ','none','DEVICE_101','192.168.1.46')

device5 = device('不正ディバイス','none','none','DEVICE_35617','192.168.1.47')
device6 = device('不正ディバイス','none','none','DEVICE_35617','192.168.1.48')
device7 = device('不正ディバイス','none','none','DEVICE_35617','192.168.1.49')
device8 = device('不正ディバイス','none','none','DEVICE_35617','192.168.1.50')
device9 = device('不正ディバイス','none','none','DEVICE_35617','192.168.1.')


#ここからGWのdbを見て、なかったら登録されていませんとして遮断する
#通信をしようとするのがいる.

#シート内の情報を取得
sheet = worksheet.get_all_values()

def device_check(sheet,device):
    count = 0
    
    for item in sheet:
        #print(item)
        count +=1
        if item[1] == device.Name_d :
            if item[3] == device.Number_d:
                print("ディバイスは登録されています.")
                return
        else :
            if(len(sheet) == count):
                print("ディバイスは未登録です.")

time_sta = time.time()

#登録されているディバイス
device_check(sheet,device1)
#登録されていないディバイス
device_check(sheet,device3)

time.sleep(1)
time_end = time.time()
tim = time_end- time_sta
print(tim)

#10 : 1.00519
#516 : 1.000916
#1000 : 1.00519