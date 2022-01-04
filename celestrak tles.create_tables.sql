drop table sat_groups;
drop table tles;
delete from groups;

create table
tles (
    sat varchar(70) not null,
    sat_cat_num varchar(5) primary key,
    tle varchar(140) not null
);

create table
sat_groups (
    id mediumint not null auto_increment primary key,
    sat_cat_num varchar(5) not null,
    group_name varchar(20) not null,
    foreign key (sat_cat_num) references tles(sat_cat_num),
    foreign key (group_name) references groups(group_name)
);

create table
groups (
    group_name varchar(20) primary key
);

insert into groups (group_name) values ('stations'), ('weather'), ('noaa'), ('goes'), ('resource'), ('sarsat'), ('dmc'), ('tdrss'), ('argos'), ('planet'), ('spire'), ('geo'), ('intelsat'), ('ses'), ('iridium'), ('iridium-NEXT'), ('starlink'), ('oneweb'), ('orbcomm'), ('globalstar'), ('swarm'), ('amateur'), ('x-comm'), ('other-comm'), ('satnogs'), ('gorizont'), ('raduga'), ('molniya'), ('gnss'), ('gps-ops'), ('glo-ops'), ('galileo'), ('beidou'), ('sbas'), ('nnss'), ('musson'), ('science'), ('geodetic'), ('education'), ('engineering'), ('military'), ('radar'), ('cubesat'), ('other');
insert into groups set group_name = 'stations';

select * from groups;
select * from sat_groups;
select * from tles;

delete from tles;
delete from sat_groups;
delete from groups;


select sat 
from sat_groups natural join tles
where group_name = 'weather';