-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 13, 2025 at 08:33 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `visual3_2310010619`
--

-- --------------------------------------------------------

--
-- Table structure for table `dzikir_playlist`
--

CREATE TABLE `dzikir_playlist` (
  `id_playlist` varchar(20) NOT NULL,
  `nama_dzikir` varchar(100) NOT NULL,
  `jenis_dzikir` varchar(50) DEFAULT NULL,
  `deskripsi` varchar(255) DEFAULT NULL,
  `audio_path` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payment_type`
--

CREATE TABLE `payment_type` (
  `id_payment` varchar(20) NOT NULL,
  `nama_payment` varchar(50) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `deskripsi` varchar(255) DEFAULT NULL,
  `provider` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shadaqah_history`
--

CREATE TABLE `shadaqah_history` (
  `id_shadaqah` varchar(20) NOT NULL,
  `id_user` varchar(20) NOT NULL,
  `id_payment` varchar(20) NOT NULL,
  `jumlah_donasi` varchar(20) DEFAULT NULL,
  `tanggal_donasi` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id_user` varchar(20) NOT NULL,
  `nama_user` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `kota` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `zikir_counter`
--

CREATE TABLE `zikir_counter` (
  `id_counter` varchar(20) NOT NULL,
  `id_user` varchar(20) NOT NULL,
  `id_playlist` varchar(20) NOT NULL,
  `total_zikir` varchar(20) DEFAULT NULL,
  `tanggal` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dzikir_playlist`
--
ALTER TABLE `dzikir_playlist`
  ADD PRIMARY KEY (`id_playlist`);

--
-- Indexes for table `payment_type`
--
ALTER TABLE `payment_type`
  ADD PRIMARY KEY (`id_payment`);

--
-- Indexes for table `shadaqah_history`
--
ALTER TABLE `shadaqah_history`
  ADD PRIMARY KEY (`id_shadaqah`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_payment` (`id_payment`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `zikir_counter`
--
ALTER TABLE `zikir_counter`
  ADD PRIMARY KEY (`id_counter`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_playlist` (`id_playlist`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `shadaqah_history`
--
ALTER TABLE `shadaqah_history`
  ADD CONSTRAINT `shadaqah_history_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`),
  ADD CONSTRAINT `shadaqah_history_ibfk_2` FOREIGN KEY (`id_payment`) REFERENCES `payment_type` (`id_payment`);

--
-- Constraints for table `zikir_counter`
--
ALTER TABLE `zikir_counter`
  ADD CONSTRAINT `zikir_counter_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`),
  ADD CONSTRAINT `zikir_counter_ibfk_2` FOREIGN KEY (`id_playlist`) REFERENCES `dzikir_playlist` (`id_playlist`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
