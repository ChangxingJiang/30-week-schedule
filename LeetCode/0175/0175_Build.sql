# 创建Person表
Create table Person
(
    PersonId  int,
    FirstName varchar(255),
    LastName  varchar(255)
);

# 创建Address表
Create table Address
(
    AddressId int,
    PersonId  int,
    City      varchar(255),
    State     varchar(255)
);

# 清除Person表中的所有数据，但表格本身会继续存在
Truncate table Person;

# 在Person表中写入1条记录
insert into Person (PersonId, LastName, FirstName)
values ('1', 'Wang', 'Allen');

# 清除Address表中的所有数据，但表格本身会继续存在
Truncate table Address;

# 在Address表中写入1条记录
insert into Address (AddressId, PersonId, City, State)
values ('1', '2', 'New York City', 'New York');