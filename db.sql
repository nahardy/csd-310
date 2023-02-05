
use pysports
drop table if exists team;
drop table if exists player;
create table team (
   
   team_id int not null auto_increment,
   team_name varchar(75) not null,
   mascot varchar(75) not null,
   primary key(team_id)
);

create table player (
    player_id int not null auto_increment,
    first_name varchar(75) not null,
    last_name varchar(75) not null,
    team_id int not null,
    primary key(player_id),
    constraint fk_team
    foreign key(team_id)
    references team(team_id)

);

INSERT INTO team(team_name, mascot)
VALUES('Team Gandalf', 'White Wizards'); 

-- # mysql -u root -p Azul7334$
-- # mysql -u root -p MySQL8IsGreat!

-- # mysql -u pysports_user -p Azul7334$
-- # mysql -u pysports_user -p MySQL8IsGreat!