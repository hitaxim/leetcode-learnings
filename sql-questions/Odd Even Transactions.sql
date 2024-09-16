select transaction_date, 
  sum(if(amount%2=0,0,amount)) as odd_sum, 
  sum(if(amount%2=0,amount,0)) as even_sum 
  from transactions 
group by transaction_date 
order by transaction_date
