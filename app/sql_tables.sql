

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";




use students;

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `id` int(10) NOT NULL,
  `firstName` varchar(23) NOT NULL,
  `lastName` varchar(23) NOT NULL,
  `clas` varchar(23) NOT NULL,
  `nationality` varchar(20) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

