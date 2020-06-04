# exploring_crypto
Taking a look into a slice of time in the crypto world 

Here is a look into historical crypto data from 08-30-2019. This is the most current data I could retrieve for free. The date this data was retrieved has no significant meaning. While I am not particularly interested in cryptocurrencies, I felt this project was good practice for quering data and working with an online API. 

The data was retrieved from CoinMarketCap's API. CoinMarketCap is a highly referenced crypto-asset tracking website commonly cited by CNBC, Bloomberg, and crypto enthausists across the world. The CoinMarketCap API does require an API key, which can be obtained by signing up for a free account from their website here: https://coinmarketcap.com/api/. Please refer to importing_crypto.py file for step by step insturction on obtaining the requested data.

# lets get into the data:
The first table below shows the prices of the top 10 most expensive coins. Funny enough Bitcoin's price at 9,558.551637 is right around where it stands today (06-2-2020) at a current price of 9,522.45. 

Graphing the change in price over time could be a good update to make in a future version.

1. Bitcoin: 9558.551637
2. Maker: 471.141888
3. Bitcoin Cash: 281.029003
4. Ethereum: 168.688634
5. Bitcoin SV: 128.391324
6. Dash: 81.019993 
7. Monero: 67.641131 
8. Litecoin: 64.349090 
9. Zcash: 44.863475 
10. Decred: 22.798488 

Bitcoin's price is much much higher than all the other 100 crypto coins I researched. Does their market cap represent a similar finding?

Looking into Figure_1 you can see this is definitely the case. 

On 08-30-2019 Bitcoin's market cap was 76.5% of all 100 crypto coins researched. In comparison, the second largest coin Ethereum, totalled a whopping 7.6%. In other words, Bitcoin is by far the largest coin and controls a massive amount of the crypto market cap.

What other characteristics are crypto coins known for? Volatility. This was also convenient to graph from the extracted data. Figure_2 shows the top 10 coins with the largest price % changes in the last 24 hours.

The graph on the left reveals some shocking statistics. Wanchain, shot up over 21% in the prior 24 hours. Aurora also did pretty well that day raising almost 17% over the same time frame. On the flip side, the biggest loser was ICON that lost -3.88%. BitShares took second biggest loser, erasing -3.81% of its value in 24 hours. Is betting on random coins a viable investment tactic? It may seem to be if the largest single day difference between the biggest winner Wanchain and the biggest loser ICON is ~17%...

Similar to crypto coins, stocks can move up or down 10% on any given day. Lets see what the prices of these coins have done over a week period. Figure_3 shows the biggest winners and losers over a week timeframe. Here we see a different story. The biggest loser was Grin, losing -25.56 of its value, while the biggest winner was Synthetix Network Token adding +28.62%.

Looking at the graph of the biggest losers on the left, we see the top 9 biggest losers all lost 20% or more of their value over this particular weeks period, where only one coin gained 20% of its value. Also note in the top 10 winner over the week time frame features Wanchain, our biggest one day winner, which we stated earlier gained 21%. However, for the week time frame, Wanchain only gained a much more moderate +3.69%. This paints a little clearer of a picture on our new investment strategy. Wanchain for the win1.

1 WARNING: The cryptocurrency market is exceptionally volatile and any money you put in might disappear into thin air. Cryptocurrencies mentioned here might be scams similar to Ponzi Schemes or have many other issues (overvaluation, technical, etc.). Please do not mistake this for investment advice.
