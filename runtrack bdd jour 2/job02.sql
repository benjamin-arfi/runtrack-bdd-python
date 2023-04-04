create table etage
    -> (
    -> id int primary key not null auto_increment,
    -> nom varchar(255),
    -> numero int,
    -> superficie int
    -> );

create table salles
    -> (
    -> id int primary key not null auto_increment,
    -> nom varchar(255),
    -> id_etage int,
    -> capacite int
    -> );