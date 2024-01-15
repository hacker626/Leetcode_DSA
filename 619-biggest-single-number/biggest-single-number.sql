# Write your MySQL query statement below
SELECT if(count(num) = 1,num,null) num
FROM MyNumbers 
group by
num 
order by 
num desc limit 1

# "WHERE num = (SELECT num
#              FROM MyNumbers
#              GROUP BY num
             
#              order by num desc limit 1)";


# select product_id,min(year) first_year,quantity,price from Sales group by product_id;
# where (product_id,year) in (select product_id,min(year) as year from Sales group by product_id);`