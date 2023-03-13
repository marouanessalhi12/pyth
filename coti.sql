-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 13 mars 2023 à 12:09
-- Version du serveur : 10.4.24-MariaDB
-- Version de PHP : 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `coti`
--

-- --------------------------------------------------------

--
-- Structure de la table `charges`
--

CREATE TABLE `charges` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `libelle` text NOT NULL,
  `somme` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `charges`
--

INSERT INTO `charges` (`id`, `date`, `libelle`, `somme`) VALUES
(3, '2023-01-01', 'hareeee', 4000);

-- --------------------------------------------------------

--
-- Structure de la table `contributions`
--

CREATE TABLE `contributions` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `apartment_number` varchar(30) NOT NULL,
  `month` varchar(30) NOT NULL,
  `contribution_amount` int(11) NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `contributions`
--

INSERT INTO `contributions` (`id`, `name`, `apartment_number`, `month`, `contribution_amount`, `year`) VALUES
(3, 'Essalhi', '2', 'May', 1000, 0),
(4, 'gafa', '7', 'Juin', 2000, 2018),
(5, 'FDVDFV', '1', 'AVRIL', 100, 2019),
(7, 'ghg', '8', 'mars', 91819, 2020),
(8, 'dedf', '6', 'MAY', 19099, 2021),
(9, 'gdhgdhg', '9', 'Juin', 8000, 2021),
(11, 'hdghz', '9', 'February', 19999, 2023),
(12, 'ghfhf', '11', 'May', 4000, 2023);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `charges`
--
ALTER TABLE `charges`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `contributions`
--
ALTER TABLE `contributions`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `charges`
--
ALTER TABLE `charges`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `contributions`
--
ALTER TABLE `contributions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
