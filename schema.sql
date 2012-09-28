drop table if exists rooms;
create table rooms (
    room_id integer primary key not null,
    name string not null,
    capacity integer not null,
    type string not null,
    num_whiteboards integer not null
);

drop table if exists reservations;
create table reservations (
    reservation_id integer primary key not null,
    room_id integer not null,
    start_time datetime not null,
    end_time datetime not null,
    host string not null,
    num_attendees integer not null,
    description string,
    foreign key ( room_id ) references rooms ( room_id )
);

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Yukon', 5, 'ops', 2
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Northwest Territories', 5, 'ops', 2
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Nunavut', 5, 'ops', 2
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Newfoundland', 5, 'ops', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Ringo Starr', 1, 'beatles', 0
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'George Harrison', 1, 'beatles', 0
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Paul McCartney', 1, 'beatles', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'John Lennon', 1, 'beatles', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Prince Edward Island', 10, 'hr', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'New Brunswick', 10, 'hr', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Nova Scotia', 10, 'hr', 2
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Manitoba', 5, 'exec', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Ontario', 5, 'exec', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Quebec', 5, 'exec', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'British Columbia', 5, 'support', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Alberta', 5, 'support', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Saskatchawan', 5, 'support', 1
    );

insert into rooms (
        name, capacity, type, num_whiteboards
    ) values (
        'Loft', 100, 'loft', 0
    );