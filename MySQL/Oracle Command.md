# Oracle Command

```sql
행 row
열 column
```

DESC   
dept 테이블 구성 살펴보기
```sql
DESC dept;
```

emp 테이블 전체 열 조회하기
```sql
SELECT * FROM emp;
```

DISTINCT   
열 중복 제거
```sql
SELECT DISTINCK job, deptno FROM emp;
```

ALL   
열 제거 없이 그대로 출력
```sql
SELECT ALL job, deptno FROM emp;
```

열에 연산식을 사용하여 출력하기
```sql
SELECT ename, sal, sal*12+comm, comm FROM emp;
```

AS   
annsal 이라는 별칭 지정
```sql
SELECT ename, sal, sal*12+comm AS annsal, comm FROM emp;
```

ORDER BY   
오름차순
```sql
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
```sql
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
```sql
and 연산자   
T T = T   
T F = F   
F T = F   
F F = F
```
or 연산자로 여러 개의 출력 조건 사용
```sql
select * from emp where deptno = 30 or job  'clerk';
```
```sql
or 연산자   
T T = T   
T F = T   
F T = T   
F F = F  
```
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
job이 manager, salesman, clerk 중 하나라면 모두 조회
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
↑높은 순서  
↓낮은 순서
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

replace   
특정 문자열 데이터에 포함된 문자를 다른 문자로 대체할 경우 사용
```sql
replace([문자열 데이터 또는 열 이름(필수)], [찾는 문자(필수)], [대체할 문자(선택)])
```
```sql
select '010-1234-5678' as replace_before,
      replace('010-1234-5678','-', ' ') as replace_1,
      replace('010-1234-5678', '-') as replace_2 
      from dual;

 replace_before|   replace_1   |  replace_2
 010-1234-5678 | 010 1234 5678 | 01012345678
```

lpad, rpad   
데이터의 빈 공간을 특정 문자로 채우는 함수
```sql
select 'Oracle', lpad('Oracle', 10, '#') as lpad_1,
                 rpad('Oracle', 10, '*') as rpad_1,
                 lpad('Oracle', 10) as lpad_2,
                 rpad('Oracle', 10) as rpad_2, 
from dual;

| Oracle   | ####Oracle | Oracle**** |    Oracle | Oracle    |
```

concat   
두 문자열 데이터를 합치는 함수
```sql
select concat(empno, ename),
       concat(empno, concat(' : ', ename))
from emp where ename = 'SCOTT';

7788SCOTT | 7788 : SCOTT

concat = ||
```

trim, ltrim, rtrim   
문자열 데이터 내에서 특정 문자를 지우기 위해 사용되는 함수
```sql
trim([삭제 옵션(선택)] [삭제할 문자(선택)] from [원본 문자열 데이터(필수)])

삭제 옵션 :
leading  = 왼쪽에 있는 글자를 지움
trailing = 오른쪽에 있는 글자를 지움
both     = 양쪽에 있는 글자를 지움
```
```sql
공백 제거
select '[' || trim(' --Oracle-- ') || ']' as trim,
       '[' || trim(leading from ' --Oracle-- ') || ']' as trim_leading,
       '[' || trim(trailing from ' --Oracle-- ') || ']' as trim_trailing,
       '[' || trim(both from ' --Oracle-- ') || ']' as trim_both
from dual;

 trim       | trim_leading | trim_trailing | trim_both  | 
[--Oracle--]|[--Oracle-- ] | [ --Oracle--] |[--Oracle--]|
```
```sql
ltrim([원본 문자열 데이터(필수)], [삭제할 문자 집합(선택)])
rtrim([원본 문자열 데이터(필수)], [삭제할 문자 집합(선택)])
```

round   
지정된 숫자의 특정 위치에서 반올림한 값을 반환
```sql
round([숫자(필수)], [반올림 위치(선택)])
```
```sql
select round(1234.5678) as round,               -- 1235
       round(1234.5678, 0) as round_0,          -- 1235
       round(1234.5678, 1) as round_1,          -- 1234.6
       round(1234.5678, 2) as round_2,          -- 1234.57
       round(1234.5678, -1) as round_minus1,    -- 1230
       round(1234.5678, -2) as round_minus2     -- 1200
from dual;
```

trunc   
지정된 자리에서 숫자를 버림 처리하는 함수
```sql
trunc([숫자(필수)], [버림 위치(선택)])
```
```sql
select trunc(1234.5678) as trunc,
       trunc(1234.5678, 0) as trunc_0,          -- 1234
       trunc(1234.5678, 1) as trunc_1,          -- 1234.5
       trunc(1234.5678, 2) as trunc_2,          -- 1234.56
       trunc(1234.5678, -1) as trunc_minus1,    -- 1230
       trunc(1234.5678, -2) as trunc_minus2,    -- 1200
from dual;
```

ceil, floor   
입력된 숫자와 가까운 큰 정수, 작은 정수를 반환하는 함수
```sql
ceil([숫자(필수)])
floor([숫자[필수]])
```
```sql
select ceil(3.14),      -- 4
       floor(3.14),     -- 3
       ceil(-3.14),     -- -3
       flooe(-3.14)     -- -4
from dual;
```

mod   
나머지 값 구하는 함수
```sql
mod([나눗셈 될 숫자(필수)], [나눌 숫자(필수)])
```
```sql
select mod(15,6), -- 3
       mod(10,2), -- 0
       mod(11,2), -- 1
from dual;
```

sysdate   
가장 대표 날자 함수
```sql
select sysdate as now from dual;    -- 2023-04-24 오전 02:34:17
```

형 변환 함수
```sql
to_char   = 숫자 또는 날짜 데이터를 문자 데이터로 변환
to_number = 문자 데이터를 숫자 데이터로 변환 
to_date   = 문자 데이터를 날짜 데이터로 변환

숫자 ↔ 문자 ↔ 날짜
문자를 중심으로 데이터의 변환이 이루어짐.
```

to_char
```sql
to_char([날짜데이터(필수)], '[출력되길 원하는 문자 형태(필수)]')
```
```sql
select to_char(sysdate, 'YYYY/MM/DD HH24:MI:SS') as 현재날짜시간 from dual;   -- 2023/04/24/ 02:34:17
```
날짜 형식
```sql
CC          = 세기 
YYYY, RRRR  = 연(4자리 숫자)
YY, RR      = 연(2자리 숫자)
MM          = 월(2자리 숫자)
MON         = 월(언어별 월 이름 약자)
MONTH       = 월(언어별 월 이름 전체)
DD          = 일(2자리 숫자)
DDD         = 1년 중 며칠 (1~366)
DY          = 요일(언어별 요일 이름 약자)
DAY         = 요일(언어별 요일 이름 전체)
W           = 1년 중 몇 번째 주 (1~53)
```
```sql
select to_char(sysdate, 'MON', 'nls_date_language = korean') as mon_kr from dual;

언어별 선택
nls_date_language = korean
nls_date_language = japanese
nls_date_language = english
```

시간 형식
```sql
HH24              = 24시간으로 표현한 시간
HH, HH12          = 12시간으로 표현한 시간
MI                = 분
SS                = 초
AM, PM, A,M, P.M  = 오전, 오후 표시
```

숫자 데이터 형식
```sql
9  = 숫자의 한 자리를 의미함(빈 자리를 채우지 않음)
0  = 빈 자리를 0으로 채움
$  = 달러($) 표시를 붙여서 출력
L  = L(Locale) 지역 화폐 단위 기호를 붙여서 출력
.  = 소수점을 표시
,  = 천 단위의 구분 기호를 표시
```

to_number   
문자 데이터를 숫자 데이터로 변환
```sql
to_number('[문자열 데이터(필수)]' ,'[인식될 숫자형태(필수)]')
```
```sql
select to_number('1,300', '999,999') - to_number('1,500', '999,999') from dual; -- -200
```

to_date   
```sql
to_date('[문자열 데이터(필수)]', '[인식될 날짜형태(필수)]')
```
```sql
select to_date('2023-04-24', 'YYYY-MM-DD'), 
       to_date('20230424', 'YYYY-MM-DD') from dual; -- 2023/04/24
```
nvl   
```sql
nvl([null인지 여부를 검사할 데이터 또는 열(필수)], [앞의 데이터가 null일 경우 반환할 데이터(필수)])
```
```sql
select comm, nvl(comm, 0), sal+nvl(comm, 0) from emp;

comm | nvl(comm, 0) | sal+nvl(comm, 0) 
  200|           200|             350 
     |             0|               0
  500|           500|            1000
```

nvl2   
```sql
nvl2([null인지 여부를 검사할 데이터 또는 열(필수)], 
     [앞 데이터가 null이 아닐 경우 반환할 데이터 또는 계산식(필수)], 
     [앞 데이터가 null일 경우 반환할 데이터 또는 계산식(필수)])
```
```sql
select empno, ename, comm, nvl2(comm, 'O', 'X') from emp;
```

decode   
if 조건문
```sql
decode([검사 대상이 될 열 또는 데이터, 연산이나 함수의 결과], 
       [조건 1], [조건1이 만족할 때 반환할 결과],
       [조건 2], [조건2가 만족할 때 반환할 결과],
       …
       [조건 n], [조건n이 만족할 떄 반환할 결과],
       [위 조건1~n과 일치한 경우가 없을 때 반환할 결과])
```
```sql
select empno, job, sal, decode(job, 
                                    'manager', sal*1.1, 
                                    'salesman', sal*1.05, 
                                    sal*1.03) 
as upsal
```

case   
decode처럼 특정 조건에 따라 반환할 데이터를 설정할 때 사용한다.   
하지만 decode와 달리 case문은 각 조건에 사용하는 데이터가 서로 상관없어도 된다.    
또 기준 데이터 값이 같은 데이터 외에 다양한 조건을 사용할 수 있다.
```sql
case [검사 대상이 될 열 또는 데이터, 연산이나 함수의 결과(선택)]
      when [조건1] then [조건1의 결과 값이 true일 때, 반환할 결과]
      when [조건2] then [조건2의 결과 값이 true일 때, 반환할 결과]
      …
      when [조건n] then [조건n의 결과 값이 true일 때, 반환할 결과]
      else [위 조건1~n과 일치하는 경우가 없을 떄 반환할 결과]
end
```
```sql
select empno, ename, job, sal, case job
                                    when 'manager' then sal*1.1
                                    when 'salesman' then sal*1.05
                                    else sal*1.03
                                    end as upsal
from emp;
```

다중행 함수
```sql
sum   = 지정한 데이터의 합 반환
count = 지정한 데이터의 개수 반환
max   = 지정한 데이터 중 최댓값 반환
min   = 지정한 데이터 중 최솟값 반환
avg   = 지정한 데이터의 평균값 반환

sum([distinct, all 중 선택하거나 지정하지 않음(선택)]
    [**(sum=합계)를 구할 열이나 연산자, 함수를 사용한 데이터(필수)])
count, max min, avg 동일
distinct = 중복 제거
```

group by   
그룹화   
순서도
```sql
select   [조회할 열1 이름, [열2 이름], ...]
from     [조회할 테이블 이름]
where    [조회할 행을 선별하는 조건식]
group by [그룹화할 열을 지정(여러 개 지정 가능)]
order by [정렬하려는 열 지정]
```
```sql
부서(deptno)별 평균 급여(sal) 출력
select avg(sal), deptno from emp group by deptno;

★선택한 column은 반드시 group by에 모두 포함시켜야 한다.
ex)
select deptno, ename from emp group by deptno;        -- X
select deptno, ename from emp group by deptno, ename; -- O
```

having   
순서도
```sql
select   [조회할 열1 이름, [열2 이름], ...]
from     [조회할 테이블 이름]
where    [조회할 행을 선별하는 조건식]
group by [그룹화할 열을 지정(여러 개 지정 가능)]
having   [출력 그룹을 제한하는 조건식]
order by [정렬하려는 열 지정]
```
```sql
where 안쓰고 having만 쓴 경우
select deptno, job, avg(sal) from emp 
      group by deptno, job 
            having avg(sal) >= 2000 
      order by deptno, job;

where, having 둘 다 쓴 경우
select deptno, job, avg(sal) from emp 
            where sal <= 3000
      group by deptno, job 
            having avg(sal) >= 2000 
      order by deptno, job;
```

listagg   
그룹에 속해 이쓴 데이터를 가로로 나열할 때 사용
```sql
select ??? 
      listagg([나열할 열(필수)], [각 데이터를 구분하는 구분자(선택)]) 
      within group(order by 나열할 열의 정렬 기준 열(선택)) 
from ??? where ???
```
```sql
select deptno, 
      listagg(ename, ', ') 
      within group(order by sal desc) as enames 
from emp group by deptno;
```

join   
2개 이상의 테이블을 조회할 때 column의 이름이 겹칠 때 설정하는 것
```sql
selct * from emp, dept where emp.deptno = dept.deptno order by empno;

emp.deptno = dept.deptno
```

테이블 별칭 설정
```sql
from 테이블이름1 별칭1, 테이블이름2 별칭2, 테이블이름 별칭3, ...

select * from emp e, dept d where e.deptno = d.deptno order by empno;

e.deptno = d.deptno
```

서브쿼리   
필요한 데이터를 추가로 조회하기 위할 때 사용
```sql
select ename, sal from emp where sal > ( select sal from emp where ename = 'jones');
```
```sql
서브쿼리의 특징
1. 서브쿼리는 연산자와 같은 비교 또는 조회 대상의 오른쪽에 놓이며 괄호()로 묶어서 사용한다.
2. 특수한 몇몇 경우를 제외한 대부분의 서브쿼리에서는 order by절을 사용할 수 없다.
3. 서브쿼리의 select절에 명시한 열은 메인쿼리의 비교 대상과 같은 자료형과 같은 개수로 지정해야 한다. 즉 메인쿼리의 비교 대상 데이터가 하나라면 서브쿼리의 select절 역시 같은 자료형인 열을 하나 지정해야 한다.
4. 서브쿼리에 있는 select문의 결과 행 수는 함께 사용하는 메인쿼리의 연산자 종류와 호환 가능해야 한다. 예를 들어 메인쿼리에 사용한 연산자가 단 하나의 데이터로만 연산이 가능한 연산자라면 서브쿼리의 결과 행 수는 반드시 하나여야 한다.
```

단일행 연산자
```sql
>   = 초과
>=  = 이상
=   = 같음
<=  = 이하
<   = 미만
<>  = 같지 않음
^=  = 같지 않음
!=  = 같지 않음
```

any, some   
서브쿼리에서의 in 역할   
```sql
서브쿼리 결과 값 중 하나라도 참이면 true
select * from emp where sal = any (select max(sal) from emp group by deptno);
select * from emp where sal = some (select max(sal) from emp group by deptno);
```

all   
any, some과는 달리 모든 결과가 참이어야 true
```sql
select * from emp where sal = all (select max(sal) from emp group by deptno);
```

exists   
서브쿼리에 결과 값이 하나 이상 존재하면 모두 true,   
하나라도 없으면 false
```sql
select * from emp where exists (select max(sal) from emp group by deptno);

만약 false 라면 아무 값도 출력되지 않는다.
```

다중열 서브쿼리
```sql
select * from emp where (deptno ,sal) in (select deptno, max(sal) from emp group by deptno);
```

from절에 사용하는 서브쿼리
```sql
select ~~~
```

select절에 사용하는 서브쿼리
```sql
select ~~~
```

테이블 생성
```sql
create table [테이블 이름];
```

기존 테이블 복사해서 생성
```sql
dept 테이블 정보를 복사해서 dept_temp 테이블에 생성 
create table dept_temp as select * from dept;
```

테이블 지우기
```sql
drop table [테이블 이름];
```

insert   
테이블에 데이터 추가
```sql
insert into 테이블이름 [열1,     열2,    열3, ...,]
               values [데이터1, 데이터2, 데이터3, ...,];
```

update
```sql
update [변경할 테이블] set [변경할 열1]=[데이터], [변경할 열2]=[데이터], ... [where 데이터를 변경할 대상 행을 선별하기 위한 조건];
```
```sql
update dept_temp1 set loc = 'seoul';
```

rollback   
수정한 내용을 되돌리고 싶을 때
```sql
rollback;
```

delete   
테이블에 있는 데이터 삭제
```sql
delete [from] [테이블 이름] [where 삭제할 대상 행을 선별하기 위한 조건식];
```
```sql
delete from emp_temp1 where job='manager';
```

create
```sql
create table emp_ddl(
      empno       number(4),
      ename       varchar2(10),
      job         varchar2(9),
      mgr         number(4),
      hiredate    date,
      sal         number(7,2),
      comm        number(7,2),
      deptno      number(2)
);
```

column alter   
이미 만들어진 테이블에 column을 수정 때 이용하는 명령어
```sql
add
alter table emp add hp varchar(20);       -- hp column 새롭게 추가

rename
alter table emp rename column hp to tel;  -- hp column 이름이 tel로 변경

modify
alter table emp modify empno numver(5);   -- empno column 속성이 number(4)에서 number(5)로 변경

drop
alter table emp drop column tel;          -- tel column 이 삭제
```

table alter   
테이블 수정
```sql
rename
rename emp to emp_rename;                 -- emp 테이블 이름을 emp_rename 으로 변경

truncate
truncate table emp_rename;                -- emp_rename 테이블 전체 데이터 삭제 (rollback 불가)

drop
drop table emp_rename;                    -- emp_rename 테이블 삭제
```

view   
서브쿼리와 비슷하지만 보안성이 가미된.
```sql
select * from vw_emp20;

view 설정을 해놓으면 vm_emp20 이렇게만 입력해도 
select * from (empno, ename, job, deptno from emp where deptno = 20); 
해당 select절이 입력된 것처럼 행동한다.
```
```sql
system 계정 접속.
grant create view to scott;

scott 계정 접속.
create view vm_emp20 as (select empno, ename, job, deptno from emp where deptno = 20);
vm_emp20 이름의 view 생성 완료.

view 내용 확인하기
select view_name, text_length, text from user_views;

view 지우기
drop view vw_emp20;
```


