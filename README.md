# JPMC Task 1
Starter repo for task 1 of the JPMC software engineering program


import urllib.request
 import time
 import json
@@ -35,14 +15,13 @@ def getDataPoint(quote):
 	stock = quote['stock']
 	bid_price = float(quote['top_bid']['price'])
 	ask_price = float(quote['top_ask']['price'])
-	price = bid_price
+	price = (bid_price/ask_price)/2
 	return stock, bid_price, ask_price, price
 
 def getRatio(price_a, price_b):
-	""" Get ratio of price_a and price_b """
-	""" ------------- Update this function ------------- """
-	""" Also create some unit tests for this function in client_test.py """
-	return 1
+if(price_b==0):
+  return
+return price_a/price_b  
 
 # Main
 if __name__ == "__main__":
@@ -56,4 +35,4 @@ if __name__ == "__main__":
 			stock, bid_price, ask_price, price = getDataPoint(quote)
 			print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
 
-		print ("Ratio %s" % getRatio(price, price))
+		print ("Ratio %s" % getRatio(price['ABC'], price['DEF']))
\ No newline at end of file
-- 
2.17.1
