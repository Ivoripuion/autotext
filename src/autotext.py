# coding=utf-8
import pyautogui
from xpinyin import Pinyin

rubbish_dic=1

if rubbish_dic==0:
    chinese_rubbish=(
    u"草泥马",
    u"你妈死了",
    u"你是不是",
    u"低能",
    u"人话都听不懂",
    u"没家教的狗东西",   
    )
elif rubbish_dic==1:
    rubbish_file=open("rubbish_dic.txt")
    chinese_rubbish=rubbish_file.read().splitlines()


rubbish_set=[]    #最终的拼音方式
p=Pinyin()      #用于转换拼音

#通过点击的方式切屏        
def trans_screen():
    pyautogui.doubleClick(492,974)
    pyautogui.typewrite(['enter'],0.01)

#将中文转化成拼音
def trans_chinese():
    for c_rubbish in chinese_rubbish:
        pin=p.get_pinyin(c_rubbish,'')
        pin_list=list(pin)
        pin_list.append("1")
        rubbish_set.append(pin_list)

#发送text
def send_rubbish():  
    for p_rubbish in rubbish_set:
        pyautogui.typewrite(p_rubbish,0.01)
        pyautogui.typewrite(['enter'],0.01)

#查看当前的rubbish_set内容
def chk_rubbish():
    for p_dirty in rubbish_set:
        print(p_dirty)

if __name__ == "__main__":
    trans_chinese()
    #chk_rubbish()
    trans_screen()
    send_rubbish()
