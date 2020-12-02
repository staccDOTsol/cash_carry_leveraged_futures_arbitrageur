import os
apikey = os.environ['key']#'IO7okj6AU7sgEKq4M_T2Ld-KO1VTXpSuq3WkfUF0'
apisecret = os.environ['secret']#'1DMOnLSW3fk3SF8KVCbsKTTgqxSdl78tRZja_zQo'
divisor=1000
abc = -937.0961358420444
abc = abc / 28 / 10
print(abc)

import requests 
import math
from datetime import timedelta
import datetime
import sys
from threading import Timer
import threading
import linecache
from time import sleep

ts = []
import ccxt
binance  = ccxt.binance({'enableRateLimit': True,
"options":{"defaultMarket":"futures"},
'urls': {'api': {
						 'public': 'https://dapi.binance.com/dapi/v1',
						 'private': 'https://dapi.binance.com/dapi/v1',},}
})

#print(dir(binance))
#sleep(1)
SECONDS_IN_DAY	= 3600 * 24
from cryptofeed import FeedHandler
from cryptofeed import FeedHandler
from cryptofeed.callback import BookCallback, TickerCallback, TradeCallback
from cryptofeed.defines import TICKER_FUTURES, TICKER_OKS, BID, ASK, FUNDING, L2_BOOK, OPEN_INTEREST, TICKER, TRADES
from cryptofeed.exchanges import OKEx, KrakenFutures, HuobiDM, BinanceFutures, FTX
fh = FeedHandler()
fundingwinners = []
from flask import Flask

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from flask import jsonify
import threading

print(2)
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
	if warmup == False:
		exc_type, exc_obj, tb = sys.exc_info()
		f = tb.tb_frame
		lineno = tb.tb_lineno
		filename = f.f_code.co_filename
		linecache.checkcache(filename)
		line = linecache.getline(filename, lineno, f.f_globals)
		string = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
		if 'rder already queued for cancellatio' not in string:
			print   (string)
	##sleep(1)
	#if 'UNI' not in string:
		##sleep(1)
#	   if 'Account does not have enough margin for order' not in string:
			##sleep(1)

warmup = True

def handle_function():
	global warmup
	warmup = False
	print(warmup)
thread = Timer(25,handle_function)
thread.daemon = True
thread.start()
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
 
   # print(feed + '-' + name + '-' + dt +': ' + str( 0.5 * ( float(bid) + float(ask))))
	mids[ex][name + '-' + dt] = 0.5 * ( float(ask) + float(bid))
	bids[ex][name + '-' + dt] = float(bid)
	asks[ex][name + '-' + dt] = float(ask) 
async def book(feed, pair, book, timestamp, receipt_timestamp):
	global mids
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
	name = pair.split('20'+dt)[0]
	#print(name)
  #  if 'BTC' in name and lastex != feed and lastbtc != 0.5 * ( float(bid) + float(ask)):
	#	lastex = feed
   #	 lastbtc = 0.5 * ( float(bid) + float(ask))
		#print(feed + '-' + name + '-' + dt +': ' + str( 0.5 * ( float(bid) + float(ask))))
	#print(pair)
	mids['huobi'][name + '-' + dt] = 0.5 * ( float(la) + float(hb))
	#print(mids)
	
	#print(f'Timestamp: {timestamp} Feed: {feed} Pair: {pair} Book Bid Size is {len(book[BID])} Ask Size is {len(book[ASK])}')
def cancelall():
	try:
	
		try:
			
			ftx.privateDeleteOrders(  )
		except Exception as e:
			PrintException()


	except Exception as e:
		PrintException()
arbwinnersavg = []
arbwinnersc = []
maxmax = 0
levs = {}
trading = {}
def doOrder(coin, direction, wantingcoin, prc, count, laste=[], postonly=True):
	if wantingcoin * mids['ftx'][coin] < 0.1:
		return
	try:
		#print(wantingcoin * mids['ftx'][coin])
		f = ftx.createOrder(  coin, 'limit', direction, wantingcoin, prc, {'postOnly': postonly})
		print(f)
	except Exception as e:
		try:
			dummy_event.wait(timeout=((1/25)*1))
			if 'Size too small' in str(e):
				laste.append('small')
				if len(laste) > 4:
					if laste[-1] == 'small' and laste[-3] == 'small' and laste[-5] == 'small' and laste[-2] == 'large'  and laste[-4] == 'large':
						return
				#PrintException()
				return doOrder(coin, direction, wantingcoin * (3 * count), prc, count + 1, laste, postonly)
			elif 'Account does not have enough' in str(e):
				laste.append('large')
				if len(laste) > 4:
					if laste[-2] == 'small' and laste[-4] == 'small' and laste[-1] == 'large' and laste[-3] == 'large'  and laste[-5] == 'large':
						return
				#PrintException()
				return doOrder(coin, direction, wantingcoin / (3 * count), prc, count + 1, laste, postonly)	
			else:
				PrintException()
		except:
			PrintException()

start_time = datetime.datetime.utcnow()- timedelta(hours = 0)
SECONDS_IN_DAY	  = 3600 * 24
def output_status():
	try:
		now	 = datetime.datetime.utcnow()
		days	= ( now - start_time ).total_seconds() / SECONDS_IN_DAY
		print( '********************************************************************' )
		
		#print( '%% Delta:		   %s%%'% round( self.get_pct_delta() / PCT, 1 ))
		#print( 'Total Delta (BTC): %s'   % round( sum( self.deltas.values()), 2 ))		
		#print_dict_of_dicts( {
		#	k: {
		#		'BTC': self.deltas[ k ]
		#	} for k in self.deltas.keys()
		#	}, 
		#	roundto = 2, title = 'Deltas' )
		
		#print(self.positions)

		print('Positions')
		for s in usdpos:
			if usdpos[s] > balance / 100 or usdpos[s] < -1 * balance / 50:
				print(s + ': $' + str(round(usdpos[s] * 100) / 100))
		print('Skews')
		for s in skews:
			if skews[s] > balance / 100 or skews[s] < -1 * balance / 50:
				print(s + ': $' + str(round(skews[s] * 100) / 100))
		print('Orders #')
		print(lenords)
		print( 'Start Time:		%s' % start_time.strftime( '%Y-%m-%d %H:%M:%S' ))
		print( 'Current Time:	  %s' % now.strftime( '%Y-%m-%d %H:%M:%S' ))
		print( 'Days:			  %s' % round( days, 1 ))
		print( 'Hours:			 %s' % round( days * 24, 1 ))
		
		equity_usd = balance
		equity_btc = round(balance / mids['ftx']['BTC-PERP'] * 100000000) / 100000000
		pnl_usd = equity_usd - firstbalance
		pnl_btc = equity_btc - firstbtc
		
		print( 'Equity ($):		%7.2f'   % equity_usd)
		print( 'P&L ($)			%7.2f'   % pnl_usd)
		print( 'Equity (BTC):	  %7.4f'   % equity_btc)
		print( 'P&L (BTC)		  %7.4f'   % pnl_btc)
		print('\nLeverage: ' + str(lev))	
		num = threading.active_count() 
		print('Threads: ' + str(num) + ' out of ' + str(startnum * 3 + 1))	
		
		print('Percs')
		print(percs)
		t = 0
		for r in percs:
			t = t + math.fabs(percs[r])
		print('t result ' + str(t))
	except:
		PrintException()	
	"""
	print( '\nMean Loop Time: %s' % round( self.mean_looptime, 2 ))
	#self.cancelall()
	print( '' )	
	print(' ')
	days	= ( datetime.utcnow() - self.start_time ).total_seconds() / SECONDS_IN_DAY
	print('Volumes Traded Projected Daily of Required (' + str(days) + ' days passed thus far...)')
	print('Equity: $' + str(round(self.equity_usd*100)/100))
	btc = self.get_spot('BTC/USDT')
	print('btc')
	percent = self.equity_usd / btc
	volumes = []
	tradet = 0
	feest = 0
	for pair in pairs:
		gettrades = self.getTrades(pair, 0, 0, 0)

		#print(gettrades)
		volume = (gettrades[0] / (gettrades[2]))
		feest = feest + gettrades[0] * 0.0002
		tradet = tradet + volume * 30
		printprint = True
		if pair in fifteens:
			volume = (volume / 15000)
		elif pair in tens:
			volume = (volume / 10000)
		elif pair in fives:
			volume = (volume / 5000)
		elif pair in threes:
			volume = (volume / 3000)
		else:
			printprint = False
			volume = (volume / 25000)
		volumes.append(volume)
		#print(volume)
		if printprint == True:
			print(pair + ': ' + str(round(volume*1000)/10) + '%' + ', (Real) USD traded: $' + str(round(gettrades[0]*100)/100) + ', fees paid: $' + str(round(gettrades[1] * 10000)/10000))
		else:
			print('(Real) USD traded: $' + str(round(gettrades[0]*100)/100) + ', fees paid: $' + str(round(gettrades[1] * 10000)/10000))
	volumes.sort()
	h = 100
	for i in range(0,5):
		if volumes[-i] < h and volumes[-i] > 0:
			h = volumes[-i]
			if h > 1:
				h = 1
	try:
		h = 1 / h
	except:
		h = 1
	mult = h
	h = h * self.equity_usd

	print('Approx. traded volumes over 30 days: ' + str(tradet) + ', in BTC: ' + str(round(tradet/btc*1000)/1000))
	print('Approx. Min Equity at 25x in USD to Achieve 100% Daily Requirements Across 6 Highest %s Above: $' + str(round(h * 100)/100))
	diff = h / self.equity_usd
	print('That\'s ' + str(round(diff*100)/100) + 'x the balance now, bringing projected USD/month to: ' + str(round(tradet * diff * 100)/100) + ', and BTC: ' + str(round((tradet * diff / btc)* 100)/100))
	apy = 365 / (gettrades[2])
	pnl = (((self.equity_usd + feest) / self.equity_usd) -1) * 100
	pnl2 = pnl * apy
	print('Now, if we were running in a trial mode of Binance Market Maker Program\'s Rebates, or if we had achieved these rates already, we would have earned $' + str(round(feest * 100)/100) + ' by now, or rather earning ' + str(round(pnl*1000)/1000) + '% PnL so far, or ' + str(round(pnl2*1000)/1000) + ' % Annual Percentage Yield!')
	btcneed = (((tradet * diff / btc) / 3000) )
	if btcneed < 1 and btcneed != 0:
		h = h / btcneed
		print('For 3000 btc/month volumes, would make the equity minimum approx. $' + str(round(h * 100)/100))
	"""
lenords = {}
def aThread(coin):
	while True:
		try:
			global skews, lenords
			#print(coin)
			dummy_event.wait(timeout=((1/25)*1))
			ords = ftx.fetchOpenOrders( coin )
			lenords[coin] = len(ords)
			#if len(ords) > 0:
				#print(coin + ' lenords: ' + str(len(ords)) + ' & lev: ' + str(levs[coin.split('-')[0]]))
			
			direction = 'buy'
			prc = bids['ftx'][coin]
			go = True
			print(wanting)
			#sleep(1000)


			if coin.split('-')[0] not in skews:
				skews[coin.split('-')[0]] = 0
			for direction in ['buy', 'sell']:
				if direction == 'buy' and skews[coin.split('-')[0]] < -1 * balance * 0.75 or direction == 'sell' and skews[coin.split('-')[0]] > balance * 0.75:
					print('wowwwww market out yo ' + coin)
					#if 'ETH' in coin:
						#print(wanting[coin])
					#trading[coin] = True
					amt = wanting[coin]

					if amt < 0:
						amt = amt * -1
					if direction == 'buy':
						prc = asks['ftx'][coin]
					elif direction == 'sell':

						prc = bids['ftx'][coin]
					doOrder(coin, direction, amt, prc, 1, [], False)
			if coin in wanting:
				
				
				if go == True:
					wanting[coin] = (wanting[coin] / percs[coin.split('-')[0]]) * 3
					if wanting[coin] < balance / 7:
						wanting[coin] = wanting[coin] * 2
				   # #sleep(1)
					try:
						#dummy_event.wait(timeout=((1/25)*1))
						#ords = ftx.fetchOpenOrders( coin )
						gogo = True
						for o in ords:
							if direction == o['info']['side'] and o['info']['future'] == coin:
								gogo = False

								qty = o['info']['remainingSize'] 
								if qty < 0:
									qty = -1 * qty
								print(qty)
								#138 < 18 * 0.15
								#if 'BTC' in coin:
									#print('skews n wanting ' + coin)
									#print(direction)
									#print(skews[coin.split('-')[0]])
									#print(wanting[coin] * 0.15)
									##sleep(1)
								
								if direction == 'sell' and -1 * balance / 4 < skews[coin.split('-')[0]] or direction == 'buy' and balance / 4 > skews[coin.split('-')[0]]:
									if prc != o['info']['price']:

										trading[coin] = True
										dummy_event.wait(timeout=((1/25)*1))
										try:
											e = ftx.editOrder( o['info']['id'], coin, 'limit', direction, float(qty), prc, {'postOnly': True} )
										except Exception as e:
											PrintException()
											try:
												e = ftx.cancelOrder(o['info']['id'], coin)
											except:
												abc=123
										##sleep(1)	
								else:
									print(coin + ' skew bad on ' + direction)
								#print(e)
						print(wanting)
						#sleep(1000)
						#if 'ETH' in coin:
							#print(gogo)
							#print(direction)
							#print(skews[coin.split('-')[0]])
							#print(wanting[coin] * 0.15 )
						if gogo == True:
							
							if 'BTC' in coin:
								#print('skews n wanting ' + coin)
								#print(direction)
								#print(skews[coin.split('-')[0]])
								#print(wanting[coin] * 0.15)
								if direction == 'sell' and -1 * balance / 4 < skews[coin.split('-')[0]] or direction == 'buy' and balance / 4 > skews[coin.split('-')[0]]:
									abc=123
								else:
									print('can\'t ' + direction)
							   ##sleep(10)

							if direction == 'sell' and -1 * balance / 4 > skews[coin.split('-')[0]] and direction == 'buy' and balance / 4 < skews[coin.split('-')[0]]:
								print('bad can\'t order!')
								dummy_event.wait(timeout=5)
							if direction == 'sell' and -1 * balance / 4 < skews[coin.split('-')[0]] or direction == 'buy' and balance / 4 > skews[coin.split('-')[0]]:
								  
								#if 'ETH' in coin:
									#print(wanting[coin])
								trading[coin] = True
								doOrder(coin, direction, wanting[coin], prc, 1)
							else:
								print(coin + ' skew bad on ' + direction)
							

						
					except:
						PrintException()
						
				
		except:
			PrintException()
			
	
runtimefirst = True
def doCheckTrading():
	global trading, wanting, skews
	for coin in mids['ftx']:
		if coin.split('-')[0] in levs:
			
			try:
				if coin.split('-')[0] not in skews:
					skews[coin.split('-')[0]] = 0
				direction = 'buy'
				prc = bids['ftx'][coin]
				go = False
				
				if coin in wanting:
					if wanting[coin] > 0:
						go = True
						#print('1')
						try:
							if skews[coin.split('-')[0]] > wanting[coin] * 0.15:
								#print('cancel2! ' + coin)
								#ords = ftx.fetchOpenOrders( coin )
								gogo = True
								#for o in ords:
									#ftx.cancelOrder( o['info']['id'] , o['info']['future'])
								go = False
						except:
							PrintException()
					if wanting[coin] < 0:
						go = True
						#print('3')
						try:
							if skews[coin.split('-')[0]] < wanting[coin] * 0.15 * mids['ftx'][coin]:   
								
								#ords = ftx.fetchOpenOrders( coin )
								gogo = True
								#for o in ords:
								#	ftx.cancelOrder( o['info']['id'] , o['info']['future'])
								#print('cancel! ' + coin)
								go = False
						except:
							PrintException()
						wanting[coin] = wanting[coin] * -1
						direction = 'sell'
						prc = asks['ftx'][coin]
					
					if go == True:
						wanting[coin] = (wanting[coin] / levs[coin.split('-')[0]]) * 3
					   # #sleep(1)
						try:
							dummy_event.wait(timeout=((1/25)*1))
							ords = ftx.fetchOpenOrders( coin )

							lenords[coin] = len(ords)

							gogo = True
							for o in ords:
								if direction == o['info']['side'] and o['info']['future'] == coin:
									gogo = False

									qty = o['info']['remainingSize'] 
									#138 < 18 * 0.15
									#if 'BTC' in coin:
										#print('skews n wanting ' + coin)
										#print(direction)
										#print(skews[coin.split('-')[0]])
										#print(wanting[coin] * 0.15)
										##sleep(1)

									
									if direction == 'sell' and -1 * balance / 4 < skews[coin.split('-')[0]] or direction == 'buy' and balance / 4 > skews[coin.split('-')[0]]:
										if prc != o['info']['price']:

											trading[coin] = True
											#e = ftx.editOrder( o['info']['id'], coin, 'limit', direction, float(qty), prc, {'postOnly': True} )
											##sleep(1)	
									else:
										print(coin + ' skew bad on ' + direction)
									#print(e)
							#if 'ETH' in coin:
								#print(gogo)
								#print(direction)
								#print(skews[coin.split('-')[0]])
								#print(wanting[coin] * 0.15 )
							if gogo == True:
								

								if direction == 'sell' and -1 * balance / 4 > skews[coin.split('-')[0]] and direction == 'buy' and balance / 4 < skews[coin.split('-')[0]]:
									print('bad can\'t order!')
									dummy_event.wait(timeout=5)
								if direction == 'sell' and -1 * balance / 4 < skews[coin.split('-')[0]] or direction == 'buy' and balance / 4 > skews[coin.split('-')[0]]:
									  
									#if 'ETH' in coin:
										#print(wanting[coin])
									trading[coin] = True
									#doOrder(coin, direction, wanting[coin], prc, 1)
								else:
									print(coin + ' skew bad on ' + direction)

							
						except:
							PrintException()
							
					
			except:
				PrintException()
				

def doCalc():
	index = 59
	while True:
		try:
			#sleep(3)
			r = random.randint(0, 1000)
			if r <= 5:
				cancelall()

			global levs, premiumwinners, arbwinnersc, arbwinnersavg, maxmax, trading, ts, runtimefirst
			#dt_to_string = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

			#added = worksheet2.append_row([dt_to_string, '=VALUE(' + str((balance/firstbalance-1)*100) + ')'], 'USER_ENTERED')
			
			
			
			doCheckTrading()
			rans = []
			toran = []
			#print('w3')
			#print(wanting['BTC-0326'])
			#print(wanting['BTC-1225'])
			#print(wanting['BTC-PERP'])
			donecoins = []
			print(len(wanting))
			for w in wanting:
				toran.append(w)
			for i in range(0, len(toran)*4-1):
				ran = random.randint(0, len(toran)-1)
				coin = toran[ran]
				if coin not in donecoins:
					print(coin)		
					donecoins.append(coin)
				
					

					 

					t = threading.Thread(target=aThread, args=(coin,))
					t.daemon = True
					ts.append(t)
					t.start()
			rans = [] 
			donecoins = []		   
			toran = []
			for t in trading:
				if t in marketList:
					if trading[t] == False or result[t.split('-')[0]] <= 1:
						toran.append(t)
			
				for i in range(0, len(toran)*4-1):
					ran = random.randint(0, len(toran)-1)
					
					coin = toran[ran]
					if coin not in donecoins:
						donecoins.append(coin)   
						#print(coin)	 
						if coin in marketList:
						
							t = threading.Thread(target=doMm, args=(coin,))
							#t.daemon = True
							#ts.append(t)
							#t.start()
			done = False
			#sleep(5)
			num = threading.active_count() 
			print('threads outside loop: ' + str(num) + ' out of ' + str(startnum * 3 + 1))
			while done == False:
				#sleep(5)
				
				#print(num % 4)
				
					
					
				#print('threads: ' + str(num))
				if num <= startnum * 3 + 1:
					
					done = True
					#for t in ts:
					#	t.exit()
					ts = []
				index = index + 1
				if index >= 10:
					index = 0
					output_status()
				sleep(1)
			sleep(1)
		except:
			PrintException()
ftx  = ccxt.ftx({
'apiKey': apikey,   
			'secret': apisecret,
'enableRateLimit': True

})
markets = ftx.fetchMarkets()
marketList = []
for m in markets:
	if 'OIL' not in m['symbol'] and '-' in m['symbol']:
		marketList.append(m['symbol'])
print(marketList)
cancelall()
sizeIncrements = {}
r = requests.get('https://ftx.com/api/markets').json()['result']
for m in r:
	sizeIncrements[m['name']] = m['sizeIncrement'] 
markets = binance.fetchMarkets()
futs = '200925'
for m in markets:
	#print(m['id'])
	try:
		binance.dapiPrivatePostLeverage({'symbol': m['id'], 'leverage': 75})
	except:
		abc=123
huobi = ccxt.huobipro({"urls": {'api':{'public': 'https://api.hbdm.com/swap-api',
'private': 'https://api.hbdm.com/swap-api'}}})
insts			  = binance.fetchMarkets()
#print(insts[0])

bin_futures_all =   insts
funding = {}
exchanges = ['binance', 'kraken', 'ftx', 'huobi', 'okex']
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
ticksizes = {}
rates = {}
for ex in exchanges:
	rates[ex] = {}
"""
huobi = requests.get("https://api.hbdm.com/api/v1/contract_contract_info").json()['data']
huobis = []
dts = []
for market in huobi:
	#stri = str(huobi[market])
		#if 'usd' in market['quoteId']:
	if market['symbol'] not in huobis:
		huobis.append(market['symbol'])
	dt = market['delivery_date']
	expiry  = datetime.datetime.strptime( 
										   dt, 
											'%Y%m%d' )
			
	#print(dt)
	dt = dt[-4:]
	if dt not in dts:
		dts.append(dt)		  
	now  = datetime.datetime.utcnow()

	days	= ( expiry - now ).total_seconds() / SECONDS_IN_DAY
	#print(days)
	expis[dt] = days
	#print(expis)

	#print(huobi[market])

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

		now  = datetime.datetime.utcnow()
		days	= ( expi - now ).total_seconds() / SECONDS_IN_DAY
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

allfuts = []
expiries = {}
hcontracts = []

for contract in huobis:
	for futureend in futureends:
		hcontracts.append(contract + futureend)

config = {L2_BOOK: hcontracts}
fh.add_feed(HuobiDM(config=config, callbacks={L2_BOOK: BookCallback(book)}))
kcontracts = []
binance = requests.get("https://dapi.binance.com/dapi/v1/premiumIndex").json()
#binance_f = requests.get("https://fapi.binance.com/fapi/v1/premiumIndex").json()
kraken = requests.get("https://futures.kraken.com/derivatives/api/v3/tickers").json()

for market in kraken['tickers']:
	if 'tag' in market:
		kcontracts.append(market['symbol'].upper())
#print(kcontracts)
config = {TICKER: kcontracts}
fh.add_feed(KrakenFutures(config=config, callbacks={TICKER: TickerCallback(ticker)}))
"""
fcontracts = []
ftxmarkets = requests.get("https://ftx.com/api/futures").json()['result']
for market in ftxmarkets:
	if 'MOVE' not in market['name'] and 'HASH' not in market['name'] and 'BERNIE' not in market['name'] and 'TRUMP' not in market['name'] and 'BIDEN' not in market['name'] and 'HASH' not in market['name'] and 'BLOOM' not in market['name'] and 'PETE' not in market['name'] and 'WARREN' not in market['name'] : 
		fcontracts.append(market['name'])
config = {TICKER: fcontracts}
fh.add_feed(FTX(config=config, callbacks={TICKER: TickerCallback(ticker)}))
#loop = asyncio.get_event_loop()

t = threading.Thread(target=loop_in_thread, args=())
t.start()
sleep(5)
levs = {'EXCH': 0.37553863680201305, 'BTMX': 1.5414075400914378e-07, 'KNC': 6.504949311775132e-05, 'AMPL': 0.0003068704707663269, 'XRP': 0.0006384053495788409, 'ZEC': 0.013748364608799758, 'COMP': 0.0629017519054634, 'ETH': 2.0804287716760284, 'PAXG': 0.06948621343310857, 'FIL': 0.18360624334823186, 'OKB': 0.004431717207269474, 'SUSHI': 0.0007188568091976016, 'LINK': 0.10218120047799369, 'PRIV': 0.05535607927851392, 'EOS': 0.013079940586044732, 'LEO': 1.0682260698596705e-05, 'UNI': 0.006283060901768046, 'ATOM': 0.0039046197880313782, 'TRX': 4.467987974508902e-05, 'BNB': 0.07183256137756255, 'HNT': 1.960033017153904e-05, 'YFI': 2.0804287716760284, 'DEFI': 0.7226054407069601, 'AAVE': 0.011336436999694966, 'TRYB': 2.6519982646385847e-06, 'AVAX': 0.0013048080367771176, 'VET': 1.3166190327889263e-06, 'ALT': 0.5072715134352992, 'ADA': 0.00011662264337981375, 'TOMO': 7.651949823380968e-05, 'BTC': 2.0804287716760284, 'CREAM': 0.029009585298679273, 'DOT': 0.0069686083325276845, 'BCH': 0.8946385933299136, 'XTZ': 0.002295816002623051, 'ETC': 0.0006230217286083596, 'THETA': 0.000824750143370905, 'DOGE': 4.9580533201608386e-08, 'LTC': 0.21036516090203852, 'USDT': 0.00025816775330248843, 'XAUT': 0.05589805457579935, 'DMG': 8.515814764419041e-06, 'MTA': 3.780109516306997e-05, 'SHIT': 0.17053239923391053, 'MKR': 0.01108933548734965, 'CUSDT': 1.3594205858973971e-07, 'CHZ': 1.1212631509476283e-07, 'DRGN': 0.03747354727919051, 'MATIC': 3.849056292476446e-06, 'FLM': 2.4591184576301782e-05, 'BAL': 0.0009743637094156327, 'BSV': 0.6206267187197785, 'BRZ': 1.901169209272247e-06, 'HT': 0.0008406819850498995, 'MID': 0.3298700363253504, 'OMG': 0.0003251759801236203, 'NEO': 0.0024258124136339668, 'ALGO': 0.0002364707420270012, 'RUNE': 6.511742139383555e-05, 'UNISWAP': 0.41328401717525715, 'SXP': 0.002745614771531447, 'SOL': 0.00039568130566015446}
for lev in levs:
	if levs[lev] == 0:
		levs[lev] = 1

dummy_event = threading.Event()
levsdone = True
def ohlcvs():
	global levs, levsdone
	while True:
		try:
			cvs = {}
			for arb in mids['ftx']:
				if 'PERP' in arb:
					try:
						if 'PERP' in arb:
							dummy_event.wait(timeout=((1/25)*1))
							ohlcvs = ftx.fetch_ohlcv(arb)
							vs = []
							for ohlcv in ohlcvs:
								vs.append(ohlcv[-1] * ohlcv[-2])
							#print(arb)
							#print(sum(vs))
							if len(vs) > 0:
								cvs[arb.split('-')[0]] = (sum(vs))
							else:
								cvs[arb.split('-')[0]] = 0
					except Exception as e:
						print(e)
			t = 0
			c = 0
			maxi = 0
			maxi2 = 0
			maxi3 = 0
			maxi4 = 0
			for v in cvs:
				t = t + cvs[v]
				c = c + 1
				if cvs[v] > maxi:
					maxi4 = maxi3
					maxi3 = maxi2
					maxi2 = maxi
					maxi = cvs[v]
			t = t - maxi - maxi2 - maxi3 - maxi4
			avg = t / cw
			#print(avg)
			levs = {}
			newlist = {}
			
			t = 0
			for v in cvs:
				if cvs[v] < maxi3:
					t = t + cvs[v]
					newlist[v] = cvs[v]
					
			#print(t)
			#print('average')
			#print(avg)
			maxlev = 0
			for v in cvs:
				
				levs[v] = (5 * cvs[v] / t)
				if levs[v] > 10:
					levs[v] = 4.5
				if levs[v] > 7:
					levs[v] = 3.5
				if levs[v] > maxlev:
					maxlev = levs[v]
			levsnew = {}
			t = 0
			for l in levs:
				t = t + levs[l]
			margin = ftx.privateGetAccount()
#			marg = 1 / margin['result']['openMarginFraction']

			marg  = 5
			mult = 5
			if marg > 20: #((20 / 20.53) * 20) / 2
				mult = ((5 / marg) * 5) / 2
			print('mult')
			print(mult)
			#sleep(1000)
			for l in levs:

				levsnew[l] = (levs[l] / t) * mult# edit to account for int rounddown of percs object later
			#levs = levsnew
			levsdone = True

			#print('levs')
			#print(levs)
			
			#levs['BTC'] = 10
			#levs['ETH'] = 10
			#newlevs = levs
			#percs2 = {}
			#for l in levs:
			#	percs2[l] = levs[l] / maxlev
			#	newlevs[l] = percs2[l] * 7.5
			#levs = newlevs
			#for lev in levs:
			#	if levs[lev] == 0:
			#		levs[lev] = 1
			print('levs')
			print(levs)
			
		except Exception as e:
			print(e)


t = threading.Thread(target=ohlcvs, args=())
t.daemon = True
ts.append(t)
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
	  #	  #print(coin)
	  #	  #print(math.fabs(maximum) * 100)
	  #	  #print(math.fabs(minimum) * 100)	 
	  #	  #print(str(0.015*3))
	  #	  #print(' ')
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
	 #		   #print({'ex': ex, 'coin': coin, 'arb': APRS[ex][coin]})
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
	#print(percs)		
	for coin in longshorts:
		if longshorts[coin] == 'short':
			try:
				tobuy[coin] = tobuy[coin] * -1
				tobuy[coin.replace('PERP', futs)] = tobuy[coin.replace('PERP', futs)] * -1
			except:
				abc=123
	#print(tobuy)
	##sleep(100)
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
					
					#print(int(tobuy[coin] / divisor))
					#print(tobuy[coin])
					if direction == 'SELL':
						
						binance.dapiPrivatePostOrder(  {'timeInForce': 'GTC', 'symbol': coin, 'side': direction, 'type': 'LIMIT', 'price': bbo['bid'], 'quantity': int(tobuy[coin] / divisor),"newClientOrderId": "x-v0tiKJjj-" + randomword(15)})
					else:
						binance.dapiPrivatePostOrder(  {'timeInForce': 'GTC', 'symbol': coin, 'side': direction, 'type': 'LIMIT', 'price': bbo['ask'], 'quantity': int(tobuy[coin] / divisor),"newClientOrderId": "x-v0tiKJjj-" + randomword(15)})
		except:
			PrintException()
	#print(tobuy)
balances = {}
totrade = ['BTC', 'ETH', 'LINK', 'ADA']
pos = {}
usdpos = {}
skews = {}
for t in totrade:
	balances[t] = 0
def updatePositions():
	while True:
		try:
			#sleep(3)
			global positions, skews
			skewsnew = {}
			positions	  = ftx.privateGetPositions()['result']
			for p in positions:
				name = p['future']
			
				#if p['entryPrice'] is not None:
				#	#print(p)
				skewsnew[p['future'].split('-')[0]] = 0
				size = float(p['size'])
				if p['side'] == 'sell':
					size = size * -1
				pos[p['future']] = size
				usdpos[p['future']] = float(p['cost'])
				
			for p in positions:
				size = float(p['cost'])
				#if p['side'] == 'sell':
				 #   size = size * -1
				
				skewsnew[p['future'].split('-')[0]] = skewsnew[p['future'].split('-')[0]] + size
			
			skews = skewsnew
			for skew in skews:
				if skews[skew] > 0.75 * balance or skews[skew] < -0.75 * balance:
					print('skew ' + skew + ': ' + str(skews[skew]))
			#sleep(3)
			dummy_event.wait(timeout=((1/25)*1))
		except:
			#sleep(9)
			PrintException()
	
lev = 0
firstrun = True
firstbalance = 0
firstbtc = 0
def updateBalance():
	while True:
		try:
			#sleep(3)
			global firstrun, firstbalance, balance, lev, firstbtc
			bal2 = ftx.fetchBalance()
			newbal = 0
			##print(bal2)
			for coin in bal2['info']['result']:
				newbal = newbal + coin['usdValue']  
			t = 0
			for pos in usdpos:
				t = t + math.fabs(usdpos[pos])
			lev = t / newbal
			balance = newbal
			#print(balance)
			#print(lev)
			if firstrun == True and balance != 0 and mids['ftx']['BTC-PERP'] > 0:
				firstrun = False
				firstbalance = balance

				firstbtc = round(balance / mids['ftx']['BTC-PERP'] * 100000000) / 100000000
			#if random.randint(0,100) <= 1:
			#	print('balance: ' + str(balance))
			#sleep(3)
			dummy_event.wait(timeout=((1/25)*1))
		except:
			#sleep(10)
			PrintException()

print(1)
startnum = threading.active_count() 

t = threading.Thread(target=updateBalance, args=())
t.daemon = True
ts.append(t)
t.start()
print(3)
#sleep(1)
t = threading.Thread(target=updatePositions, args=())
t.daemon = True
ts.append(t)
t.start()
print(2)

wanting = {}
percs = {}
def wantingThread():
	global wanting, maxmax, trading, ts, runtimefirst, expis, result, percs

	while True:
		try:
			for ex in mids:
				for dt in mids[ex]:
					if dt.split('-')[1] not in expis:
						try:
						
							if 'PERP' in dt:
								expis[dt.split('-')[1]] = 30000
							else:
								now  = datetime.datetime.utcnow()
								expiry  = datetime.datetime.strptime( 
														   '2021' + dt.split('-')[1], 
															'%Y%m%d' )
								days	= ( expiry - now ).total_seconds() / SECONDS_IN_DAY
								#print(days)
								#print(dt.split('-')[1])
								expis[dt.split('-')[1]] = days
						except:
							abc=123
			try:
				if levsdone == True:
					dts = []
					coins = []
					tempmids = mids

					for ex in tempmids:
						for coin in tempmids[ex]:
							#print(coin)
							if coin.split('-')[1] not in dts:
								dts.append(coin.split('-')[1])
							if coin.split('-')[0] not in coins:
								coins.append(coin.split('-')[0])
					arbs = {}
					exes = {}
					#print(expis)
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
									
									exes[coin][dt.split('-')[1]][tempmids[ex][dt]] = ex
								except:
									abc=123
									#PrintException()
							   # print(dt)
								if coin in dt:
									
									try:
										if '-' in dt:
											if 'e' not in str(tempmids[ex][dt]):
											
												arbs[coin][dt.split('-')[1]].append(tempmids[ex][dt])
											
									except:
										#PrintException()
										abc=123
					
					
					perps = {}
					lalaexes = {}
					for coin in coins:
						for ex in tempmids:
							for dt in tempmids[ex]:
							   # print(dt)
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
					#			PrintException()
								PrintException()
					#print(exes)
					#print(arbs)
					#print(expis)
					thearbs = []
					coinarbs = {}

					"""
					print('arbs')
					print(len(arbs))
					print('expis')
					print(len(expis))
					print('tempmids')
					print(len(tempmids['ftx']))
					"""
					for coin in arbs:
						for dt in expis:
							if dt != 'PERP' and coin + '-PERP' in marketList:
								trading[coin + '-PERP'] = False
								trading[coin + '-' + dt] = False
								try:
									#print(len(arbs[coin][dt]))
									#if len(arbs[coin][dt]) > 0:
									minimum = tempmids['ftx'][coin + '-PERP']  #10900/10709 #pos long perp, neg short perp
									
									maximum = tempmids['ftx'][coin + '-' + dt] #pos short fut, neg long fut #pos long perp, neg short perp
						 #		   if coin == 'BTC':
						 ##			   #print(arbs[coin][dt])
						  #			  #print(maximum / minimum)
									thearb = ((((maximum / minimum)-1)*100)*365*levs[coin]) #1.1/1.05 = 
									#print(thearb)
									#print(expis[dt])
									#print('thearb of ' + coin + ' at ' + dt + ' in total ' + str(thearb)) 
									thearb = thearb / expis[dt] 
									coinarbs[thearb] = coin + '-' + dt 
									#print(thearb)
									#print( ' ' )
									#print(thearb)
									if thearb > 0.005 or thearb < -0.005:
										thearbs.append(thearb)
									else:
										thearbs.append(0)
									"""
									if thearb > 10 and coin != 'USDT':
									   # print(exes[coin][dt])
										thearbs.append({'exlong': exes[coin][dt][minimum], 'exshort': exes[coin][dt][maximum], 'coin': coin, 'thearb': thearb, 'dt': dt, 'arbscoindt': arbs[coin][dt]})
										#print({'exlong': exes[coin][dt][minimum], 'exshort': exes[coin][dt][maximum], 'coin': coin, 'thearb': thearb, 'dt': dt, 'arbscoindt': arbs[coin][dt]})
									"""
								  #  print('and after figuring out daily arb it\'s ' +  str(thearb))
									
								except Exception as e:
									if coin not in str(e):
										PrintException()
									abc=123#PrintException()
					t = 0
					c = 0
					#print('thearbs')
					#print(len(thearbs))
					for arb in thearbs:
						
						t = t + math.fabs(arb)
						if arb != 0:
							c = c + 1
					percs = {}

					result = {}
					wanting = {}
					if c > 0:
						avg = t / c
						c1 = c
						
						t = 0 
						c = 0 
						maxi = 0
						
						t = 0 
						c = 0 
						maxi = 0
						for arb in thearbs:
							if math.fabs(arb) > avg:
								#print(coinarbs[arb] + ' is a good coin no?')
								if arb > maxi:
									maxi = arb
								if arb > maxmax:
									maxmax = arb
								t = t + math.fabs(arb)
								c = c + 1
						cvs = {}
						for arb in thearbs:
							if arb != 0:	
								try:
									#if math.fabs(arb) > avg:
											
									percs[coinarbs[arb].split('-')[0]] = arb / t
									lev = coinarbs[arb].split('-')[0]
									percs[lev] = percs[lev] * 10
									result[lev] = ((2 * percs[lev] + 2 * levs[lev]) / 4) * 10
						
									if coinarbs[arb] in usdpos: #-0.3 * 10 * 100 + 360 #-0.16*400*10+1826=1186
																				   #-0.16*400*10-266=-906
										wanting[coinarbs[arb]] = percs[lev] * balance
										wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * -1
										wanting[coinarbs[arb]] = wanting[coinarbs[arb]]  - usdpos[coinarbs[arb]]
								
									else:
										wanting[coinarbs[arb]] = percs[lev] * balance
									
										wanting[coinarbs[arb]] = wanting[coinarbs[arb]] * -1
									if coinarbs[arb].split('-')[0] + '-PERP' in usdpos:
										wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  percs[lev] * balance - usdpos[coinarbs[arb].split('-')[0] + '-PERP']
									else:
										wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  percs[lev] * balance
									"""
									
								else:
									if arb != 0:
										percs[coinarbs[arb].split('-')[0]] = 0
										if coinarbs[arb] in usdpos:
										
											wanting[coinarbs[arb]] = -1 * usdpos[coinarbs[arb]]
										else:
											
											wanting[coinarbs[arb]] = 0
										if coinarbs[arb].split('-')[0] + '-PERP' in usdpos:
											wanting[coinarbs[arb].split('-')[0] + '-PERP'] = -1 * usdpos[coinarbs[arb].split('-')[0] + '-PERP']
											
										else:
										
											wanting[coinarbs[arb].split('-')[0] + '-PERP'] =  0
									"""
								except:
									PrintException()
						for pos2 in usdpos:
							if pos2 not in wanting:
								if usdpos[pos2] != 0:
									wanting[pos2] = -1 * usdpos[pos2]
									#print(pos2)
									#print(wanting)
									##sleep(10)
						
						#print('w1')
						#print(wanting['BTC-0326'])
						#print(wanting['BTC-1225'])
						#print(wanting['BTC-PERP'])
						#pos short fut, neg long fut #pos long perp, neg short perp
						for coin in wanting:
							wanting[coin] = wanting[coin] / mids['ftx'][coin] / (balance / 200) 
							#   round(0.1 * (0.1)) / 0.1
							# abc = -937.0961358420444
							# abc = abc / 28 / 10
							# abc = ( round(abc * (0.1)) / 0.1)
							wanting[coin] = ( round(wanting[coin] * (1/sizeIncrements[coin])) / (1/sizeIncrements[coin]))   
						lowers = {}
						counts = {}
						twanting = {}
						#print('w2')
						#print(wanting['BTC-0326'])
						#print(wanting['BTC-1225'])
						#print(wanting['BTC-PERP'])
						for arb in wanting:
							lowers[arb] = 999999999999999
							counts[arb.split('-')[0]] = 0
							
							twanting[arb] = 0
						for arb in wanting:
							if 'PERP' not in arb:

								try:
									counts[arb.split('-')[0]] = counts[arb.split('-')[0]] + 1
									twanting[arb.split('-')[0] + '-PERP'] = twanting[arb.split('-')[0] + '-PERP'] + wanting[arb]
								except:
									counts[arb.split('-')[0]] = 1
									twanting[arb.split('-')[0] + '-PERP'] = 0 + wanting[arb]
						for arb in wanting:
							#print(arb)
							try:
								if counts[arb.split('-')[0]] == 2 and 'PERP' not in arb:
									wanting[arb] = wanting[arb] * mids['ftx'][arb] * (balance / 50) 
									wanting[arb] = wanting[arb] + usdpos[arb]
									wanting[arb] = wanting[arb] * -1
									
									
									twanting[arb] = wanting[arb] / 2
									twanting[arb] = twanting[arb] - usdpos[arb]
									twanting[arb] = twanting[arb] * -1
									twanting[arb] = twanting[arb] / mids['ftx'][arb] / (balance / 50) 
									
								elif counts[arb.split('-')[0]] == 2 and 'PERP' in arb:
									wanting[arb.split('-')[0] + '-PERP'] = wanting[arb.split('-')[0] + '-PERP'] * mids['ftx'][arb.split('-')[0] + '-PERP'] * (balance / 50) 
									wanting[arb.split('-')[0] + '-PERP'] = wanting[arb.split('-')[0] + '-PERP'] + usdpos[arb.split('-')[0] + '-PERP']
									twanting[arb.split('-')[0] + '-PERP'] = wanting[arb.split('-')[0] + '-PERP'] / 2
									wanting[arb.split('-')[0] + '-PERP'] = wanting[arb.split('-')[0] + '-PERP'] - usdpos[arb.split('-')[0] + '-PERP']
									
									twanting[arb.split('-')[0] + '-PERP'] = twanting[arb.split('-')[0] + '-PERP'] / mids['ftx'][arb.split('-')[0] + '-PERP'] / (balance / 50) 
								else:
									twanting[arb] = wanting[arb]
								twanting[arb] = round(twanting[arb] * (1/sizeIncrements[arb])) / (1/sizeIncrements[arb])  
							except:
								twanting[arb] = wanting[arb]
						wanting = twanting
					
			except:
				PrintException()
				#sleep(2)
		except:
			PrintException()
			#sleep(2)

t = threading.Thread(target=wantingThread, args=())
t.daemon = True
t.start()
"""
import gspread


spreadsheetId = "1kJIZH2Ku2M_T_Grz6rGqMLfCrJhO_y-V77RCuMh4BeA"  # Please set the Spreadsheet ID.
sheetName = 'Sheet1'  # Please set the sheet name.
client = gspread.service_account(filename='../google.json')

sh = client.open_by_key(spreadsheetId)
worksheet = sh.worksheet("Sheet1")
try:   
	worksheet2 = sh.worksheet(apikey)
except:
	sh.add_worksheet(apikey, 1, 2)
	
	worksheet2 = sh.worksheet(apikey)
	worksheet2.append_row(['datetime', 'balance'])

"""
#sleep(10)

#sleep(2)

	#print(levs)
	##sleep(1000)
	##sleep(1000)
#ohlcvs()




def doMm(coin):
	global trading
	while True:
		try:
			try:
				if skews[coin.split('-')[0]] > 0:
					abc=123
			except:
				skews[coin.split('-')[0]] = 0
			
			for direction in ['buy', 'sell']:
				try:
					if direction == 'buy':

						prc = bids['ftx'][coin]
					else:
						prc = asks['ftx'][coin]
				except:
					abc=123
					#ob = ftx.fetchOrderBook(coin, 1)
					#print(ob)
				dummy_event.wait(timeout=((1/25)*1))
				ords = ftx.fetchOpenOrders( coin )
				lenords[coin] = len(ords)

				gogo = True
				for o in ords:
					if direction == o['info']['side'] and o['info']['future'] == coin:
						gogo = False
						#if 'ETH' in coin:
							#print('edit')
						qty = o['info']['remainingSize'] 
						if qty < 0:
							qty = -1 * qty
						print(qty)
						#138 < 18 * 0.15
						
							##sleep(1)
						try:
							if skews[coin.split('-')[0]] > 0:
								abc=123
						except:
							skews[coin.split('-')[0]] = 0
						if direction == 'sell' and -1 * balance / 80 < skews[coin.split('-')[0]] or direction == 'buy' and balance / 80 > skews[coin.split('-')[0]]:
							if prc != o['info']['price']:

								trading[coin] = True
								dummy_event.wait(timeout=((1/25)*1))
								try:
									e = ftx.editOrder( o['info']['id'], coin, 'limit', direction, float(qty), prc, {'postOnly': True} )
								except Exception as e:
									PrintException()
									try:
										e = ftx.cancelOrder(o['info']['id'], coin)
									except:
										abc=123
								#if direction == 'buy':
								#if 'DEFI' in coin:
									#print(direction + ' mm edit ' + coin)
									#PrintException()
							#else:
								#if 'DEFI' in coin:
									#print('same price mm edit gogo false...')
				if gogo == True:

					try:
						try:
							if skews[coin.split('-')[0]] > 0:
								abc=123
						except:
							skews[coin.split('-')[0]] = 0
						if direction == 'sell' and -1 * balance / 80 < skews[coin.split('-')[0]] or direction == 'buy' and balance / 80 > skews[coin.split('-')[0]]:
							#print(10 / mids['ftx'][coin])
							mm = doOrder(coin, direction, ((balance / 700)) / mids['ftx'][coin], prc, 1)
							#if direction == 'buy':
								#print('mm ' + coin)
								#print(mm)
					except Exception as e:
						if coin.split('-')[0] in str(e):
							mm = doOrder(coin, direction, 1 / mids['ftx'][coin], prc, 1)
							#if 'DEFI' in coin:
								#print(direction + ' mm ' + coin)
			

		except:
			PrintException()

			
import sys


print(0)
##sleep(1)
#sleep(7)
doCalc()

##sleep(1)
##sleep(20)
#updateBalance()
##sleep(5)
#doupdates()
##sleep(35)

startnum = 0
