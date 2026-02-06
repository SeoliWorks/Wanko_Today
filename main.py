#Copyright (c) 2025 SeoliWorks
#This software is released under the MIT License, see LICENSE.

import autogui101Wankov
import webbrowser
import datetime
import tkinter as tk
import tkinter.simpledialog as simpledialog

Wanko_URL = 'https://www.fujitv.co.jp/meza/wanko/index.html'
webbrowser.open(Wanko_URL)

tk.Tk().withdraw()
Pic_num = int(simpledialog.askstring('','上から何番目の写真を壁紙にしたいか、半角数字一桁で入力してください。'))

#以下、「https://www.fujitv.co.jp/meza/wanko/photo/w250502_03.jpg」の「w250502」（2025.5.2）を日付情報から求めていく
dt = datetime.datetime.today()
year_20xx = dt.year - 2000
month = dt.month
day = dt.day
weekday = dt.weekday()

if month < 10:
    month = '0' + str(month)

if weekday == 5: #saturday
    day -= 1
elif weekday == 6: #sunday
    day -= 2

if day < 10:
    day = '0' + str(day)

daytime_info_needed = str(year_20xx) + str(month) + str(day) #Ex:250502_=_2025年5月2日

Pic_URL = f'www.fujitv.co.jp/meza/wanko/photo/w{daytime_info_needed}_0{Pic_num}.jpg'
Pic_name = f'w{daytime_info_needed}_0{Pic_num}.jpg'

autogui101Wankov.autogui_101(Pic_URL,Pic_name)

#references
#https://atmarkit.itmedia.co.jp/ait/articles/2111/02/news019.html
#https://qiita.com/sastrum/items/518579bc00dfae3cd293
#https://magazine.techacademy.jp/magazine/22727
#https://www.insource.co.jp/python-gakuin/mail-backnumber/vol27.html
