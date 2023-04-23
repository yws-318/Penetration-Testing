# Oracle Command

DESC   
dept 테이블 구성 살펴보기
```
DESC dept;
```

emp 테이블 전체 열 조회하기
```
SELECT * FROM emp;
```

DISTINCT   
열 중복 제거
```
SELECT DISTINCK job, deptno FROM emp;
```

ALL   
열 제거 없이 그대로 출력
```
SELECT ALL job, deptno FROM emp;
```

열에 연산식을 사용하여 출력하기
```
SELECT ename, sal, sal*12+comm, comm FROM emp;
```

AS   
annsal 이라는 별칭 지정
```sql
SELECT ename, sal, sal*12+comm AS annsal, comm FROM emp;
```

ORDER BY   
오름차순
```
SELECT * FROM emp ORDER BY sal;
```
```
10
20
30
40
40
40
50
50
```


order by _ desc   
내림차순
```
SELECT * FROM emp ORDER BY sal DESC;
```

WHERE
특정 데이터만 출력
```sql
select * from emp where deptno = 30;
```

and 연산자로 여러 개의 조건식 사용
```sql
select * from emp where deptno = 30 and job = 'salesman';
```
and 연산자   
T T = T   
T F = F   
F T = F   
F F = F

or 연산자로 여러 개의 출력 조건 사용
```sql
select * from emp where deptno = 30 or job  'clerk';
```
or 연산자   
T T = T   
T F = T   
F T = T   
F F = F  

곱셈 산술 연산자
```sql
select * from emp where sal*12=36000;
```

<>=!^    
대소 비교 연산자
```sql
select * from emp where sal>=3000;
select * from emp where ename=>'F';
select * from emp where sal != 3000;
select * from emp where sal <> 3000;
select * from emp where sal ^= 3000;
select * from emp where not sal = 3000;
```
```sql
A 값이 B 값과 같을 경우 true, 다를 경우 false 
= 

A 값이 B 값과 같을 경우 false, 다를 경우 true 
!=
<>
^=
```

not
논리 부정 연산자
```sql
select * from emp where not sal = 3000;
```

in
job 이 manager, salesman, clerk 중 하나라면 모두 조회
```sql
select * from emp where job in ('manager','salesman','clerk');
=
select * from emp where job='manager' or job='salesman' or job='clerk';
```
not in
```sql
select * from emp where job not in ('manager','salesman','clerk');
=
select * from emp where job != 'manager' and job <> 'salesman' and job^='clerk';
```

berween a and b   
특정 열 값의 최소, 최고 범위 지정해서 해당 범위 내의 데이터만 조회
```sql
select * from emp where sal between 2000 and 3000;
```
```sql
select * from emp where sal not between 2000 and 3000;
```

like   
일부 문자열이 포함된 데이터를 조회
```sql
select * from emp where ename like 's%';
select * from emp where ename like '%am%';
select * from emp where ename not like '%adfzxc%';

와일드 카드 문자가 데이터 일부일 경우 
_ %
select * from some_table where some_column like 'A\_A%' ESCAPE '\';
```

null
```sql
null + 100 = null
null > 100 = null
null = ∞ = ?
```

is null   
해당 열의 값을 null인 데이터로 출력하고 싶을 때
```sql
select * from emp where comm is null;
```
```sql 
select * from emp where mgr is not null;
```

union   
집합 연산자.   
★두 개의 select문 결과 값을 연결할 때 각 select문이 출력하려는 열 개수와 열 자료형이 순서별로 일치해야 함.★
```sql
select empno,ename,sal from emp where deptno=10 union 
select sal,job,deptno from emp where deptno=20;
```
```sql
union = 연결된 select 문의 결과 값을 합집합으로 묶어 준다. 결과값의 중복은 제거.
union all = 연결된 select 문의 결과 값을 합집합으로 묶어 준다. 중복된 결과 값도 제거 없이 모두 출력   
minus = 먼저 작성한 select 문의 결과 값에서 다음 select 문의 결과 값을 차집함 처리.    
        먼저 작성한 select 문의 결과 값 중 다음 select 문에 존재하지 않는 데이터만 출력
intersect = 먼저 작성한 select 문과 다음 select 문의 결과 값이 같은 데이터만 출력. 교집합.
```

연산자 우선순위   
높은 순서에서   
낮은 순서
```sql
*, /                                    = 곱하기, 나누기
+, -                                    = 더하기, 빼기
=, !=, ^=, <>, >, >=, <, <= =           = 대소 비교 연산자
is (not) null, (not) like, (not) in     = (그 외)비교 연산자
between a and b                         = between 연산자
not                                     = 논리 부정 연산자
and                                     = 논리 연산자 and
or                                      = 논리 연산자 or
```

upper()   
괄호 안 문자 데이터를 모두 대문자로 변환   
lower()   
소문자로 변환   
initcap()   
문자 데이터 중 첫 글자는 대문자로, 나머지 문자를 소문자로 변환
```sql
select ename, upper(ename),lower(ename),initcap(ename) from emp;
```
```sql
게시판의 글 제목이나 글 본문처럼 가변 길이 문자열 데이터에서 특정 문자열을 포함하는 데이터를 조회할 경우

select * from 게시판테이블 where 게시판 제목 열 like '%Oracle%' 
                             or 게시판 본문 열 like '%Oracle%';
하지만 이 경우에는 ORACLE, oracle, OrAcLe 같이 대소문자를 구분하여 찾아낼 수는 없음.
```

```sql
emp table 에서 사원 이름이 대-소문자 상관없이 scott인 사람을 찾을 때
select * from emp where upper(ename)=upper('scott');

게시판 제목, 본문 동시 조회
select * from emp where upper(게시판 제목 열) like upper('%scott%')
                     or upper(게시판 본문 열) like upper('%scott%');
```

length   
문자열 길이 구하는 함수
```sql
select ename, length(ename) from emp;

ename  | length(ename)
       |
smith  | 5
allen  | 5
ward   | 4
miller | 6
```

lengthb   
문자열 바이트 수 반환
```sql
select length('한글'), lengthb('한글') from dual;

length('한글') | lengthb('한글')
               |
             2 |             4
```

substr   
문자열 일부를 추출하는 함수
```sql
substr(문자열 데이터, 시작 위치, 추출 길이)
문자열 데이터의 시작 위치부터 추출 길이만큼 추출.

substr(문자열 데이터, 시작위치)
문자열 데이터의 시작 위치부터 문자열 데이터 끝까지 추출.

(시작 위치가 음수(-)일 경우 뒤에서 시작.)
job = salesman

substr(job, -3)
=
man
```
```sql
select job, substr(job,1,2), substr(job,5) from emp;
```

instr   
문자열 데이터 안에 특정 문자나 문자열이 어디에 포함되어 있는지를 알고자 할 때 사용
```sql
instr([대상 문자열 데이터(필수)],
      [위치를 찾으려는 부분 문자(필수)],
      [위치 찾기를 시작할 대상 문자열 데이터 위치(선택, 기본값 1)],
      [시작 위치에서 찾으려는 문자가 몇 번째인지 지정(선택, 기본값 1)])

select instr('hello, oracle!', 'l') as instr_1,
       instr('hello, oracle!', 'l', 5) as instr_2,
       instr('hello, oracle!', 'l', 2, 2) as instr_3 from dual;
    
instr_1 | instr_2 | instr_3 | 
      3 |      12 |       4 |
```
```sql
instr 함수로 사원 이름에 문자 S가 있는 행 구하기
select * from emp where instr(ename, 'S') > 0;

like 연산자로 사원 이름에 문자 S가 있는 행 구하기
select * from emp where ename like '%S%';
```
