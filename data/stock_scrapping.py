from os import name
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def write_data(name,url,headers):
    req = requests.get(url, headers=headers)
    req.raise_for_status()

    soup = BeautifulSoup(req.text, 'lxml')

    s = soup.find('tr', attrs={'class':'gray'})
    if s == None:
        return

    s = s.parent
    ss = s.find_all('tr')

    with open(name + '_onehot2' + '.csv', 'a', encoding='utf-8') as f:
        for s in ss[1:][::-1]:
            s_ats = s.find_all("td")
            f.write(s_ats[0].text + ',')
            d = datetime.strptime('20' + s_ats[0].text, '%Y/%m/%d')
            f.write(str(d.weekday()) + ',')
            f.write(s_ats[1].text.replace(',','') + ',')
            dp = float(s_ats[3].span.text) 
            if dp > 5:
                f.write('1,0,0,0,0,')
            elif dp <= 5 and dp > 1:
                f.write('0,1,0,0,0,')
            elif dp <= 1 and dp > -1:
                f.write('0,0,1,0,0,')
            elif dp <= -1 and dp > -5:
                f.write('0,0,0,1,0,')
            elif dp <= -5:
                f.write('0,0,0,0,1,')
            f.write(s_ats[4].text.replace(',','') + ',')
            f.write(s_ats[5].text.replace(',','') + ',')
            f.write(s_ats[6].text.replace(',','') + ',')
            f.write(s_ats[7].text.replace(',',''))
            f.write('\n')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
y1 = 2017
y2 = 2021
codes = {'SamsungE' : '005930' , 'LGE': '066570', 'SamsungEU':'005935', 'SKH':'000660', 'SamsungBL':'207940', 'NAVER':'035420'}

for name,code in codes.items():
    with open(name + '_onehot2' + '.csv', 'w', encoding='utf-8') as f:
        lst = ['date', 'weekdate', name+'_RU', name+'_U', name+'_UC', name+'_D', name+'_RD' ,name + '_end', name +'_start', name +'_high', name +'_low', name +'_abount']
        f.write(','.join(lst))
        f.write('\n')

    for y in range(y1,y2+1):
        for i in range(10,0,-1):
            url = f'https://vip.mk.co.kr/newSt/price/daily.php?p_page={i}&y1={y}&m1=01&d1=01&y2={y}&m2=12&d2=31&stCode={code}'
            write_data(name,url,headers)