create database Manufacturer
create table Product
	(product_id char(20) not null,
	product_name char(50) not null,
	quantity float null,
	constraint product_pk primary key(product_id)
	)

create table Component
	(component_id char(20) not null,
	component_name char(50) not null,
	quantity float null,
	description_ char(70) null,
	constraint component_pk primary key(component_id)
	)

create table Supplier
	(supplier_id char(20) not null,
	supplier_name char(50) not null,
	address_ char(70) null,
	email char(50) null,
	phone char(20) null,
	constraint supplier_pk primary key(supplier_id)
	)

create table Supply
	(supplier_id char(20) not null,
	component_id char(20) not null,
	primary key (supplier_id, component_id),
	foreign key (supplier_id) references dbo.Supplier,
	foreign key (component_id) references dbo.Component
	)

create table Production
	(product_id char(20) not null,
	component_id char(20) not null,
	primary key (product_id, component_id),
	foreign key (product_id) references dbo.Product,
	foreign key (component_id) references dbo.Component
	)

select * from [dbo].[Product]