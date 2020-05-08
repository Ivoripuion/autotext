# coding=utf-8
import pyautogui
from xpinyin import Pinyin

chinese_dirty=(
u"草泥马",
u"你妈死了",
u"你是不是",
u"低能",
u"人话都听不懂",
u"没家教的狗东西",    
)

dirty_set=[]    #最终的拼音方式
p=Pinyin()      #用于转换拼音

#通过点击的方式切屏        
def trans_screen():
    pyautogui.doubleClick(492,974)
    pyautogui.typewrite(['enter'],0.01)

#将中文转化成拼音
def trans_chinese():
    for c_dirty in chinese_dirty:
        pin=p.get_pinyin(c_dirty,'')
        pin_list=list(pin)
        pin_list.append("1")
        dirty_set.append(pin_list)

#发送text
def send_dirty():  
    for p_dirty in dirty_set:
        pyautogui.typewrite(p_dirty,0.01)
        pyautogui.typewrite(['enter'],0.01)

#查看当前的dirty_set内容
def chk_dirty():
    for p_dirty in dirty_set:
        print(p_dirty)

if __name__ == "__main__":
    trans_chinese()
    trans_screen()
    send_dirty()
