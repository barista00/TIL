SHOW COLUMNS FROM users;
SELECT * FROM users;
DROP TABLE users;
-- 문제1 필드 정보를 참고해서 테이블 users 를 생성하시오.
CREATE TABLE IF NOT EXISTS users(
	userId INT AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    city VARCHAR(100), 
    country VARCHAR(100),
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NULL,
    PRIMARY KEY (userId)
);

-- 문제2 레코드 정보를 보고 테이블 users 에 데이터를 입력하시오.
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo', 'Jeong', '1000-01-01', '', '', 'beemo@hphk.kr'),
	('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', ''),	
	('Dami', 'Kim',	'1995-04-09', 'Seoul', 'Korea', ''),	
	('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', '');

-- 문제3 테이블 users 에 임의로 데이터 5개를 입력하시오.
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('', '', '1000-01-01', '', '', ''),
    ('', '', '1000-01-01', '', '', ''),
    ('', '', '1000-01-01', '', '', ''),
    ('', '', '1000-01-01', '', '', ''),
    ('', '', '1000-01-01', '', '', '');

-- 문제4 2번 레코드의 first_name, last_name, birthday 필드 값을 자신의 이름, 성, 생년월일로 변경하시오.
UPDATE
	users
SET
	first_name = 'BS',
    last_name = 'MUN',
    birthday = '1997-06-27'
WHERE
	userId = 2;

-- 문제5 테이블 users 에서 country 필드가 NULL 인 모드 레코드의 country 필드 값을 Korea 로 변경하시오.
set sql_safe_updates=0;
UPDATE
	users
SET
	country = 'Korea';

-- 문제6 테이블 users 에서 first_name 필드가 Beemo 인 레코드를 삭제하시오.
DELETE FROM
	users
WHERE
	first_name = 'Beemo';

-- 문제7 테이블 users 에서 first_name 필드가 Kwangsoo, last_name 필드가 Lee 인 레코드를 삭제하시오.
DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo' AND
    last_name = 'Lee';

-- 문제8 테이블 users 에서 가장 나중에 생성한 레코드 1개를 삭제하시오.
DELETE FROM
	users
ORDER BY
	created_at DESC
LIMIT 1;
    