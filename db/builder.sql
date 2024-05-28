-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mar 28 Mai 2024 à 00:05
-- Version du serveur :  5.6.20-log
-- Version de PHP :  5.4.31

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
  `action` varchar(255) DEFAULT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Contenu de la table `cartechance`
--

INSERT INTO `cartechance` (`id_CarteChance`, `titre`, `contennu`, `action`) VALUES
(1, 'blblblbl', 'ouiiiiii', '');

-- --------------------------------------------------------

--
-- Structure de la table `cases`
--

CREATE TABLE IF NOT EXISTS `cases` (
`Id_Cases` int(11) NOT NULL,
  `type_case` varchar(255) DEFAULT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prix` decimal(10,2) DEFAULT NULL,
  `loyer` decimal(10,2) DEFAULT NULL,
  `resource_contenue` varchar(255) DEFAULT NULL,
  `num_hamaux` int(11) DEFAULT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=33 ;

--
-- Contenu de la table `cases`
--

INSERT INTO `cases` (`Id_Cases`, `type_case`, `nom`, `prix`, `loyer`, `resource_contenue`, `num_hamaux`) VALUES
(1, 'Case_propriete', 'Nether', '60.00', '30.00', 'tractopelle', NULL),
(2, 'Case_ressource', '', '0.00', '0.00', 'camion', NULL),
(3, 'Case_propriete', 'End', '60.00', '30.00', 'tractopelle', NULL),
(4, 'Case_vol', '', '0.00', '0.00', 'tractopelle', NULL),
(5, 'Case_propriete', 'Dust 2', '100.00', '50.00', 'tractopelle', NULL),
(6, 'Case_chance', '', '0.00', '0.00', 'tractopelle', NULL),
(7, 'Case_propriete', 'Mirage', '100.00', '50.00', 'tractopelle', NULL),
(8, 'Case', '', '0.00', '0.00', 'tractopelle', NULL),
(9, 'Case_propriete', 'Minas Tirith', '140.00', '70.00', 'tractopelle', NULL),
(10, 'Case_ressource', '', '0.00', '0.00', 'bateau', NULL),
(11, 'Case_propriete', 'Minas Morgul', '140.00', '70.00', 'tractopelle', NULL),
(12, 'Case_vol', '', '0.00', '0.00', 'tractopelle', NULL),
(13, 'Case_propriete', 'Tatooine', '180.00', '90.00', 'tractopelle', NULL),
(14, 'Case_chance', '', '0.00', '0.00', 'tractopelle', NULL),
(15, 'Case_propriete', 'Coruscant', '180.00', '90.00', 'tractopelle', NULL),
(16, 'Case', '', '0.00', '0.00', 'tractopelle', NULL),
(17, 'Case_propriete', 'Rue du Flop', '220.00', '110.00', 'tractopelle', NULL),
(18, 'Case_ressource', '', '0.00', '0.00', 'tractopelle', NULL),
(19, 'Case_propriete', 'Avenue de Ratio', '220.00', '110.00', 'tractopelle', NULL),
(20, 'Case_vol', '', '0.00', '0.00', 'tractopelle', NULL),
(21, 'Case_propriete', 'Farland', '260.00', '130.00', 'tractopelle', NULL),
(22, 'Case_chance', '', '0.00', '0.00', 'tractopelle', NULL),
(23, 'Case_propriete', 'Aether', '260.00', '130.00', 'tractopelle', NULL),
(24, 'Case_police', '', '0.00', '0.00', 'tractopelle', NULL),
(25, 'Case_propriete', 'Internat Fille', '300.00', '150.00', 'tractopelle', NULL),
(26, 'Case_ressource', '', '0.00', '0.00', 'grue', NULL),
(27, 'Case_propriete', 'Internat GarÃ§on', '300.00', '150.00', 'tractopelle', NULL),
(28, 'Case_vol', '', '0.00', '0.00', 'tractopelle', NULL),
(29, 'Case_propriete', 'Tilted Tower', '400.00', '200.00', 'tractopelle', NULL),
(30, 'Case_chance', '', '0.00', '0.00', 'tractopelle', NULL),
(31, 'Case_propriete', 'Salty Spring', '400.00', '200.00', 'tractopelle', NULL),
(32, 'Case', '', '0.00', '0.00', 'tractopelle', NULL);

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
MODIFY `id_CarteChance` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `cases`
--
ALTER TABLE `cases`
MODIFY `Id_Cases` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=33;
--
-- AUTO_INCREMENT pour la table `plateau`
--
ALTER TABLE `plateau`
MODIFY `num` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
