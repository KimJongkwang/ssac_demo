use prj1;

create table global_def_cnt(
	area varchar(30), 
    area_cn varchar(30),
    area_en varchar(30), 
    creat_dt datetime not null, 
    nat_death_cnt int, 
    nat_death_rate float, 
    nat_def_cnt int, 
    nat varchar(30), 
    nat_cn varchar(30), 
    nat_en varchar(30), 
    seq int primary key, 
    stdday date not null, 
    update_dt datetime);  


select * from global_def_cnt;


use prj1;
show tables;

create table obs_dust(
	obs_dt date not null,
    stn_nm varchar(20) primary key,
    no2 double default 0,
    o3 double default 0,
    co2 double default 0,
    so2 double default 0,
    pm10 int default 0,
    pm25 int default 0);
    
select * from obs_dust;