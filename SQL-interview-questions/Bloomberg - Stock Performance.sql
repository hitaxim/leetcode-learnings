
WITH RankedStockPrices AS ( 
SELECT date, ticker, close, 
LAG(close) OVER (PARTITION BY ticker ORDER BY date) AS prev_month_close, 
LAG(close, 3) OVER (PARTITION BY ticker ORDER BY date) AS three_months_ago_close 
FROM stock_prices )

SELECT date, ticker, close, 
close - prev_month_close AS close_diff_consecutive_months, 
close - three_months_ago_close AS close_diff_three_months_prior 
FROM RankedStockPrices 
WHERE prev_month_close IS NOT NULL AND three_months_ago_close IS NOT NULL 
ORDER BY date;
