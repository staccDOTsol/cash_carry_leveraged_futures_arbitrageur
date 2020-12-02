
var btc = 0;
const ccxt = require('ccxt')
          apikey = process.env.key
apisecret = process.env.secret

         ////////console.log(ftx)

        client     = new ccxt.ftx({
'apiKey': apikey,   
            'secret': apisecret
 })

        client1999     = new ccxt.binance({
'apiKey': 'O5Vi79dmUap4gFuSYTtnpyCwJsEimuAaV2lXNhefVhp5znuyJxhTWv28Ilx57RcL',   
            'secret': '7yCHza9tNBe5MkfYkoSuFAi1tjsGEYRkXsqrCWLTUIT7sZwErUcAwBDxlxlq7V7a',
            "options":{"defaultMarket":"futures"},
            'urls': {'api': {
                                     'public': 'https://testnet.binancefuture.com/dapi/v1',
                                     'private': 'https://testnet.binancefuture.com/dapi/v1',},}
 })

var client2 = new ccxt.ftx(

            {"apiKey": "",
            "secret": ""
 })
///client.urls['api'] = client.urls['test']
var usd2 = 0
var IM = 0
var orders = []
var LEV = 0
var olength = 0
var LEV_LIM = parseFloat(process.env.limit)
var startTime = new Date().getTime()
var oldstartTime = new Date().getTime() - 1000 * 60 * 60 * 24 * 7
var btcstart
var usdstart
var aprs = []
var yields = []
var btc4start
var usd4start
var usds = []
var levs = []
var usd4s = []
var prices = []
var btc4s = []
var btcs = []
var btc2 = 0
var apr;
var usdcad = 1;
var request = require("request")
async function getusdcad(){

	request.get('https://free.currconv.com/api/v7/convert?q=USD_CAD&compact=ultra&apiKey=56f9c260d80c736e4fc8', function(e, r, d){
		try{
			//usdcad = JSON.parse(d)['USD_CAD']
		}
		catch(err){
			//////console.log(err)
		}
	})
	
}
getusdcad()
setInterval(function(){
getusdcad()
}, 1000 * 60)

var usd4 = 0
var btc4 = 0
var ids = []
var vol = 0
var line
var tradesArr = []
var first = true;
var m;
var lines = []
var fee = 0
var btcusd;
var btcusdstart;
var positions = []
async function recursiveIncomes(thetime, thetime2, USDold){
				//////console.log(aprs.length)
					//////console.log(usds.length)
////console.log(thetime2)
	if (thetime == 9999999999999999999999){
	incomes = await client.dapiPrivateGetIncome({'limit': 1000, 'startTime': oldstartTime})
	
	incomes2 = await client1999.dapiPrivateGetIncome({'limit': 1000, 'startTime': oldstartTime})
	}
	else{
		incomes = await client.dapiPrivateGetIncome({'limit': 1000, 'endTime': thetime, 'startTime': 1597664686000})
	incomes2 = await client1999.dapiPrivateGetIncome({'limit': 1000, 'endTime': thetime, 'startTime': 1597664686000})
	
	}
	////console.log(incomes.length)
	////////////console.log(incomes)
	startbal = 0
	var newaprs = []
	var newusds = []

	var oldthetime2 = thetime2
	for(var inc in incomes2){
		if (incomes2[inc].asset == 'BTC'){
			if (incomes2[inc].time < thetime){
				thetime = incomes2[inc].time

			}
			if (incomes2[inc].time > thetime2){
				oldthetime2 = thetime2
				thetime2 = incomes2[inc].time
			}
			if (incomes2[inc].incomeType != 'TRANSFER' && incomes[inc].incomeType !='CROSS_COLLATERAL_TRANSFER'){
USDold += parseFloat(incomes2[inc].income)
}
else {
	////console.log(incomes2[inc].incomeType)
}
		}
	}
	for(var inc in incomes){
		if (incomes[inc].asset == 'BTC'){
			if (incomes[inc].time < thetime){
				thetime = incomes[inc].time

			}
			if (incomes[inc].time > thetime2){
				oldthetime2 = thetime2
				thetime2 = incomes[inc].time
			}
			if (incomes[inc].incomeType != 'TRANSFER' && incomes[inc].incomeType !='CROSS_COLLATERAL_TRANSFER'){
USDold += parseFloat(incomes[inc].income)
}
else {
	////console.log(incomes[inc].incomeType)
}
		}
	}
if (incomes.length == 1000){
	return(recursiveIncomes(thetime, thetime2, USDold))
}
else{
	return([thetime, USDold, thetime2])
}
}
/*
setInterval(async function(){
					//////console.log(aprs.length)
					//////console.log(usds.length)


	incomes = await recursiveIncomes(9999999999999999999999, 0, 0)
	////console.log(incomes)
		var d = incomes[2]
		var d2 = incomes[0]
		//////console.log(d2)
		var diff = d - d2;

		var s = diff / 1000
		var m = s / 60
		var h = m / 60
		var d = h / 24
		//////console.log(d)
		var y = d / 365


		apr = (incomes[1] - 0) / y
		////console.log(apr)
		if (usd2 != 0){
		btcs.push( [new Date().getTime(), -1 * (1-(btc2 / btcstart)) * 100])
				
				aprs.push( [new Date().getTime(), apr / 365])
				yields.push( [new Date().getTime(), (apr / 365) / (usd2)])
			}
			else {
				aprs.push( [new Date().getTime(), apr / 365])
			}
			//////console.log( aprs  )
}, 15000)
*/
async function testing123(){
	
}
testing123()
setInterval(function(){
	testing123()
}, 5 * 60 * 1000)
var adausd
var linkusd
setInterval(async function(){
	
	ethusd = await client2.fetchTicker('ETH-PERP')
	ethusd = ethusd['last']
	btcusd = await client2.fetchTicker('BTC-PERP')
	linkusd = await client2.fetchTicker('LINK-PERP')
	adausd = await client2.fetchTicker('ADA-PERP')
	//console.log(adausd)
	////////////console.log(btcusd)
btcusd = btcusd['last']
adausd = adausd['last']
linkusd = linkusd['last']

	////////////console.log(btcusd)
ethbtc = btcusd/ethusd

	if (first){
		m = await client.fetchMarkets()
	}
	
	//////////////////console.log(trades.length)

//////////////////console.log(account)
//account         = await client.fetchBalance()
//////////////////console.log(account)
//////////////console.log(account)
////////////console.log(btc)
 
btc = 0
////////////console.log(btc)
btc4 = 0
btc3  = 0

 bal2 = await client.fetchBalance()
 ////console.log(bal2)
for (var coin in bal2['info']['result']){
            btc4 += bal2['info']['result'][coin]['usdValue']  
}
	if (first)
{
	
first = false;
usdstart = btc4
}

 usds.push( [new Date().getTime(), -1 * (1-(btc4 / usdstart)) * 100])
 var d = new Date().getTime()
				var d2 = usds[0][0] //- 1000 * 60 * 60 * 24
				//////console.log(d2)
				var diff = d - d2;

				var s = diff / 1000
				var m = s / 60
				var h = m / 60
				var d = h / 24
				//////console.log(d)
				var y = d / 365


				apr = (usds[usds.length-1][1] -usds[0][1]) / y // (usds[usds.length-1][1] - 0.01348379) / y
				////console.log('')
				////console.log(apr)
					aprs.push( [new Date().getTime(), apr  ])
 yields.push( [new Date().getTime(), -1 * (1-(btc4 / usdstart)) * 100])
// aprs.push( [new Date().getTime(), -1 * (1-(btc4 / usdstart)) * 100])
				
 //bal3 = await client1999.fetchBalance()
 LEV = 0

//console.log(bal2.info.result)
// //////console.log(bal2)
 //btc3 = 0
 	//btc3 += parseFloat(bal2.info.totalMarginBalance)
 	//btc3 += parseFloat(bal3.info.totalMarginBalance)
 	////////console.log(bal2.info.result[c].usdValue / btcusd)
  //console.log(btc3)
  if (btc4 != 0){
        positions	   = await client.privateGetPositions()
        positions = positions['result']
        poses = 0
        for (var p in positions){
            name = positions[p]['future']
        if (parseFloat(positions[p]['entryPrice']) > 0)
            {
        	console.log(positions[p])
            size = parseFloat(positions[p]['cost'])
            if (size < 0){
            	size = size * -1
            }
            poses =  poses + size
            }
            }
            console.log('pos btc4 lev')
            console.log(poses)
            console.log(btc4)
            LEV = poses / btc4
            levs.push( [new Date().getTime(), LEV / LEV_LIM * 100])
            console.log(LEV)
        }

   //btc3=     parseFloat(bal = bal2.info.result[ 'USD' ] ['total'])

//////////////////console.log(account)

//btc3 = parseFloat(account2 [ 'info' ] ['totalMarginBalance'])
////////////////console.log(btc)

btc2 = btc  /  btcusd + btc3  /  btcusd

usd2 = parseFloat(btc + btc3)
//////console.log(btc2)

btc4 = btc /  btcusd
usd4 = btc4

////////console.log(bal2)
////////console.log(bal2['info'])
IM = LEV / 2 
       ////////console.log('lev')
       ////////console.log(LEV)	
//////////////console.log(btc2)


if (btc4 != 0){

prices.push([new Date().getTime(), -1 * (1-(btcusd / btcusdstart)) * 100])
	

//////console.log(usd2)
//////console.log(usdcad)
//////console.log(usd2)

btcs.push( [new Date().getTime(), -1 * (1-(btc2 / btcstart)) * 100])
	usd4s.push( [new Date().getTime(), -1 * (1-(usd4 / usd4start)) * 100])

btc4s.push( [new Date().getTime(), -1 * (1-(btc4 / btc4start)) * 100])

topost = {'theurl': theurl, 'amounts': 0, 'fees': 0, 'startTime': startTime, 'apikey': process.env.binancekey, 'usd': usd2, 'btc': btc2, 'btcstart': btc4start, 'usdstart': usd4start, 'funding': true}
                if (!first){
               request.post("http://jare.cloud:8080/subscribers", {json:topost}, function(e,r,d){
               	////////console.log(d)
               })
               	} 
               }
//////////////////console.log(btc)
}, 4500)
var theurl = process.env.theurl


const express = require('express');
var cors = require('cors');
var app = express();
app.use(cors());
var bodyParser = require('body-parser')
app.use(bodyParser.json()); // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({ // to support URL-encoded bodies
    extended: true
}));
app.set('view engine', 'ejs');
app.listen(process.env.PORT || 8888, function() {});
subscribers = {}
setInterval(async function(){
subscribers = {}

}, 10 * 60 * 1000)
app.post('/subscribers', cors(), (req, res) => {
let apikey = req.body.apikey
let apikey2 = req.body.apikey2
let usdstrat = false
if (apikey2 != undefined){
if (apikey2.length < 2){
usdstrat = false
}
else {
usdstrat = true

}
}

let btcsub = req.body.btc
let btcstartsub = req.body.btcstart
let fees = parseFloat(req.body.fees) * btcusd
let amounts = parseFloat(req.body.amounts)
let usdsub = req.body.usd
let usdstartsub = req.body.usdstart
let startTime = req.body.startTime
if (subscribers[apikey] == undefined && parseFloat(btcstartsub) != 0 && parseFloat(usdstartsub) != 0){
subscribers[apikey] = {'usdstrat': usdstrat, 'amounts': amounts, 'fees': fees, 'btc': btcsub, 'btcstart': btcstartsub, 'usd': usdsub, 'usdstart': usdstartsub, 'pnlbtc': [startTime, 0], 'pnlusd': [startTime,0]}
////////console.log(apikey)
}
else{
	if (parseFloat(btcstartsub) != 0 && parseFloat(usdstartsub) != 0){
	subscribers[apikey].amounts = amounts
	subscribers[apikey].usdstrat = usdstrat
	subscribers[apikey].fees = fees
	subscribers[apikey].btc = btcsub
	subscribers[apikey].btcstart = btcstartsub
	subscribers[apikey].usd = usdsub
	subscribers[apikey].usdstart = usdstartsub

subscribers[apikey].pnlbtc.push({'pnl': [startTime, -1 * (1-(btcsub / btcstartsub)) * 100], 'usdstrat': usdstrat})
subscribers[apikey].pnlusd.push({'pnl': [ startTime,-1 * (1-(usdsub / usdstartsub)) * 100], 'usdstrat': usdstrat})
}
	}
	//////////console.log(subscribers)
	//////////console.log(apikey + ' recent pnl btc: ' + subscribers[apikey].pnlbtc[subscribers[apikey].pnlbtc.length-1])

	//////////console.log(apikey + ' recent pnl usd: ' + subscribers[apikey].pnlusd[subscribers[apikey].pnlusd.length-1])
	res.send('ok')

	})


app.get('/update', cors(), (req, res) => {
pnlbtcs ={}
pnlusds = {}
feebtcs = {}
amtusds = {}
bal = 0
	usd = 0
	btcstart2 = 0
	usdstart2 = 0
	btc3 = 0
	usd3 = 0
	for (var sub in subscribers){
		usd3+=parseFloat(subscribers[sub].usd)
		usdstart2=parseFloat(subscribers[sub].usdstart)
	}
	for (var sub in subscribers){
		btc3=parseFloat(subscribers[sub].btc) 
		btcstart2=parseFloat(subscribers[sub].btcstart)
	}
for (var apikey in subscribers){
pnlbtcs[apikey.substring(0, 2)] = subscribers[apikey].pnlbtc[subscribers[apikey].pnlbtc.length-1]
pnlusds[apikey.substring(0, 2)] = subscribers[apikey].pnlusd[subscribers[apikey].pnlusd.length-1]
amtusds[apikey.substring(0, 2)] = parseFloat(subscribers[apikey].amounts )
feebtcs[apikey.substring(0, 2)] = parseFloat(subscribers[apikey].fees )
}
    res.json({btc: [new Date().getTime(), -1 * (1-(btc2 / btcstart)) * 100], 
    	btcusd: [new Date().getTime(), -1 * (1-(btcusd / btcusdstart)) * 100], 
    	btcusdprice: btcusd,
    	usd: [new Date().getTime(), -1 * (1-(usd2 / usdstart)) * 100],
    	lev: levs[levs.length-1],
    	usdbal: [new Date().getTime(), usd2],
    	orders: orders,
    	positions:positions,
    	usds: [usds[usds.length-1][0],usds[usds.length-1][1]],
    	aprs: [aprs[aprs.length-1][0], aprs[aprs.length-1][1]],
    	yields: [yields[yields.length-1][0], yields[yields.length-1][1]],
    	 qty: vol, line:line, fee:fee * btcusd,
        theurl: theurl,
        olength: olength ,
        start: startTime,
        apikey: "VCFund",
    	 pnlbtcs: pnlbtcs, subscribers: subscribers, feebtcs: feebtcs, amtusds: amtusds,
    	 pnlusds: pnlusds,btcbal: btc2, usddiff: -1 * (1-(usd3/ usdstart2)) * 100,  btcdiff:-1 * (1-(btc4 / btcstart2)) * 100, btcstart2, btcstart:btcstart, usdstart:usdstart})


})

app.get('/', (req, res) => {
	console.log(usds)
        res.render('indexFundingBulek.ejs', {
            btc: btcs, lines:lines,
            orders: orders,
            levs: levs,
    	usds: usds,
    	aprs: aprs,
    	yields: yields,
            btcusd: prices,btcusdprice: btcusd,
        theurl: theurl
        })

});


