with cte as (
  select user_id, count(product_id) as purchase_count, transaction_date
  from user_transactions
  group by user_id, transaction_date
  order by user_id asc, transaction_date desc
)
select transaction_date, user_id, purchase_count 
from cte
where transaction_date in (
  select latest_date from (
    select user_id, max(transaction_date) as latest_date
    from user_transactions
    group by user_id
  ) x
)
group by transaction_date, user_id, purchase_count
order by transaction_date asc 
;

