with cte as (
    select * from UserActivity
    where user_id in (
        select user_id from UserActivity
        where activity_type = 'paid'
    )
)
select user_id,
round(avg(case when activity_type = 'free_trial' then activity_duration else null end), 2) as trial_avg_duration,
round(avg(case when activity_type = 'paid' then activity_duration else null end), 2) as paid_avg_duration
from cte
group by user_id
having round(avg(case when activity_type = 'free_trial' then activity_duration else null end), 2) is not null
order by user_id;
