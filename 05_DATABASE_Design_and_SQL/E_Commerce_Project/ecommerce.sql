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

select * 
from market_fact
--where prod_idnew = 1 and ord_idnew = 3954 and ship_idnew = 5495 and cust_idnew = 1369
order by prod_idnew

select Cust_id from cust_dimen

--
ALTER TABLE market_fact
ADD PRIMARY KEY (prod_idnew, ord_idnew, ship_idnew, cust_idnew)

