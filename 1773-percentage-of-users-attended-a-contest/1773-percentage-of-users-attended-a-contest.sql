# Write your MySQL query statement below

-- select *, count(contest_id) / count(])
-- from Register
-- group by contest_id

-- select r.contest_id, round(((count(r.contest_id) / count(u.user_id)) * 100), 2)
-- select round(count(r.contest_id) / count(distinct user_id) * 100), 2
-- from Register r
-- group by r.contest_id 
-- -- order by percentage desc, contest_id asc

select contest_id, round(((count(user_id) / (select count(*) from Users)) * 100), 2) as percentage
from register
group by contest_id
order by percentage desc, contest_id
