-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Sep 21, 2023 at 01:46 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cv`
--

-- --------------------------------------------------------

--
-- Table structure for table `info`
--

CREATE TABLE `info` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `resume_description` text DEFAULT NULL,
  `job_title` varchar(255) DEFAULT NULL,
  `work_citytown` varchar(255) DEFAULT NULL,
  `employer` varchar(255) DEFAULT NULL,
  `work_startdate` date DEFAULT NULL,
  `work_enddate` date DEFAULT NULL,
  `work_description` text DEFAULT NULL,
  `degree` varchar(255) DEFAULT NULL,
  `education_citytown` varchar(255) DEFAULT NULL,
  `school` varchar(255) DEFAULT NULL,
  `education_startdate` date DEFAULT NULL,
  `education_enddate` date DEFAULT NULL,
  `education_description` text DEFAULT NULL,
  `hobby` varchar(255) DEFAULT NULL,
  `skills` varchar(255) DEFAULT NULL,
  `profilepicture` longblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `info`
--

INSERT INTO `info` (`id`, `user_id`, `first_name`, `last_name`, `email`, `address`, `zip_code`, `phone_number`, `city`, `resume_description`, `job_title`, `work_citytown`, `employer`, `work_startdate`, `work_enddate`, `work_description`, `degree`, `education_citytown`, `school`, `education_startdate`, `education_enddate`, `education_description`, `hobby`, `skills`, `profilepicture`) VALUES
(25, 16, 'Stefan', 'Stankovic', 'sstankovic0111@gmail.com', 'Nikoletine Bursaca 15', '18000', '0692297279', 'Nis, Serbia', '', '', '', '', '0000-00-00', '0000-00-00', '', '', '', '', '0000-00-00', '0000-00-00', '', '', '', 0x7374617469632f75706c6f6164732f6d617273682e6a7067),
(26, 17, 'Andrija', 'Tesovic', 'andrija.t2010@gmail.com', 'Njegoseva 47', '18230', '0668085396', 'Sokobanja', 'Volim zene ali one malo manje volemene', 'fadsfdsf', 'dasdasdas', 'ffasfsdf', '0000-00-00', '0000-00-00', 'Mnogo dobro spasavam', 'Bachelors', 'Nis, Serbia', 'ATVSS', '0000-00-00', '0000-00-00', 'Sve samnaucio', 'Producer', 'Html , Css, Js, Python', 0x7374617469632f75706c6f6164732f6d617273682e6a7067),
(27, 16, 'Stefan', 'Stankovic', 'sstankovic0111@gmail.com', 'Nikoletine Bursaca 15', '18000', '0692297279', 'Nis, Serbia', '', '', '', '', '0000-00-00', '0000-00-00', '', '', '', '', '0000-00-00', '0000-00-00', '', '', '', 0x7374617469632f75706c6f6164732f6d617273682e6a7067);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(16, 'stefan ', 'pbkdf2:sha256:600000$qwkZauckHaSNMxlY$cd99676a5c6adfbc69ce37b522edf347ed4d351abf46b51d098a4525153c5c36'),
(17, 'tesha', 'pbkdf2:sha256:600000$tqcf1on9EURpvdkb$06aee7daf6d6e9774fdd38888cbd409d63683e920976133c7b86687b8a9456ff');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `info`
--
ALTER TABLE `info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `info`
--
ALTER TABLE `info`
  ADD CONSTRAINT `info_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
