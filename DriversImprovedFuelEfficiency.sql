with cte as (
    select
        t.driver_id,
        d.driver_name as driver_name,
        avg(case when extract(month from t.trip_date) < 7
            then t.distance_km / t.fuel_consumed end) as first_half_raw,
        avg(case when extract(month from t.trip_date) >= 7
            then t.distance_km / t.fuel_consumed end) as second_half_raw
    from drivers d
    join trips t
        on d.driver_id = t.driver_id
    group by
        t.driver_id, d.driver_name
)
select
    driver_id,
    driver_name,
    round(first_half_raw, 2) as first_half_avg,
    round(second_half_raw, 2) as second_half_avg,
    round(second_half_raw - first_half_raw, 2) as efficiency_improvement
from cte
where
    first_half_raw is not null
    and second_half_raw is not null
    and second_half_raw > first_half_raw
order by
    efficiency_improvement desc,
    driver_name;
