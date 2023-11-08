from websocket import create_connection
import json
import csv

headers = json.dumps({
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9,ko;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'Upgrade',
    'Host':'data.tradingview.com',
    'Origin':'https://www.tradingview.com',
    'Pragma':'no-cache',
    'Sec-Websocket-Extensions':'permessage-deflate; client_max_window_bits',
    'Sec-Websocket-Key':'f+a85jCIQrkRpSRiBGNYeQ==',
    'Sec-Websocket-Version':'13',
    'Upgrade':'websocket',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
})

data = {}
csv_header=['FEDFUNDS','US01M','US02Y','US03MY','US05Y','US10Y','US20Y','US30Y','VIX','DJT','XLE','XLF','XLI','XLK','XLP','XLU','XLV','XLY','VIX','VIX3M','VIX9D','PC','PCC','TICK','TICK.NQ','TICK.US','TICKI','TICKQ','TKVD.US','1/VOLX','VIXM/VIXY','XLY*XLK/(XLP*XLU)','ATHI.NQ-ATLO.NQ','ATHI.US-ATLO.US','HYG/UB1!']

with open('data.csv','w',encoding='UTF8', newline='') as f:

    writer = csv.writer(f)

    writer.writerow(csv_header)

    while True:
        ws = create_connection('wss://data.tradingview.com/socket.io/websocket?from=&date=2023_11_07-11_29',headers=headers)

        first = ws.recv()
        #print(first)


        ws.send('''~m~36~m~{"m":"set_data_quality","p":["low"]}''')
        ws.send('''~m~784~m~{"m":"set_auth_token","p":["eyJhbGciOiJSUzUxMiIsImtpZCI6IkdaeFUiLCJ0eXAiOiJKV1QifQ.eyJ1c2VyX2lkIjo2NTk4NDI1NiwiZXhwIjoxNjk4OTc3OTUxLCJpYXQiOjE2OTg5NjM1NTEsInBsYW4iOiJwcm9fcHJlbWl1bSIsImV4dF9ob3VycyI6MSwicGVybSI6IiIsInN0dWR5X3Blcm0iOiJ0di1wcm9zdHVkaWVzLHR2LXZvbHVtZWJ5cHJpY2UsdHYtY2hhcnRwYXR0ZXJucyx0di1jaGFydF9wYXR0ZXJucyIsIm1heF9zdHVkaWVzIjoyNSwibWF4X2Z1bmRhbWVudGFscyI6MCwibWF4X2NoYXJ0cyI6OCwibWF4X2FjdGl2ZV9hbGVydHMiOjQwMCwibWF4X3N0dWR5X29uX3N0dWR5IjoyNCwibWF4X292ZXJhbGxfYWxlcnRzIjoyMDAwLCJtYXhfYWN0aXZlX3ByaW1pdGl2ZV9hbGVydHMiOjQwMCwibWF4X2FjdGl2ZV9jb21wbGV4X2FsZXJ0cyI6NDAwLCJtYXhfY29ubmVjdGlvbnMiOjUwfQ.NQh2yFIZNT7pgQGJp8TUOQNReNu4rON2ypc9-8VEy0G0xbGKUsdz_godn8yQz0gXSrcCQFpRaMyG-EESS-At8xf4M90G6HZOv28EzV92YxwWKtljBgaus4b4wLjScxNsPbdFIMNVfmy6IAyHtL9vDiWCrDD_XBhEyR7-VRkgo9w"]}''')
        ws.send('''~m~34~m~{"m":"set_locale","p":["en","US"]}''')
        ws.send('''~m~83~m~{"m":"quote_create_session","p":["qs_snapshoter_basic-symbol-quotes_VahuCbWgVFBm"]}''')
        ws.send('''~m~406~m~{"m":"quote_set_fields","p":["qs_snapshoter_basic-symbol-quotes_VahuCbWgVFBm","pro_name","base_name","short_name","description","type","exchange","typespecs","listed_exchange","lp","country_code","provider_id","symbol-primaryname","logoid","base-currency-logoid","currency-logoid","source-logoid","update_mode","source","source2","pricescale","minmov","fractional","visible-plots-set","industry","sector"]}''')



        # Printing all the result

        try:
            ws.send('''~m~568~m~{"m":"quote_add_symbols","p":["qs_snapshoter_basic-symbol-quotes_VahuCbWgVFBm","USI:ATHI.NQ-USI:ATLO.NQ","USI:ATHI.US-USI:ATLO.US","AMEX:HYG/CBOT:UB1!","USI:PC","USI:PCC","USI:TICK","USI:TICK.NQ","USI:TICK.US","USI:TICKI","USI:TICKQ","USI:TKVD.US","1/FX:VOLX","AMEX:VIXM/AMEX:VIXY","AMEX:XLY*AMEX:XLK/(AMEX:XLP*AMEX:XLU)","FRED:FEDFUNDS","TVC:US01M","TVC:US02Y","TVC:US03MY","TVC:US05Y","TVC:US10Y","TVC:US20Y","TVC:US30Y","TVC:VIX","DJ:DJT","AMEX:XLE","AMEX:XLF","AMEX:XLI","AMEX:XLK","AMEX:XLP","AMEX:XLU","AMEX:XLV","AMEX:XLY","CBOE:VIX","CBOE:VIX3M","CBOE:VIX9D"]}''')
            result = ws.recv()
        #  if (result=='~m~4~m~~h~1'):
        #      ws.send('~m~4~m~~h~1')
            # Split the data by "~m~" to separate individual JSON objects
            segments = result.split('~m~')

            # Iterate through the segments and parse the JSON
            for segment in segments:
                if segment:
                    try:
                        json_data = json.loads(segment)
                        if 'lp' in json_data['p'][1]['v']:
                            name = json_data['p'][1]['v']['short_name']
                            lp_value = json_data['p'][1]['v']['lp']
                            data[name]=lp_value

                            print(f"{name}: {lp_value}")
                    except:
                        pass
        except Exception as e:
            print(e)
            break

        csv_data = []

        for i in range(0,len(csv_header)):
            try:
                csv_data.append(data[csv_header[i]])
            except:
                csv_data.append('')
        writer.writerow(csv_data) 
