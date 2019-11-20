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

-- Dumping structure for table memestock.portfolio
CREATE TABLE IF NOT EXISTS `portfolio` (
  `SSN` varchar(9) NOT NULL,
  `StockID` int(11) NOT NULL DEFAULT 0,
  `Volumn` int(11) NOT NULL DEFAULT 0,
  `TotalValue` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`SSN`,`StockID`),
  KEY `portfolio_stockid_ref_stocksid` (`StockID`),
  CONSTRAINT `portfolio_ssn_ref_users_ssn` FOREIGN KEY (`SSN`) REFERENCES `users` (`SSN`),
  CONSTRAINT `portfolio_stockid_ref_stocksid` FOREIGN KEY (`StockID`) REFERENCES `stocks` (`StockID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table memestock.portfolio: ~2 rows (approximately)
/*!40000 ALTER TABLE `portfolio` DISABLE KEYS */;
INSERT INTO `portfolio` (`SSN`, `StockID`, `Volumn`, `TotalValue`) VALUES
	('123456789', 1010, 5, 1500),
	('123456789', 1011, 10, 20000);
/*!40000 ALTER TABLE `portfolio` ENABLE KEYS */;

-- Dumping structure for table memestock.stocks
CREATE TABLE IF NOT EXISTS `stocks` (
  `StockID` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Author` varchar(20) NOT NULL DEFAULT 'N/A',
  `LaunchDate` date NOT NULL,
  PRIMARY KEY (`StockID`),
  UNIQUE KEY `name_unique` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table memestock.stocks: ~2 rows (approximately)
/*!40000 ALTER TABLE `stocks` DISABLE KEYS */;
INSERT INTO `stocks` (`StockID`, `Name`, `Author`, `LaunchDate`) VALUES
	(1010, 'Doge', 'Homestar Runner', '2005-06-24'),
	(1011, 'Kappa', 'Josh DeSeno', '2010-06-17');
/*!40000 ALTER TABLE `stocks` ENABLE KEYS */;

-- Dumping structure for table memestock.stocks_price_history
CREATE TABLE IF NOT EXISTS `stocks_price_history` (
  `StockID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Open` int(11) NOT NULL DEFAULT 0,
  `Close` int(11) NOT NULL DEFAULT 0,
  `High` int(11) NOT NULL DEFAULT 0,
  `Low` int(11) NOT NULL DEFAULT 0,
  `VolumnsTraded` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`StockID`,`Date`),
  CONSTRAINT `stockid_in_history_ref_stocks` FOREIGN KEY (`StockID`) REFERENCES `stocks` (`StockID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table memestock.stocks_price_history: ~4 rows (approximately)
/*!40000 ALTER TABLE `stocks_price_history` DISABLE KEYS */;
INSERT INTO `stocks_price_history` (`StockID`, `Date`, `Open`, `Close`, `High`, `Low`, `VolumnsTraded`) VALUES
	(1010, '2019-10-17', 200, 210, 250, 188, 10020310),
	(1010, '2019-10-18', 240, 300, 340, 220, 44444444),
	(1011, '2019-10-17', 420, 690, 750, 333, 83741927),
	(1011, '2019-10-18', 720, 1473, 1887, 690, 341937861);
/*!40000 ALTER TABLE `stocks_price_history` ENABLE KEYS */;

-- Dumping structure for table memestock.trades
CREATE TABLE IF NOT EXISTS `trades` (
  `SSN` varchar(9) NOT NULL,
  `TradeID` int(11) NOT NULL DEFAULT 0,
  `StockID` int(11) NOT NULL DEFAULT 0,
  `Volumn` int(11) NOT NULL DEFAULT 0,
  `Date` date NOT NULL DEFAULT '0000-00-00',
  `PricePerShare` int(11) NOT NULL DEFAULT 0,
  `TotalCost` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`TradeID`,`SSN`),
  KEY `trades_ssn_ref_users_ssn` (`SSN`),
  KEY `trades_stockid_ref_stocks_stockid` (`StockID`),
  CONSTRAINT `trades_ssn_ref_users_ssn` FOREIGN KEY (`SSN`) REFERENCES `users` (`SSN`),
  CONSTRAINT `trades_stockid_ref_stocks_stockid` FOREIGN KEY (`StockID`) REFERENCES `stocks` (`StockID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table memestock.trades: ~2 rows (approximately)
/*!40000 ALTER TABLE `trades` DISABLE KEYS */;
INSERT INTO `trades` (`SSN`, `TradeID`, `StockID`, `Volumn`, `Date`, `PricePerShare`, `TotalCost`) VALUES
	('123456789', 1, 1010, 10, '2019-10-17', 205, 1025),
	('123456789', 2, 1011, 5, '2019-10-17', 750, 3750);
/*!40000 ALTER TABLE `trades` ENABLE KEYS */;

-- Dumping structure for table memestock.users
CREATE TABLE IF NOT EXISTS `users` (
  `SSN` varchar(9) NOT NULL DEFAULT '',
  `Fullname` varchar(256) NOT NULL,
  `Username` varchar(256) NOT NULL,
  `Balance` int(11) NOT NULL DEFAULT 0,
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

-- Dumping data for table memestock.users: ~1 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`SSN`, `Fullname`, `Username`, `Balance`, `Pass`, `Email`, `Gender`) VALUES
	('123456789', 'Jia Ming Ma', 'jma8774', 21500, 'jma8774jma8774', 'jma8774@gmail.com', 'Male');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
users