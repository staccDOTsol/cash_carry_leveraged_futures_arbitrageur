const secret = '91571e8c-159aecb5-9bee9823-94dd8'
const key = "02f5fc60-ntmuw4rrsr-1b239bab-a21fb"
var ccxt = require('./ccxt')
var huobi = new ccxt.huobipro({
'apiKey': key,   
            'secret': secret
 })
var futs = new ccxt.huobifuts({
'apiKey': key,   
            'secret': secret
 })
var swap = new ccxt.huobiswap({
'apiKey': key,   
            'secret': secret
 })
let mids = {}
async function dorequest(ccsc){
	request("https://api.hbdm.com/swap-ex/market/detail/merged?contract_code=" + ccsc, function (e,r,d){
		d = JSON.parse(d)
		mids[ccsc.split('-')[0]] = d['tick']['ask'][0]
		//console.log(mids[ccs[c].split('-')[0]])
	})
}
var request = require("request")
let coinsto = ['BTC', 'ETH', 'XRP', 'BCH', 'LTC', 'EOS', 'LINK', 'DOT', 'ADA', 'BSV', 'ETC', 'TRX']
let ccs = []
for (var c in coinsto){
    ccs.push(coinsto[c] + '-USD')
}
async function lala(){
	tickers = await huobi.fetchTickers()
	for(var t in tickers){
		mids[t.split('/')[0]] = tickers[t].bid
	}
for (var c in ccs){
	dorequest(ccs[c])
}
	bal = await huobi.fetchBalance()
	bal2 = await swap.privatePostSwapAccountInfo()
	bal3 = await futs.privatePostContractAccountInfo()
	
	balance = 0
	for(var s in bal2['data'])
	{
		if (mids[bal2['data'][s].symbol]  != undefined){
balance = balance + parseFloat(bal2['data'][s].margin_balance) * mids[bal2['data'][s].symbol]
	}
}

	for(var s in bal3['data'])
	{
		if (mids[bal3['data'][s].symbol] != undefined){
balance = balance + parseFloat(bal3['data'][s].margin_balance) * mids[bal3['data'][s].symbol]
	}
}
	for(var t in bal['total']){
		if (t == 'USDT'){
			balance = balance + bal['total'][t]

		}
else {
	if(mids[t] != undefined){
	balance = balance + bal['total'][t] * mids[t]
}
}
	}
	console.log(balance)
}
lala()
setInterval(function(){
	lala()
}, 4000)