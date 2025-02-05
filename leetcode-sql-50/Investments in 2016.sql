# Write your MySQL query statement below
/* Write your T-SQL query statement below */
with cte AS(
    select pid,
        tiv_2015,
        tiv_2016 ,
        count(pid)OVER(partition by tiv_2015 )AS tv_cnt,
        count(pid)OVER(partition by lat,lon)AS l_cnt 
from insurance
)
select round(sum(tiv_2016),2)AS tiv_2016  from cte where tv_cnt >1 and l_cnt <2
