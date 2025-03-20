-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2023 at 08:26 AM
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
-- Database: `freelancer`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL,
  `schedule_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `adate` varchar(30) NOT NULL,
  `atime` varchar(30) NOT NULL,
  `reason` varchar(1000) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`booking_id`, `schedule_id`, `user_id`, `adate`, `atime`, `reason`, `status`) VALUES
(1, 1, 1, '2023-04-24', '2023-04-24', 'backpain', 'paid'),
(2, 2, 2, '2023-04-25', '2023-04-25', 'fever', 'pending'),
(3, 5, 3, '2023-04-28', '2023-04-28', 'headache', 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `chat` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`chat_id`, `sender_id`, `receiver_id`, `chat`) VALUES
(1, 5, 2, 'doctor,severe backpain..please give a remedy'),
(2, 2, 5, 'I suggest a medicine..use this daily before sleep'),
(3, 2, 5, 'metahdopsis - for 1 week');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `department_id` int(11) NOT NULL,
  `department` varchar(50) NOT NULL,
  `description` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`department_id`, `department`, `description`) VALUES
(1, 'physician', 'treat as a general for all diseases and injuries'),
(2, 'orthology', 'treat for muscles joints etc'),
(3, 'neurology', 'treat for neurons,spinal cors etc'),
(4, 'Homeopathic', 'as looking lifestyle and treat the disease'),
(5, 'Gynacologist', 'treat for pregannacy issuses'),
(6, 'pediatrician', 'treat for babies');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `doctor_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `dept_id` int(11) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `consulting_place` varchar(30) NOT NULL,
  `consulting_time` varchar(30) NOT NULL,
  `certificate` varchar(1000) NOT NULL,
  `status` varchar(30) NOT NULL,
  `date` varchar(30) NOT NULL,
  `image` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`doctor_id`, `login_id`, `dept_id`, `fname`, `lname`, `place`, `phone`, `email`, `gender`, `consulting_place`, `consulting_time`, `certificate`, `status`, `date`, `image`) VALUES
(1, 2, 1, 'Navas', 'c a', 'aluva', '975645778', 'navas@gmail.com', 'Male', 'aluva', '09:00', 'static/de2ab6fe-ff73-4bde-94f7-503b68953fc8MCA.pdf', 'active', '2023-04-24', 'static/026a4795-1cc3-4b3b-a721-274cd98eccc2MCA.pdf'),
(2, 3, 2, 'Nizar', 'c h', 'kaloor', '9553366787', 'nizar@gmail.com', 'Male', 'kaloor', '13:00', 'static/e234ab11-4d56-4dde-bcba-0571b35b9c74game theory.pdf', 'active', '2023-04-24', 'static/cf9cf37c-62e5-4d31-99ab-fdf43b5f65dcgame theory.pdf'),
(3, 4, 3, 'salam', 'n s', 'ernakulam', '953356678', 'salam@gmail.com', 'Male', 'ernakulam', '10:00', 'static/ab99a1a2-04bf-4d88-8717-89e9acd5ada5game theory.pdf', 'inactive', '2023-04-24', 'static/ca59a8ef-ea01-47e3-8532-c11251ced615game theory.pdf'),
(4, 7, 4, 'Sahala', 'n a', 'aluva', '96434678', 'sahu@gmail.com', 'Female', 'aluva', '09:00', 'static/1f449785-732c-4a50-af50-beb63df4845aproject123.pdf', 'active', '2023-04-24', 'static/97da726a-7bcd-4e1e-9e25-59bad0c16688project123.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `feedback` varchar(1000) NOT NULL,
  `date` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feedback_id`, `user_id`, `feedback`, `date`) VALUES
(1, 1, 'good service', '2023-04-24'),
(2, 3, 'very fast and secure..happy with it', '2023-04-24');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `usertype` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`login_id`, `username`, `password`, `usertype`) VALUES
(1, 'admin', 'admin', 'admin'),
(2, 'navas', 'navas', 'doctor'),
(3, 'nizar', 'nizar', 'doctor'),
(4, 'salam', 'salam', 'reject'),
(5, 'rasheeda', 'rasheeda', 'user'),
(6, 'rahmath', 'rahmath', 'user'),
(7, 'sahala', 'sahala', 'doctor'),
(8, 'sali', 'sali', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `date` varchar(30) NOT NULL,
  `amount` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `booking_id`, `date`, `amount`) VALUES
(1, 1, '2023-04-24', '250'),
(2, 3, '2023-04-24', '250');

-- --------------------------------------------------------

--
-- Table structure for table `salary`
--

CREATE TABLE `salary` (
  `salary_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `amount` varchar(1000) NOT NULL,
  `date` varchar(30) NOT NULL,
  `month` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `salary`
--

INSERT INTO `salary` (`salary_id`, `doctor_id`, `amount`, `date`, `month`) VALUES
(1, 1, '50000', '2023-04-24', '2023-04');

-- --------------------------------------------------------

--
-- Table structure for table `schedule`
--

CREATE TABLE `schedule` (
  `schedule_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `available_date` varchar(30) NOT NULL,
  `starting_time` varchar(30) NOT NULL,
  `ending_time` varchar(30) NOT NULL,
  `interval` varchar(30) NOT NULL,
  `fees` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `schedule`
--

INSERT INTO `schedule` (`schedule_id`, `doctor_id`, `available_date`, `starting_time`, `ending_time`, `interval`, `fees`) VALUES
(1, 1, '2023-04-24', '09:00', '12:00', '15', '250'),
(2, 1, '2023-04-25', '09:00', '12:00', '15', '250'),
(3, 1, '2023-04-26', '09:00', '12:00', '15', '250'),
(4, 2, '2023-04-27', '13:00', '16:00', '20', '250'),
(5, 2, '2023-04-28', '13:00', '16:00', '20', '250');

-- --------------------------------------------------------

--
-- Table structure for table `treatment`
--

CREATE TABLE `treatment` (
  `treatment_id` int(11) NOT NULL,
  `treatment` varchar(1000) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `date` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `treatment`
--

INSERT INTO `treatment` (`treatment_id`, `treatment`, `booking_id`, `date`) VALUES
(1, 'take rest', 1, '2023-04-24'),
(2, 'take parecetamol in 3 times in aday', 3, '2023-04-24');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `login_id` int(11) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `login_id`, `fname`, `lname`, `place`, `phone`, `email`) VALUES
(1, 5, 'Rasheeda', 't v', 'paravoor', '745367878', 'rashee@gmail.com'),
(2, 6, 'Rahmath', 'n p', 'kothamangalam', '96535678', 'rahu@gmail.com'),
(3, 8, 'salih', 'b k', 'perumbavoor', '74566778', 'sali@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`booking_id`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`chat_id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`department_id`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`doctor_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `salary`
--
ALTER TABLE `salary`
  ADD PRIMARY KEY (`salary_id`);

--
-- Indexes for table `schedule`
--
ALTER TABLE `schedule`
  ADD PRIMARY KEY (`schedule_id`);

--
-- Indexes for table `treatment`
--
ALTER TABLE `treatment`
  ADD PRIMARY KEY (`treatment_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `chat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `department_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `doctor`
--
ALTER TABLE `doctor`
  MODIFY `doctor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `salary`
--
ALTER TABLE `salary`
  MODIFY `salary_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `schedule`
--
ALTER TABLE `schedule`
  MODIFY `schedule_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `treatment`
--
ALTER TABLE `treatment`
  MODIFY `treatment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
