with last3 as (
    select
        e.employee_id as eid,
        e.name as nm,
        p.rating as latest,
        lag(p.rating, 1) over (partition by p.employee_id order by p.review_date) as prev,
        lag(p.rating, 2) over (partition by p.employee_id order by p.review_date) as prev2,
        row_number() over (partition by p.employee_id order by p.review_date desc) as rn
    from
        employees e join performance_reviews p
    on
        e.employee_id = p.employee_id
    order by
        p.review_date desc
),
inc as (
    select * from last3
    where 
        latest > prev
        and prev > prev2
        and rn = 1
)
select
    eid as employee_id,
    nm as name,
    latest - prev2 as improvement_score
from inc
order by 
    latest - prev2 desc,
    nm;
