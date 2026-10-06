with cte as (
    select 
        b.book_id as book_id,
        b.title as title,
        b.author as author,
        b.genre as genre,
        b.pages as pages,
        count(r.session_id) as reads, 
        max(session_rating) as highest,
        min(session_rating) as lowest,
        count(case when r.session_rating >= 4 then 1 end) as exh,
        count(case when r.session_rating <= 2 then 1 end) as exl
    from books b join reading_sessions r
    on b.book_id = r.book_id
    group by b.book_id, b.title, b.title, b.title, b.genre, b.pages
    having count(r.session_id) >= 5
    and count(case when r.session_rating >= 4 then 1 end) >= 1
    and count(case when r.session_rating <= 2 then 1 end) >= 1
),  
cte2 as (
    select 
        book_id,
        title,
        author,
        genre,
        pages,
        highest - lowest as rating_spread,
        round((exl + exh) / reads, 2) as polarization_score
    from cte
)
select * from cte2
where polarization_score >= 0.6
order by polarization_score desc, title desc
;
