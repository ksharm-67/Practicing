with cte as (
    select *,
    lead(people, 1) over (order by id) as next_id,
    lead(people, 2) over (order by id) as next_next_id
    from Stadium
)
select id, visit_date, people from cte
where id in (
    with ids as (
        select id from cte where 
        people >= 100 and next_id >= 100 and next_next_id >= 100 
    )
    select id from ids
    union select id + 1 from ids
    union select id + 2 from ids
)
order by id;
