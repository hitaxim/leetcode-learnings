SELECT 
  transactions.store_id, 
  SUM(payouts.payout_amount) AS total_payout
FROM trade_in_transactions AS transactions
INNER JOIN trade_in_payouts AS payouts
  ON transactions.model_id = payouts.model_id
GROUP BY transactions.store_id
ORDER BY total_payout DESC;
