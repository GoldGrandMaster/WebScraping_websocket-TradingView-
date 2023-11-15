from websocket import create_connection
import json
import csv
import time
from datetime import datetime,timedelta
import pytz



previos_date=""


headers = json.dumps({
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9,ko;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'Upgrade',
    'Host':'data.tradingview.com',
    'Origin':'https://www.tradingview.com',
    'Pragma':'no-cache',
    'Sec-Websocket-Extensions':'permessage-deflate; client_max_window_bits',
    'Sec-Websocket-Key':'65WxschehURh8PzaVoBe5Q==',
    'Sec-Websocket-Version':'13',
    'Upgrade':'websocket',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
})

data = {}
csv_header=['Timestamp','US01M','US03MY','US02Y','US05Y','US10Y','US20Y','US30Y','FEDFUNDS','TIP','TIP_Vol','TIPS','TIPS_Vol','VIX','DJT','DJT_Vol','XLE','XLE_Vol','XLF','XLF_Vol','XLI','XLI_Vol','XLK','XLK_Vol','XLP','XLP_Vol','XLU','XLU_Vol','XLV','XLV_Vol','XLY','XLY_Vol','VIX','VIX3M','VIX9D','VVIX','UVIX','UVIX_Vol','PC','PCC','TICK','TICK.NQ','TICK.US','TICKI','TICKQ','TKVD.US','1/VOLX','1/VOLX_Vol','VIXM/VIXY','VIXM/VIXY_Vol','XLY*XLK/(XLP*XLU)','XLY*XLK/(XLP*XLU)_Vol','ATHI.NQ-ATLO.NQ','ATHI.US-ATLO.US','HYG/UB1!','HYG/UB1!_Vol','6A1!','6A1!_Vol','6B1!','6B1!_Vol','6C1!','6C1!_Vol','6E1!','6E1!_Vol','6J1!','6J1!_Vol','6S1!','6S1!_Vol','CL1!','CL1!_Vol','CL2!','CL2!_Vol','HG1!','HG1!_Vol','PL1!','PL1!_Vol','SI1!','SI1!_Vol','GC1!','GC1!_Vol','ES1!','ES1!_Vol','NG1!','NG1!_Vol','YM1!','YM1!_Vol','RTY1!','RTY1!_Vol','ZT1!','ZT1!_Vol','ZF1!','ZF1!_Vol','ZN1!','ZN1!_Vol','ZB1!','ZB1!_Vol','UB1!','UB1!_Vol','RB1!','RB1!_Vol','RB2!','RB2!_Vol']


while True:
        dt_uk = datetime.now(pytz.timezone('Europe/London'))
        time = dt_uk.strftime("%H:%M")
        if (time>="23:00" and time<="24:00"):
            plus_uk = dt_uk+timedelta(days=1)
            current_date = plus_uk.strftime("%Y-%m-%d")
        if (time>="00:00" and time<="22:00"):
            current_date = dt_uk.strftime("%Y-%m-%d")
        filename = current_date+"-MarketData"+".csv"

        with open(filename,'a',encoding='UTF8', newline='') as f:

            writer = csv.writer(f)
            if(current_date!=previos_date):
                writer.writerow(csv_header)
                previos_date = current_date
            dt_uk = datetime.now(pytz.timezone('Europe/London'))
            try:
                # ws = create_connection('wss://data.tradingview.com/socket.io/websocket?from=&date=2023_11_10-11_41',headers=headers)
                # first = ws.recv()
                # ws.send('''~m~784~m~{"m":"set_auth_token","p":["eyJhbGciOiJSUzUxMiIsImtpZCI6IkdaeFUiLCJ0eXAiOiJKV1QifQ.eyJ1c2VyX2lkIjo2NTk4NDI1NiwiZXhwIjoxNjk4OTc3OTUxLCJpYXQiOjE2OTg5NjM1NTEsInBsYW4iOiJwcm9fcHJlbWl1bSIsImV4dF9ob3VycyI6MSwicGVybSI6IiIsInN0dWR5X3Blcm0iOiJ0di1wcm9zdHVkaWVzLHR2LXZvbHVtZWJ5cHJpY2UsdHYtY2hhcnRwYXR0ZXJucyx0di1jaGFydF9wYXR0ZXJucyIsIm1heF9zdHVkaWVzIjoyNSwibWF4X2Z1bmRhbWVudGFscyI6MCwibWF4X2NoYXJ0cyI6OCwibWF4X2FjdGl2ZV9hbGVydHMiOjQwMCwibWF4X3N0dWR5X29uX3N0dWR5IjoyNCwibWF4X292ZXJhbGxfYWxlcnRzIjoyMDAwLCJtYXhfYWN0aXZlX3ByaW1pdGl2ZV9hbGVydHMiOjQwMCwibWF4X2FjdGl2ZV9jb21wbGV4X2FsZXJ0cyI6NDAwLCJtYXhfY29ubmVjdGlvbnMiOjUwfQ.NQh2yFIZNT7pgQGJp8TUOQNReNu4rON2ypc9-8VEy0G0xbGKUsdz_godn8yQz0gXSrcCQFpRaMyG-EESS-At8xf4M90G6HZOv28EzV92YxwWKtljBgaus4b4wLjScxNsPbdFIMNVfmy6IAyHtL9vDiWCrDD_XBhEyR7-VRkgo9w"]}''')
                # ws.send('''~m~83~m~{"m":"quote_create_session","p":["qs_snapshoter_basic-symbol-quotes_LODv0v1tgLp5"]}''')
                # ws.send('''~m~406~m~{"m":"quote_set_fields","p":["qs_snapshoter_basic-symbol-quotes_LODv0v1tgLp5","pro_name","base_name","short_name","description","type","exchange","typespecs","listed_exchange","lp","country_code","provider_id","symbol-primaryname","logoid","base-currency-logoid","currency-logoid","source-logoid","update_mode","source","source2","pricescale","minmov","fractional","visible-plots-set","industry","sector"]}''')
                # ws.send('''~m~861~m~{"m":"quote_add_symbols","p":["qs_snapshoter_basic-symbol-quotes_LODv0v1tgLp5","USI:ATHI.NQ-USI:ATLO.NQ","USI:ATHI.US-USI:ATLO.US","AMEX:HYG/CBOT:UB1!","USI:PC","USI:PCC","USI:TICK","USI:TICK.NQ","USI:TICK.US","USI:TICKI","USI:TICKQ","USI:TKVD.US","1/FX:VOLX","AMEX:VIXM/AMEX:VIXY","AMEX:XLY*AMEX:XLK/(AMEX:XLP*AMEX:XLU)","FRED:FEDFUNDS","TVC:US01M","TVC:US02Y","TVC:US03MY","TVC:US05Y","TVC:US10Y","TVC:US20Y","TVC:US30Y","TVC:VIX","DJ:DJT","AMEX:XLE","AMEX:XLF","AMEX:XLI","AMEX:XLK","AMEX:XLP","AMEX:XLU","AMEX:XLV","AMEX:XLY","CBOE:VIX","CBOE:VIX3M","CBOE:VIX9D","CME:6A1!","CME:6B1!","CME:6C1!","CME:6E1!","CME:6J1!","CME:6S1!","NYMEX:CL1!","NYMEX:CL2!","COMEX:HG1!","NYMEX:PL1!","COMEX:SI1!","COMEX:GC1!","CME_MINI:ES1!","NYMEX:NG1!","CBOT_MINI:YM1!","CME_MINI:RTY1!","CBOT:ZT1!","CBOT:ZF1!","CBOT:ZN1!","CBOT:ZB1!","CBOT:UB1!","NYMEX:RB1!","NYMEX:RB2!"]}''')
                # # Printing all the result
                # result = ws.recv()

                ws = create_connection('wss://data.tradingview.com/socket.io/websocket?from=&date=2023_11_13-11_29',headers=headers)
                first = ws.recv()
                ws.send('''~m~784~m~{"m":"set_auth_token","p":["eyJhbGciOiJSUzUxMiIsImtpZCI6IkdaeFUiLCJ0eXAiOiJKV1QifQ.eyJ1c2VyX2lkIjo2NTk4NDI1NiwiZXhwIjoxNjk4OTc3OTUxLCJpYXQiOjE2OTg5NjM1NTEsInBsYW4iOiJwcm9fcHJlbWl1bSIsImV4dF9ob3VycyI6MSwicGVybSI6IiIsInN0dWR5X3Blcm0iOiJ0di1wcm9zdHVkaWVzLHR2LXZvbHVtZWJ5cHJpY2UsdHYtY2hhcnRwYXR0ZXJucyx0di1jaGFydF9wYXR0ZXJucyIsIm1heF9zdHVkaWVzIjoyNSwibWF4X2Z1bmRhbWVudGFscyI6MCwibWF4X2NoYXJ0cyI6OCwibWF4X2FjdGl2ZV9hbGVydHMiOjQwMCwibWF4X3N0dWR5X29uX3N0dWR5IjoyNCwibWF4X292ZXJhbGxfYWxlcnRzIjoyMDAwLCJtYXhfYWN0aXZlX3ByaW1pdGl2ZV9hbGVydHMiOjQwMCwibWF4X2FjdGl2ZV9jb21wbGV4X2FsZXJ0cyI6NDAwLCJtYXhfY29ubmVjdGlvbnMiOjUwfQ.NQh2yFIZNT7pgQGJp8TUOQNReNu4rON2ypc9-8VEy0G0xbGKUsdz_godn8yQz0gXSrcCQFpRaMyG-EESS-At8xf4M90G6HZOv28EzV92YxwWKtljBgaus4b4wLjScxNsPbdFIMNVfmy6IAyHtL9vDiWCrDD_XBhEyR7-VRkgo9w"]}''')
                ws.send('''~m~52~m~{"m":"quote_create_session","p":["qs_RMGANN3F5mzQ"]}''')
                ws.send('''~m~474~m~{"m":"quote_set_fields","p":["qs_RMGANN3F5mzQ","base-currency-logoid","ch","chp","currency-logoid","currency_code","currency_id","base_currency_id","current_session","description","exchange","format","fractional","is_tradable","language","local_description","listed_exchange","logoid","lp","lp_time","minmov","minmove2","original_name","pricescale","pro_name","short_name","type","typespecs","update_mode","volume","value_unit_id","rchp","rtc","country_code","provider_id"]}''')
                ws.send('''~m~876~m~{"m":"quote_add_symbols","p":["qs_RMGANN3F5mzQ","USI:ATHI.NQ-USI:ATLO.NQ","USI:ATHI.US-USI:ATLO.US","AMEX:HYG/CBOT:UB1!","USI:PC","USI:PCC","USI:TICK","USI:TICK.NQ","USI:TICK.US","USI:TICKI","USI:TICKQ","USI:TKVD.US","1/FX:VOLX","AMEX:VIXM/AMEX:VIXY","AMEX:XLY*AMEX:XLK/(AMEX:XLP*AMEX:XLU)","FRED:FEDFUNDS","TVC:US01M","TVC:US02Y","TVC:US03MY","TVC:US05Y","TVC:US10Y","TVC:US20Y","TVC:US30Y","TVC:VIX","DJ:DJT","AMEX:XLE","AMEX:XLF","AMEX:XLI","AMEX:XLK","AMEX:XLP","AMEX:XLU","AMEX:XLV","AMEX:XLY","CBOE:VIX","CBOE:VIX3M","CBOE:VIX9D","CME:6A1!","CME:6B1!","CME:6C1!","CME:6E1!","CME:6J1!","CME:6S1!","NYMEX:CL1!","NYMEX:CL2!","COMEX:HG1!","NYMEX:PL1!","COMEX:SI1!","COMEX:GC1!","CME_MINI:ES1!","NYMEX:NG1!","CBOT_MINI:YM1!","CME_MINI:RTY1!","CBOT:ZT1!","CBOT:ZF1!","CBOT:ZN1!","CBOT:ZB1!","CBOT:UB1!","NYMEX:RB1!","NYMEX:RB2!","AMEX:TIP","MIL:TIPS","CBOE:VVIX","AMEX:UVIX"]}''')

                result = ws.recv()

                # ws = create_connection('wss://data.tradingview.com/socket.io/websocket?from=&date=2023_11_07-18_13',headers=headers)
                # first = ws.recv()
                # ws.send('''~m~784~m~{"m":"set_auth_token","p":["eyJhbGciOiJSUzUxMiIsImtpZCI6IkdaeFUiLCJ0eXAiOiJKV1QifQ.eyJ1c2VyX2lkIjo2NTk4NDI1NiwiZXhwIjoxNjk4OTc3OTUxLCJpYXQiOjE2OTg5NjM1NTEsInBsYW4iOiJwcm9fcHJlbWl1bSIsImV4dF9ob3VycyI6MSwicGVybSI6IiIsInN0dWR5X3Blcm0iOiJ0di1wcm9zdHVkaWVzLHR2LXZvbHVtZWJ5cHJpY2UsdHYtY2hhcnRwYXR0ZXJucyx0di1jaGFydF9wYXR0ZXJucyIsIm1heF9zdHVkaWVzIjoyNSwibWF4X2Z1bmRhbWVudGFscyI6MCwibWF4X2NoYXJ0cyI6OCwibWF4X2FjdGl2ZV9hbGVydHMiOjQwMCwibWF4X3N0dWR5X29uX3N0dWR5IjoyNCwibWF4X292ZXJhbGxfYWxlcnRzIjoyMDAwLCJtYXhfYWN0aXZlX3ByaW1pdGl2ZV9hbGVydHMiOjQwMCwibWF4X2FjdGl2ZV9jb21wbGV4X2FsZXJ0cyI6NDAwLCJtYXhfY29ubmVjdGlvbnMiOjUwfQ.NQh2yFIZNT7pgQGJp8TUOQNReNu4rON2ypc9-8VEy0G0xbGKUsdz_godn8yQz0gXSrcCQFpRaMyG-EESS-At8xf4M90G6HZOv28EzV92YxwWKtljBgaus4b4wLjScxNsPbdFIMNVfmy6IAyHtL9vDiWCrDD_XBhEyR7-VRkgo9w"]}''')
                # ws.send('''~m~83~m~{"m":"quote_create_session","p":["qs_snapshoter_basic-symbol-quotes_IZ0XuizBELqr"]}''')
                # ws.send('''~m~406~m~{"m":"quote_set_fields","p":["qs_snapshoter_basic-symbol-quotes_IZ0XuizBELqr","pro_name","base_name","short_name","description","type","exchange","typespecs","listed_exchange","lp","country_code","provider_id","symbol-primaryname","logoid","base-currency-logoid","currency-logoid","source-logoid","update_mode","source","source2","pricescale","minmov","fractional","visible-plots-set","industry","sector"]}''')
                # ws.send('''~m~93~m~{"m":"quote_add_symbols","p":["qs_snapshoter_basic-symbol-quotes_IZ0XuizBELqr","NYMEX:RB1!"]}''')

                # result =result + ws.recv()

                # ws = create_connection('wss://data.tradingview.com/socket.io/websocket?from=&date=2023_11_07-18_13',headers=headers)
                # first = ws.recv()
                # ws.send('''~m~784~m~{"m":"set_auth_token","p":["eyJhbGciOiJSUzUxMiIsImtpZCI6IkdaeFUiLCJ0eXAiOiJKV1QifQ.eyJ1c2VyX2lkIjo2NTk4NDI1NiwiZXhwIjoxNjk4OTc3OTUxLCJpYXQiOjE2OTg5NjM1NTEsInBsYW4iOiJwcm9fcHJlbWl1bSIsImV4dF9ob3VycyI6MSwicGVybSI6IiIsInN0dWR5X3Blcm0iOiJ0di1wcm9zdHVkaWVzLHR2LXZvbHVtZWJ5cHJpY2UsdHYtY2hhcnRwYXR0ZXJucyx0di1jaGFydF9wYXR0ZXJucyIsIm1heF9zdHVkaWVzIjoyNSwibWF4X2Z1bmRhbWVudGFscyI6MCwibWF4X2NoYXJ0cyI6OCwibWF4X2FjdGl2ZV9hbGVydHMiOjQwMCwibWF4X3N0dWR5X29uX3N0dWR5IjoyNCwibWF4X292ZXJhbGxfYWxlcnRzIjoyMDAwLCJtYXhfYWN0aXZlX3ByaW1pdGl2ZV9hbGVydHMiOjQwMCwibWF4X2FjdGl2ZV9jb21wbGV4X2FsZXJ0cyI6NDAwLCJtYXhfY29ubmVjdGlvbnMiOjUwfQ.NQh2yFIZNT7pgQGJp8TUOQNReNu4rON2ypc9-8VEy0G0xbGKUsdz_godn8yQz0gXSrcCQFpRaMyG-EESS-At8xf4M90G6HZOv28EzV92YxwWKtljBgaus4b4wLjScxNsPbdFIMNVfmy6IAyHtL9vDiWCrDD_XBhEyR7-VRkgo9w"]}''')
                # ws.send('''~m~83~m~{"m":"quote_create_session","p":["qs_snapshoter_basic-symbol-quotes_IZ0XuizBELqr"]}''')
                # ws.send('''~m~406~m~{"m":"quote_set_fields","p":["qs_snapshoter_basic-symbol-quotes_IZ0XuizBELqr","pro_name","base_name","short_name","description","type","exchange","typespecs","listed_exchange","lp","country_code","provider_id","symbol-primaryname","logoid","base-currency-logoid","currency-logoid","source-logoid","update_mode","source","source2","pricescale","minmov","fractional","visible-plots-set","industry","sector"]}''')
                # ws.send('''~m~93~m~{"m":"quote_add_symbols","p":["qs_snapshoter_basic-symbol-quotes_IZ0XuizBELqr","NYMEX:NG1!"]}''')

                # result =result + ws.recv()

                segments = result.split('~m~')

                # Iterate through the segments and parse the JSON
                for segment in segments:
                    if segment:
                        try:
                            json_data = json.loads(segment)
                            if 'lp' in json_data['p'][1]['v']:
                                name = json_data['p'][1]['v']['short_name']
                                lp_value = json_data['p'][1]['v']['lp']
                                try:
                                    lp_volume = json_data['p'][1]['v']['volume']
                                except:
                                    lp_volume =""
                                data[name]=lp_value
                                if lp_volume !="":
                                    data[name+'_Vol']=lp_volume

                                print(f"{name}: {lp_value}")
                        except:
                            pass
                
            
            except Exception as e:
                print(e)
                break


            dt_uk = datetime.now(pytz.timezone('Europe/London'))    
            csv_data = [dt_uk.strftime("%Y:%m:%d %H:%M:%S")]

            for i in range(1,len(csv_header)):
                try:
                    csv_data.append(data[csv_header[i]])
                except:
                    csv_data.append('')
            writer.writerow(csv_data)