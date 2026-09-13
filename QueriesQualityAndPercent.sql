select query_name, 
round(sum(rating::decimal / position) / count(query_name), 2) as quality,
round(100 * sum(case when rating < 3 then 1 else 0 end)::decimal / count(query_name), 2) as poor_query_percentage
from Queries
group by query_name;
