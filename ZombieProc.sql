with cte as (
    select e1.session_id, e1.user_id, 
    extract(epoch from (max(e1.event_timestamp) - min(e1.event_timestamp))) / 60 as session_duration_minutes,
    count(case when e1.event_type = 'click' then 1 end) as clicks,
    count(case when e1.event_type = 'scroll' then 1 end) as scrolls,
    sum(case when e1.event_type = 'purchase' then e1.event_value end) as purch
    from app_events e1 
    group by e1.session_id, e1.user_id
)
select cte.session_id, cte.user_id, session_duration_minutes, scrolls as scroll_count
from cte
where session_duration_minutes > 30
and scrolls >= 5
and clicks::float / scrolls < 0.2
and coalesce(purch, 0) = 0
order by scrolls desc, cte.session_id;
