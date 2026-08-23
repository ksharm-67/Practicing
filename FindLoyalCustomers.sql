with cte as (
    select customer_id, 
    count(case when transaction_type = 'purchase' then transaction_date end) as purchases,
    count(case when transaction_type = 'refund' then transaction_date end) as refunds,
    count(transaction_date) as total_transactions,
    max(transaction_date) - min(transaction_date) as days_active
    from customer_transactions
    group by customer_id
)
select customer_id from cte
where days_active >= 30
and purchases >= 3
and (refunds::decimal / total_transactions) < 0.2
order by customer_id;
