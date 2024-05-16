-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Jeu 16 Mai 2024 à 06:47
-- Version du serveur :  5.6.20-log
-- Version de PHP :  5.4.31

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `builder`
--

-- --------------------------------------------------------

--
-- Structure de la table `cartechance`
--

CREATE TABLE IF NOT EXISTS `cartechance` (
`id_CarteChance` int(11) NOT NULL,
  `titre` varchar(255) DEFAULT NULL,
  `contennu` text,
  `action` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `cases`
--

CREATE TABLE IF NOT EXISTS `cases` (
`Id_Cases` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prix` decimal(10,2) DEFAULT NULL,
  `loyer` decimal(10,2) DEFAULT NULL,
  `resource_contenue` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `plateau`
--

CREATE TABLE IF NOT EXISTS `plateau` (
`num` int(11) NOT NULL,
  `id_Cases` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `cartechance`
--
ALTER TABLE `cartechance`
 ADD PRIMARY KEY (`id_CarteChance`);

--
-- Index pour la table `cases`
--
ALTER TABLE `cases`
 ADD PRIMARY KEY (`Id_Cases`);

--
-- Index pour la table `plateau`
--
ALTER TABLE `plateau`
 ADD PRIMARY KEY (`num`), ADD KEY `id_Cases` (`id_Cases`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `cartechance`
--
ALTER TABLE `cartechance`
MODIFY `id_CarteChance` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `cases`
--
ALTER TABLE `cases`
MODIFY `Id_Cases` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `plateau`
--
ALTER TABLE `plateau`
MODIFY `num` int(11) NOT NULL AUTO_INCREMENT;SET FOREIGN_KEY_CHECKS=1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
