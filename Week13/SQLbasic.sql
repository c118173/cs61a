create table parents as
    select "delano" as parent, "herbert" as child union
    select "abraham"         , "barack"           union
    select "abraham"         , "clinton"          union
    select "fillmore"        , "abraham"          union
    select "fillmore"        , "delano"           union
    select "fillmore"        , "grover"           union
    select "eisenhower"      , "fillmore";


-- Projecting Existing Tables
select parent from parents where parent > child;


-- Arithmetic in select expressions
create table lift as
    select 101 as chair, 2 as single, 2 as couple union
    select 102         , 0          , 3           union
    select 103         , 4          , 1;

select chair, single + 2 * couple as total from lift;


create table ints as
    select "zero" as word, 0 as one, 0 as two, 0 as four, 0 as eight union
    select "one"         , 1       , 0       , 0        , 0          union
    select "two"         , 0       , 2       , 0        , 0          union
    select "three"       , 1       , 2       , 0        , 0          union
    select "four"        , 0       , 0       , 4        , 0          union
    select "five"        , 1       , 0       , 4        , 0;

select word, one + two + four + eight as value from ints;

select word from ints where one + two/2 + four/4 + eight/8 = 1;

-- Joining Tables
select * from parents, dog;
select * from parents, dogs where child = name and fur = 'curly';
select parent from parents, dogs where child = name and fur = 'curly';


-- Aliases and Dot Expressions
select a.child as first, b.child as second
    from parents as a, parents as b
    where a.parent = b.parent and a.child < b.child;


-- Joining Multiple Tables
create table grandparents as
    select a.parent as grandog, b.child as grandpup
           from parents as a, parents as b
           where a.child = b.parent;

select grandog from grandparents, dogs as c, dogs as d
    where grandog = c.name and 
          grandpup = d.name and 
          c.fur = d.fur;


-- Numerical Expressions
create table cities as
    select 38 as latitude, 122 as longitude, "Berkeley" as name union
    select 42,              71,              "Cambridge"        union
    select 45,              93,              "Minneeapolis"     union

create table cold as
    select name from cities where latitude >= 43;
select name from cold union
    select "Chicago";

create table distances as 
    select a.name as first, b.name as second,
           60 * (b.latitude - a.latitude) as distance
           from cities as a, cities as b
select second from distances
       where first = 'Minneapolis'
       order by distance;


-- String Expressions
select "hello," || "world";

create table phrase as select "hello, world" as s;
select substr(s, 4, 2) || substr(s, instr(s, " ") + 1, 1) from phrase;

create table lists as select "one" as car, "two, three, four" as cdr;
select substr(cdr, 1, instr(cdr, ",") -1) as cadr from lists;

create table nouns as
    select "dog" as phrase union
    select "car"           union
    select "bird";
select subject.phrase || "chased" || object.phrase
    from nouns as subject, nouns as object
    where subject.phrase <> object.phrase;


-- Aggregation
create table animals as
    select "dog" as kind, 4 as legs, 20 as weight union
    select "cat"        , 4        , 10           union
    select "ferret"     , 4        , 10           union
    select "parrot"     , 2        , 6            union
    select "penguin"    , 2        , 10           union
    select "t-rex"      , 2        , 12000;
select max(legs) from animals;
select sum(weight) from animals;
select min(legs), max(weight) from animals 
    where kind <> "t-rex";
select avg(legs) from animals;
select count(*) from animals;          -- how many rows
select count(distinct legs) from animals;
select sum(distinct weight) from animals;
select max(weight), kind from animals; -- aggregate selects a row
select min(kind), kind from animals;
select avg(weight), kind from animals; -- unmeaningful value
select max(legs), kind from animals;   -- arbitrary value


-- Group
select legs, max(weight) from animals group by legs;
select legs, count(*) from animals group by legs;
select legs, weight from animals group by legs, weight;
select weight/legs, count(*) from animals group by weight/legs having count(*)>1;