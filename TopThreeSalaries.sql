with cte as (
  select d.department_name as dept_name, e.name as emp_name, e.salary as salary
  from department d join employee e 
  on d.department_id = e.department_id 
  group by d.department_name, e.name, e.salary
)
select dept_name, emp_name, salary from (
  select dept_name, emp_name, salary,
  dense_rank() over (partition by dept_name order by salary desc) as r
  from cte 
  order by dept_name asc, salary desc, emp_name asc
) x 
where r <= 3
;
