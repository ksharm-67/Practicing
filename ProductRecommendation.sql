with cte as (
    select p1.product_id as product1_id, 
    p2.product_id as product2_id, 
    p1i.category as product1_category, 
    p2i.category as product2_category,
    count((p1.user_id, p2.user_id)) as customer_count
    
    from ProductPurchases p1 
    join ProductPurchases p2 on p1.user_id = p2.user_id
    join ProductInfo p1i on p1.product_id = p1i.product_id
    join ProductInfo p2i on p2.product_id = p2i.product_id

    where p1.product_id < p2.product_id
    group by (p1.product_id, p2.product_id), p1i.category, p2i.category
)
select * from cte
where customer_count >= 3
order by customer_count desc, product1_id, product2_id;
