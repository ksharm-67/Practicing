with cte as (
    select s.id,
    case
        when s.id % 2 = 0 then p.student
        when n.student is null then s.student
        else n.student
    end as student
    from Seat s
    left join Seat p on s.id = p.id + 1
    left join Seat n on s.id = n.id - 1
)

select id, student
from cte
order by id;
