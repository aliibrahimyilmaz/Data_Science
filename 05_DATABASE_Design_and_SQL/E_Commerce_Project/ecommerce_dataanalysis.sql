--DATA ANALYSIS
/*1. Join all the tables and create a new table with all of the columns, called
combined_table. (market_fact, cust_dimen, orders_dimen, prod_dimen,
shipping_dimen)*/

select *
into combined_table  -- adding table, shortest way
from
(
	select *
	from market_fact as mf
		inner join cust_dimen as cd on mf.cust_idnew = cd.Cust_id
		inner join orders_dimen as od on mf.ord_idnew = od.Ord_id
		inner join prod_dimen as pd on mf.prod_idnew = pd.Prod_id
		inner join shipping_dimen as sd on mf.ship_idnew = sd.Ship_id
) as a

select * from combined_table

--2. Find the top 3 customers who have the maximum count of orders.

select TOP 3 Cust_id, Customer_Name, count(distinct Ord_id) as number_of_orders
from combined_table
group by Customer_Name, Cust_id
order by 3 desc


/*3. Create a new column at combined_table as DaysTakenForDelivery that
contains the date difference of Order_Date and Ship_Date.*/

alter table combined_table
add DaysTakenForDelivery int  --created new column into a table

update combined_table
set DaysTakenForDelivery = datediff(day, Order_Date, Ship_Date) --filled the empty table with values

select Cust_id, Order_Date, Ship_Date, DaysTakenForDelivery
from combined_table
order by 4 desc


-- 4. Find the customer whose order took the maximum time to get delivered.

select TOP 1 Cust_id, Customer_Name, Order_Date, Ship_Date, DaysTakenForDelivery
from combined_table
order by 5 desc
--OR

select cust_id, Customer_Name, Order_Date, Ship_Date, DaysTakenForDelivery
from combined_table
where DaysTakenForDelivery = 
	(
	select max(DaysTakenForDelivery)
	from combined_table
	)

select Cust_id, Customer_Name, Order_Date, Ship_Date, DaysTakenForDelivery
from combined_table
where Cust_id = 157


--5. Retrieve total sales made by each product from the data (use Window function)

ALTER TABLE combined_table
ALTER COLUMN Sales float

select Prod_id, sum(Sales)
from combined_table
group by Prod_id
order by 2 desc
--OR
select distinct Prod_id, sum(Sales) over (partition by prod_id)
from combined_table
order by 2 desc


--6. Retrieve total profit made from each product from the data (use windows function)

ALTER TABLE combined_table
ALTER COLUMN Profit float

select Prod_id, sum(Profit) as total_profit
from combined_table
group by Prod_id
order by 2 desc
--OR
select distinct Prod_id, sum(Profit) over (partition by prod_id)
from combined_table
order by 2 desc


/* 7.Count the total number of unique customers in January and how many of them
came back every month over the entire year in 2011 */

select distinct Cust_id, Order_Date
from combined_table
where year(Order_Date) = 2011 and month(Order_Date) = 01
order by 1 asc

/* select year(Order_Date) as 'year', month(Order_Date) as 'month',
	count(distinct Cust_id) over (partition by month(Order_date) order by month(Order_date) desc) as total_cust
from combined_table
where year(Order_Date) = 2011 and Cust_id in (
	select distinct Cust_id
	from combined_table
	where year(Order_Date) = 2011 and month(Order_Date) = 01
	) */ 
-- distinct with over partition can not be used, therefore group by must be used:

select 
	year(Order_Date) as 'year',
	month(Order_Date) as 'month',
	count(distinct Cust_id) as total_cust
from combined_table
where 
	year(Order_Date) = 2011 
	and
	Cust_id in (
				select distinct Cust_id
				from combined_table
				where year(Order_Date) = 2011 and month(Order_Date) = 01
				)
group by 
	year(Order_Date),
	month(Order_Date)
order by
	month(order_date)


--CUSTOMER RETENTION ANALYSIS:
/*Find month-by-month customer retention rate since the start of the business
(using views).*/

/* 1. Create a view where each user’s visits are logged by month, allowing for the
possibility that these will have occurred over multiple years since whenever
business started operations.*/

select year(Order_Date) as year, month(Order_Date) as month, count(distinct Cust_id) as num_of_cust
from combined_table
group by year(Order_Date), month(Order_Date)
order by 1, 2

select cust_id, count_in_month, convert(date, Month + '-1') as month_date  --converted into date mit day
from
	(
	select cust_id, SUBSTRING(cast(Order_Date as varchar), 1,7) as Month, count (*) as count_in_month
	from combined_table
	group by
		cust_id, SUBSTRING(cast(Order_Date as varchar), 1,7)
	) a


/* 2. Identify the time lapse between each visit. So, for each person and for each
month, we see when the next visit is.*/



-- 3. Calculate the time gaps between visits.



--4. Categorise the customer with time gap 1 as retained, >1 as irregular and NULL as churned.



--5. Calculate the retention month wise.
