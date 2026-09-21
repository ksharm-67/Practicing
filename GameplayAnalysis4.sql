with cte as (
    select player_id, min(event_date) as first_login
    from Activity
    group by player_id
)
select round(count(distinct player_id)::decimal / (select count(distinct player_id) from Activity), 2) as fraction
from cte
where (player_id, first_login + 1) in (select player_id, event_date from Activity);
