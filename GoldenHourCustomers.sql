with golden as (
    select
        customer_id,
        count(order_id) as total_orders,
        100 * count(
            case when 
                (order_timestamp::time >= '11:00:00' and order_timestamp::time <= '14:00:00')
                or (order_timestamp::time >= '18:00:00' and order_timestamp::time <= '21:00:00')
            then 1 end                    
        )::decimal / count(order_id) as peak_orders,
        avg(order_rating) as ar,
        100 * count(
            case when order_rating is not null
            then 1 end
        )::decimal / count(order_id) as rated_orders
    from
        restaurant_orders
    group by
        customer_id
    order by
        customer_id
)  
select 
    customer_id,
    total_orders,
    round(peak_orders) as peak_hour_percentage,
    round(ar, 2) as average_rating
from 
    golden
where
    total_orders >= 3
    and peak_orders >= 60
    and rated_orders >= 50
    and round(ar, 2) >= 4.0
order by
    ar desc,
    customer_id desc;
