import csv
import webbrowser
import time
import keyboard
import os

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
#safari_path = 'open -a /Applications/Google\ Chrome.app %s'

with open ('textNEWru.txt', 'r') as f:
    text = f.read()

waLinks = []
url = 'https://api.whatsapp.com/send/?phone=7{}&text={}&app_absent=0'

waLinks.append(url.format('7014209166', text))


with open('all_regions_phoneN.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        waLinks.append(url.format(row[0][1:], text))
cnt = 0
for link in waLinks:
    cnt += 1
    webbrowser.get(chrome_path).open(link)
    print(cnt, link[:48])
    time.sleep(5)
    keyboard.press_and_release('enter')
    os.system("killall -9 'Google Chrome'")


print('Done')

