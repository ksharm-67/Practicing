with all_transacs as (
  select *, 
         lag(transaction_date, 1) over (order by transaction_date) as yesterday,
         lag(transaction_date, 2) over (order by transaction_date) as day_before
  from (
    with filtered_transac as (
      select *
      from transactions 
      where user_id in (
        with cte as (
          select user_id, count(transaction_date) as num_transac
          from transactions
          group by user_id
          order by user_id
        )
        select user_id
        from cte 
        where num_transac >= 3
      ) 
      order by user_id, transaction_date desc
    )
    select *
    from filtered_transac
    order by user_id asc
  ) t
)
select distinct user_id
from all_transacs
where day_before::date - yesterday::date <= 1 
and yesterday::date - transaction_date::date <= 1
order by user_id asc;
