with dilute as (
  select category, product, sum(spend) as total_spend
  from product_spend
  where transaction_date > '2022-01-01'
  and transaction_date < '2023-01-01'
  group by category, product
)
select category, product, total_spend from (
  select category, product, total_spend, 
  row_number() over 
    (partition by category
    order by total_spend desc) as rn
  from dilute
  group by category, product, total_spend
) t 
where rn < 3
;
