import numpy as np
from dataclasses import dataclass

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

#ディバイス情報の表示
def deviceprint(e):
    print("製品名 : " + str(e.Name_d) + "\n" + "機能 : " + str(e.Function_d) + "\n" + "データ : " + str(e.data_d) + "\n" + "製品番号 : " + str(e.Number_d) + "\n" + "IPアドレス : " + str(e.IP_d) + "\n")

#GWの表示
def GWprint(e):
    print("GW自身のIPアドレス : " + str(e.IP_gw) + "\n" + "データ : " + str(e.data_gw) + "\n")

#ディバイス情報の登録
device1 = device('カメラ','写真を撮影','none','DEVICE_101','192.168.1.2')
device2 = device('テレビ','投影','none','DEVICE_1234','192.168.1.3')

#GWのIPアドレスとデータ設定
hostdata = GW('123.456.7.8','none')

#ディバイス情報を表示させてみる
deviceprint(device1)
deviceprint(device2)

#GW情報を表示
GWprint(hostdata)

#デバイス1からパケットを送る(不正に送ろうとした時)
packetD1_D2["Sender"] = [device1.IP_d]
packetD1_D2["Middle"] = [device2.IP_d]
packetD1_D2["Receiver"] = [device2.IP_d]
packetD1_D2["data"] = ["撮影したデータ"]
packetD1_D2["Number"] = [1]

#デバイス1からGW経由でデバイス2にパケットを送ろうとした場合
packetD1_GW["Sender"] = [device1.IP_d]
packetD1_GW["Middle"] = [hostdata.IP_gw]
packetD1_GW["Receiver"] = [device2.IP_d]
packetD1_GW["data"] = ["撮影したデータrfahrjoajaofarkforghaorjaifnafaofjirjao"] #データが多かったら入らない
packetD1_GW["Number"] = [2]

#パケットを表示させてみる
print(packetD1_D2)
print(packetD1_GW)

#検証する( GWスイッチ部分 )
def SwicthA(p,gw):
    if p[0][1] != gw.IP_gw :
        print("不適切な通信です.通信を遮断します")
        #通信の遮断と逆にIPから端末の探索して,パケットを破損させてもいいかも
    elif p[0][1] == gw.IP_gw:
        print("gwに通りました.")
        #情報を登録する.data_gwを受け取ったpの
        hostdata.data_gw = p[0][3]
        GWprint(hostdata) #gwが更新されているかの確認
        gw_Process(p,gw)

def gw_div(paket): #ここでGW内の送信の区別を行う。どこがどこに送るのか
    if paket[0][2] == '192.168.1.2':
        return device1
    elif paket[0][2] == '192.168.1.3':
        return device2
    # elif ...
    # elif ...

#GWで宛先に送る作業
def gw_Process(r,s):#実際ここでセキュリティの色々な処理をしている
    if r[0][3] != []: #rのIPアドレスがあったら
        Redivice = gw_div(r)
        Redivice.data_d = s.data_gw#そのr[0][3]に送る
        deviceprint(device2)

#packetD1_D2間で行おうとする場合( 不正な通信 )
SwicthA(packetD1_D2,hostdata)

#正規ルートの通信
SwicthA(packetD1_GW,hostdata)
