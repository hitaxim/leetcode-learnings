SELECT ticker, COUNT(ticker) 
FROM stock_prices
WHERE (close-open)/open > 0.10 OR (close-open)/open < -0.10
GROUP BY ticker 
ORDER BY count DESC;
