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


-- Dumping database structure for stockmarket
CREATE DATABASE IF NOT EXISTS `stockmarket` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `stockmarket`;

-- Dumping structure for table stockmarket.portfolio
CREATE TABLE IF NOT EXISTS `portfolio` (
  `SSN` varchar(9) NOT NULL,
  `StockID` varchar(20) NOT NULL DEFAULT '0',
  `Volume` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`SSN`,`StockID`),
  KEY `portfolio_stockid_ref_stocks_stockid` (`StockID`),
  CONSTRAINT `portfolio_ssn_ref_users_ssn` FOREIGN KEY (`SSN`) REFERENCES `users` (`SSN`) ON UPDATE CASCADE,
  CONSTRAINT `portfolio_stockid_ref_stocks_stockid` FOREIGN KEY (`StockID`) REFERENCES `stocks` (`StockID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table stockmarket.portfolio: ~0 rows (approximately)
/*!40000 ALTER TABLE `portfolio` DISABLE KEYS */;
INSERT INTO `portfolio` (`SSN`, `StockID`, `Volume`) VALUES
	('123456789', 'AAPL', 1289);
/*!40000 ALTER TABLE `portfolio` ENABLE KEYS */;

-- Dumping structure for table stockmarket.stocks
CREATE TABLE IF NOT EXISTS `stocks` (
  `StockID` varchar(20) NOT NULL DEFAULT '',
  `Name` varchar(20) DEFAULT NULL,
  `LaunchDate` date DEFAULT NULL,
  PRIMARY KEY (`StockID`),
  UNIQUE KEY `name_unique` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table stockmarket.stocks: ~0 rows (approximately)
/*!40000 ALTER TABLE `stocks` DISABLE KEYS */;
INSERT INTO `stocks` (`StockID`, `Name`, `LaunchDate`) VALUES
	('AAPL', 'Apple', '2019-12-01');
/*!40000 ALTER TABLE `stocks` ENABLE KEYS */;

-- Dumping structure for table stockmarket.trades
CREATE TABLE IF NOT EXISTS `trades` (
  `SSN` varchar(9) NOT NULL,
  `TradeID` int(11) NOT NULL DEFAULT 0,
  `StockID` varchar(20) NOT NULL DEFAULT '0',
  `Volume` int(11) NOT NULL DEFAULT 0,
  `Date` date NOT NULL DEFAULT '0000-00-00',
  `PricePerShare` int(11) NOT NULL DEFAULT 0,
  `TotalCost` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`TradeID`,`SSN`),
  KEY `trades_ssn_ref_users_ssn` (`SSN`),
  KEY `trades_stockid_ref_stocks_stockid` (`StockID`),
  CONSTRAINT `trades_ssn_ref_users_ssn` FOREIGN KEY (`SSN`) REFERENCES `users` (`SSN`) ON UPDATE CASCADE,
  CONSTRAINT `trades_stockid_ref_stocks_stockid` FOREIGN KEY (`StockID`) REFERENCES `stocks` (`StockID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table stockmarket.trades: ~0 rows (approximately)
/*!40000 ALTER TABLE `trades` DISABLE KEYS */;
/*!40000 ALTER TABLE `trades` ENABLE KEYS */;

-- Dumping structure for table stockmarket.users
CREATE TABLE IF NOT EXISTS `users` (
  `SSN` varchar(9) NOT NULL DEFAULT '',
  `Fullname` varchar(256) NOT NULL,
  `Username` varchar(256) NOT NULL,
  `Balance` double NOT NULL DEFAULT 0,
  `Pass` varchar(256) NOT NULL,
  `Email` varchar(256) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  PRIMARY KEY (`SSN`),
  UNIQUE KEY `email_unique` (`Email`),
  UNIQUE KEY `user_unique` (`Username`),
  CONSTRAINT `username_nospace` CHECK (`Username`  not like '% %'),
  CONSTRAINT `password_nospace` CHECK (`Pass`  not like '% %'),
  CONSTRAINT `minimum_length_pass_ck` CHECK (char_length(`Pass`) > 8),
  CONSTRAINT `email_valid` CHECK (`Email` like '%@%' and (`Email` like '%.com' or `Email` like '%.edu')),
  CONSTRAINT `ssn_9_chars` CHECK (char_length(`SSN`) = 9),
  CONSTRAINT `SSN_numbers_only` CHECK (`SSN` regexp '^[0-9]+$')
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='-ssn primary key\r\n-email unique, email must contain ''@'' and ends with ''.com'' or ''.edu''\r\n-username unique, no space allowed\r\n-check ssn must be 9 digits\r\n-password > 8 chars, no space allowed';

-- Dumping data for table stockmarket.users: ~2 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`SSN`, `Fullname`, `Username`, `Balance`, `Pass`, `Email`, `Gender`) VALUES
	('123456789', 'Jia Ming Ma', 'jma8774', 21232, 'jma8774jma8774', 'jma8774@gmail.com', 'Male'),
	('987654321', 'TESTESTTEST', 'TESTESTTEST', 0, 'TESTESTTEST', 'TESTESTTEST@TESTESTTEST.com', 'Non-Binary');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
