select 
    extract(year from trans_date)::text || '-' || (
        case when extract(month from trans_date) > 9 
            then extract(month from trans_date)::text 
            else '0' || extract(month from trans_date)::text 
        end
    ) as month,
    country,
    count(id) as trans_count,
    count(case when state = 'approved' then 1 else null end) as approved_count,
    sum(amount) as trans_total_amount,
    sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions
group by 
    extract(year from trans_date),
    extract(month from trans_date),
    country;
