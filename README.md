# Algorithmic-Trading-Bot
Uses AWS Chalice, Python, Pine Script, TradingView Charts, and the Alpaca API in conjunction to make a stock trading bot which runs in a virtual environment. 
First, we create a virtual environment then activate it. Next we install AWS chalice into the virtual environment, then create a new calice project. We edit the 
code in 'app.py' to make it a POST request, so that everytime something is posted to the API link, the code is executed. We then use TradingView charts to create alerts
based on our custom pine script, and within the alerts we paste the API link into the webhook url section. Now, when the alerts hit, the trades will be executed, which 
signifies the copletion of the trading bot.
