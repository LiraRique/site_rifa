-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 25-Nov-2020 às 00:15
-- Versão do servidor: 10.4.16-MariaDB
-- versão do PHP: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `rifa`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `pessoa`
--

CREATE TABLE `pessoa` (
  `id_pessoa` bigint(20) NOT NULL,
  `cpf_pessoa` varchar(40) DEFAULT NULL,
  `nome_pessoa` varchar(50) DEFAULT NULL,
  `endereco` varchar(50) DEFAULT NULL,
  `cep` int(11) DEFAULT NULL,
  `complemento` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `numero_telefone` varchar(14) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `sorteio_rifa`
--

CREATE TABLE `sorteio_rifa` (
  `id_rifa` int(11) NOT NULL,
  `id_pessoa` bigint(20) NOT NULL,
  `numero_rifa` bigint(20) DEFAULT NULL,
  `status_rifa` tinyint(4) DEFAULT NULL,
  `data_reserva` date DEFAULT NULL,
  `data_compensacao` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `status_rifa`
--

CREATE TABLE `status_rifa` (
  `id_rifa` int(11) NOT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `descricao_status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `pessoa`
--
ALTER TABLE `pessoa`
  ADD PRIMARY KEY (`id_pessoa`),
  ADD UNIQUE KEY `cpf_pessoa` (`cpf_pessoa`);

--
-- Índices para tabela `sorteio_rifa`
--
ALTER TABLE `sorteio_rifa`
  ADD PRIMARY KEY (`id_rifa`),
  ADD UNIQUE KEY `numero_rifa_unique` (`numero_rifa`),
  ADD KEY `id_pessoa_fk` (`id_pessoa`);

--
-- Índices para tabela `status_rifa`
--
ALTER TABLE `status_rifa`
  ADD KEY `id_rifa_fk` (`id_rifa`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `sorteio_rifa`
--
ALTER TABLE `sorteio_rifa`
  MODIFY `id_rifa` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `status_rifa`
--
ALTER TABLE `status_rifa`
  MODIFY `id_rifa` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `sorteio_rifa`
--
ALTER TABLE `sorteio_rifa`
  ADD CONSTRAINT `id_pessoa_fk` FOREIGN KEY (`id_pessoa`) REFERENCES `pessoa` (`id_pessoa`);

--
-- Limitadores para a tabela `status_rifa`
--
ALTER TABLE `status_rifa`
  ADD CONSTRAINT `id_rifa_fk` FOREIGN KEY (`id_rifa`) REFERENCES `sorteio_rifa` (`id_rifa`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
