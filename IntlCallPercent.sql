with cte as (
  select case when sender != receiver then 1 else 0 end as intl
  from 
  (
    select calls.caller_id,
    info.country_id as sender,
    calls.receiver_id,
    recv.country_id as receiver
  
    from phone_info info join phone_calls calls
    on info.caller_id  = calls.caller_id 
    join phone_info recv 
    on calls.receiver_id = recv.caller_id
    order by calls.caller_id
  ) x 
)
select round(count(case when intl = 1 then 1 else null end) * 100.0 / count(*), 1)
from cte
;
