with cte as (
    select customer_id, min(delivery_id), 
    min(order_date) as od, min(customer_pref_delivery_date) as cd
    from Delivery
    group by customer_id
    order by customer_id
)
select round(
    sum(case when od = cd then 1 else 0 end)::decimal * 100 / count(*), 2)
    as immediate_percentage from cte;
