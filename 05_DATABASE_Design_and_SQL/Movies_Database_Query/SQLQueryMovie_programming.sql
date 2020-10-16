--1.CREATING and execute a STORED PROCEDURE
use Movies
go --begins a new batch
---------------------------------------------------------------------
create proc spFilmList
as
begin
	select FilmName, FilmReleaseDate, FilmRunTimeMinutes
	from tblFilm
	order by FilmName asc
end
-----------------------------------------------------------------------
--modify Stored Procedure
alter proc spFilmList
as
begin
	select FilmName, FilmReleaseDate, FilmRunTimeMinutes
	from tblFilm
	order by FilmName desc --modified asc
end

--execute spFilmList --we can make this in other queries
--drop proc spFilmList  -- deletes
-----------------------------------------------------------------------
--2.STORED PROCEDURE PARAMETERS

use Movies
go --begins a new batch
-----------------------------------------------------------------------
create proc spFilmCriteria(@MinLength as int)
as
begin
	select FilmName, FilmRunTimeMinutes
	from tblFilm
	where FilmRunTimeMinutes > @MinLength  --PARAMETER
	order by FilmRunTimeMinutes asc
end
-----------------------------------------------------------------------
exec spFilmCriteria 150, 180
-----------------------------------------------------------------------
ALTER proc [dbo].[spFilmCriteria]
	(
		@MinLength as int
		, @MaxLength as int
	)
as
begin
	select FilmName, FilmRunTimeMinutes
	from tblFilm
	where FilmRunTimeMinutes >= @MinLength and
		  FilmRunTimeMinutes < @MaxLength
	order by FilmRunTimeMinutes asc
end
----------------------------------------------------------
--named parameters
exec spFilmCriteria @MinLength=150, @MaxLength=180
----------------------------------------------------------
--text parameter
ALTER proc [dbo].[spFilmCriteria]
	(
		@MinLength as int
		, @MaxLength as int
		, @Title as varchar(max)
	)
as
begin
	select FilmName, FilmRunTimeMinutes
	from tblFilm
	where FilmRunTimeMinutes >= @MinLength and
		  FilmRunTimeMinutes < @MaxLength and
		  FilmName like '%' + @Title + '%' --wildcard character
	order by FilmRunTimeMinutes asc
end

exec spFilmCriteria @MinLength=120, @MaxLength=180, @Title='star'
-------------------------------------------------------------
--optional parameters
ALTER proc [dbo].[spFilmCriteria]
	(
		@MinLength as int = 0 --optional parameter
		, @MaxLength as int
		, @Title as varchar(max)
	)
as
begin
	select FilmName, FilmRunTimeMinutes
	from tblFilm
	where FilmRunTimeMinutes >= @MinLength and
		  FilmRunTimeMinutes < @MaxLength and
		  FilmName like '%' + @Title + '%' --wildcard character
	order by FilmRunTimeMinutes asc
end

exec spFilmCriteria @MinLength=120, @MaxLength=180, @Title='die'
exec spFilmCriteria @MaxLength=180, @Title='die'

ALTER proc [dbo].[spFilmCriteria]
	(
		@MinLength as int = NULL --optional parameter
		, @MaxLength as int = NULL
		, @Title as varchar(max)
	)
as
begin
	select FilmName, FilmRunTimeMinutes
	from tblFilm
	where (@MinLength is null or FilmRunTimeMinutes >= @MinLength) and
		  (@MaxLength is null or FilmRunTimeMinutes < @MaxLength) and
		  FilmName like '%' + @Title + '%' --wildcard character
	order by FilmRunTimeMinutes asc
end

exec spFilmCriteria @Title='star'
exec spFilmCriteria @Title='star', @MinLength=120
--these stored procedures can be used under REPORTS
--------------------------------------------------------------
--3. VARIABLES
use Movies
go

set nocount on -- row count message is disappeared in Messages 

declare @MyDate datetime
declare @NumFilms int

set @MyDate = '1970-01-01'
set @NumFilms = (select count(*) from tblFilm where FilmReleaseDate >= @MyDate)

select 'number of films', @NumFilms --shows in Results as a table
print 'number of films = ' + cast(@NumFilms as varchar(max)) --shows in Messages

select FilmName as name, FilmReleaseDate as date, 'Film' as type
from tblFilm
where FilmReleaseDate >= @MyDate

UNION ALL

select ActorName, ActorDOB, 'Actor'
from tblActor
where ActorDOB >= @MyDate

UNION ALL

select DirectorName, DirectorDOB, 'Director'
from tblDirector
where DirectorDOB >= '1970-01-01'
order by date asc
-------------------------------------------------------------
--reading a record into a set of variables
declare @Date datetime
declare @ID int
declare @Name varchar(max)

select top 1 -- all the values are assigned in the select statement
		@ID = ActorID
		, @Name = ActorName
		, @Date = ActorDOB
from tblActor
where ActorDOB >= '1970-01-01'
order by ActorDOB asc

select @Name, @Date

select f.FilmName, c.CastCharacterName
from tblFilm as f
	inner join tblCast as c on f.FilmID = c.CastFilmID
where c.CastActorID = @ID

--Accumulating Values in Variables
declare @NameList varchar(max)
set @NameList = '' -- initilize not null

select @NameList = @NameList + ActorName + ', '
from tblActor
where year(ActorDOB) = 1970

print @NameList
------
declare @NameList varchar(max)
set @NameList = '' -- initilize not null

select @NameList = @NameList + ActorName + char(10) + char(13)
from tblActor
where year(ActorDOB) = 1970

print @NameList
------
declare @NameList varchar(max)
set @NameList = '' -- initilize not null

select @NameList = @NameList + ActorName + char(10)
from tblActor
where year(ActorDOB) = 1970

print @NameList
-------
--GLOBAL VARIABLES
select @@SERVERNAME

select * from tblActor
select @@ROWCOUNT
--------------------------------------------------------------
--4. OUTPUT PARAMETERS AND RETURN VARIABLES
create proc spFilmsInYear
	(
		@Year int
	)
as
begin
	select
		FilmName
	from 
		tblFilm
	where
		year(FilmReleaseDate) = @Year
	order by
		FilmName asc
end
---------
exec spFilmsInYear @Year = 2000 
---------
alter proc spFilmsInYear
	(
		@Year int
		, @FilmList varchar(max) OUTPUT
		, @FilmCount int OUTPUT
	)
as
begin
	declare @Films varchar(max)
	set @Films = ''
	
	select
		@Films = @Films + FilmName + ', '
	from 
		tblFilm
	where
		year(FilmReleaseDate) = @Year
	order by
		FilmName asc

	SET @FilmCount = @@ROWCOUNT  -- OUTPUT PARAMETERS
	SET @FilmList = @Films --OUTPUT PARAMETERS

end
---------
declare @Names varchar(max)
declare @Count int

exec spFilmsInYear
	@Year = 2000
	, @FilmList = @Names OUTPUT
	, @FilmCount = @Count OUTPUT --output parameters compulsory

select @Count as number_of_Films, @Names as list_of_Films
---------
alter proc spFilmsInYear
	(
		@Year int
	)
as
begin
	
	select
		FilmName
	from 
		tblFilm
	where
		year(FilmReleaseDate) = @Year
	order by
		FilmName asc

	RETURN @@ROWCOUNT
end
----------
declare @Count int
exec @Count = spFilmsInYear @Year = 2000
select @Count as Number_of_Films
------------------------------------------------------------------------------
--5. IF STATEMENTS
declare @NumFilms int

set @NumFilms = (select count(*) from tblFilm where FilmDirectorID = 4)

if @NumFilms > 60
	print 'There are too many films in the database'
else
	print 'There are no more films in the database'
----------
declare @NumFilms int
declare @NumStudio int

set @NumFilms = (select count(*) from tblFilm where FilmDirectorID = 4)
set @NumStudio = (select count(*) from tblFilm where FilmStudioID = 5)

if @NumFilms > 5
	begin
		print 'There are too many films in the database'
		PRINT 'WARNING!'
		if @NumStudio > 10
			begin
				print 'Phew! There are many Studios'
			end
		else
			begin
				print 'There are not enough Studios'
			end
	end
else
	begin
		print 'There are no more films in the database'
		PRINT 'INFORMATION'
	end
-----------
create proc spVariableData
	(
		@InfoType varchar(9)  --This can be ALL, AWARD or FINANCIAL
	)
as
begin
	if @InfoType = 'ALL'
		begin
			(select * from tblFilm)
			return
		end
end

exec spVariableData @InfoType = 'ALL'
-----------
alter proc spVariableData
	(
		@InfoType varchar(9)  --This can be ALL, AWARD or FINANCIAL
	)
as
begin
	if @InfoType = 'ALL'
		begin
			(select * from tblFilm)
			return
		end
	if @InfoType = 'AWARD'
		begin
			(select FilmName, FilmOscarWins, FilmOscarNominations from tblFilm)
			return
		end
	if @InfoType = 'FINANCIAL'
		begin
			(select FilmName, FilmBoxOfficeDollars, FilmBudgetDollars from tblFilm)
			return
		end
	SELECT 'You must choose ALL, AWARD or FINANCIAL'
end

exec spVariableData @InfoType = 'xxxx' --This can be ALL, AWARD or FINANCIAL
------------------------------------------------------------------------------
--6. WHILE LOOP
declare @Counter INT
declare @MaxOscars int
declare @NumFilms int

set @Counter = 0
set @MaxOscars = (select max(FilmOscarWins) from tblFilm)

while @Counter <= @MaxOscars
	begin
		set @NumFilms = (select count(*) from tblFilm where FilmOscarWins = @Counter)
		
		print CAST(@NumFilms as varchar(3)) + ' films have won ' +  
				CAST(@Counter as varchar(2)) + ' Oscars'
		
		set @Counter = @Counter + 1
	end
--------
--BREAK
declare @Counter INT
declare @MaxOscars int
declare @NumFilms int

set @Counter = 0
set @MaxOscars = (select max(FilmOscarWins) from tblFilm)

while @Counter <= @MaxOscars
	begin
		set @NumFilms = (select count(*) from tblFilm where FilmOscarWins = @Counter)

		--if @NumFilms = 0 BREAK
		
		print CAST(@NumFilms as varchar(3)) + ' films have won ' +  
				CAST(@Counter as varchar(2)) + ' Oscars'
		
		set @Counter = @Counter + 1
	end
-----------
--CURSOR
declare @FilmID int
declare @FilmName varchar(max)

declare FilmCursor cursor for
	select FilmID, FilmName from tblFilm

open FilmCursor

fetch next from FilmCursor into @FilmID, @FilmName

while @@FETCH_STATUS = 0 --this means that it selects a new record and cursor move to the next record
	begin
		print 'Characters in the film ' + @FilmName
		select CastCharacterName from tblCast where CastFilmID = @FilmID

		fetch next from FilmCursor into @FilmID, @FilmName
	end

close FilmCursor
deallocate FilmCursor

--7. USER DEFINED FUNCTIONS
select FilmName
	, FilmReleaseDate
	, DATENAME(DW, FilmReleaseDate) + ' ' +
	DATENAME(D, FilmReleaseDate) +  ' ' +
	DATENAME(M, FilmReleaseDate) + ' ' +
	DATENAME(YY, FilmReleaseDate) 
from tblFilm

--template or scratch
--scalar-valued Function -- silly and awkward, we crearted from the scratch
use Movies
go

create function fnLongDate
	(
		@FullDate as datetime
	)
returns varchar(max)
as
begin
	return DATENAME(DW, @FullDate) + ' ' +
	DATENAME(D, @FullDate) +  ' ' +
	DATENAME(M, @FullDate) + ' ' +
	DATENAME(YY, @FullDate)  
end
--------
--use the function in the select
select FilmName
	, FilmReleaseDate
	, [dbo].[fnLongDate](FilmReleaseDate) --function we created
from tblFilm
---------
--modify the function ALTER or right click and choose modify
use Movies
go
alter function fnLongDate
	(
		@FullDate as datetime
	)
returns varchar(max)
as
begin
	return DATENAME(DW, @FullDate) + ' ' +
	DATENAME(D, @FullDate) +
	case
		when day(@FullDate) in (1,21,31) then 'st'
		when day(@FullDate) in (2,22) then 'nd'
		when day(@FullDate) in (3,23) then 'rd'
		else 'th'
	end + ' ' +
	DATENAME(M, @FullDate) + ' ' +
	DATENAME(YY, @FullDate)  
end

--execute
select FilmName
	, FilmReleaseDate
	, [dbo].[fnLongDate](FilmReleaseDate) --function we created
from tblFilm

select ActorName, ActorDOB, dbo.fnLongDate(ActorDOB)
from  tblActor

--complex expression
select DirectorName
	,left(DirectorName,CHARINDEX(' ', DirectorName)-1) -- looking for a space and show allthe characters on the left
from tblDirector

select ActorName
	,left(ActorName,CHARINDEX(' ', ActorName)-1) -- looking for a space and show allthe characters on the left
from tblActor

--create function
create function fnFirstName
	(
		@FullName as varchar(max)
	)
returns varchar(max)
as
begin
	declare @SpacePosition as int
	declare @Answer as varchar(max)

	set @SpacePosition = CHARINDEX(' ', @FullName)

	if @SpacePosition = 0
		set @Answer = @FullName
	else
		set @Answer = left(@FullName,@SpacePosition-1)

	return @Answer
end
--execute
select ActorName
	,[dbo].[fnFirstName](ActorName)-- looking for a space and show allthe characters on the left
from tblActor

-----------------------------------------------------------------
--8.TEMPORARY TABLES
select FilmName, FilmReleaseDate
into #TempFilms -- creates temporary table
from tblFilm
where FilmName like '%star%'

select * from #TempFilms  -- temperory table
---------------
--second way to create
create table #TempFilms2
(
	Title varchar(max)
	,ReleaseDate datetime
)
insert into #TempFilms2
select FilmName, FilmReleaseDate
from tblFilm
where FilmName like '%star%'

select * from #TempFilms2  -- temperory table
---------------
--global temptable
create table ##TempFilms2
(
	Title varchar(max)
	,ReleaseDate datetime
)
insert into ##TempFilms2
select FilmName, FilmReleaseDate
from tblFilm
where FilmName like '%star%'

select * from ##TempFilms2
--------
--explicitly drop temp table
drop table #TempFilms
--------------------------------------------------------------------------
--9.TABLE VARIABLES
use Movies

create table #TempPeople
(
	PersonName varchar(max)
	,PersonDate datetime
)
insert into #TempPeople
select ActorName, ActorDOB
from tblActor
where ActorDOB < '1950-01-01'

select * from #TempPeople
--------
--new technik table variable, very flexible in changes
use Movies

declare @TempPeople TABLE --table variable
( --the definition of our table is identical how we create temptable
	PersonName varchar(max)
	,PersonDOB datetime
)
insert into @TempPeople
select ActorName, ActorDOB
from tblActor
where ActorDOB < '1950-01-01'

select * from @TempPeople
------------------------------------------------------------------------

--10.TABLE VALUED FUNCTIONS
use Movies
--scalar-valued function
select FilmName, [dbo].[fnLongDate](FilmReleaseDate) 
from tblFilm

--table-valued function
select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where year(FilmReleaseDate) = 2000

--defining a function
use Movies
go

create function FilmsInYear
	(
		@FilmYear INT
	)
RETURNS TABLE
as
RETURN
	select FilmName, FilmReleaseDate, FilmRunTimeMinutes
	from tblFilm
	where year(FilmReleaseDate) = @FilmYear
--------------
--execute
	select FilmName, FilmReleaseDate, FilmRunTimeMinutes
	from [dbo].[FilmsInYear](2000)  --inline table-valued function, dbo schema mus be here

--modifying 1st way, or right click modify
alter function FilmsInYear
	(
		@StartYear INT
		,@EndYear INT
	)
RETURNS TABLE
as
RETURN
	select FilmName, FilmReleaseDate, FilmRunTimeMinutes
	from tblFilm
	where year(FilmReleaseDate) between @StartYear and @EndYear
----------
	select FilmName, FilmReleaseDate, FilmRunTimeMinutes
	from [dbo].[FilmsInYear](2000, 2002)

--multistatement tabled_value function
use Movies
go

create function PeopleInYear
	(
		@BirthYear INT
	)
RETURNS @t TABLE
	(
		PersonName varchar(max)
		,PersonDOB datetime
		,PersonJob varchar(8)
	)
AS
BEGIN

	INSERT INTO @t
	SELECT DirectorName, DirectorDOB, 'Director'
	FROM tblDirector
	where year(DirectorDOB) = @BirthYear

	INSERT INTO @t
	SELECT ActorName, ActorDOB, 'actor'
	FROM tblActor
	where year(ActorDOB) = @BirthYear

	RETURN 
END

--execeute
use Movies

select *
from dbo.PeopleInYear(1945)

--modifying same as before
----------------------------------------------------------------------
--11. CTEs: COMMON TABLE EXPRESSIONS

select FilmCountryID, count(*)
from tblFilm
group by FilmCountryID
---------
With FilmCounts as
(
	select FilmCountryID, count(*) as NumberofFilms
	from tblFilm
	group by FilmCountryID
)
select
	avg(NumberofFilms)
from
	FilmCounts

---------------
With FilmCounts(Country, NumberofFilms) as
(
	select FilmCountryID, count(*)
	from tblFilm
	group by FilmCountryID
)
select
	avg(NumberofFilms)
from
	FilmCounts
--
With FilmCounts(Country, NumberOfFilms) as --you have to select the same number of columns
(
	select FilmCountryID, count(*)
	from tblFilm
	group by FilmCountryID
)
select
	Country, NumberOfFilms
from
	FilmCounts
--------------
--List of CTEs
with EarlyFilms AS
(
	select FilmName, FilmReleaseDate
	from tblFilm
	where FilmReleaseDate < '2000-01-01'
),
RecentFilms AS
(
	select FilmName, FilmReleaseDate
	from tblFilm
	where FilmReleaseDate >= '2000-01-01'
)
select *
from EarlyFilms as e
	inner join RecentFilms r on e.FilmName = r.FilmName

-------------------------------------------------------------------
--12.CURSORS

--declaring a cursor
DECLARE FilmCursor CURSOR
	FOR SELECT FilmID, FilmName, FilmReleaseDate FROM tblFilm
--------------
--opening and closing cursors
open FilmCursor
	--Do something useful
close FilmCursor
deallocate FilmCursor
--------------
--moving thorough the set of data, called FETCH
open FilmCursor
	--Do something useful
	FETCH NEXT FROM FilmCursor
close FilmCursor
deallocate FilmCursor
--------------
open FilmCursor
	--Do something useful
	FETCH NEXT FROM FilmCursor
	WHILE @@FETCH_STATUS = 0
		FETCH NEXT FROM FilmCursor
close FilmCursor
deallocate FilmCursor
--------------
DECLARE FilmCursor CURSOR SCROLL
	FOR SELECT FilmID, FilmName, FilmReleaseDate FROM tblFilm
open FilmCursor
	--Do something useful
	FETCH LAST FROM FilmCursor --NEXT or FIRST
	WHILE @@FETCH_STATUS = 0
		FETCH PRIOR FROM FilmCursor --NEXT or PRIOR
close FilmCursor
deallocate FilmCursor
--------------
DECLARE FilmCursor CURSOR SCROLL
	FOR SELECT FilmID, FilmName, FilmReleaseDate FROM tblFilm
open FilmCursor
	--Do something useful
	FETCH ABSOLUTE 10 FROM FilmCursor --NEXT or FIRST
	WHILE @@FETCH_STATUS = 0
		FETCH RELATIVE 10 FROM FilmCursor --NEXT or PRIOR or -10
close FilmCursor
deallocate FilmCursor
--------------
DECLARE @ID INT
DECLARE @Name VARCHAR(MAX)
DECLARE @Date DATETIME

DECLARE FilmCursor CURSOR SCROLL
	FOR SELECT FilmID, FilmName, FilmReleaseDate FROM tblFilm
open FilmCursor
	--Do something useful
	FETCH NEXT FROM FilmCursor INTO @ID, @Name, @Date 
	WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT @Name + ' released  on ' + CONVERT(CHAR(10), @Date,103) --date format converted into char
			PRINT '======================================================'
			PRINT 'List of Characters'

			select CastCharacterName
			from tblCast
			where CastFilmID = @ID

			FETCH NEXT FROM FilmCursor INTO @ID, @Name, @Date 
		END
close FilmCursor
deallocate FilmCursor
-------------

--Calling Strored Procedures in a Cursor
CREATE PROC spListCharacters
(
	@FilmID INT
	,@FilmName VARCHAR(MAX)
	,@FilmDate DATETIME
)
AS
BEGIN
		PRINT @FilmName + ' released  on ' + CONVERT(CHAR(10), @FilmDate,103) --date format converted into char
		PRINT '======================================================'
		PRINT 'List of Characters'

		select CastCharacterName
		from tblCast
		where CastFilmID = @FilmID
END
-----------
--using the stored procedure in our loop
DECLARE @ID INT
DECLARE @Name VARCHAR(MAX)
DECLARE @Date DATETIME

DECLARE FilmCursor CURSOR SCROLL
	FOR SELECT FilmID, FilmName, FilmReleaseDate FROM tblFilm
open FilmCursor
	--Do something useful
	FETCH NEXT FROM FilmCursor INTO @ID, @Name, @Date 
	WHILE @@FETCH_STATUS = 0
		BEGIN
			EXEC spListCharacters @ID, @Name, @Date
			FETCH NEXT FROM FilmCursor INTO @ID, @Name, @Date 
		END
close FilmCursor
deallocate FilmCursor

--------------
--scope of a cursor, LOCAL or GLOBAL
open FilmCursor LOCAL --or GLOBAL, default is GLOBAL and you can use it everywhere
	--Do something useful
close FilmCursor --LOCAL cursor can only be used in a unique batch
deallocate FilmCursor

--------------
--scroll settings of the cursor
--SCROLL : FETCH FIRST, LAST etc.
--FORWARD ONLY : only FETCH NEXT

--------------
--records options of the cursor
--FAST_FORWARD, STATIC, KEYSET, DYNAMIC

--------------
--Lock Options of the cursor
--READ_ONLY, SCROLL_LOCKS, OPTIMISTIC

--------------
--combining cursor options
--GLOBAL FORWARD_ONLY STATIC READ_ONLY , this is a combination setting of the cursor, it is also possible
--CURSOR LINK:
--https://docs.microsoft.com/en-us/sql/t-sql/language-elements/declare-cursor-transact-sql?redirectedfrom=MSDN&view=sql-server-ver15 

--------------
--Updates and running totals

declare @FilmOscars INT
declare @TotalOscars int

set @TotalOscars = 0

declare FilmCursor CURSOR
	FOR SELECT FilmOscarWins from tblFilm
	FOR UPDATE OF FilmCumulativeOscars

open FilmCursor

	FETCH NEXT FROM FilmCursor INTO @FilmOscars

	WHILE @@FETCH_STATUS = 0
	BEGIN

		SET @TotalOscars += @FilmOscars

		--PRINT @TotalOscars
		UPDATE tblFilm
		SET FilmCumulativeOscars = @TotalOscars
		WHERE CURRENT OF FilmCursor

		FETCH NEXT FROM FilmCursor INTO @FilmOscars

	END
close FilmCursor
deallocate FilmCursor

select * from tblFilm
-----------------------------------------------------------------------

--13.DYNAMIC SQL

--1st way EXEC:
execute ('select * from tblFilm')


--2nd way stored procedures:
EXEC sp_executesql N'select * from tblFilm'  --N creates a unicode String
------------------

--concatenating an SQL string
DECLARE @Tablename NVARCHAR(128)
DECLARE @SQLString NVARCHAR(MAX)

SET @Tablename = N'tblActor'

SET @SQLString = N'select * from ' + @Tablename

EXEC sp_executesql @SQLString
----------------

--numbers in the Strings and CONCAT

declare @Number INT
declare @NumberString NVARCHAR(4)
declare @SQLString2 NVARCHAR(MAX)

set @Number = 30
set @NumberString = CAST(@Number as nvarchar(4))

set @SQLString2 = N'SELECT TOP ' + @NumberString + ' * from tblFilm order by FilmReleaseDate'

EXEC sp_executesql @SQLString2
-----------------------
--creating a stored procedure
create proc spVariableTable
(
	@TableName NVARCHAR(128)
)
as
BEGIN

	declare @SQLString3 NVARCHAR(MAX)
	set @SQLString3 = N'SELECT * FROM ' + @TableName

	EXEC sp_executesql @SQLString3

END

EXEC spVariableTable 'tblActor'
----------------

--Adding multiple parameters
alter proc spVariableTable
(
	@TableName NVARCHAR(128)
	, @Number INT
)
as
BEGIN

	declare @SQLString3 NVARCHAR(MAX)
	declare @NumberString NVARCHAR(4)

	set @NumberString = CAST(@Number as NVARCHAR(4))
	set @SQLString3 = N'SELECT TOP ' + @NumberString + ' * FROM ' + @TableName
	

	EXEC sp_executesql @SQLString3

END

EXEC spVariableTable 'tblActor', 3
-------------

--Dynamic SQL and the IN Operator
--normal IN usage
select * from tblFilm 
where year(FilmReleaseDate) in (1980, 1990, 2000) 
order by FilmReleaseDate

--with stored Procedure
create proc spFilmYears
(
	@YearList NVARCHAR(MAX)
)
as
BEGIN
	declare @SQLString NVARCHAR(MAX)
	set @SQLString =
		N'select * 
		from tblFilm 
		where year(FilmReleaseDate) in (' + @YearList + N') 
		order by FilmReleaseDate'
	exec sp_executesql @SQLString
END

exec spFilmYears '2000, 2001, 2005'
---------------

--Parameters of sp_executesql
exec sp_executesql
	N'select FilmName, FilmReleaseDate, FilmRunTimeMinutes
	from tblFilm 
	where FilmRunTimeMinutes > @Length
	and FilmReleaseDate > @StartDate' 
	,N'@Length INT, @StartDate datetime'
	,@Length = 180
	,@StartDate = '2000-01-01'

---------------
--SQL Injection Attacks
/*For more information on SQL injection attacks and how to prevent them
you can't do better than Erland Sommarskog's definitive article:
--http://www.sommarskog.se/dynamic_sql.html*/

-----------------------------------------------------------------------------
--14.TRANSACTIONS
--Basic Transactions, when one of the three below statements is executed, then a transaction log occurs
/*A transaction is a logical unit of work that contains one or more SQL statements. 
... A transaction ends when it is committed or rolled back, either explicitly with a COMMIT 
or ROLLBACK statement or implicitly when a DDL statement is issued. 
To illustrate the concept of a transaction, consider a banking database.*/

--Adding new records
INSERT INTO tblFilm (FilmName, FilmReleaseDate, FilmID)
VALUES ('Iron Man 3', '2013-04-25', 1000)

--Updating existing records
UPDATE tblFilm
SET FilmBoxOfficeDollars = 284946699
WHERE FilmName = 'Iron Man 3'

--Deleting existing records
DELETE FROM tblFilm
WHERE FilmName = 'Iron Man 3'
----------

--beginning a transaction
BEGIN TRAN

INSERT INTO tblFilm (FilmName, FilmReleaseDate, FilmID)
VALUES ('Iron Man 3', '2013-04-25', 1000)

SELECT * FROM tblFilm WHERE FilmName = 'Iron Man 3'

COMMIT TRANSACTION -- COMMIT or COMMIT TRAN also works
----------
BEGIN TRAN

INSERT INTO tblFilm (FilmName, FilmReleaseDate, FilmID)
VALUES ('Iron Man 3', '2013-04-25', 1000)

SELECT * FROM tblFilm WHERE FilmName = 'Iron Man 3'

ROLLBACK TRANSACTION --make a move backwards

SELECT * FROM tblFilm WHERE FilmName = 'Iron Man 3'
-----------

--naming Transactions
BEGIN TRAN AddIronMan3

INSERT INTO tblFilm (FilmName, FilmReleaseDate, FilmID)
VALUES ('Iron Man 3', '2013-04-25', 1000)

COMMIT TRAN AddIronMan3
-------------

--If statements with Transactions
DECLARE @IronMen INT

BEGIN TRAN AddIronMan3

INSERT INTO tblFilm (FilmName, FilmReleaseDate, FilmID)
VALUES ('Iron Man 3', '2013-04-25', 1001)

SELECT @IronMen = Count(*) from tblFilm Where FilmName = 'Iron Man 3'

if @IronMen > 1
	BEGIN
		ROLLBACK TRAN AddIronMan3
		PRINT 'Iron Man 3 was already there'
	END
else
	begin
		commit Tran AddIronMan3
		PRINT 'Iron Man 3 added to database'
	end
-------------

--using error handling and auto rollback
BEGIN TRY
	BEGIN TRAN AddIM
	INSERT INTO tblFilm (FilmName, FilmReleaseDate, FilmID)
	VALUES ('Iron Man 3', '2013-04-25', 1001)

	UPDATE tblFilm
	SET FilmDirectorID = 4
	WHERE FilmName = 'Iron Man 3'

	COMMIT TRAN AddIM
END TRY
BEGIN CATCH
	ROLLBACK TRAN AddIM
	PRINT 'Adding Iron Man failed- check data types'
END CATCH

SELECT * from tblFilm Where FilmName = 'Iron Man 3'

DELETE FROM tblFilm
WHERE FilmName = 'Iron Man 3'
------------

--nested Transactions
BEGIN TRAN Tran1
	PRINT @@TRANCOUNT

	BEGIN TRAN Tran2
		PRINT @@TRANCOUNT
	COMMIT TRAN Tran2
	PRINT @@TRANCOUNT
	PRINT @@TRANCOUNT
COMMIT TRAN Tran1
-----------
BEGIN TRAN Tran1
	PRINT @@TRANCOUNT

	BEGIN TRAN
		PRINT @@TRANCOUNT
	COMMIT TRAN
	PRINT @@TRANCOUNT

ROLLBACK TRAN Tran1 --rolled back to 1, first value
------------
BEGIN TRAN Tran1
	PRINT @@TRANCOUNT

	BEGIN TRAN
		PRINT @@TRANCOUNT
	ROLLBACK TRAN --everything is rolled back
	PRINT @@TRANCOUNT

COMMIT TRAN Tran1
------------

--saving point TRANSACTION
BEGIN TRAN Tran1
	PRINT @@TRANCOUNT

	SAVE TRAN SavePoint --save overall the transaction
		PRINT @@TRANCOUNT
	ROLLBACK TRAN SavePoint --roled back to previously saved stage
	PRINT @@TRANCOUNT

COMMIT TRAN Tran1
------------

--Nested Transactions and stored procedures

CREATE PROC spGetDirector(@DirectorName VARCHAR(MAX))
AS
BEGIN
	DECLARE @ID INT
	SAVE TRAN AddDirector
	INSERT INTO tblDirector (DirectorName)
	VALUES (@DirectorName)
	IF (SELECT COUNT(*) FROM tblDirector WHERE DirectorName=@DirectorName) > 1
		BEGIN
			PRINT 'Director already existed'
			ROLLBACK TRAN AddDirector
		END
	SELECT @ID = DirectorID FROM tblDirector WHERE DirectorName=@DirectorName
	RETURN @ID
END
---------
DECLARE @DirectorID INT
BEGIN TRAN AddIM
	INSERT INTO tblFilm(FilmName, FilmReleaseDate, FilmID)
	VALUES ('Iron Man 3', '2013-04-25', 1002)

	EXEC @DirectorID=spGetDirector 'Shane Black'

	UPDATE tblFilm
	SET FilmDirectorID = @DirectorID
	WHERE FilmName = 'Iron Man 3'

COMMIT TRAN AddIM
--------------------------------------------------------------------------

--15. DML TRIGGERS
--create Trigger
use Movies
go

create trigger trgActorsChanged
on tblActor
after insert, update, delete
as
begin
	print 'Something happend to the Actor table'
end
-----------------
--use trigger
use Movies
go

set nocount on -- turn off row counts

insert into tblActor(ActorID, ActorName) --insert record
values (999, 'Test Actor')

update tblActor  --update record
set ActorDOB = getdate()
where ActorID = 999

delete from tblActor
where ActorID = 999
--------------
--modify a trigger
alter trigger trgActorsChanged
on tblActor
after insert, update, delete
as
begin
	print 'Data was changed in the Actor table'
end
--------------
-- instead of
use Movies
go

create trigger trgActorsInserted
on tblActor
INSTEAD OF insert  --completely replaces what the orijinal event would have done
as
begin
	RAISERROR ('No more actors can be inserted', 16, 1)
end
go
----------
use Movies
go

set nocount on -- turn off row counts

insert into tblActor(ActorID, ActorName) --insert record
values (999, 'Test Actor')
go

select * from tblActor where ActorID = 999
--------------

--the inserted and Deleted Tables
use Movies
go

alter trigger trgActorsInserted
on tblActor
after insert 
as
begin
	select * from inserted --inserted table
end
go
-----------
use Movies
go

set nocount on -- turn off row counts

insert into tblActor(ActorID, ActorName) --insert record
values (999, 'Test Actor')
go
------------

--validating data
use Movies
go

create trigger trgCastMemberAdded
on tblCast
after insert 
as
begin
	if exists(
		select * from tblActor as a inner join inserted as i on a.ActorID = i.CastActorID
		where actordateofdeath is not null
	)
	BEGIN
		RAISERROR('Sorry, that actor has expired', 16,1)
		rollback transaction
		return
	END
end
go
--------------------------------------------------------------------
--16. DDL TRIGGERS
--https://www.youtube.com/watch?v=9XCB0y44b1g&feature=emb_logo&ab_channel=WiseOwlTutorials
--create, alter, disable, enable, change the order of trigger

--------------------------------------------------------------------
--17. PIVOT TABLE
--https://www.youtube.com/watch?v=C37-SKZDsdU&t=480s&ab_channel=WiseOwlTutorials

--------------------------------------------------------------------
--18. DYNAMIC PIVOT TABLE
--https://www.youtube.com/watch?v=uZGjHYS9lzI&ab_channel=AnthonyB.Smoak


--END OF SQL PROGRAMMING