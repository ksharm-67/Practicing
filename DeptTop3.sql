with cte as (
    select e.id, e.name as Employee, e.salary as Salary, d.name as Department,
    dense_rank() over (partition by d.name order by e.salary desc)
    from Employee e join Department d 
    on e.departmentId = d.id
    order by d.name
)
select Employee, Salary, Department
from cte
where dense_rank <= 3;
