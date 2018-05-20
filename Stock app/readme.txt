Author of the program: Gennadii Turutin

Assignment description by David Blaikie: 

Create a class Stock which produces objects that represent a stock security 
(like AAPL (Apple) or NFLX (Netflix)).  
A Stock object's attributes hold the data reflecting the stock's name, 
its latest price, latest trading volume, and "last updated" date 
(i.e., the time the data was last read from the realtime source).
The object can also return a list of historical prices based on the price data for the day.

The Stock object will be populated using data that is downloaded in real time from the web via the Alphavantage API 
(see exercises for details on signing up to the free AlphaVantage service).

Special note:  
because Alphavantage is a popular free site, 
the servers can become overburdened, 
take several seconds to return data, and will periodically reject your request.  
Repeating the request has worked for me in these cases.  
You may also wish to save the Alphavantage data in a file and use that file 
for testing rather than querying the Alphavantage API repeatedly.

	
Generate Image of Price History

Use matplotlib with the list of values returned from 
the .get_history() method to generate a line chart showing the hourly price history for the day.  

