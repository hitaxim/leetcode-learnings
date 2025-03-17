WITH CTE AS (
SELECT issue_month, issue_year, card_name, issued_amount, 
RANK() OVER (PARTITION BY card_name ORDER BY issue_year, issue_month) AS ranks
FROM monthly_cards_issued
)

SELECT card_name, issued_amount
FROM CTE 
WHERE ranks = 1
ORDER BY issued_amount DESC;
