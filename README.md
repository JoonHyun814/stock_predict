# Stock_predict

### introduction

여러가지 주가 정보를 web-scrapping 을 통해 sequence data로 만든 후, LSTM 모델을 이용하여 예측합니다. 그 후 파이썬 알고르즘에 따라 Creaon API를 통해 자동 주식매매를 진행하고, 그 결과를 slack app을 통해 사용자에게 결과를 알려줍니다.



#### 1. Data Scrapping

<a href = https://vip.mk.co.kr/newSt/price/daily.php>MK증권<a> 사이트에서 여러 종목들의 날짜, 종가, 시가, 저가, 고가, 등락율, 거래양의 정보를 가져와서 csv파일로 저장합니다. 가져올 때, 날짜 data를 통해 요일을 추출하여 one-hot encoding 된 형태로 저장합니다.



#### 2. Data Pre-processing

 다른 주식의 변화가 또한 특정 주식의 변화에 영향을 줄 수 있다고 판단하였습니다. 그래서 여러 종목의 정보를 불러와 pandas를 사용하여 날짜를 기준으로 정렬한 후, 결측치는 등락율과 거래양은 0, 종가,시가,저가,고가의 경우는 이전 날짜의 종가로 채웠습니다.

 이렇게 concatenate된 data는 moving window 처리를 한 후, 각 window 별로 normalization 하였습니다.
