with cte as (
    select u.user_id, u.name as nm, count(m.movie_id)
    from Users u join MovieRating m
    on u.user_id = m.user_id
    group by u.user_id, u.name
    order by count(*) desc, u.name
    limit 1
),
cte2 as (
    select mov.title as mo, avg(m.rating) 
    from Movies mov join MovieRating m
    on mov.movie_id = m.movie_id
    where m.created_at >= '2020-02-01' and m.created_at < '2020-03-01'
    group by mov.title
    order by avg(m.rating) desc, mov.title
    limit 1
)
select nm as results from cte
union all
select mo as results from cte2;
