select distinct num as "ConsecutiveNums" from (
    select *, 
    lag(num, 1) over (order by id) as a,
    lag(num, 2) over (order by id) as b
    from Logs
)
where num = a and a = b;
