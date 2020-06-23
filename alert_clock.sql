
create schema alert_clock;

create table alert_clock.clock(
    id serial primary key,
    message text not null,
    timer timestamp not null,
    created timestamp not null default now()
);

