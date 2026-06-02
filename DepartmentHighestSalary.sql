with cte as (
    select d.name as "Department", e.name as "Employee", e.salary as "Salary"
    from employee e join department d
    on e.departmentId = d.id
)
select * from cte
where ("Department", "Salary") in (
    select "Department", max("Salary") from cte
    group by "Department"
)
;
