with cte as (
  select measurement_id, measurement_value, measurement_time,
  row_number() over 
    (partition by measurement_time::date order by measurement_time asc) as rn 
  from measurements
)
select date(measurement_time) as measurement_day,
sum(case when cte.rn % 2 <> 0 then measurement_value else 0 end) as odd_sum, 
sum(case when cte.rn % 2 = 0 then measurement_value else 0 end) as even_sum
from cte 
group by date(measurement_time)
order by date(measurement_time) asc 
;
