with cte as (
    select t.request_at, 
    count(t.id) as requests,
    t.status
    from trips t join users u1
    on t.client_id = u1.users_id
    join users u2 
    on t.driver_id = u2.users_id
    where u2.banned = 'No'
    and u1.banned = 'No'
    and t.request_at::date between '2013-10-01'::date
    and '2013-10-03'::date
    group by t.request_at, t.status
)
select request_at as "Day", 
round(sum(case when status = 'cancelled_by_client' or status = 'cancelled_by_driver'
then requests else 0 end) / sum(requests), 2) as "Cancellation Rate"
from cte
group by request_at
;
