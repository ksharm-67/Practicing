with cte as (
    select product_id as pid, min(year) as yr
    from Sales
    group by product_id
)
select product_id, 
year as first_year,
quantity,
price
from Sales
where (product_id, year) in (select pid, yr from cte);
