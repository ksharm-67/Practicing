select id,
case when p_id is null then 'Root' else (
    case when id in (select p_id from Tree) then 'Inner' else 'Leaf' end
) end as type
from Tree;
