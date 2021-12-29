create table
tles (
    sat varchar(70) not null primary key,
    tle varchar(140) not null
);

create table
sat_groups (
    id mediumint not null auto_increment primary key,
    sat varchar(70) not null,
    group_name varchar(20),
    foreign key (group_name) references groups(group_name)
);

create table
groups (
    group_name varchar(20) primary key
)

insert into groups (group_name) values ('weather'), ('noaa'), ('goes'), ('resource'), ('sarsat'), ('dmc'), ('tdrss'), ('argos'), ('planet'), ('spire'), ('geo'), ('intelsat'), ('ses'), ('iridium'), ('iridium-NEXT'), ('starlink'), ('oneweb'), ('orbcomm'), ('globalstar'), ('swarm'), ('amateur'), ('x-comm'), ('other-comm'), ('satnogs'), ('gorizont'), ('raduga'), ('molniya'), ('gnss'), ('gps-ops'), ('glo-ops'), ('galileo'), ('beidou'), ('sbas'), ('nnss'), ('musson'), ('science'), ('geodetic'), ('education'), ('engineering'), ('military'), ('radar'), ('cubesat'), ('other');

select * from groups;
select * from sat_groups;
select * from tles;

drop table sat_groups;
delete from groups;

select group_name from sat_groups
where sat like 'NOAA 15%';