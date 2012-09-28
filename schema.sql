drop table if exists rooms;
create table rooms (
    id integer prmary key autoincrement,
    name string not null,
    capacity integer not null,
    type integer not null
    );

drop table if exists reservations;
create table reservations (
    foreign key ( reservation_room_id ) references rooms ( room_id ),
    start_time datetime not null,
    end_time datetime not null,
    host string not null,
    num_attendees integer not null,
    description string
    );
