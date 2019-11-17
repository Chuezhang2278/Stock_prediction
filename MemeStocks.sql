-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for memestock
CREATE DATABASE IF NOT EXISTS `memestock` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `memestock`;

-- Dumping structure for table memestock.users
CREATE TABLE IF NOT EXISTS `users` (
  `Fullname` varchar(256) NOT NULL,
  `SSN` int(9) NOT NULL,
  `Username` varchar(256) NOT NULL,
  `Pass` varchar(256) NOT NULL,
  `Email` varchar(256) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  PRIMARY KEY (`SSN`),
  UNIQUE KEY `email_unique` (`Email`),
  UNIQUE KEY `user_unique` (`Username`),
  CONSTRAINT `ssn_9_digits` CHECK (`SSN` > 99999999),
  CONSTRAINT `username_nospace` CHECK (`Username`  not like '% %'),
  CONSTRAINT `password_nospace` CHECK (`Pass`  not like '% %'),
  CONSTRAINT `minimum_length_pass_ck` CHECK (char_length(`Pass`) > 8),
  CONSTRAINT `email_valid` CHECK (`Email` like '%@%' and (`Email` like '%.com' or `Email` like '%.edu'))
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='-ssn primary key\r\n-email unique, email must contain ''@'' and ends with ''.com''\r\n-username unique, no space allowed\r\n-check ssn must be > 99999999 (9 -chars)\r\n-password > 8 chars, no space allowed';

-- Dumping data for table memestock.users: ~8 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`Fullname`, `SSN`, `Username`, `Pass`, `Email`, `Gender`) VALUES
	('Game', 123123123, 'JOHN', '123123123', '123123@123asd.com', 'Male'),
	('asdsadsadsa', 123456333, 'adsaasddsadsad', 'asdasdsadsadasd', '13412321321@masd.edu', 'Female'),
	('asdsadsadsadsadsa', 123456755, 'ASDLKASJDALSDASDALJ', 'LITTY_AF_DUDE', 'jma8774@behs.com', 'Male'),
	('John Doe', 123456789, 'JohnDope', '205042278', 'RealJohnDoe@gmail.com', 'Male'),
	('Jeemong', 123456917, 'jeemong1', 'animeweeb69', 'asd@gasl.com', 'Male'),
	('Jia Ming ma', 123467123, 'JEEMONG', 'lmaolmaolmao', 'asdsad@asd.com', 'Male'),
	('Jia Ming Ma ', 184912314, 'nospaceallowed', 'nospaceallowed', 'jma8774@bths.com', 'Male'),
	('Jia Ming Ma', 555444333, 'imcoolaf', 'thismustbelength9plus', 'asd@asd.com', 'Non-Binary');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
