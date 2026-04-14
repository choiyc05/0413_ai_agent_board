CREATE TABLE `board`.`list` (
	`no` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'no',
	`name` TEXT COMMENT '작성자, 이름',
	`title` TEXT COMMENT '제목',
	`content` TEXT COMMENT '내용',
	`delYn` TEXT COMMENT '삭제 여부, 0:기본값,  1:삭제 ',
	`regDate` DATETIME DEFAULT CURRENT_TIMESTAMP,
	`modDate` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='프롬프트로 게시판 기능 만들어 보기.';
  
