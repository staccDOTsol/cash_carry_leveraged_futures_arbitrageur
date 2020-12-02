import os






apikey = os.environ['key']
apisecret = os.environ['secret']
divisor=100
LEV_MAX = 7.5
import requests 
import math
from datetime import timedelta
import datetime
import sys
import threading
import linecache
from time import sleep
coinsto = ['BTC', 'ETH', 'XRP', 'BCH', 'LTC', 'EOS', 'LINK', 'DOT', 'ADA', 'BSV', 'ETC', 'TRX']
wantingold = {}
for coin in coinsto:
    wantingold[coin] = None
import ccxt
binance     = ccxt.binance({'enableRateLimit': True,
"options":{"defaultMarket":"futures"},
'urls': {'api': {
                         'public': 'https://dapi.binance.com/dapi/v1',
                         'private': 'https://dapi.binance.com/dapi/v1',},}
})
levs = {}

#print(dir(binance))
abc=432#sleep(1)
SECONDS_IN_DAY      = 3600 * 24
from cryptofeed import FeedHandler
from cryptofeed import FeedHandler
from cryptofeed.callback import BookCallback, TickerCallback, TradeCallback
from cryptofeed.defines import TICKER_FUTURES, TICKER_OKS, BID, ASK, FUNDING, L2_BOOK, OPEN_INTEREST, TICKER, TRADES
from cryptofeed.exchanges import OKEx, KrakenFutures, BinanceFutures, FTX
from cryptofeed.exchanges import HuobiDM as hdm
fh = FeedHandler()
fundingwinners = []
from flask import Flask

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from flask import jsonify

minArb = 0.015
print(minArb)

minArb = minArb * 75
print(minArb)
minArb = minArb * 365 
print(minArb)
premiumwinners = []
@app.route('/json')
def summary():
    global fundingwinners, premiumwinners
    return jsonify({'premiumwinners': premiumwinners, 'fundingwinners': fundingwinners})

def loop_in_thread():
    fh.run()
def loop_in_thread2():
    app.run(host='0.0.0.0', port=8080)

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    string = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    print    (string)
    if 'UNI' not in string and 'PostCross' not in string and 'PostFuture' not in string:
        abc=432#sleep(0.1)
#        if 'Account does not have enough margin for order' not in string:
            #abc=432#sleep(1)
async def ticker(feed, pair, bid, ask, timestamp, ex):
    global mids
    #print(f'Ex?: {ex} Timestamp: {timestamp} Feed: {feed} Pair: {pair} Bid: {bid} Ask: {ask}')
    if 'OKEX' in feed.upper():
        ex = 'ftx'
        if 'USDT' not in pair:
            name = pair.split('-')[0]
            if '-' not in pair:
                return
            dt = pair[-4:]
            if dt == 'SWAP':
                dt = 'PERP'
            #print(pair)
        else:
            return
    elif 'FTX' in feed:
        ex = 'ftx'
        name = pair.split('-')[0]
        if '-' not in pair:
            return
        dt = pair.split('-')[1]
        #print(dt)
    elif 'KRAKEN' in feed:
        if 'PI' in pair:
            p = pair.split('_')[1]
            name = p.replace('USD','').replace('XBT','BTC')
            dt = 'PERP'
        else:
            name = pair.split('_')[1].split('_')[0].replace('USD', '').replace('XBT', 'BTC')
            dt = pair[-4:]
        ex = 'kraken'
    elif 'BINANCE' in feed:
        #ETH-USD_200925
        name = pair.split('-')[0]
        dt = pair[-4:]
        ex = 'binance'
        #print(dt)
 
   # abc=123#Print(feed + '-' + name + '-' + dt +': ' + str( 0.5 * ( float(bid) + float(ask))))
    mids[ex][name + '-' + dt] = 0.5 * ( float(ask) + float(bid))
    bids[ex][name + '-' + dt] = float(bid)
    asks[ex][name + '-' + dt] = float(ask) 
pairs = {}
async def book(feed, pair, book, timestamp, receipt_timestamp):
    global mids, pairs
    hb = 0
    la = 99999999999999
    for bid in book[BID]:
        if bid > hb:
            hb = bid
    for ask in book[ASK]:
        if ask < la:
            la = ask
    #print(pair)
    dt = pair[-4:]

    name = pair.split('21')[0].split('21')[0].split('20')[0].split('20')[0]
    pairs[name + '-' + dt] = pair
    #print(name)
  #  if 'BTC' in name and lastex != feed and lastbtc != 0.5 * ( float(bid) + float(ask)):
    #    lastex = feed
   #     lastbtc = 0.5 * ( float(bid) + float(ask))
        #print(feed + '-' + name + '-' + dt +': ' + str( 0.5 * ( float(bid) + float(ask))))
    #print(pair)
    #print(name + '-' + dt)
    if name in coinsto:
        mids['huobi'][name + '-' + dt] = 0.5 * ( float(la) + float(hb))
        #print(mids)
        bids['huobi'][name + '-' + dt] = float(hb)
        asks['huobi'][name + '-' + dt] = float(la) 
    #print(f'Timestamp: {timestamp} Feed: {feed} Pair: {pair} Book Bid Size is {len(book[BID])} Ask Size is {len(book[ASK])}')
def cancelall():
    try:
        #print()
        """
        ords = ftx.fetchOpenOrders( )
        for order in ords:
            ###print(order)
            oid = order['info'] ['id']
            #print(order)
           # abc=432#sleep(100)
           # ##print(order)
            try:
                
                ftx.cancelOrder( oid , order['info']['future'])
            except Exception as e:
                PrintException()

        """
    except Exception as e:
        PrintException()
arbwinnersavg = []
arbwinnersc = []
maxmax = 0
def doCalc():
    try:
        offsets = {}
        hspot.privatePostOrderOrdersBatchCancelOpenOrders()
        global premiumwinners, arbwinnersc, arbwinnersavg, maxmax, mids
        
        for contract in huobisw:
            if contract.split('-')[0] in huobis and contract.split('-')[0] in coinsto:
                data = requests.get("https://api.hbdm.com/swap-ex/market/detail/merged?contract_code=" + contract).json()['tick']
                ask = data['ask'][0]
                bid = data['bid'][0]
                name = contract.split('-')[0]
                dt = 'PERP'
                ex = 'huobi'
                mids[ex][name + '-' + dt] = 0.5 * ( float(ask) + float(bid))
                bids[ex][name + '-' + dt] = float(bid)
                asks[ex][name + '-' + dt] = float(ask) 
                #print(name)
        #print(1)
        dts = []
        coins = []
        tempmids = mids
        for ex in tempmids:
            for coin in tempmids[ex]:
                
                #print(coin)
                if '-' in coin:
                    if coin.split('-')[1] not in dts:
                        dts.append(coin.split('-')[1])
                    if coin.split('-')[0] not in coins:
                        coins.append(coin.split('-')[0].split('20')[0].split('21')[0])
        arbs = {}
        exes = {}
        #print(expis)
        for contract in huobis:
            for exp in expis:
                sizeIncrements[contract + '-' + exp] = sizeIncrements[contract]
                
        for coin in coins:
            arbs[coin] = {}
            exes[coin] = {}
            for ex in tempmids:
                for dt in expis:
                    arbs[coin][dt] = []
                    exes[coin][dt] = {}
        for coin in coins:
            for ex in tempmids:
                for dt in tempmids[ex]:
                    try:
                        if '-' in dt:
                         exes[coin][dt.split('-')[1]][tempmids[ex][dt]] = ex
                    except:
                        abc=123
                      #  PrintException()
                   # abc=123#Print(dt)
                    if coin in dt:
                        
                        try:
                            if '-' in dt:
                                if 'e' not in str(tempmids[ex][dt]):
                                
                                    arbs[coin][dt.split('-')[1]].append(tempmids[ex][dt])
                                
                        except:
                            PrintException()
                            abc=123
        
        
        perps = {}
        lalaexes = {}
        for coin in coins:
            for ex in tempmids:
                for dt in tempmids[ex]:
                   # abc=123#Print(dt)
                    if coin in dt and 'PERP' in dt:
                        perps[coin] = tempmids[ex][dt]
                        lalaexes[coin] = ex
                        
        for coin in arbs:
            for dt in arbs[coin]:
                try:
                    if '-' in dt:
                        if 'e' not in str(perps[coin]):
                            arbs[coin][dt].append(perps[coin])
                            exes[coin][dt][perps[coin]] = lalaexes[coin]
                except:
        #            PrintException()
                    PrintException()
        #print(exes)
        #print(arbs)
        #print(expis)
        thearbs = []
        coinarbs = {}
        minmax = {}
        windts = {}
        winprices = {}
        #print(2)
        for coin in arbs:
            minmax[coin] = []
            windts[coin] = {}
            winprices[coin] = {}
            for dt in expis:
                if dt != 'PERP':
                    try:
                        #print(len(arbs[coin][dt]))
                        #if len(arbs[coin][dt]) > 0:
                        minmax[coin].append(math.fabs(tempmids['huobi'][coin + '-' + dt] - tempmids['huobi'][coin + '-PERP']))
                        windts[coin][math.fabs(tempmids['huobi'][coin + '-' + dt] - tempmids['huobi'][coin + '-PERP'])] = dt
                        winprices[coin][math.fabs(tempmids['huobi'][coin + '-' + dt] - tempmids['huobi'][coin + '-PERP'])] = tempmids['huobi'][coin + '-' + dt]
                        #minimum = tempmids['ftx'][coin + '-PERP']  #10900/10709 #pos long perp, neg short perp
                    except:
                        PrintException()
                        abc=123
        for coin in arbs:

            try:
                maximum = max(minmax[coin])
                
                windt = windts[coin][maximum]
                maximum = winprices[coin][maximum]
                minimum = tempmids['huobi'][coin + '-PERP']
                #maximum = tempmids['ftx'][coin + '-' + dt] #pos short fut, neg long fut #pos long perp, neg short perp
     #           if coin == 'BTC':
     ##               abc=123#Print(arbs[coin][dt])
      #              abc=123#Print(maximum / minimum)
                thearb = ((((maximum / minimum)-1)*100)*365*levs[coin]) #1.1/1.05 = 
                #print(thearb)
                #print(expis[dt])
                #print('thearb of ' + coin + ' at ' + dt + ' in total ' + str(thearb)) 
                thearb = thearb / expis[windt] 
                
                #print(thearb)
                #print( ' ' )
                thearb = thearb #- 36
                coinarbs[thearb] = coin + '-' + windt 
                if thearb > 50 or thearb < -50:
                    thearbs.append(thearb)
                    abc=123#Print(thearb)
                    #print(coinarbs[thearb])
                    abc=123#Print(windt)
                    abc=123#Print(maximum)
                    abc=123#Print(minimum)
                else:
                    thearbs.append(0)
                """
                if thearb > 10 and coin != 'USDT':
                   # abc=123#Print(exes[coin][dt])
                    thearbs.append({'exlong': exes[coin][dt][minimum], 'exshort': exes[coin][dt][maximum], 'coin': coin, 'thearb': thearb, 'dt': dt, 'arbscoindt': arbs[coin][dt]})
                    abc=123#Print({'exlong': exes[coin][dt][minimum], 'exshort': exes[coin][dt][maximum], 'coin': coin, 'thearb': thearb, 'dt': dt, 'arbscoindt': arbs[coin][dt]})
                """
              #  abc=123#Print('and after figuring out daily arb it\'s ' +  str(thearb))
                
            except:
                PrintException()
                PrintException()
                PrintException()
        t = 0
        c = 0
        #print(3)
        #print(thearbs)
        for arb in thearbs:
            
            t = t + math.fabs(arb)
            if arb != 0:
                c = c + 1
        percs = {}
        wanting = {}
        if c > 0:
            avg = t / c
            c1 = c
            
            t = 0 
            c = 0 
            maxi = 0
            for arb in thearbs:
                if math.fabs(arb) > avg:
                    abc=123#Print(coinarbs[arb] + ' is a good coin no?')
                    if arb > maxi:
                        maxi = arb
                    if arb > maxmax:
                        maxmax = arb
                    t = t + math.fabs(arb)
                    c = c + 1
            for arb in thearbs:
                try:
                    if arb in coinarbs:
                        if '-' in coinarbs[arb]:
                            if math.fabs(arb) > avg:
                                percs[coinarbs[arb].split('-')[0]] = arb / t
                                if coinarbs[arb] in usdpos: #-0.3 * 10 * 100 + 360 #-0.16*400*10+1826=1186
                                                                                   #-0.16*400*10-266=-906
                                    wanting[coinarbs[arb]] = arb / t * (levs[coinarbs[arb].split('-')[0]]) * balance
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * -1
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] # - usdpos[coinarbs[arb]]
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] / (levs[coinarbs[arb].split('-')[0]])
                                    wanting[coinarbs[arb]] = round(wanting[coinarbs[arb]] / 10) * 10
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * (levs[coinarbs[arb].split('-')[0]])
                                
                                else:
                                    wanting[coinarbs[arb]] = arb / t * (levs[coinarbs[arb].split('-')[0]]) * balance
                                    
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * -1
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] / (levs[coinarbs[arb].split('-')[0]])
                                    wanting[coinarbs[arb]] = round(wanting[coinarbs[arb]] / 10) * 10
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * (levs[coinarbs[arb].split('-')[0]])
                                if coinarbs[arb].split('-')[0] + '-PERP' in usdpos:
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  percs[coinarbs[arb].split('-')[0]] * (levs[coinarbs[arb].split('-')[0]]) * balance #- usdpos[coinarbs[arb].split('-')[0] + '-PERP']
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] / (levs[coinarbs[arb].split('-')[0]])
                                    
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = round(wanting[coinarbs[arb].split('-')[0] + '-PERP'] / 10) * 10
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] * (levs[coinarbs[arb].split('-')[0]])
                                else:
                                   # if percs[coinarbs[arb].split('-')[0]] > 0:
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  percs[coinarbs[arb].split('-')[0]] * LEV_MAX * balance
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] / (levs[coinarbs[arb].split('-')[0]])
                                    
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = round(wanting[coinarbs[arb].split('-')[0] + '-PERP'] / 10) * 10
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] * (levs[coinarbs[arb].split('-')[0]])
                                
                            else:
                                #if arb != 0:
                                
                                if arb in coinarbs:
                                    if '-' in coinarbs[arb]:
                                        percs[coinarbs[arb].split('-')[0]] = 0
                                        if coinarbs[arb] in usdpos:
                                        
                                            wanting[coinarbs[arb]] = -1 #* usdpos[coinarbs[arb]]
                                            wanting[coinarbs[arb]] = wanting[coinarbs[arb]] / (levs[coinarbs[arb].split('-')[0]])
                                            wanting[coinarbs[arb]] = round(wanting[coinarbs[arb]] / 10) * 10
                                            wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * (levs[coinarbs[arb].split('-')[0]])
                                        else:
                                            
                                            wanting[coinarbs[arb]] = 0
                                        if coinarbs[arb].split('-')[0] + '-PERP' in usdpos:
                                            wanting[coinarbs[arb].split('-')[0] + '-PERP'] = -1 #* usdpos[coinarbs[arb].split('-')[0] + '-PERP']
                                            wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] / (levs[coinarbs[arb].split('-')[0]])
                                
                                            wanting[coinarbs[arb].split('-')[0] + '-PERP'] = round(wanting[coinarbs[arb].split('-')[0] + '-PERP'] / 10) * 10
                                            wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] * (levs[coinarbs[arb].split('-')[0]])
                                        else:
                                        
                                            wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  0
                                                
                                    
                            
                except:
                    PrintException()
            #print(wanting)
            #print(4)
            for pos2 in usdpos:
                if pos2 not in wanting:
                    if usdpos[pos2] != 0:
                        #wanting[pos2] = -1 * usdpos[pos2]
                        abc=123#Print(pos2)
                        abc=123#Print(wanting)
                        #abc=432#sleep(10)
            abc=123#Print(wanting)
            """
            twanting = {}
            futwants = {}
            lowers = {}
            counts = {}
            twanting = {}
            for arb in wanting:
                lowers[arb] = 999999999999999
                counts[arb.split('-')[0]] = 0
                
                twanting[arb] = 0
            for arb in wanting:
                if 'PERP' not in arb:
                    futwants[arb.split('-')[0]] = 0
                    
                    counts[arb.split('-')[0]] = counts[arb.split('-')[0]] + 1
                    #twanting[arb.split('-')[0] + '-PERP'] = wanting[arb.split('-')[0] + '-PERP'] + wanting[arb]
            
            for arb in wanting:
                if 'PERP' not in arb:
                    futwants[arb.split('-')[0]] = futwants[arb.split('-')[0]] + wanting[arb]
                    
            for arb in futwants:
                for coin in wanting:
                    if 'PERP' in coin:
                        twanting[coin] = futwants[coin.split('-')[0]] * -1
                    else:
                        twanting[coin] = wanting[coin]
            wanting = twanting
            """
            print(wanting)
            abc=432#sleep(1)
            
           # wanting = twanting
            for arb in wanting:
                try:
                    coin = arb
                    wanting[coin] = wanting[coin]  / (240) #/ mids['huobi'][coin]
                    
                    #   round(0.1 * (0.1)) / 0.1
                    # abc = -937.0961358420444
                    # abc = abc / 28 / 10
                    # abc = ( round(abc * (0.1)) / 0.1)
                    wanting[coin] = round(wanting[coin] / 10) * 1
                    if arb.split('-')[0] not in swapbs:
                        swapbs[arb.split('-')[0]] = 0
                    if arb.split('-')[0] not in futbs:
                        futbs[arb.split('-')[0]] = 0
                    if arb not in usdpos:
                        usdpos[arb] = 0
                    offsets[arb] = 'open'
                    print(arb)
                    print(swapbs[arb.split('-')[0]])
                    print(futbs[arb.split('-')[0]] * 1.25)
                    print(futbs[arb.split('-')[0]] * 0.75)
                    
                    if 'PERP' not in arb and swapbs[arb.split('-')[0]] < futbs[arb.split('-')[0]] * 0.4 or 'PERP' not in arb and swapbs[arb.split('-')[0]] > futbs[arb.split('-')[0]] * 2:
                        print('bad ' + arb)
                        offsets[arb] = 'close'
                        toborrow = 15 / mids['huobi'][arb]
                        tocheck = toborrow
                        arandom = random.randint(1,10) / 10
                        try:
                            print(str( arandom * math.fabs(round((toborrow) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])))
                            hspot.v2PrivatePostAccountTransfer({'from': 'swap', 'to': 'spot', 'currency': arb.split('-')[0].lower(), 'amount': str(arandom * math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]]))}) 
                        except:
                            PrintException()
                        try:
                            print(str(arandom * math.fabs(round((toborrow) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])))
                            hspot.privatePostFuturesTransfer({'type': 'futures-to-pro', 'currency': arb.split('-')[0].lower(), 'amount': str( arandom *math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]]))})
                        except:
                            PrintException()
                        try:

                            borrowed = hspot.privatePostOrderOrdersPlace({'account-id':str(accountnum),'symbol': arb.split('-')[0].lower() + 'usdt', 'type': 'sell-limit', 'amount':  str( arandom *math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])), 'price': str(mids['spot'][arb.split('-')[0].lower() + 'usdt']['ask'])})   
                            #borrowed = hspot.privatePostCrossMarginOrders({'symbol': arb.split('-')[0].lower() + 'usdt', 'currency': arb.split('-')[0].lower(), 'amount':  str( round((toborrow * 1.01) * 1000)/ 1000)})   
                            #print(borrowed)   
                        except:
                            PrintException()
                        offset = offsets[coin]

                        direction = 'buy'
                        prc = bids['huobi'][coin]
                        go = True
                        if coin.split('-')[0] not in skews:
                            skews[coin.split('-')[0]] = 0
                        if wanting[coin] > 0:
                            go = True
                            abc=123#Print('1')
                            try:
                                if skews[coin.split('-')[0]] > wanting[coin] * 0.8:# * mids['huobi'][coin]:
                                    abc=123#Print('cancel2!')
                                    #ords = ftx.fetchOpenOrders( coin )
                                    gogo = True
                                    #for o in ords:
                                    #    ftx.cancelOrder( o['info']['id'] , o['info']['future'])
                                    #go = False
                            except:
                                PrintException()
                        if wanting[coin] < 0:
                            go = True
                            abc=123#Print('3')
                            try:
                                if skews[coin.split('-')[0]] < wanting[coin] * 0.8: #* tempmids['huobi'][coin]:   
                                    
                                    #ords = ftx.fetchOpenOrders( coin )
                                    gogo = True
                                    #for o in ords:
                                    #    ftx.cancelOrder( o['info']['id'] , o['info']['future'])
                                    #print('cancel!')
                                    #go = False
                            except:
                                PrintException()
                            wanting[coin] = wanting[coin] * -1
                            direction = 'sell'
                            prc = asks['huobi'][coin]
                        
                        if go == True:
                            #print(62)
                            #print(wanting[coin])
                            #print(direction)
                            #print(direction == 'sell' and skews[coin.split('-')[0]]  / 10 > wanting[coin] * 0.8)
                            #print(direction == 'buy' and skews[coin.split('-')[0]]  / 10 < wanting[coin] * 0.8)
                           # abc=432#sleep(1)
                            try:
                                #ords = ftx.fetchOpenOrders( coin )
                                gogo = True
                                if 'PERP' not in coin:
                                    ords = hfutures.privatePostContractOpenorders({'symbol': coin.split('-')[0]})
                                    
                                    #print(63)
                                    for o in ords['data']['orders']:
                                        if direction == o['direction'] and o['symbol'] in coin:
                                            #gogo = False
                                            #qty = o['volume'] 
                                            if direction == 'sell' and skews[coin.split('-')[0]] / 10 > wanting[coin] * 0.8  or direction == 'buy' and skews[coin.split('-')[0]] / 10 < wanting[coin] * 0.8 :
                                                if prc != o['price']:
                                                    ordid = o['order_id']
                                                    e = hfutures.privatePostContractCancel( {'symbol': coin.split('-')[0], 'order_id': str(ordid)} )
                                                    #print(e)
                                            """
                                            elif offset == 'close':
                                                if wanting[coin] == 0:
                                                    wanting[coin] = 1
                                                if prc != o['price']:
                                                    ordid = o['order_id']
                                                    e = hfutures.privatePostContractCancel( {'symbol': coin.split('-')[0], 'order_id': str(ordid)} )
                                                    #print(e)
                                            """
                                            PrintException()
                                
                                    if gogo == True:
                                        if direction == 'sell' and skews[coin.split('-')[0]]  / 10 > wanting[coin] * 0.8  or direction == 'buy' and skews[coin.split('-')[0]]  / 10 < wanting[coin] * 0.8:
                                            #if usdpos[coin.split('-')[0]] < wanting[coin]:
                                            #    offset = 'open'
                                            #else:
                                            #    offset = 'close'    
                                            #print(offset)
                                            print('futs')
                                            print(coin)
                                            print(offset)

                                            print(wanting[coin])
                                            if offset == 'close' and direction == 'sell':
                                                direction = 'sell'
                                                e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                                direction = 'buy'
                                                e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                            elif offset == 'close' and direction == 'buy':
                                                direction = 'sell'
                                                e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                                direction = 'buy'
                                                e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                            #Print( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': wanting[coin], 'direction': direction, 'lever_rate': 5, 'order_price_type': 'post_only'})
                                            elif offset =='open':
                                                e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                        """
                                        elif offset == 'close':
                                            if wanting[coin] == 0:
                                                wanting[coin] = 1
                                            #print(offset)
                                            #Print( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': wanting[coin], 'direction': direction, 'lever_rate': 5, 'order_price_type': 'post_only'})
                                            h1 = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': wanting[coin], 'direction': direction, 'lever_rate': 5, 'order_price_type': 'post_only'})
                                            #print(h1)
                                        """
                                else:
                                    #print(64)
                                    ords = hswap.privatePostSwapOpenorders({'contract_code': coin.replace('PERP', 'USD')})
                                    
                                    for o in ords['data']['orders']:
                                        if direction == o['direction'] and o['symbol']  == coin.split('-')[0]:
                                            #ogo = False
                                            qty = o['volume'] 
                                            if direction == 'sell' and skews[coin.split('-')[0]]  / 10> wanting[coin] * 0.8 or direction == 'buy' and skews[coin.split('-')[0]] / 10 < wanting[coin] * 0.8:
                                                if prc != o['price']:
                                                    ordid = o['order_id']
                                                    e = hswap.privatePostSwapCancel( {'contract_code': coin.replace('PERP', 'USD'), 'order_id': str(ordid)} )
                        #                            print(e)
                                            """
                                            elif offset == 'close':

                                                if wanting[coin] == 0:
                                                    wanting[coin] = 1
                                                if prc != o['price']:
                                                    ordid = o['order_id']
                                                    e = hswap.privatePostSwapCancel( {'contract_code': coin.replace('PERP', 'USD'), 'order_id': str(ordid)} )
                                                    #print(e)
                                            """
                                            PrintException()
                                
                                    if gogo == True:
                                        if direction == 'sell' and skews[coin.split('-')[0]]  / 10 > wanting[coin] * 0.8  or direction == 'buy' and skews[coin.split('-')[0]]  / 10 < wanting[coin] * 0.8 :
                                            #if usdpos[coin.split('-')[0]] < wanting[coin]:
                                            #    offset = 'open'
                                            #else:
                                            #    offset = 'close'  
                                            #print(offset)
                                            print('swap')
                                            print(coin)
                                            print(offset)
                                            if offset == 'close' and direction == 'sell':
                                                direction = 'buy'
                                                e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                                direction = 'sell'
                                                e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                            elif offset == 'close' and direction == 'buy':
                                                direction = 'buy'
                                                e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                                direction = 'sell'
                                                e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                            elif offset == 'open':
                                                print(wanting[coin])
                                                e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                                print(e)
                                        """"
                                        elif offset == 'close':

                                            if wanting[coin] == 0:
                                                wanting[coin] = 1
                                            #print(offset)
                                            h2 = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': wanting[coin], 'direction': direction, 'lever_rate': 5, 'order_price_type': 'post_only'})
                                            #print(h2)
                                        """
                            except:        

                                PrintException()
                    #if 'PERP' in arb:
                    toborrow = math.fabs(wanting[arb]) / (levs[arb.split('-')[0]])
                    toborrow = math.floor((toborrow * 1.02) / 10) * 10 
                    #if arb in wantingold:
                    #    tocheck = math.fabs(wantingold[arb]) / LEV_MAX
                    #    tocheck = math.floor((tocheck * 1.02) / 10) * 10 
                    #else:
                    tocheck = toborrow
                    if arb.split('-')[0] in swapbs:
                        toborrow = toborrow - swapbs[arb.split('-')[0]] * 2#1.2345 * 1000
                    elif arb in futbs:
                        toborrow = toborrow - futbs[arb] * 2#1.2345 * 1000
                    #print(toborrow)
                    #if toborrow > 0:
            
            
                    toborrow = toborrow / mids['huobi'][arb]
                    toborrow = math.fabs(toborrow)
                    #tocheck = tocheck / mids['huobi'][arb]
                    tocheck = math.fabs(tocheck)
                    abc=123#Print(toborrow)
                    toborrow = math.floor(toborrow * 1000) / 1000
                    abc=123#Print(arb)
                    abc=123#Print(toborrow)
                    abc=123#Print({'symbol': arb.split('-')[0].lower() + 'usdt', 'currency': arb.split('-')[0].lower(), 'amount':  str( toborrow)})
                    
                    if tocheck > 0 or tocheck < 0:
                        #print(tocheck  > usdpos[arb]* 10 - balance / 16)
                        if tocheck > usdpos[arb] * 10 - balance / 16:
                            wantingold[arb.split('-')[0]] = toborrow * mids['huobi'][arb]
                            try:
                                print(str( math.fabs(round((0.1*toborrow * mids['huobi'][arb]) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])))
                                print(str( math.fabs(round((0.1*toborrow) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])))
                                borrowed = hspot.privatePostOrderOrdersPlace({'account-id':str(accountnum),'symbol': arb.split('-')[0].lower() + 'usdt', 'type': 'buy-limit', 'amount':  str( math.fabs(round((0.1*toborrow ) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])), 'price': str(mids['spot'][arb.split('-')[0].lower() + 'usdt']['bid'])})   
                                #borrowed = hspot.privatePostCrossMarginOrders({'symbol': arb.split('-')[0].lower() + 'usdt', 'currency': arb.split('-')[0].lower(), 'amount':  str( round((toborrow * 1.01) * 1000)/ 1000)})   
                                #Print(borrowed)         
                            except Exception as e:
                                PrintException()
                                abc=432#sleep(2)
                        #print(tocheck < usdpos[arb] * 10 + balance / 16)
                        #print( ' ' )
                        print(' ')
                        print(arb)
                        print(tocheck)
                        print(usdpos[arb]* 10 )
                        print(balance / 16)
                        print(tocheck < usdpos[arb]* 10 + balance / 16)       
                        if tocheck < usdpos[arb]* 10 + balance / 16:
                            offsets[arb] = 'close'
                            wantingold[arb.split('-')[0]] = toborrow * mids['huobi'][arb]
                            try:
                                arandom = random.randint(1,10) / 10
                                try:
                                    print(str( arandom * math.fabs(round((toborrow) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])))
                                    hspot.v2PrivatePostAccountTransfer({'from': 'swap', 'to': 'spot', 'currency': arb.split('-')[0].lower(), 'amount': str(arandom * math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]]))}) 
                                except:
                                    PrintException()
                                try:
                                    print(str(arandom * math.fabs(round((toborrow) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])))
                                    hspot.privatePostFuturesTransfer({'type': 'futures-to-pro', 'currency': arb.split('-')[0].lower(), 'amount': str( arandom *math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]]))})
                                except:
                                    PrintException()
                                try:

                                    borrowed = hspot.privatePostOrderOrdersPlace({'account-id':str(accountnum),'symbol': arb.split('-')[0].lower() + 'usdt', 'type': 'sell-limit', 'amount':  str( arandom *math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])), 'price': str(mids['spot'][arb.split('-')[0].lower() + 'usdt']['ask'])})   
                                    #borrowed = hspot.privatePostCrossMarginOrders({'symbol': arb.split('-')[0].lower() + 'usdt', 'currency': arb.split('-')[0].lower(), 'amount':  str( round((toborrow * 1.01) * 1000)/ 1000)})   
                                    #print(borrowed)   
                                except:
                                    PrintException()
                                """
                                try:
                                    hspot.privatePostCrossMarginTransferIn({'currency': arb.split('-')[0].lower(), 'amount': str(toborrow / mids['huobi'][arb])})
                                except:
                                    PrintException()
                                try:
                                    loans = hspot.privateGetCrossMarginLoanOrders({'size': "100",'currency': arb.split('-')[0].lower(), 'state': 'accrual'})
                                except:
                                    PrintException()
                                for l in loans['data']:
                                    try:
                                        if float(l['loan-balance']) > 0:
                                            torepay = float(l['loan-balance'])
                                            torepayi = float(l['interest-amount'])
                                            try:
                                                hspot.v2PrivatePostAccountTransfer({'from': 'swap', 'to': 'spot', 'currency': arb.split('-')[0].lower(), 'amount': str(torepayi / 2)}) 
                                            except:
                                                PrintException()
                                            try:
                                                hspot.privatePostFuturesTransfer({'type': 'futures-to-pro', 'currency': arb.split('-')[0].lower(), 'amount': str(torepayi / 2)})
                                            except:
                                                PrintException()
                                            try:
                                                hspot.privatePostCrossMarginTransferIn({'currency': arb.split('-')[0].lower(), 'amount': str(torepayi)})
                                            except:
                                                PrintException()
                                            identifier = l['id']
                                            hspot.privatePostCrossMarginOrdersIdRepay({'id': identifier, 'amount': str(torepay)})
                                            #hspot.privatePostCrossMarginOrdersIdRepay({'id': identifier, 'amount': str(toborrow / mids['huobi'][arb])})
                                    except Exception as e:
                                        PrintException()
                                        abc=432#sleep(2)
                                """               
                            except Exception as e:
                                PrintException()
                                abc=432#sleep(2)
                                
                            
                        #print(borrowed)
                        #print(5)
                        abc=123#Print('111')
                        abc=123#Print(wanting)
                except:
                    PrintException()
            for arb in thearbs:
                try:
                
                    if arb in coinarbs:
                        if '-' in coinarbs[arb]:
                            if math.fabs(arb) > avg:
                                percs[coinarbs[arb].split('-')[0]] = arb / t
                                if coinarbs[arb] in usdpos: #-0.3 * 10 * 100 + 360 #-0.16*400*10+1826=1186
                                                                                   #-0.16*400*10-266=-906
                                    wanting[coinarbs[arb]] = arb / t * (levs[coinarbs[arb].split('-')[0]]) * balance
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * -1
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]]  - usdpos[coinarbs[arb]] * 10
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] / (levs[coinarbs[arb].split('-')[0]])
                                    wanting[coinarbs[arb]] = round(wanting[coinarbs[arb]] / 10) * 10
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * (levs[coinarbs[arb].split('-')[0]])
                                
                                else:
                                    wanting[coinarbs[arb]] = arb / t * (levs[coinarbs[arb].split('-')[0]]) * balance
                                    
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * -1
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] / (levs[coinarbs[arb].split('-')[0]])
                                    wanting[coinarbs[arb]] = round(wanting[coinarbs[arb]] / 10) * 10
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * (levs[coinarbs[arb].split('-')[0]])
                                if coinarbs[arb].split('-')[0] + '-PERP' in usdpos:
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  percs[coinarbs[arb].split('-')[0]] * (levs[coinarbs[arb].split('-')[0]]) * balance - usdpos[coinarbs[arb].split('-')[0] + '-PERP'] * 10
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] / (levs[coinarbs[arb].split('-')[0]])
                                    
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = round(wanting[coinarbs[arb].split('-')[0] + '-PERP'] / 10) * 10
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] * (levs[coinarbs[arb].split('-')[0]])
                                else:
                                   # if percs[coinarbs[arb].split('-')[0]] > 0:
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  percs[coinarbs[arb].split('-')[0]] * (levs[coinarbs[arb].split('-')[0]]) * balance
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] / (levs[coinarbs[arb].split('-')[0]])
                                    
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = round(wanting[coinarbs[arb].split('-')[0] + '-PERP'] / 10) * 10
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] * (levs[coinarbs[arb].split('-')[0]])
                                
                            else:
                                #if arb != 0:
                                percs[coinarbs[arb].split('-')[0]] = 0
                                if coinarbs[arb] in usdpos:
                                
                                    wanting[coinarbs[arb]] = -1 * usdpos[coinarbs[arb]] * 10
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] / 10
                                    wanting[coinarbs[arb]] = round(wanting[coinarbs[arb]] / 10) * 10
                                    wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * 10
                                else:
                                    
                                    wanting[coinarbs[arb]] = 0
                                if coinarbs[arb].split('-')[0] + '-PERP' in usdpos:
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = -1 * usdpos[coinarbs[arb].split('-')[0] + '-PERP'] * 10
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] / 10
                        
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = round(wanting[coinarbs[arb].split('-')[0] + '-PERP'] / 10) * 10
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] = wanting[coinarbs[arb].split('-')[0] + '-PERP'] * 10
                                else:
                                
                                    wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  0
                                        
                            
                    
                except:
                    PrintException()
            for pos2 in usdpos:
                if pos2 not in wanting:
                    if usdpos[pos2] != 0:
                        wanting[pos2] = -1 * usdpos[pos2] * 10
                        abc=123#Print(pos2)
                        abc=123#Print(wanting)
                        #abc=432#sleep(10)
            #print(6)
            abc=123#Print(wanting)
            """
            twanting = {}
            futwants = {}
            lowers = {}
            counts = {}
            twanting = {}
            for arb in wanting:
                lowers[arb] = 999999999999999
                counts[arb.split('-')[0]] = 0
                
                twanting[arb] = 0
            for arb in wanting:
                if 'PERP' not in arb:
                    futwants[arb.split('-')[0]] = 0
                    
                    counts[arb.split('-')[0]] = counts[arb.split('-')[0]] + 1
                    #twanting[arb.split('-')[0] + '-PERP'] = wanting[arb.split('-')[0] + '-PERP'] + wanting[arb]
            
            for arb in wanting:
                if 'PERP' not in arb:
                    futwants[arb.split('-')[0]] = futwants[arb.split('-')[0]] + wanting[arb]
                    
            for arb in futwants:
                for coin in wanting:
                    try:
                        if 'PERP' in coin:
                            twanting[coin] = futwants[coin.split('-')[0]] * -1
                        else:
                            twanting[coin] = wanting[coin]
                    except:
                        abc=123
            wanting = twanting
            """
            print(wanting)
           
            
            #pos short fut, neg long fut #pos long perp, neg short perp
            for coin in wanting:
                #wanting[coin] = round(wanting[coin] / (100 * 10)) * (100 * 10) 
                wanting[coin] = wanting[coin]  / (240) #/ mids['huobi'][coin]
                #   round(0.1 * (0.1)) / 0.1
                # abc = -937.0961358420444
                # abc = abc / 28 / 10
                # abc = ( round(abc * (0.1)) / 0.1)
                wanting[coin] = round(wanting[coin] / 10) * 1
                
            abc=123#Print('222')
            print(wanting)
                        #wanting = twanting
            abc=123#Print(twanting)
            
            abc=123#Print(wanting)      
            
            #for arb in wanting:
            #    if wanting[arb] < lowers[arb]:
            #        lowers[arb] = wanting[arb]
            #wanting = lowers
            #print(wanting['CREAM-PERP'])
            #abc=432#sleep(100)
            #Print(wanting)
            for coin in wanting:
                try:
                    #print(61)
                    arb = coin
                    if wanting[arb] == 0 and usdpos[arb] * 10 > 10:
                        print('extra special!')
                        #sleep(1)
                        toborrow = 15 / mids['huobi'][arb]
                        tocheck = toborrow
                        offsets[arb] = 'close'
                        
                        wantingold[arb.split('-')[0]] = toborrow * mids['huobi'][arb]
                        try:
                            arandom = 1
                            try:
                                print(str( arandom * math.fabs(round((toborrow) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])))
                                hspot.v2PrivatePostAccountTransfer({'from': 'swap', 'to': 'spot', 'currency': arb.split('-')[0].lower(), 'amount': str(arandom * math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]]))}) 
                            except:
                                PrintException()
                            try:
                                print(str(arandom * math.fabs(round((toborrow) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])))
                                hspot.privatePostFuturesTransfer({'type': 'futures-to-pro', 'currency': arb.split('-')[0].lower(), 'amount': str( arandom *math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]]))})
                            except:
                                PrintException()
                            try:

                                borrowed = hspot.privatePostOrderOrdersPlace({'account-id':str(accountnum),'symbol': arb.split('-')[0].lower() + 'usdt', 'type': 'sell-limit', 'amount':  str( arandom *math.fabs(round((toborrow / 2) * 10 ** precisions[arb.split('-')[0]])/ 10 ** precisions[arb.split('-')[0]])), 'price': str(mids['spot'][arb.split('-')[0].lower() + 'usdt']['ask'])})   
                                #borrowed = hspot.privatePostCrossMarginOrders({'symbol': arb.split('-')[0].lower() + 'usdt', 'currency': arb.split('-')[0].lower(), 'amount':  str( round((toborrow * 1.01) * 1000)/ 1000)})   
                                #print(borrowed)   
                            except:
                                PrintException()
                            """
                            try:
                                hspot.privatePostCrossMarginTransferIn({'currency': arb.split('-')[0].lower(), 'amount': str(toborrow / mids['huobi'][arb])})
                            except:
                                PrintException()
                            try:
                                loans = hspot.privateGetCrossMarginLoanOrders({'size': "100",'currency': arb.split('-')[0].lower(), 'state': 'accrual'})
                            except:
                                PrintException()
                            for l in loans['data']:
                                try:
                                    if float(l['loan-balance']) > 0:
                                        torepay = float(l['loan-balance'])
                                        torepayi = float(l['interest-amount'])
                                        try:
                                            hspot.v2PrivatePostAccountTransfer({'from': 'swap', 'to': 'spot', 'currency': arb.split('-')[0].lower(), 'amount': str(torepayi / 2)}) 
                                        except:
                                            PrintException()
                                        try:
                                            hspot.privatePostFuturesTransfer({'type': 'futures-to-pro', 'currency': arb.split('-')[0].lower(), 'amount': str(torepayi / 2)})
                                        except:
                                            PrintException()
                                        try:
                                            hspot.privatePostCrossMarginTransferIn({'currency': arb.split('-')[0].lower(), 'amount': str(torepayi)})
                                        except:
                                            PrintException()
                                        identifier = l['id']
                                        hspot.privatePostCrossMarginOrdersIdRepay({'id': identifier, 'amount': str(torepay)})
                                        #hspot.privatePostCrossMarginOrdersIdRepay({'id': identifier, 'amount': str(toborrow / mids['huobi'][arb])})
                                except Exception as e:
                                    PrintException()
                                    abc=432#sleep(2)
                            """               
                        except Exception as e:
                            PrintException()
                            abc=432#sleep(2)
                            

                    if coin not in offsets:
                        offsets[coin] = 'open'
                    offset = offsets[coin]

                    direction = 'buy'
                    prc = bids['huobi'][coin]
                    go = True
                    if coin.split('-')[0] not in skews:
                        skews[coin.split('-')[0]] = 0
                    if wanting[coin] > 0:
                        go = True
                        abc=123#Print('1')
                        try:
                            if skews[coin.split('-')[0]] > wanting[coin] * 0.8:# * mids['huobi'][coin]:
                                abc=123#Print('cancel2!')
                                #ords = ftx.fetchOpenOrders( coin )
                                gogo = True
                                #for o in ords:
                                #    ftx.cancelOrder( o['info']['id'] , o['info']['future'])
                                #go = False
                        except:
                            PrintException()
                    if wanting[coin] < 0:
                        go = True
                        abc=123#Print('3')
                        try:
                            if skews[coin.split('-')[0]] < wanting[coin] * 0.8: #* tempmids['huobi'][coin]:   
                                
                                #ords = ftx.fetchOpenOrders( coin )
                                gogo = True
                                #for o in ords:
                                #    ftx.cancelOrder( o['info']['id'] , o['info']['future'])
                                #print('cancel!')
                                #go = False
                        except:
                            PrintException()
                        wanting[coin] = wanting[coin] * -1
                        direction = 'sell'
                        prc = asks['huobi'][coin]
                    
                    if go == True:
                        #print(62)
                        #print(wanting[coin])
                        #print(direction)
                        #print(direction == 'sell' and skews[coin.split('-')[0]]  / 10 > wanting[coin] * 0.8)
                        #print(direction == 'buy' and skews[coin.split('-')[0]]  / 10 < wanting[coin] * 0.8)
                       # abc=432#sleep(1)
                        try:
                            #ords = ftx.fetchOpenOrders( coin )
                            gogo = True
                            if 'PERP' not in coin:
                                ords = hfutures.privatePostContractOpenorders({'symbol': coin.split('-')[0]})
                                
                                #print(63)
                                for o in ords['data']['orders']:
                                    if direction == o['direction'] and o['symbol'] in coin:
                                        #gogo = False
                                        #qty = o['volume'] 
                                        if direction == 'sell' and skews[coin.split('-')[0]] / 10 > wanting[coin] * 0.8  or direction == 'buy' and skews[coin.split('-')[0]] / 10 < wanting[coin] * 0.8 :
                                            if prc != o['price']:
                                                ordid = o['order_id']
                                                e = hfutures.privatePostContractCancel( {'symbol': coin.split('-')[0], 'order_id': str(ordid)} )
                                                #print(e)
                                        """
                                        elif offset == 'close':
                                            if wanting[coin] == 0:
                                                wanting[coin] = 1
                                            if prc != o['price']:
                                                ordid = o['order_id']
                                                e = hfutures.privatePostContractCancel( {'symbol': coin.split('-')[0], 'order_id': str(ordid)} )
                                                #print(e)
                                        """
                                        PrintException()
                            
                                if gogo == True:
                                    if direction == 'sell' and skews[coin.split('-')[0]]  / 10 > wanting[coin] * 0.8  or direction == 'buy' and skews[coin.split('-')[0]]  / 10 < wanting[coin] * 0.8:
                                        #if usdpos[coin.split('-')[0]] < wanting[coin]:
                                        #    offset = 'open'
                                        #else:
                                        #    offset = 'close'    
                                        #print(offset)
                                        print('futs')
                                        print(coin)
                                        print(offset)

                                        print(wanting[coin])
                                        if offset == 'close' and direction == 'sell':
                                            direction = 'sell'
                                            e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                            direction = 'buy'
                                            e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                        elif offset == 'close' and direction == 'buy':
                                            direction = 'sell'
                                            e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                            direction = 'buy'
                                            e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                        #Print( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': wanting[coin], 'direction': direction, 'lever_rate': 5, 'order_price_type': 'post_only'})
                                        elif offset =='open':
                                            e = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                    """
                                    elif offset == 'close':
                                        if wanting[coin] == 0:
                                            wanting[coin] = 1
                                        #print(offset)
                                        #Print( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': wanting[coin], 'direction': direction, 'lever_rate': 5, 'order_price_type': 'post_only'})
                                        h1 = hfutures.privatePostContractOrder( {'offset': offset,'contract_code': pairs[coin], 'price': prc, 'volume': wanting[coin], 'direction': direction, 'lever_rate': 5, 'order_price_type': 'post_only'})
                                        #print(h1)
                                    """
                            else:
                                #print(64)
                                ords = hswap.privatePostSwapOpenorders({'contract_code': coin.replace('PERP', 'USD')})
                                
                                for o in ords['data']['orders']:
                                    if direction == o['direction'] and o['symbol']  == coin.split('-')[0]:
                                        #ogo = False
                                        qty = o['volume'] 
                                        if direction == 'sell' and skews[coin.split('-')[0]]  / 10> wanting[coin] * 0.8 or direction == 'buy' and skews[coin.split('-')[0]] / 10 < wanting[coin] * 0.8:
                                            if prc != o['price']:
                                                ordid = o['order_id']
                                                e = hswap.privatePostSwapCancel( {'contract_code': coin.replace('PERP', 'USD'), 'order_id': str(ordid)} )
                    #                            print(e)
                                        """
                                        elif offset == 'close':

                                            if wanting[coin] == 0:
                                                wanting[coin] = 1
                                            if prc != o['price']:
                                                ordid = o['order_id']
                                                e = hswap.privatePostSwapCancel( {'contract_code': coin.replace('PERP', 'USD'), 'order_id': str(ordid)} )
                                                #print(e)
                                        """
                                        PrintException()
                            
                                if gogo == True:
                                    if direction == 'sell' and skews[coin.split('-')[0]]  / 10 > wanting[coin] * 0.8  or direction == 'buy' and skews[coin.split('-')[0]]  / 10 < wanting[coin] * 0.8 :
                                        #if usdpos[coin.split('-')[0]] < wanting[coin]:
                                        #    offset = 'open'
                                        #else:
                                        #    offset = 'close'  
                                        #print(offset)
                                        print('swap')
                                        print(coin)
                                        print(offset)
                                        if offset == 'close' and direction == 'sell':
                                            direction = 'buy'
                                            e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                            direction = 'sell'
                                            e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                        elif offset == 'close' and direction == 'buy':
                                            direction = 'buy'
                                            e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                            direction = 'sell'
                                            e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                        elif offset == 'open':
                                            print(wanting[coin])
                                            e = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': round(wanting[coin]), 'direction': direction, 'lever_rate': levs[coin.split('-')[0]], 'order_price_type': 'post_only'})
                                            print(e)
                                    """"
                                    elif offset == 'close':

                                        if wanting[coin] == 0:
                                            wanting[coin] = 1
                                        #print(offset)
                                        h2 = hswap.privatePostSwapOrder( {'offset': offset, 'contract_code': coin.replace('PERP','USD'), 'price': prc, 'volume': wanting[coin], 'direction': direction, 'lever_rate': 5, 'order_price_type': 'post_only'})
                                        #print(h2)
                                    """
                        except:        

                            PrintException()
                except:
                    PrintException()
            #print(7)
            if c > 0:
                avg2 = t / c
                arbwinnersavg.append(avg2)
                arbwinnersc.append(c)
                c2 = c
                t = 0
                c = 0
                for arb in arbwinnersavg:
                    t = t + arb
                    c = c + 1
                avg3 = t / c
                abc=123#Print('%s are calculated based on 15x leverage, and double the funds available via cross margin borrowing (less about 36% APR for borrowing)')
                abc=123#Print('%s in Annual Percentage Yield')
                abc=123#Print('avg opportunity (over 20%): ' + str(round(avg*1000)/1000))
                #print('max opportunity (over 25%): ' + str(round(maxi*1000)/1000))
                abc=123#Print('# opps: ' + str(c1))
                abc=123#Print('avg opportunity over the avg: ' + str(round(avg2*1000)/1000))
                abc=123#Print('# opps over avg: ' + str(c2))
                abc=123#Print('avg of ' + str(c) + ' minute-long runs: ' + str(round(avg3*1000)/1000))
                day = avg3 / 365
                day = 100 / day
                abc=123#Print('doubling money every ' + str(round(day*1000)/1000) + ' days!')
                abc=123#Print(' ')
                #print('max of all to date: ' + str(round(maxmax*1000)/1000))
                abc=123#Print(' ')
                # todo remove
        
                
    except:
        PrintException()
        abc=123
ftx     = ccxt.ftx({
'apiKey': apikey,   
            'secret': apisecret,
'enableRateLimit': True

})

cancelall()
sizeIncrements = {}
r = requests.get('https://ftx.com/api/markets').json()['result']
#for m in r:
    #sizeIncrements[m['name']] = m['sizeIncrement'] 
markets = binance.fetchMarkets()
futs = '200925'
for m in markets:
    #print(m['id'])
    try:
        binance.dapiPrivatePostLeverage({'symbol': m['id'], 'leverage': 75})
    except:
        abc=123
        
from pprint import pprint

#### input huobi dm url
URL = 'https://api.hbdm.com/swap-'
URL2 = 'https://api.hbdm.com'
####  input your access_key and secret_key below:



hswap = ccxt.huobiswap({
'apiKey': apikey,   
            'secret': apisecret,
'enableRateLimit': True})
hfutures = ccxt.huobifuts({
'apiKey': apikey,   
            'secret': apisecret,
'enableRateLimit': True})

huobi = ccxt.huobipro({"urls": {'api':{'public': 'https://api.hbdm.com/swap-api',
'private': 'https://api.hbdm.com/swap-api'}}})

hspot = ccxt.huobipro({
'apiKey': apikey,   
            'secret': apisecret,
'enableRateLimit': True})

hspotm               = hspot.fetchMarkets()
#margt = hspot.privatePostCrossMarginTransferOut({'currency': 'usdt', 'amount': str(999)})
                      
data =  hspot.privateGetAccountAccounts()
for d in data['data']:
    if d['type'] == 'spot':
        accountnum = d['id']
#abc=432#sleep(100)
print('s,s,f')
print(len(hspotm))
print(dir(hspot))
insts               = binance.fetchMarkets()
#print(insts[0])

bin_futures_all    =    insts
funding = {}
exchanges = ['huobi']
mids = {}
bids = {}
asks = {}
for ex in exchanges:
    funding[ex] = {}
    mids[ex] = {}
    bids[ex] = {}
    asks[ex] = {}
expis = {}
futureends = ["_CW", "_NW", "_CQ", "_NQ"]
precisions = {}
p = requests.get("https://api.huobi.pro/v1/common/symbols").json()['data']
for pr in p:
    precisions[pr['base-currency'].upper()] = pr['amount-precision']   -1
ticksizes = {}
rates = {}
for ex in exchanges:
    rates[ex] = {}
huobisw = []
huobis = []
huobi = requests.get("https://api.hbdm.com//swap-api/v1/swap_contract_info").json()['data']

for market in huobi:
    #stri = str(huobi[market])
        #if 'usd' in market['quoteId']:
    if market['contract_code'] not in huobisw:
        huobisw.append(market['contract_code'])
huobi = requests.get("https://api.hbdm.com/api/v1/contract_contract_info").json()['data']

dts = []
for market in huobi:
    #stri = str(huobi[market])
        #if 'usd' in market['quoteId']:
    if market['symbol'] not in huobis:
        huobis.append(market['symbol'])
        sizeIncrements[market['symbol']] = market['contract_size']
    dt = market['delivery_date']
    expiry  = datetime.datetime.strptime( 
                                           dt, 
                                            '%Y%m%d' )
            
    #print(dt)
    dt = dt[-4:]
    if dt not in dts:
        dts.append(dt)            
    now     = datetime.datetime.utcnow()

    days    = ( expiry - now ).total_seconds() / SECONDS_IN_DAY
    #print(days)
    expis[dt] = days
    expis['PERP'] = 30000
    #print(expis)

    #print(huobi[market])

"""
bcontracts = []

pairs = requests.get('https://dapi.binance.com/dapi/v1/exchangeInfo').json()
for symbol in pairs['symbols']:
    split = len(symbol['baseAsset'])
    #if 'BTC' in symbol['symbol']:
        #print(symbol['symbol'])
    normalized = symbol['symbol'][:split] + '-' + symbol['symbol'][split:]
    bcontracts.append(normalized)
config = {TICKER: bcontracts}
fh.add_feed(BinanceFutures(config=config, callbacks={TICKER: TickerCallback(ticker)}))

ofuts = []
oswaps = []
swaps = requests.get('https://www.okex.com/api/swap/v3/instruments').json()

futures = requests.get('https://www.okex.com/api/futures/v3/instruments').json()
for s in swaps:
    oswaps.append(s['instrument_id'])
for f in futures:
    ofuts.append(f['instrument_id'])
config = {TICKER_OKS: oswaps
,TICKER_FUTURES: ofuts}
fh.add_feed(OKEx(config=config, callbacks={TICKER_FUTURES: TickerCallback(ticker), TICKER_OKS: TickerCallback(ticker)}))

#print(expis)
takens = []
dts.sort()
#print(dts)
times = {"_CW": dts[0], "_NW": dts[1], "_CQ": dts[2], "_NQ": dts[3]}
for fut in bin_futures_all:
    try:
        split = (fut['info']['symbol']).split('_')[1][-4:]
        
        expi = datetime.datetime.fromtimestamp(fut['info']['deliveryDate'] / 1000)

        now     = datetime.datetime.utcnow()
        days    = ( expi - now ).total_seconds() / SECONDS_IN_DAY
        #print(days)
        #print(days)
        expis[split] = days
        precisions[fut['info']['symbol']] = 1
        ticksizes[fut['info']['symbol']] = 1
        for precision in range(0, fut['info']['pricePrecision']):
            precisions[fut['info']['symbol']] = precisions[fut['info']['symbol']] / 10
            ticksizes[fut['info']['symbol']]= ticksizes[fut['info']['symbol']] / 10
        #print(fut['info']['symbol'])
        #print(ticksizes_binance[fut['info']['symbol']])
        #print(precisions_binance[fut['info']['symbol']])
    except:
        PrintException()

ftx = requests.get("https://ftx.com/api/funding_rates").json()['result']
doneFtx = {}
for rate in ftx:
    doneFtx[rate['future'].replace('-PERP', '')] = False
for rate in ftx:
    if rate['future'].replace('-PERP', '') != 'BTC' and rate['future'].replace('-PERP', '') != 'ETH':
        if doneFtx[rate['future'].replace('-PERP', '')] == False:
            doneFtx[rate['future'].replace('-PERP', '')] = True
            rates['ftx'][rate['future'].replace('-PERP', '')] = rate['rate'] * 24

"""
allfuts = []
expiries = {}
hcontracts = []
for contract in huobis:
    for futureend in futureends:
        hcontracts.append(contract + futureend)
        

#for contract in huobisw:
#    hcontracts.append(contract)

config = {L2_BOOK: hcontracts}
fh.add_feed(hdm(config=config, callbacks={L2_BOOK: BookCallback(book)}))
kcontracts = []
"""
binance = requests.get("https://dapi.binance.com/dapi/v1/premiumIndex").json()
#binance_f = requests.get("https://fapi.binance.com/fapi/v1/premiumIndex").json()
kraken = requests.get("https://futures.kraken.com/derivatives/api/v3/tickers").json()

for market in kraken['tickers']:
    if 'tag' in market:
        kcontracts.append(market['symbol'].upper())
#print(kcontracts)
config = {TICKER: kcontracts}
fh.add_feed(KrakenFutures(config=config, callbacks={TICKER: TickerCallback(ticker)}))

fcontracts = []
ftxmarkets = requests.get("https://ftx.com/api/futures").json()['result']
for market in ftxmarkets:
    if 'MOVE' not in market['name'] and 'HASH' not in market['name']:
        fcontracts.append(market['name'])
config = {TICKER: fcontracts}
fh.add_feed(FTX(config=config, callbacks={TICKER: TickerCallback(ticker)}))
#loop = asyncio.get_event_loop()
"""
t = threading.Thread(target=loop_in_thread, args=())
t.start()

#t = threading.Thread(target=loop_in_thread2, args=())
#t.start()
print(expis)

import random, string
import requests
import math

funding = {}
exchanges = ['binance']#['binance', 'kraken', 'ftx', 'phemex', 'okex']
for ex in exchanges:
    funding[ex] = {}
def randomword(length):
       letters = string.ascii_lowercase
       return ''.join(random.choice(letters) for i in range(length))
def doupdates():
    global fundingwinners
    #todo: replace with dapi.binance.com/, and change all of the ccxt stuff in ccxt/binance.py to dapi.binance.com
    binance2 = requests.get('https://dapi.binance.com/dapi/v1/premiumIndex').json()
    for obj in binance2:
        try:
            funding['binance'][obj['symbol'].replace('USDT', '')] = float(obj['lastFundingRate']) * 3
        except:
            abc=123
    """
    kraken = requests.get('https://futures.kraken.com/derivatives/api/v3/tickers').json()['tickers']
    for obj in kraken:
        if 'tag' in obj:
            if obj['tag'] == 'perpetual':
                funding['kraken'][obj['pair'].replace('XBT','BTC').replace(':USD', '')] = float(obj['fundingRate']) * 3
           
    ftx = requests.get('https://ftx.com/api/funding_rates').json()['result']
    takenftx = []
    for obj in ftx:
        if obj['future'].replace('-PERP','') not in takenftx:
            takenftx.append(obj['future'].replace('-PERP',''))
            funding['ftx'][obj['future'].replace('-PERP','')] = float(obj['rate']) * 24
    
    phemproducts = requests.get('https://api.phemex.com/exchange/public/cfg/v2/products').json()['data']['products']
    phemperps = []
    for obj in phemproducts:
        if obj['type'] == 'Perpetual':
            phemperps.append(obj['symbol'])
    for perp in phemperps:
        phemex = requests.get('https://api.phemex.com/md/ticker/24hr?symbol=' + perp).json()['result']
        funding['phemex'][perp.replace('USD', '')] = float(phemex['fundingRate'])/100000000*3
        
    
    swaps = requests.get('https://www.okex.com/api/swap/v3/instruments').json()
    for s in swaps:
        okex = requests.get('https://www.okex.com/api/swap/v3/instruments/' + s['instrument_id'] + '/funding_time').json()
        funding['okex'][okex['instrument_id'].replace('-USDT-SWAP', '').replace('-USD-SWAP', '')] = float(okex['funding_rate']) * 3
    """
    rates = {}
    for ex in funding:
        rates[ex] = {}
        for coin in funding[ex]:
            rates[ex][coin] = []
    for ex in funding:
        for coin in funding[ex]:
            rates[ex][coin].append(float(funding[ex][coin]))
    APRS = {}
    longshorts = {}
    for ex in rates:
        APRS[ex] = {}
        for coin in rates[ex]:
                
            maximum = max(rates[ex][coin])
            minimum = min(rates[ex][coin])
      #      abc=123#Print(coin)
      #      abc=123#Print(math.fabs(maximum) * 100)
      #      abc=123#Print(math.fabs(minimum) * 100)     
      #      abc=123#Print(str(0.015*3))
      #      abc=123#Print(' ')
            if math.fabs(maximum) > math.fabs(minimum):
                if (math.fabs(maximum) * 365 * 100 * 75 / 2) - minArb > 0:
                    if maximum < 0:
                        longshorts[coin] = 'long'
                    else:
                        longshorts[coin] = 'short'
                    APRS[ex][coin] = (math.fabs(maximum) * 365 * 100 * 75 / 2) - minArb
            else:
                if  (math.fabs(minimum) * 365 * 100 * 75 / 2) - minArb > 0:
                    if minimum < 0:
                        longshorts[coin] = 'long'
                    else:
                        longshorts[coin] = 'short'
                    APRS[ex][coin] = (math.fabs(minimum) * 365 * 100 * 75 / 2) - minArb

    
    fundingwinners = []
    t = 0
    c = 0
    for ex in APRS:
        maximum = 0

        winner = ""
        for coin in APRS[ex]:
            if APRS[ex][coin] > 0 and 'LINK' in coin or 'BTC' in coin or 'ETH' in coin or 'ADA' in coin:
                t = t + APRS[ex][coin]
                c = c + 1
                
                fundingwinners.append({'ex': ex, 'coin': coin, 'arb': APRS[ex][coin]})
     #           abc=123#Print({'ex': ex, 'coin': coin, 'arb': APRS[ex][coin]})
       #print('The Maximum funding opportunity on ' + ex + ' now is ' + winner + ' with ' + str(maximum) + '%!')
    percs = {}
    tobuy = {}
    for ex in APRS:
        maximum = 0

        winner = ""
        for coin in APRS[ex]:
            
            if APRS[ex][coin] > 0 and 'LINK' in coin or 'BTC' in coin or 'ETH' in coin or 'ADA' in coin:
                    percs[coin] = 1#APRS[ex][coin] / t
                                   #((1000000 * 0.66) * 75 /2) / 10
                    #((25 * 0.25 ) * 75 / 2) / 10
                    
                    tobuy[coin] = ((balances[coin.split('_')[0].replace('USD', '')] * percs[coin]) * 75 / 2) / 10
                    tobuy[coin.replace('PERP', futs)] = tobuy[coin] * -1
                    
            elif 'LINK' in coin or 'BTC' in coin or 'ETH' in coin or 'ADA' in coin:
                tobuy[coin] = 0
                tobuy[coin.replace('PERP', futs)] = 0
    abc=123#Print(percs)        
    for coin in longshorts:
        if longshorts[coin] == 'short':
            try:
                tobuy[coin] = tobuy[coin] * -1
                tobuy[coin.replace('PERP', futs)] = tobuy[coin.replace('PERP', futs)] * -1
            except:
                abc=123
    abc=123#Print(tobuy)
    #abc=432#sleep(100)
    for coin in tobuy:
        #cancelall(coin)
        #-100 btc
        #-800 
        #100
        #800
        try:
            
        
            if math.fabs((tobuy[coin]) / (balances[coin.split('_')[0].replace('USD', '')] * 75)) > ((1/divisor) * 0.5) / 75: 
                        
                if 'BTC' in coin:
                    tobuy[coin] = tobuy[coin] / 10
                    tobuy[coin] = tobuy[coin] - pos[coin] / 10
                else:
                    tobuy[coin] = tobuy[coin] - pos[coin] / 100
                #print(tobuy)
                direction = 'BUY'
                if tobuy[coin] < 0:
                    direction = 'SELL'
                    tobuy[coin] = tobuy[coin] * -1
                if tobuy[coin] != 0:
                    #print(tobuy[coin])
                    bbo = mids['binance'][coin.replace('USD', '-USD')]
                    
                    abc=123#Print(int(tobuy[coin] / divisor))
                    abc=123#Print(tobuy[coin])
                    if direction == 'SELL':
                        
                        binance.dapiPrivatePostOrder(  {'timeInForce': 'GTC', 'symbol': coin, 'side': direction, 'type': 'LIMIT', 'price': bbo['bid'], 'quantity': int(tobuy[coin] / divisor),"newClientOrderId": "x-v0tiKJjj-" + randomword(15)})
                    else:
                        binance.dapiPrivatePostOrder(  {'timeInForce': 'GTC', 'symbol': coin, 'side': direction, 'type': 'LIMIT', 'price': bbo['ask'], 'quantity': int(tobuy[coin] / divisor),"newClientOrderId": "x-v0tiKJjj-" + randomword(15)})
        except:
            PrintException()
    abc=123#Print(tobuy)
balances = {}
totrade = ['BTC', 'ETH', 'XRP', 'BCH', 'LTC', 'EOS', 'LINK', 'DOT', 'ADA', 'BSV', 'ETC', 'TRX']
pos = {}
usdpos = {}
skews = {}
balancereal2 = 0
for t in totrade:
    balances[t] = 0
def updatePositions():
    
    try:
        global positions, skews, balancereal, balancereal2, first
        skews = {}
        balancereal2 = balance
        for coin in coinsto:
            skews[coin] = 0   
            positions       = hfutures.privatePostContractAccountPositionInfo({'symbol': coin})
        
            for p in positions['data']: 
                
                #if p['entryPrice'] is not None:
                #    abc=123#Print(p)
                for pos in p['positions']:
                    balancereal2 = balancereal2 + float(pos['profit_unreal'])
                   # balancereal2 = balancereal2 + float(pos['profit'])
                    
                    name = p['symbol'] + '-' +pos['contract_code'][-4:]
                    
                    size = float(pos['volume'])
                    if pos['direction'] == 'sell':
                        size = size * -1
                    pos[name] = size
                    usdpos[name] =(float(pos['volume']))
            
                #if 'BCH' in p['symbol']:
                    #Print(p)
                for pos in p['positions']: # 200 / 10
                    size = (float(pos['volume']) * 10)
                    if pos['direction'] == 'sell':
                        size = size * -1
                    
                    skews[p['symbol']] = skews[p['symbol']] + size
            
            positions = hswap.privatePostSwapAccountPositionInfo   ({'contract_code': coin+ '-USD'}) 
            for p in positions['data']: 
            
                #if p['entryPrice'] is not None:
                #    abc=123#Print(p)
                for pos in p['positions']:
                    name = p['symbol'] + '-PERP'
                    balancereal2 = balancereal2 + float(pos['profit_unreal'])
                   # balancereal2 = balancereal2 + float(pos['profit'])
                    if coin == 'EOS':
                        abc=123#Print(pos)
                    size = float(pos['volume'])
                    if pos['direction'] == 'sell':
                        size = size * -1
                    pos[name] = size
                    usdpos[name] = (float(pos['volume']))
                #if 'BCH' in p['symbol']:
                    #Print(p)
                for pos in p['positions']:
                    size = (float(pos['volume']) * 10)
                    if pos['direction'] == 'sell':
                        size = size * -1

                    skews[p['symbol']] = skews[p['symbol']] + size
            #print(skews)
        #print(usdpos)

        print(skews)
        sleep(2)
        abc=432#sleep(2)
    except Exception as e:
        PrintException()
    if first == True:
        balancereal = balancereal2
        first = False
    with open('huobi.json', 'w') as outfile:
        json.dump({'balance': balancereal2, 'startbalance': balancereal}, outfile)

import json

lev = 0
marginbs = {}
spotbs = {}
futbs = {}
swapbs = {}
#balance = 500
balance = 0
balancereal = 0 
first = True
def updateBalance():
   
    abc=123#Print('ub')
    try:
        
        global firstbalance, firstrun, balance, lev, first, balancereal, balancereal2, mids
        for contract in huobisw:
            if contract.split('-')[0] in huobis and contract.split('-')[0] in coinsto:
                data = requests.get("https://api.hbdm.com/swap-ex/market/detail/merged?contract_code=" + contract).json()['tick']
                ask = data['ask'][0]
                bid = data['bid'][0]
                name = contract.split('-')[0]
                dt = 'PERP'
                ex = 'huobi'
                mids[ex][name + '-' + dt] = 0.5 * ( float(ask) + float(bid))
                bids[ex][name + '-' + dt] = float(bid)
                asks[ex][name + '-' + dt] = float(ask) 
                #print(name)
        r = requests.get("https://api.huobi.pro/market/tickers").json()
        mids['spot'] = {}
        for sym in r['data']:
            mids['spot'][sym['symbol']] = {'ask': sym['ask'], 'bid': sym['bid']}
        bal2 = hfutures.privatePostContractAccountInfo()
        bal3 = hswap.privatePostSwapAccountInfo()
        for b in bal2['data']:
            if b['symbol'] in coinsto:
                usdpos[b['symbol']] = 0
        for b in bal3['data']:
            if b['symbol'] in coinsto:
                usdpos[b['symbol']] = 0
        for b in bal2['data']:
            if b['symbol'] in coinsto:
                abc=123#Print(b)
                if float(b['margin_balance']) > 0:
                    futbs[b['symbol']] = float(b['margin_balance'])
                #usdpos[b['symbol']] = usdpos[b['symbol']] + float(b['margin_position'])
        for b in bal3['data']:
            
            if b['symbol'] in coinsto:
                #print(b)
                if float(b['margin_balance']) > 0:
                    swapbs[b['symbol']] = float(b['margin_balance'])
                #usdpos[b['symbol']] = usdpos[b['symbol']] + float(b['margin_position'])
        abc=123#Print(futbs)
       # #Print(swapbs)
        #abc=432#sleep(100)
        """
        account_balance_list = account_client.get_account_balance()
        if account_balance_list and len(account_balance_list):
            for account_obj in account_balance_list:
                account_obj.print_object()
                abc=123#Print()
        
        abc=432#sleep(100)
        """
        #bal2 = hfutures.get_contract_account_info()
        balspot = hspot.fetchBalance()
        balance = 0
        for bal in balspot['total']:
            spotbs[bal] = balspot['total'][bal]
           #if spotbs[bal] > 0:
                #Print(bal)
            if bal == 'USDT' or bal == 'usdt':
                balance = balance + spotbs[bal]
            else:
                try:
                    balance = balance + spotbs[bal] * mids['spot'][bal.lower()+'usdt']['ask']
                except:
                    abc=123
        for s in swapbs:
            balance = balance + swapbs[s] * mids['huobi'][s+'-PERP']
        for s in futbs:
            balance = balance + futbs[s] * mids['huobi'][s+'-PERP']
        if firstrun == True and balance != 0:
            firstrun = False
            firstbalance = balance
    
        """
        if spotbs['USDT'] > 10:
            hspot.privatePostCrossMarginTransferIn({'currency': 'usdt', 'amount': str(spotbs['USDT'])})
        """
        for spot in spotbs:
            try:
                if spot != 'USDT' and spotbs[spot] > 0:
                    #Print({'from': 'spot', 'to': 'swap', 'currency': spot, 'amount': str(round(spotbs[spot] / 2.05 * 10000000) / 10000000)})
                    hspot.v2PrivatePostAccountTransfer({'from': 'spot', 'to': 'swap', 'currency': spot, 'amount': str(round(spotbs[spot] / 2.05 * 10000000) / 10000000)}) 
                    #Print({'type': 'pro-to-futures', 'currency': spot, 'amount': str(round(spotbs[spot] / 2.05 * 10000000) / 10000000)})
                    hspot.privatePostFuturesTransfer({'type': 'pro-to-futures', 'currency': spot, 'amount': str(round(spotbs[spot] / 2.05 * 10000000) / 10000000)})
            except:
                PrintException()

        print(spotbs)
        print(swapbs)
        print(futbs)
        #sleep(2)
        #abc=432#sleep(100)
        """
        bal3 = hspot.privateGetCrossMarginAccountsBalance()
        try:
            for bal in bal3['data']['list']:
                try:
                    if bal['currency'] == 'xrp':
                        #Print(bal)
                    if bal['currency'] == 'usdt':
                        abc=123#Print(bal)
                        if bal['type'] == 'trade':
                            marginbs[bal['currency']] = float(bal['balance'])
                    elif bal['type'] == 'transfer-out-available':
                        marginbs[bal['currency']] = float(bal['balance'])
                        
                except:
                    abc=123
            #abc=432#sleep(100)
            balance = marginbs['usdt']
            if first == True:
                first = False
                balancereal = balance
            abc=123#Print(marginbs)
            for m in marginbs:
                try:
                    abc=123#Print(m)
                    abc=123#Print(1)
                    if m != 'usdt' and float(marginbs[m]) > 0:
                        abc=123#Print(2)
                        abc=123#Print(marginbs[m])
                        margt = hspot.privatePostCrossMarginTransferOut({'currency': m, 'amount': str(round(marginbs[m] * 1000)/ 1000)})
                        abc=123#Print(margt)
                except: 
                    PrintException()
            abc=123#Print('b')
            abc=123#Print(balance)
        except Exception as e:
            PrintException()
            #abc=432#sleep(500)
            abc=123
            
        
        #balance = 228
        abc=123#Print(marginbs)
        """
        """
        pprint(marginbs)
        #abc=432#sleep(1)
        pprint(bal1)
        pprint(bal2)
        newbal = 0
        ##print(bal2)
        for coin in bal2['info']['result']:
            newbal = newbal + coin['usdValue']  
        t = 0
        for pos in usdpos:
            t = t + math.fabs(usdpos[pos])
        lev = t / newbal * 100
        balance = newbal
        abc=123#Print(balance)
        abc=123#Print(lev)
        balance = 50000
        """
    except:
        PrintException()
        abc=123
        
    
    #balance = 500

"""
updateBalance()
updatePositions()
try:
    for coin in coinsto:
        coin = coin.lower()
        loans = hspot.privateGetCrossMarginLoanOrders({'size': "100",'currency': coin, 'state': 'accrual'})
        for l in loans['data']:
            try:
                if float(l['loan-balance']) > 0:
                    torepay = float(l['loan-balance'])
                    identifier = l['id']
                    abc=123#Print({'from': 'swap', 'to': 'spot', 'currency': coin, 'amount': str(torepay / 2)})
                    try:
                        hspot.v2PrivatePostAccountTransfer({'from': 'swap', 'to': 'spot', 'currency': coin, 'amount': str(torepay / 2)}) 
                    except:
                        PrintException()
                        
                        
                    try:
                        hspot.privatePostFuturesTransfer({'type': 'futures-to-pro', 'currency': coin, 'amount': str(torepay / 2)})
                    except:
                        PrintException()
                    try:
                        hspot.privatePostCrossMarginTransferIn({'currency': coin, 'amount': str(torepay)})
                    except:
                        PrintException()
                    
                    torepay = float(l['interest-amount'])
                    try:
                        hspot.v2PrivatePostAccountTransfer({'from': 'swap', 'to': 'spot', 'currency': coin, 'amount': str(torepay / 2)}) 
                    except:
                        PrintException()
                        
                        
                    try:
                        hspot.privatePostFuturesTransfer({'type': 'futures-to-pro', 'currency': coin, 'amount': str(torepay / 2)})
                    except:
                        PrintException()
                    try:
                        hspot.privatePostCrossMarginTransferIn({'currency': coin, 'amount': str(torepay)})
                    except:
                        PrintException()
                    try:
                        hspot.privatePostCrossMarginOrdersIdRepay({'id': identifier, 'amount': str(torepay)})
                    except: 
                        PrintException()
                    #hspot.privatePostCrossMarginOrdersIdRepay({'id': identifier, 'amount': str(toborrow / mids['huobi'][arb])})
            except Exception as e:
                PrintException()
                abc=432#sleep(2)
except Exception as e:
    PrintException()
    abc=432#sleep(2)
"""
#abc=432#sleep(25)
for contract in huobisw:
    if contract.split('-')[0] in huobis and contract.split('-')[0] in coinsto:
        data = requests.get("https://api.hbdm.com/swap-ex/market/detail/merged?contract_code=" + contract).json()['tick']
        ask = data['ask'][0]
        bid = data['bid'][0]
        name = contract.split('-')[0]
        dt = 'PERP'
        ex = 'huobi'
        mids[ex][name + '-' + dt] = 0.5 * ( float(ask) + float(bid))
        bids[ex][name + '-' + dt] = float(bid)
        asks[ex][name + '-' + dt] = float(ask) 
        #print(name)
"""
arb = 'BTC-PERP'
toborrow = 100    
#hspot.privatePostAccountTransfer({'from': 'swap', 'to': 'spot', 'currency': arb.split('-')[0].lower(), 'amount': str(0.005)}) 
#hspot.privatePostFuturesTransfer({'type': 'futures-to-pro', 'currency': arb.split('-')[0].lower(), 'amount': str(0.005)})
#wantingold[arb.split('-')[0]] = toborrow
#hspot.privatePostCrossMarginTransferIn({'currency': arb.split('-')[0].lower(), 'amount': str(toborrow / mids['huobi'][arb])})
#borrowed = hspot.privatePostCrossMarginOrders({'symbol': arb.split('-')[0].lower() + 'usdt', 'currency': arb.split('-')[0].lower(), 'amount':  str( round((toborrow * 1.01) / mids['huobi'][arb] * 1000)/ 1000)})   
loans = hspot.privateGetCrossMarginLoanOrders({'currency': arb.split('-')[0].lower(), 'state': 'accrual'})
for l in loans['data']:
    if float(l['loan-balance']) > 0:
        torepay = l['loan-balance'] 
        abc=123#Print(torepay)
        identifier = l['id']
        hspot.privatePostCrossMarginOrdersIdRepay({'id': identifier, 'amount': str(torepay)})
"""

dts = []
#updateBalance()
import gspread


spreadsheetId = "1kJIZH2Ku2M_T_Grz6rGqMLfCrJhO_y-V77RCuMh4BeA"  # Please set the Spreadsheet ID.
sheetName = 'Sheet1'  # Please set the sheet name.
client = gspread.service_account(filename='../google.json')

sh = client.open_by_key(spreadsheetId)
worksheet = sh.worksheet("Sheet1")
try:   
    worksheet2 = sh.worksheet(os.environ['key'].split('-')[0])
except:
    sh.add_worksheet(os.environ['key'].split('-')[0], 1, 2)
    
    worksheet2 = sh.worksheet(os.environ['key'].split('-')[0])
    worksheet2.append_row(['datetime', 'balance'])


sleep(25)
def ohlcvs():
    global levs
    cvs = {}
    """
    for coin in coinsto:
        ohlcvs = hspot.fetch_ohlcv(coin + '/USDT', '30m')
        vs = []
        for ohlcv in ohlcvs:
            vs.append(ohlcv[-1] * ohlcv[-2])
        print(coin)
        print(sum(vs))
        cvs[coin] = (sum(vs))
    t = 0
    c = 0
    for v in cvs:
        t = t + cvs[v]
        c = c + 1
    avg = t / c
    print('average')
    print(avg)
    percs = {}
    for v in cvs:
        percs[v] = cvs[v] / t
        levs[v] = int(200 * percs[v])
        levs[v] = round(levs[v] / 10) * 10
        if levs[v] == 0:
            levs[v] = 1
    """
    levs = {'BTC': 50, 'ETH': 50, 'XRP': 5, 'BCH': 10, 'LTC': 5, 'EOS': 10, 'LINK': 15, 'DOT': 10, 'ADA': 5, 'BSV': 5, 'ETC': 5, 'TRX': 10}


    print(levs)

ohlcvs()
lastbalance = 1
firstbalance = 0
firstrun = True

while True:
    r = random.randint(0, 1000)
    if r <= 5:
        cancelall()
    updateBalance()
    if lastbalance / balance > 1.5 or lastbalance / balance < 0.75:
        lastbalance = balance
        rcount = worksheet.row_count + 1

        added = worksheet.append_row([os.environ['key'], str(balance), "=vlookup(A" + str(rcount) + ", Sheet2!B:C, 2, FALSE)"], "USER_ENTERED")
        print(added)
    dt_to_string = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    added = worksheet2.append_row([dt_to_string, '=VALUE(' + str((balance/firstbalance-1)*100) + '%)'], 'USER_ENTERED')
    
    updatePositions()
    huobi = requests.get("https://api.hbdm.com/api/v1/contract_contract_info").json()['data']

    dts = []
    for market in huobi:
        #stri = str(huobi[market])
            #if 'usd' in market['quoteId']:
        if market['symbol'] not in huobis:
            huobis.append(market['symbol'])
            sizeIncrements[market['symbol']] = market['contract_size']
        dt = market['delivery_date']
        expiry  = datetime.datetime.strptime( 
                                               dt, 
                                                '%Y%m%d' )
                
        #print(dt)
        dt = dt[-4:]
        if dt not in dts:
            dts.append(dt)            
        now     = datetime.datetime.utcnow()

        days    = ( expiry - now ).total_seconds() / SECONDS_IN_DAY
        #print(days)
        expis[dt] = days
        expis['PERP'] = 30000
        #print(expis)

        #print(huobi[market])
    for ex in mids:
        for dt in mids[ex]:
            if '-' in dt:
                if dt.split('-')[1] not in expis:
                    try:
                    
                        if 'PERP' in dt:
                            expis[dt.split('-')[1]] = 30000
                        else:
                            now     = datetime.datetime.utcnow()
                            expiry  = datetime.datetime.strptime( 
                                                       '2021' + dt.split('-')[1], 
                                                        '%Y%m%d' )
                            days    = ( expiry - now ).total_seconds() / SECONDS_IN_DAY
                            abc=123#Print(days)
                            abc=123#Print(dt.split('-')[1])
                            expis[dt.split('-')[1]] = days
                    except:
                        abc=123
        
    print(expis)
    doCalc()
    

    

   #abc=432#sleep(1)
    #abc=432#sleep(20)
    #updateBalance()
    #abc=432#sleep(5)
    #doupdates()
    #abc=432#sleep(35)
