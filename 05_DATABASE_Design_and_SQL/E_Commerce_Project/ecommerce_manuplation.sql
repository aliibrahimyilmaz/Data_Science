--"Success is the sum of small efforts, repeated day in and day out."

--DATA MANIPULATION
--generate Primary Keys
ALTER TABLE [dbo].[shipping_dimen]
DROP COLUMN Ship_id;

ALTER TABLE [dbo].[shipping_dimen]
ADD Ship_id INT NOT NULL IDENTITY(1,1);

ALTER TABLE [dbo].[shipping_dimen]
ADD PRIMARY KEY (Ship_id);
---------------------------------------
select * from market_fact
select Ord_id, substring(Ord_id, CHARINDEX('_', Ord_id ) + 1, len(Ord_id)) from market_fact
select Prod_id, substring(Prod_id, CHARINDEX('_', Prod_id ) + 1, len(Prod_id)) from market_fact

--taking intergers from the id values
--https://stackoverflow.com/questions/49785828/adding-a-new-column-with-data-in-sql-server
ALTER TABLE market_fact
ADD prod_idnew int null;

DECLARE @ID_info as TABLE
	(Prod_id varchar(50) not null,
	 new_id int not null
	)
INSERT INTO @ID_info(Prod_id, new_id)
select Prod_id, substring(Prod_id, CHARINDEX('_', Prod_id ) + 1, len(Prod_id)) from market_fact 

select * from @ID_info

Update m
set m.prod_idnew = i.new_id
from market_fact as m
		inner join @ID_info as i on m.Prod_id = i.Prod_id

----------
--the other 3 columns
ALTER TABLE market_fact
ADD ord_idnew int null,
	ship_idnew int null,
	cust_idnew int null

DECLARE @ID_infonew as TABLE
	(Ord_id varchar(50) not null,
	 neword_id int not null,
	 Ship_id varchar(50) not null,
	 newship_id int not null,
	 Cust_id varchar(50) not null,
	 newcust_id int not null
	)
INSERT INTO @ID_infonew(Ord_id, neword_id, Ship_id, newship_id, Cust_id, newcust_id)
select Ord_id, substring(Ord_id, CHARINDEX('_', Ord_id ) + 1, len(Ord_id)),
		Ship_id, substring(Ship_id, CHARINDEX('_', Ship_id ) + 1, len(Ship_id)),
		Cust_id, substring(Cust_id, CHARINDEX('_', Cust_id ) + 1, len(Cust_id))
from market_fact 

Update m
set m.ord_idnew = i.neword_id
from market_fact as m
		inner join @ID_infonew as i on m.Ord_id = i.Ord_id
update m
set m.ship_idnew = i.newship_id
from market_fact as m
		inner join @ID_infonew as i on m.Ship_id = i.Ship_id
update m
set m.cust_idnew = i.newcust_id
from market_fact as m
		inner join @ID_infonew as i on m.Cust_id = i.Cust_id

select Ord_id, ord_idnew, Prod_id, prod_idnew, Ship_id, ship_idnew, Cust_id, cust_idnew
from market_fact

select * from market_fact
--------------------------------------------------------------------------------------
--OR shortest way
/*
alter table orders_dimen
add  order_id int

update  orders_dimen
set order_id = substring(Ord_id, CHARINDEX('_', Ord_id ) + 1, len(Ord_id))

alter table market_fact
add primary key (cust_id, ord_id, prod_id, ship_id)
*/
---------------------------------------------------------------------------------------
--drop old varchar columns
ALTER TABLE market_fact
DROP COLUMN Ord_id, Prod_id, Ship_id,  

--join can work without primary keys but the tables should be relational with each other
select *
from market_fact mf
	inner join cust_dimen cd on cd.Cust_id = mf.cust_idnew

--Add Primary Key
--alter NULL to NOT NULL
ALTER TABLE market_fact
ALTER COLUMN prod_idnew INT NOT NULL
ALTER TABLE market_fact
ALTER COLUMN ord_idnew INT NOT NULL
ALTER TABLE market_fact
ALTER COLUMN ship_idnew INT NOT NULL
ALTER TABLE market_fact
ALTER COLUMN cust_idnew INT NOT NULL
ALTER TABLE market_fact
ALTER COLUMN Order_Quantity INT NOT NULL
select * 
from market_fact
where prod_idnew = 1 and ord_idnew = 3954 and ship_idnew = 5495 and cust_idnew = 1369
order by prod_idnew

select * 
from market_fact
where prod_idnew = 1 and ord_idnew = 3954 and ship_idnew = 5495 and cust_idnew = 1369 and Order_Quantity = 49

delete from market_fact
where prod_idnew = 1 and ord_idnew = 3954 and ship_idnew = 5495 and cust_idnew = 1369 and Order_Quantity = 49

select * 
from market_fact
where prod_idnew = 2 and ord_idnew = 933 and ship_idnew = 1290 and cust_idnew = 319 and Order_Quantity = 42

delete from market_fact
where prod_idnew = 2 and ord_idnew = 933 and ship_idnew = 1290 and cust_idnew = 319 and Order_Quantity = 42

select * 
from market_fact
where prod_idnew = 3 and ord_idnew = 685 and ship_idnew = 938 and cust_idnew = 231 and Order_Quantity = 11

delete from market_fact
where prod_idnew = 3 and ord_idnew = 685 and ship_idnew = 938 and cust_idnew = 231 and Order_Quantity = 11

select * 
from market_fact
where prod_idnew = 3 and ord_idnew = 1062 and ship_idnew = 1468 and cust_idnew = 397 --and Order_Quantity = 11

delete from market_fact
where prod_idnew = 3 and ord_idnew = 1062 and ship_idnew = 1468 and cust_idnew = 397 and Order_Quantity = 27

select * 
from market_fact
--group by prod_idnew
order by prod_idnew, ord_idnew, ship_idnew, cust_idnew
--
ALTER TABLE market_fact
ADD PRIMARY KEY (Order_Quantity, prod_idnew, ord_idnew, ship_idnew, cust_idnew)

ALTER TABLE market_fact
ADD CONSTRAINT fk_prod FOREIGN KEY (prod_idnew) REFERENCES prod_dimen(Prod_id)
ALTER TABLE market_fact
ADD CONSTRAINT fk_ord FOREIGN KEY (ord_idnew) REFERENCES orders_dimen(Ord_id),
	CONSTRAINT fk_cust FOREIGN KEY (cust_idnew) REFERENCES cust_dimen(Cust_id),
	CONSTRAINT fk_ship FOREIGN KEY (ship_idnew) REFERENCES shipping_dimen(Ship_id)

--Standart of the Date Columns
select * from orders_dimen

select CONVERT(date, Order_Date, 103) from orders_dimen

UPDATE orders_dimen
SET Order_Date = CONVERT(date, Order_Date, 103)

alter table orders_dimen
alter column Order_Date Date NOT NULL
----

select * from shipping_dimen

UPDATE shipping_dimen
SET Ship_Date = CONVERT(date, Ship_Date, 103)

alter table shipping_dimen
alter column Ship_Date Date NOT NULL

-----DATA MANIPULATION FINISHED, LET'S START ANALYSIS WITH THE OTHER QUERY

