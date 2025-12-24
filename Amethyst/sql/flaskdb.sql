-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Jun 2024 pada 09.32
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskdb`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `moods`
--

CREATE TABLE `moods` (
  `id` int(11) NOT NULL,
  `mood` varchar(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_journal`
--

CREATE TABLE `tb_journal` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tb_journal`
--

INSERT INTO `tb_journal` (`id`, `username`, `date`, `note`) VALUES
(20, 'danang', '2024-04-23', 'diberi saran yang baik oleh bos ternyata, bukan dimarahi ✅'),
(27, 'danang', '2024-05-03', 'nge date pertama hati berbunga bunga 😍❤️'),
(28, 'danang', '2024-06-01', 'hari ini sangat menyenangkan karena naik jabatan '),
(29, 'budi', '2024-06-08', 'naik gaji karena naik jabatan 😘'),
(31, 'Yono', '2024-06-02', '😭'),
(32, 'Yono', '2024-06-06', '❤️');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_user`
--

CREATE TABLE `tb_user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tb_user`
--

INSERT INTO `tb_user` (`id`, `username`, `email`, `password`) VALUES
(1, 'danang', 'danangprayogi7@gmail.com', 'scrypt:32768:8:1$2iI6ESsaMWfELqv3$9ec72e6b499b6400230946c0e422a6f35faf6b5587ffb9721649f60116179b1736e4ad95647f2108b863992bdd139ee15fb8fd140b2df76034540763c22df93f'),
(2, 'Tatang', 'danangpr9f11@gmail.com', 'scrypt:32768:8:1$vCZqU0f70ZnQByog$f46f5bd490d2a3d183b38996f6aa4608ba22ccde8c34a537386ebd07d6d7a62f87a944b4a36e9cd60b6c7e7734fd21f863fb9914dbc94d7dfff12a54347ababf'),
(3, 'baim', 'm.maulanaibrahim916@gmail.com', 'scrypt:32768:8:1$eQ8AsJ2ZyGWxhciJ$e4ae0844553a996b3fc43508948cb885ba6f0d701aa751d994dea6f36af1f8a9f23d5d09e50c040cfb120732cf28ee273e7e129d9f7cb5d6efb4d5534e6cb469'),
(4, 'ichaoo', 'icha123@gmail.com', 'scrypt:32768:8:1$KWeUWnqHwqzHoD2u$55bbc8220611552d9a9999001fdbd7e0494921c46d11d064d8f419a1911c86059f7894cdd234f59d8b89e32bea8641ed560563eeb2ce29b018999f029486c0f4'),
(5, 'budi', 'budi123@gmail.com', 'scrypt:32768:8:1$Z8yXz3RfXbCyqxU7$be13835d24f7e6f363a27491fe87d62cbf31be2e589c96469b07ce0b1fc5cb1c493971935f722bc47904aaab56cfa33da80d1e73c7c85ce896c01b06fa3c4157'),
(6, 'Yono', 'yono123@gmail.com', 'scrypt:32768:8:1$FRhMJUp35zadwPr5$e75abe865921ef02f9f65d2dfc4e0cc6ca33802e45864e396009853aa376526532eec6a417c04b4958ea6268e0d0ca896baff92ee22ce7981d10f99a0b277055');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `moods`
--
ALTER TABLE `moods`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `tb_journal`
--
ALTER TABLE `tb_journal`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `moods`
--
ALTER TABLE `moods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `tb_journal`
--
ALTER TABLE `tb_journal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT untuk tabel `tb_user`
--
ALTER TABLE `tb_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
