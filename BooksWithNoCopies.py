with cte as (
    select l.book_id as id, l.title as title, l.author as auth, l.genre as gen, l.total_copies as total, l.publication_year as yr, 
    count(b.book_id) as current_borrowers 
    from library_books l join borrowing_records b 
    on l.book_id = b.book_id
    where return_date is null 
    group by l.book_id, l.title, l.author, l.genre, l.total_copies, l.publication_year
)
select id as book_id, title, auth as author, gen as genre, yr as publication_year, current_borrowers from cte
where current_borrowers = total
order by current_borrowers desc, title asc;
