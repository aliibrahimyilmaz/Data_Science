/*
Created by wise owl
show a list of films
www.wiseowl.co.uk
*/

--1. SELECT and ORDER BY
use Movies
select TOP 10 with TIES
       FilmName Title  -- as Title or as [Title]
	   , FilmReleaseDate 'Released on' -- or [Released on]
	   , FilmRunTimeMinutes as Duration
	   , [FilmOscarWins]
from dbo.tblFilm
order by [FilmOscarWins] asc
		--, Duration desc
		--, FilmName asc

--2. WHERE
select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmRunTimeMinutes <> 120
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
--where FilmRunTimeMinutes between 120 and 150
where FilmRunTimeMinutes in (90,120,150,160)
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmName = 'die hard' --case insensitive
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmName like 'die hard%' --case insensitive and useful with wildcards
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmName like '%die hard%' --case insensitive and useful with wildcards
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmName like 'lethal weapon%' --case insensitive and useful with wildcards
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmName like 'lethal weapon__' --case insensitive and useful with wildcards
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmName like 'Twi%' --case insensitive and useful with wildcards
order by FilmRunTimeMinutes

--3. DATES
select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmReleaseDate = '1933-04-07'  --year-month-date
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmReleaseDate = '7/4/1933' -- no result
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmReleaseDate = '4/7/1933' -- month-year-date
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmReleaseDate between '2000-01-01' and '2000-12-31'  --interval
order by FilmRunTimeMinutes

--any film realeased in the month of May
select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where month(FilmReleaseDate) = 5 
order by FilmRunTimeMinutes

--any film realeased in the year of 2000
select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where year(FilmReleaseDate) = 2000 
order by FilmRunTimeMinutes

--any film realeased in the day of 22
select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where day(FilmReleaseDate) = 22 
order by FilmRunTimeMinutes

--4. AND or OR with WHERE Criteria
select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmName like '%star%' and
	  FilmReleaseDate < '2000-01-01' and
	  FilmRunTimeMinutes > 120
order by FilmRunTimeMinutes

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmRunTimeMinutes > 180 and
	  FilmName like 's%' or
	  FilmName like 't%'
order by FilmName

select FilmName, FilmReleaseDate, FilmRunTimeMinutes
from tblFilm
where FilmRunTimeMinutes > 180 and
	  (FilmName like 's%' or
	  FilmName like 't%')
order by FilmName

--5. CALCULATED Columns
select FilmName, FilmBoxOfficeDollars, FilmBudgetDollars,
	   FilmBoxOfficeDollars - FilmBudgetDollars as FilmProfitLoss
from  tblFilm

--6. SORT
select FilmName, FilmBoxOfficeDollars, FilmBudgetDollars,
	   FilmBoxOfficeDollars - FilmBudgetDollars as FilmProfitLoss
from  tblFilm
order by FilmProfitLoss desc

select FilmName, FilmBoxOfficeDollars, FilmBudgetDollars,
	   FilmBoxOfficeDollars - FilmBudgetDollars as FilmProfitLoss
from  tblFilm
where (FilmBoxOfficeDollars - FilmBudgetDollars) < 0
order by FilmProfitLoss desc

--7. datatype int into decimal
select FilmName, FilmRunTimeMinutes, FilmRunTimeMinutes/60 as RunTimeHours
from tblFilm

select FilmName, FilmRunTimeMinutes, FilmRunTimeMinutes/60.0 as RunTimeHours
from tblFilm

select FilmName, FilmBoxOfficeDollars,
	   FilmBoxOfficeDollars*0.2 as FilmTax,
	   FilmBudgetDollars + (FilmBoxOfficeDollars*0.2) as FilmTotal
from tblFilm

select FilmName, FilmRunTimeMinutes, FilmRunTimeMinutes/60 as Hours,
	   FilmRunTimeMinutes%60 as Minutes, FilmRunTimeMinutes/60.0 as RunTimeHours
from tblFilm

--8. The CASE Statement (numbers, text, dates)

select FilmName, FilmRunTimeMinutes,
	   case
			when FilmRunTimeMinutes <= 90 then 'short'
			when FilmRunTimeMinutes <= 150 then 'medium'
			when FilmRunTimeMinutes <= 180 then 'long'
			else 'epic'
	   end as FilmDuration,  -- alias must be here
	   FilmReleaseDate
from tblFilm
where -- we can NOT use the ALIAS here
	case
			when FilmRunTimeMinutes <= 90 then 'short'
			when FilmRunTimeMinutes <= 150 then 'medium'
			when FilmRunTimeMinutes <= 180 then 'long'
			else 'epic'
	   end = 'medium'

select FilmName,
	   case
			when FilmName like '%twi%' then 'just awful'
			else 'probably not bad'
		end
from tblFilm

select FilmName,
	   FilmReleaseDate,
	   case
			when FilmReleaseDate < '1927-10-01' then 'silent era'
			else 'talkie era'
		end
from tblFilm

--9. JOINS

--INNER joins
select *
from tblFilm as f
	 inner join tblDirector as d
		on f.FilmDirectorID = d.DirectorID
	 inner join tblStudio as s
		on f.FilmStudioID = s.StudioID
	 inner join tblCountry as c
		on f.FilmCountryID = c.CountryID

select f.FilmName, d.DirectorName, s.StudioName, c.CountryName
from tblFilm as f
	 inner join tblDirector as d
		on f.FilmDirectorID = d.DirectorID
	 inner join tblStudio as s
		on f.FilmStudioID = s.StudioID
	 inner join tblCountry as c
		on f.FilmCountryID = c.CountryID

--LEFT and RIGHT OUTER joins
select d.DirectorID, d.DirectorName, f.FilmName, f.FilmDirectorID
from tblDirector as d
	 left outer join tblFilm as f -- we have 265 rows with 5 nulls come from left side
		on d.DirectorID = f.FilmDirectorID
where f.FilmID is null

-- the people who are actress and directors INNER JOIN
select *
from tblActor as a
	inner join tblDirector as d on a.ActorName = d.DirectorName

-- the people only been actors not directors
select *
from tblActor as a
	left outer join tblDirector as d on a.ActorName = d.DirectorName
where d.DirectorID is null

-- the people only been directors not actors 
select *
from tblActor as a
	right outer join tblDirector as d on a.ActorName = d.DirectorName
where a.ActorID is null

--FULL OUTER joins (bring all of the information both tables, every piece of information from both tables)
select *
from tblActor as a
	full outer join tblDirector as d on a.ActorName = d.DirectorName

--10. USING FUNCTIONS and PARAMETERS and HELP (F1 Key)
--finding a list of functions from the left side under PROGRAMMABILITY
--and system functions
select FilmName, FilmReleaseDate, UPPER(FilmName)
from tblFilm

select FilmName, FilmReleaseDate, UPPER(FilmName)
	,datename(M, FilmReleaseDate) as Months,
	DATEDIFF(D,FilmReleaseDate,GETDATE()) as OLD --nested function
from tblFilm

-- 11. TEXT CALCULATIONS (concatenate, separate Strings)

-- cast and convert
select FilmName, FilmOscarWins,
		FilmName + ' won ' + cast(FilmOscarWins as varchar(2)) --cast convert data type
		, FilmName + ' won ' + convert(varchar(2),FilmOscarWins)
from tblFilm

--seperating text
select ActorName,
		left(ActorName,3)
from tblActor

select ActorName,
		left(ActorName,3),
		charindex(' ', ActorName)-1 --finds the index of empty string
from tblActor

select ActorName,
		left(ActorName,3),
		charindex(' ', ActorName)-1, --finds the index of empty string
		left(ActorName,charindex(' ', ActorName)-1)
from tblActor

select ActorName,
		right(ActorName,6)
		,len(ActorName) - charindex(' ', ActorName)
		,right(ActorName,len(ActorName) - charindex(' ', ActorName))
from tblActor

--concat again
select ActorName
		,left(ActorName,charindex(' ', ActorName)-1)
		,right(ActorName,len(ActorName) - charindex(' ', ActorName))
from tblActor

select ActorName
		,left(ActorName,charindex(' ', ActorName)-1) + ' ' + right(ActorName,len(ActorName) - charindex(' ', ActorName))
		,right(ActorName,len(ActorName) - charindex(' ', ActorName)) + ', ' + left(ActorName,charindex(' ', ActorName)-1) as reverse_name
from tblActor
order by reverse_name

-- 12. DATE CALCULATIONS

select FilmName, FilmReleaseDate,
		convert(char(8), FilmReleaseDate, 3)
from tblFilm

select FilmName, FilmReleaseDate,
		convert(char(10), FilmReleaseDate, 103)  -- from the table F1 HELP
from tblFilm

select FilmName, FilmReleaseDate,
		convert(char(10), FilmReleaseDate, 103),
		datename(dw, FilmReleaseDate) -- gives the weekday
from tblFilm

-- custom date formats
select FilmName, FilmReleaseDate,
		convert(char(10), FilmReleaseDate, 103),
		datename(dw, FilmReleaseDate), -- gives the weekday
		datename(dd, FilmReleaseDate),
		datename(MM, FilmReleaseDate),
		datename(yy, FilmReleaseDate)
from tblFilm

select FilmName, FilmReleaseDate,
		convert(char(10), FilmReleaseDate, 103),
		datename(dw, FilmReleaseDate)+ ' ' +
		datename(dd, FilmReleaseDate)+ ' ' +
		datename(MM, FilmReleaseDate)+ ' ' +
		datename(yy, FilmReleaseDate)
from tblFilm

--calculating the time between dates

select FilmName, FilmReleaseDate,
		DATEDIFF(dd, FilmReleaseDate, getdate()) -- how old are the films
from tblFilm

--raw age calculation

select FilmName, FilmReleaseDate,
		GETDATE(),
		DATEDIFF(dd, FilmReleaseDate, getdate()), -- how old are the films
		DATEDIFF(yy, FilmReleaseDate, getdate())
from tblFilm

--exact age calculation
select FilmName, FilmReleaseDate,
		GETDATE(),
		DATEDIFF(dd, FilmReleaseDate, getdate()), -- how old are the films
		DATEDIFF(yy, FilmReleaseDate, getdate()),
		dateadd(yy, DATEDIFF(yy, FilmReleaseDate, getdate()), FilmReleaseDate),
		CASE
			when dateadd(yy, DATEDIFF(yy, FilmReleaseDate, getdate()), FilmReleaseDate) > GETDATE()
			then DATEDIFF(yy, FilmReleaseDate, getdate()) - 1
			else DATEDIFF(yy, FilmReleaseDate, getdate())
		end
from tblFilm

-- 13.GROUPING and AGGREGATING

select sum(FilmRunTimeMinutes) as totalruntime,
		avg(FilmRunTimeMinutes) as averageruntime,
		max(FilmRunTimeMinutes) as maxruntime,
		min(FilmRunTimeMinutes) as minruntime,
		count(FilmRunTimeMinutes) as numberofruntime
from tblFilm

select sum(convert(bigint, FilmBoxOfficeDollars)),
	    avg(FilmRuntimeMinutes),
		avg(convert(decimal, FilmRuntimeMinutes)) --accurate reflection
from tblFilm

--GROUP BY and HAVING

select CountryName, avg(FilmRunTimeMinutes) as average,
		sum(FilmRunTimeMinutes) as summe,
		max(FilmRunTimeMinutes) as highest,
		min(FilmRunTimeMinutes) as lowest,
		count(FilmRunTimeMinutes) as count_sum
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
group by CountryName
order by countryName

--group by with rollup
select avg(FilmRunTimeMinutes) as average,
		sum(FilmRunTimeMinutes) as summe,
		max(FilmRunTimeMinutes) as highest,
		min(FilmRunTimeMinutes) as lowest,
		count(FilmRunTimeMinutes) as count_sum,
		isnull(CountryName, 'TOTAL')
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
group by CountryName with rollup -- gives also the info of entire set as a row
order by countryName asc

--group by with where and HAVING

select avg(FilmRunTimeMinutes) as average,
		sum(FilmRunTimeMinutes) as summe,
		max(FilmRunTimeMinutes) as highest,
		min(FilmRunTimeMinutes) as lowest,
		count(FilmRunTimeMinutes) as count_sum,
		isnull(CountryName, 'TOTAL')
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
where CountryName like 'U%'
group by CountryName with rollup -- gives also the info of entire set as a row
order by countryName asc

select avg(FilmRunTimeMinutes) as average,
		sum(FilmRunTimeMinutes) as summe,
		max(FilmRunTimeMinutes) as highest,
		min(FilmRunTimeMinutes) as lowest,
		count(FilmRunTimeMinutes) as count_sum,
		isnull(CountryName, 'TOTAL')
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
where min(FilmRunTimeMinutes) >= 100 -- CAN NOT USE AGGREGATE FUNCTIONS in WHERE
group by CountryName with rollup -- gives also the info of entire set as a row
order by countryName asc

select avg(FilmRunTimeMinutes) as average,
		sum(FilmRunTimeMinutes) as summe,
		max(FilmRunTimeMinutes) as highest,
		min(FilmRunTimeMinutes) as lowest,
		count(FilmRunTimeMinutes) as count_sum,
		isnull(CountryName, 'TOTAL')
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
--where min(FilmRunTimeMinutes) >= 100 -- CAN NOT USE AGGREGATE FUNCTIONS in WHERE
group by CountryName with rollup -- gives also the info of entire set as a row
having min(FilmRunTimeMinutes) >= 100
order by countryName asc

select avg(FilmRunTimeMinutes) as average,
		sum(FilmRunTimeMinutes) as summe,
		max(FilmRunTimeMinutes) as highest,
		min(FilmRunTimeMinutes) as lowest,
		count(FilmRunTimeMinutes) as count_sum,
		isnull(CountryName, 'TOTAL')
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
group by CountryName with rollup -- gives also the info of entire set as a row
having avg(FilmRunTimeMinutes) >= 125
order by countryName asc

--grouping by multiple columns
select CountryName, DirectorName, avg(convert(decimal,FilmRunTimeMinutes)) as ave_duration,
		count(*) as count_
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
	inner join tblDirector as d on d.DirectorID = f.FilmDirectorID
--where
group by CountryName, DirectorName
--having
order by CountryName

select isnull(CountryName,'Grand'),
		isnull(DirectorName,'Total'),
		avg(convert(decimal,FilmRunTimeMinutes)) as ave_duration,
		count(*) as count_
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
	inner join tblDirector as d on d.DirectorID = f.FilmDirectorID
--where
group by CountryName, DirectorName with rollup
--having
order by CountryName

select isnull(CountryName,'Grand'),
		isnull(DirectorName,'Total'),
		avg(convert(decimal,FilmRunTimeMinutes)) as ave_duration,
		count(*) as count_
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
	inner join tblDirector as d on d.DirectorID = f.FilmDirectorID
--where avg(convert(decimal,FilmRunTimeMinutes)) > 120  --does not work
group by CountryName, DirectorName with rollup
having avg(convert(decimal,FilmRunTimeMinutes)) > 120 
-- having ave_duration > 120 --does not work
order by CountryName

--14. SUBQUERIES
/*What is a Subquery?
Using Subqueries in the WHERE Clause
Using Subqueries in the SELECT List
Adding Criteria to a Subquery
Using Subqueries to Return Multiple Values
*/
use Movies

-- subquery with where
select FilmName, FilmReleaseDate, FilmOscarWins
from tblFilm
where FilmOscarWins = 
		(select max(FilmOscarWins)
		from tblFilm)

select FilmName, FilmRunTimeMinutes
from tblFilm
where FilmRunTimeMinutes >=
		(select avg(FilmRunTimeMinutes)
		from tblFilm)

-- subquery in the select list
select FilmName, FilmRunTimeMinutes,
		(select avg(FilmRunTimeMinutes)
		from tblFilm) as Average
from tblFilm
where FilmRunTimeMinutes <=
		(select avg(FilmRunTimeMinutes)
		from tblFilm)

select FilmName, FilmRunTimeMinutes, FilmReleaseDate, FilmBudgetDollars
from tblFilm
where filmbudgetdollars >
		(select max(FilmBudgetDollars)
		from tblFilm
		where FilmReleaseDate < '2000-01-01')

select FilmName, FilmReleaseDate
from tblFilm
where FilmReleaseDate = 
	(select FilmReleaseDate
	from tblFilm
	where FilmName = 'Casino')

select Filmname, FilmDirectorID, DirectorName
from tblFilm f
	inner join tblDirector d on f.FilmDirectorID = d.DirectorID
where FilmDirectorID in
		(select DirectorID
		from tblDirector
		where DirectorDOB between '1946-01-01' and '1946-12-31')
order by DirectorName

-- corraleted subqueries
use Movies

--basic query:only show the maximum value
select c.CountryName, f.FilmName, f.FilmRunTimeMinutes
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
where f.FilmRunTimeMinutes = 
		(select max(FilmRunTimeMinutes)
		from tblFilm)

--correlated query: show every max value in each countries
select c.CountryName, f.FilmName, f.FilmRunTimeMinutes
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
where f.FilmRunTimeMinutes = 
		(select max(FilmRunTimeMinutes)
		from tblFilm as g
		where f.FilmCountryID = g.FilmCountryID) -- correlated query

select c.CountryName, f.FilmName, f.FilmRunTimeMinutes
from tblFilm as f
	inner join tblCountry as c on c.CountryID = f.FilmCountryID
where f.FilmRunTimeMinutes > 
		(select avg(FilmRunTimeMinutes)
		from tblFilm as g
		where f.FilmCountryID = g.FilmCountryID) -- correlated query

select year(f.FilmReleaseDate) as y, f.FilmName, f.FilmRunTimeMinutes
from tblFilm as f
where f.FilmRunTimeMinutes > 
		(select avg(FilmRunTimeMinutes)
		from tblFilm as g
		where year(g.FilmReleaseDate) = year(f.FilmReleaseDate)) -- correlated query
order by y