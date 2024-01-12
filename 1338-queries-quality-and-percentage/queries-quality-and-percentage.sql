# Write your MySQL query statement below
select distinct 
query_name,
round(avg(rating/position),2) as quality ,
round(avg(rating<3)*100,2) as poor_query_percentage from Queries
where query_name is not null
group by query_name ;


# case when action = "confirmed" then 1.00 else 0.00 end
