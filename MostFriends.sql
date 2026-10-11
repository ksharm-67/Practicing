select id, sum(num) as num from (
    (select 
        requester_id as id,
        count(accepter_id) as num
    from RequestAccepted
    group by requester_id
    )
    union all
    (select
        accepter_id as id,
        count(requester_id) as num
    from RequestAccepted    
    group by accepter_id
    ) 
) x
group by id
order by sum(num) desc
limit 1;
