-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 28, 2021 at 02:35 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `telegramsmartassistant`
--

-- --------------------------------------------------------

--
-- Table structure for table `allchatslist`
--

CREATE TABLE `allchatslist` (
  `id` int(11) NOT NULL,
  `chatName` varchar(100) NOT NULL,
  `chatId` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `chatforwardinfo`
--

CREATE TABLE `chatforwardinfo` (
  `id` int(11) NOT NULL,
  `originChatId` bigint(20) NOT NULL,
  `destinationChatId` bigint(20) NOT NULL,
  `filterByWord` varchar(200) NOT NULL DEFAULT '[]',
  `autoBuyParserLink` varchar(300) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `chatmessageids`
--

CREATE TABLE `chatmessageids` (
  `id` int(11) NOT NULL,
  `originChatId` bigint(20) NOT NULL,
  `destinationChatId` bigint(20) NOT NULL,
  `originId` bigint(20) NOT NULL,
  `newId` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `previousforwarderdata`
--

CREATE TABLE `previousforwarderdata` (
  `id` int(11) NOT NULL,
  `chatForwardInfoId` bigint(20) NOT NULL,
  `messagesCount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `UpdateAllChatsList` tinyint(1) NOT NULL DEFAULT 1,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`UpdateAllChatsList`, `id`) VALUES
(0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `allchatslist`
--
ALTER TABLE `allchatslist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chatforwardinfo`
--
ALTER TABLE `chatforwardinfo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chatmessageids`
--
ALTER TABLE `chatmessageids`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `previousforwarderdata`
--
ALTER TABLE `previousforwarderdata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `allchatslist`
--
ALTER TABLE `allchatslist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `chatforwardinfo`
--
ALTER TABLE `chatforwardinfo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `chatmessageids`
--
ALTER TABLE `chatmessageids`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=166;

--
-- AUTO_INCREMENT for table `previousforwarderdata`
--
ALTER TABLE `previousforwarderdata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
