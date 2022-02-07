/*

select * from department;
select * from dept_emp;
select * from dept_manager;
select * from employee;
select * from salary;
select * from title;

*/

CREATE TABLE employee (
	 emp_no INT NOT NULL,
     birth_date DATE NOT NULL,
     first_name VARCHAR NOT NULL,
     last_name VARCHAR NOT NULL,
     gender VARCHAR NOT NULL,
     hire_date DATE NOT NULL,
     PRIMARY KEY (emp_no)
);

CREATE TABLE department (
    "dept_no" varchar   NOT NULL,
    "dept_name" varchar   NOT NULL,
    PRIMARY KEY ("dept_no")
);

CREATE TABLE dept_manager (
dept_no VARCHAR(4) NOT NULL,
    emp_no INT NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
FOREIGN KEY (emp_no) REFERENCES employee (emp_no),
FOREIGN KEY (dept_no) REFERENCES department (dept_no),
    PRIMARY KEY (emp_no, dept_no)
);

CREATE TABLE salary (
	emp_no INT NOT NULL,
	salary INT NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employee (emp_no),
	PRIMARY KEY (emp_no)
);

CREATE TABLE "dept_emp" (
    "emp_no" int   NOT NULL,
    "dept_no" varchar   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL,
    foreign key (emp_no) references employee (emp_no),
    foreign key (dept_no) references department (dept_no),
    primary key (emp_no, dept_no)
);

CREATE TABLE "title" (
    "emp_no" int   NOT NULL,
    "title" varchar   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

