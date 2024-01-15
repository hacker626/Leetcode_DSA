# Write your MySQL query statement below
select distinct(customer_id)  from Customer 
where (customer_id) in (select distinct customer_id from Customer group by customer_id having count(distinct product_key) = (select count(product_key) from Product))
# where (customer_id,product_key) in (distinct customer_id,)


