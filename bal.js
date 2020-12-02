
var btc = 0;
/*
var etrade = require('etrade');
 
var configuration = 
{
  useSandbox : true|true, // true if not provided
  key : '8c92ad02b3a9943eeaf4a01058c05eae',
  secret : '9a6ad6b7ca5a09f052907456abf1b474cf67332ece3566cf91898b794afc85dd'
}
 
var et = new etrade(configuration);
*/
//client.urls['api'] = client.urls['test']
var usd2 = 0
const fs = require('fs');
var IM = 0
var orders = []
var LEV = 0
var olength = 0
var LEV_LIM = parseFloat(process.env.limit)
var startTime = new Date().getTime()
var btcstart
var usdstart
var btc4start
var usd4start
var usds = []
var levs = []
var usd4s = []
var prices = []
var btc4s = []
var btcs = []
var btc2 = 0
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
var nasdaqs = []
var spxs = []
var djias = []
var btcusd;
var positions = []
async function testing123(){
	/*
	try{
	payments = await ftx.privateGetFundingPayments()
	t = 0
	c = 0
	for(var p in payments.result){
		if(payments.result[p].time == '2020-05-03T03:00:00+00:00'){
			t+=(payments.result[p].payment)
			c+=1
		}
	}
	//console.log(t/c)
	}
	catch(err){
		               request.post("http://jare.cloud:8080/badkeys", {json:{"theurl": theurl, 'ex': 'ftx (bin?)', 'err': err}}, function(e,r,d){
                //console.log(d)
            }
                )
	}
                */
}
testing123()
setInterval(function(){
	testing123()
}, 5 * 60 * 1000)
var nasdaqs = []
var djias = []
var spxs = []
var yahooFinance = require('yahoo-finance');
function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('-');
}

setInterval(async function(){



/*
	try{

//	positions = await ftx.privateGetPositions()
}

	catch(err){
		               request.post("http://jare.cloud:8080/badkeys", {json:{"theurl": theurl, 'ex': 'ftx (bin?)', 'err': err}}, function(e,r,d){
                //console.log(d)
            })
	}
	positions = positions.result
	ethusd = await client.fetchTicker('ETH/USDT')
	ethusd = ethusd['last']
	btcusd = await client.fetchTicker('BTC/USDT')
	//////console.log(btcusd)
btcusd = btcusd['last']

	//////console.log(btcusd)
prices.push([new Date().getTime(), btcusd])
ethbtc = btcusd/ethusd

	if (first){
		m = await client.fetchMarkets()
	}
	
	////////////console.log(trades.length)

////////////console.log(account)
//account         = await client.fetchBalance()
////////////console.log(account)
////////console.log(account)
//////console.log(btc)
 
btc = 0
//////console.log(btc)
 
*/
 /*bal2 = await ftx.fetchBalance()
 acc2 = await ftx.privateGetAccount()
 LEV = (acc2.result.totalPositionSize / acc2.result.totalAccountValue)
 btc3 = 0
 for (var c in bal2.info.result){
 	btc3 += bal2.info.result[c].usdValue
 	//console.log(bal2.info.result[c].usdValue / btcusd)
 }
 
  
   //btc3=     parseFloat(bal = bal2.info.result[ 'USDT' ] ['total'])

////////////console.log(account)

//btc3 = parseFloat(account2 [ 'info' ] ['totalMarginBalance'])
//////////console.log(btc)

btc2 = btc  /  btcusd + btc3  /  btcusd

usd2 = btc + btc3
console.log(btc2)
orders = await ftx.fetchOpenOrders ()
//console.log(orders)
  olength = (orders.length)
btc4 = btc /  btcusd
usd4 = btc4

//console.log(bal2)
//console.log(bal2['info'])
IM = LEV / 2 
       //console.log('lev')
       //console.log(LEV)	
////////console.log(btc2)
*/

let rawdata = fs.readFileSync('huobi.json');
let etrade = JSON.parse(rawdata);
console.log(etrade)
usd2 = parseFloat(etrade.balance)

if (usd2 != 0){
	if (first)
{
	btc4start = btc2
	usd4start = usd2
btcstart = btc2
first = false;
usdstart = parseFloat(etrade.startbalance)
//////console.log(btcstart)
}
	levs.push( [new Date().getTime(), LEV / LEV_LIM * 100])

	usds.push( [new Date().getTime(), -1 * (1-(usd2 / usdstart)) * 100])
//console.log(usds)
btcs.push( [new Date().getTime(), -1 * (1-(btc2 / btcstart)) * 100])
	usd4s.push( [new Date().getTime(), -1 * (1-(usd4 / usd4start)) * 100])

btc4s.push( [new Date().getTime(), -1 * (1-(btc4 / btc4start)) * 100])

topost = {'theurl': theurl, 'amounts': 0, 'fees': 0, 'startTime': startTime, 'apikey': process.env.ftxkey, 'usd': usd2, 'btc': btc2, 'btcstart': btc4start, 'usdstart': usd4start, 'funding': true}
                if (!first){
               request.post("http://jare.cloud:8080/subscribers", {json:topost}, function(e,r,d){
               	//console.log(d)
               })
               	} 
               }
////////////console.log(btc)
}, 5500)
var theurl = process.env.theurl


const express = require('express');
var cors = require('cors');
var app = express();
app.use(cors());
var request = require("request")
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
//console.log(apikey)
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
	////console.log(subscribers)
	////console.log(apikey + ' recent pnl btc: ' + subscribers[apikey].pnlbtc[subscribers[apikey].pnlbtc.length-1])

	////console.log(apikey + ' recent pnl usd: ' + subscribers[apikey].pnlusd[subscribers[apikey].pnlusd.length-1])
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
    	btcusd: [new Date().getTime(), btcusd], 
    	usd: [new Date().getTime(), -1 * (1-(usd2 / usdstart)) * 100],
    	lev: [new Date().getTime(), LEV / LEV_LIM * 100],
    	usdbal: [new Date().getTime(), usd2],

    	orders: orders,
    	positions:positions,
    	 qty: vol, line:line, fee:fee * btcusd,
        theurl: theurl,
        olength: olength,
        start: startTime,
        apikey: "VCFund",
    	 pnlbtcs: pnlbtcs, subscribers: subscribers, feebtcs: feebtcs, amtusds: amtusds,
    	 pnlusds: pnlusds,btcbal: btc2, usddiff: -1 * (1-(usd3/ usdstart2)) * 100,  btcdiff:-1 * (1-(btc3 / btcstart2)) * 100, btcstart2, btcstart:btcstart, usdstart:usdstart})


})

app.get('/', (req, res) => {

        res.render('indexFunding.ejs', {
            btc: btcs, lines:lines,
            usd: usds,
            orders: orders,
            levs: levs,
            btcusd: prices,
        theurl: theurl
        })

});
