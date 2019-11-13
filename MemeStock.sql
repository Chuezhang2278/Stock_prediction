-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.7-MariaDB - mariadb.org binary distribution
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
  `Fullname` varchar(255) DEFAULT NULL,
  `SSN` int(9) DEFAULT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Pass` varchar(15) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table memestock.users: ~7 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`Fullname`, `SSN`, `Username`, `Pass`, `Email`) VALUES
	('John Doe', 123456789, 'JohnDope', '205042278', 'RealJohnDoe@gmail.com'),
	('Cook', 987654321, 'John', '1', 'cook@gmail.com'),
	('a', 123456789, 'a', 'b', 'RealJohnDoe@gmail.com'),
	('Cook', 987654321, 'John', '1', 'cook@gmail.com'),
	('a', 123456789, 'a', 'b', 'RealJohnDoe@gmail.com'),
	('Chue Zhang', 123456789, 'C', 'Z', 'a@gmail.com'),
	('C', 233981871, 'blyat', 'cyka', 'as@gmail.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
