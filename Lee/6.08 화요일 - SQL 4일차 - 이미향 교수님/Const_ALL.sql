drop table dept;

create table dept
(deptno number(3),
dname varchar2(10),
loc varchar2(10),
constraint dept_deptno_pk primary key (deptno),
constraint dept_dname_uq unique (dname)
);

drop table sawon;

create table sawon
(sabun number(3),
saname varchar2(10) constraint sawon_saname_nn not null,
deptno number(3),
sajob varchar2(10),
sapay number(10),
sahire date default sysdate,
sasex varchar2(6),
samgr number(3),
constraint sawon_sabun_pk primary key (sabun),
constraint sawon_deptno_fk foreign key (deptno) references dept (deptno) on delete cascade,
constraint sawon_samgr_fk foreign key(samgr) references sawon (sabun),
constraint sawon_sasex_ck check (sasex in ('남자','여자'))
);

drop table gogek;

create table gogek
(gobun number(3),
goname varchar2(10),
gotel varchar2(20),
gojumin varchar2(14),
godam number(3),
constraint gogek_gobun_pk primary key (gobun),
constraint gogek_godam_fk foreign key (godam) references sawon (sabun)
);

on delete cascade 는 모체가 지워지면 딸린 자식들도 따라서 지워진다.
