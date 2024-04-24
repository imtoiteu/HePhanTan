CREATE DATABASE  IF NOT EXISTS `ecommerceweb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ecommerceweb`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ecommerceweb
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` bigint NOT NULL AUTO_INCREMENT,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `gender` bit(1) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `register_date` date DEFAULT NULL,
  `status` bit(1) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'236 Hoàng Quốc Việt','vuthaian13@gmail.com',_binary '','https://res.cloudinary.com/martfury/image/upload/v1654052805/users/bt7d81xysz2kwiwfapxf.png','Long Phương An','$2a$10$yvcT5zT/lDrM89Lofss6GeF0icqluuVVxo2QX4BehAh75k.eAzFIe','0969125625','2022-05-01',_binary '','eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJncmVlbnlzaG9wLmFkbUBnbWFpbC5jb20iLCJzY29wZXMiOlt7ImF1dGhvcml0eSI6IlJPTEVfQURNSU4ifV0sImlzcyI6Imh0dHA6Ly9kZXZnbGFuLmNvbSIsImlhdCI6MTY0Nzc4MjE4MywiZXhwIjoxNjQ3ODAwMTgzfQ.cLQLN6HPjClhuJFdBro1WHKEKfA7wYbBa3Eg3uHfNAE'),(3,'Vĩnh Phúc','phong01052000@gmail.com',_binary '','https://res.cloudinary.com/martfury/image/upload/v1654058485/users/p0slvf0r2jzq4w857ok8.jpg','Đỗ Thành Long','$2a$10$/KivpyMoaCkLDSycU59Mv.Hna9Wy/LMG.A0B.g2P1sy4Yylf4iQYi','0969152625','2022-05-01',_binary '','eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJodXVkb25nMjk3QGdtYWlsLmNvbSIsInNjb3BlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9BRE1JTiJ9XSwiaXNzIjoiaHR0cDovL2RldmdsYW4uY29tIiwiaWF0IjoxNjQ3Nzg5NDI5LCJleHAiOjE2NDc4MDc0Mjl9.JfbZQ2D8lRg8UPWhnnLMO9R-lFW_8-r2hxV9kOVZRZM'),(4,'Hà Tĩnh','inuayashavip123@gmail.com',_binary '','https://res.cloudinary.com/martfury/image/upload/v1654058601/users/wernu7a61ruxr0zm6e7n.jpg','Trần Thanh Phương','$2a$10$rW5wgTclOYsGmhbcGzoi6uZpsXSqsREq8OEacmYq2Oz0RFk2ir50y','0969152625','2022-05-01',_binary '','eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0aGFvY2hpNjQwNEBnbWFpbC5jb20iLCJzY29wZXMiOlt7ImF1dGhvcml0eSI6IlJPTEVfQURNSU4ifV0sImlzcyI6Imh0dHA6Ly9kZXZnbGFuLmNvbSIsImlhdCI6MTY0ODA0MzUzNywiZXhwIjoxNjQ4MDYxNTM3fQ.589LqMNNJ-NiF0s425cR_tfAr3cfhqf7rpQ_QU1AEIw'),(6,'Hải Dương','vuthaian12@gmail.com',_binary '','https://res.cloudinary.com/martfury/image/upload/v1654059720/users/ggnakp9mbuqiyv5tgjq9.jpg','Vũ Thái An','$2a$10$4OKQZm3f2IJUcRscm33aZ.ZSfZbUK2aCkAofFaRLiBXk5ovN/bnB6','0969152625','2022-06-01',_binary '','eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2dXRoYWlhbjEyQGdtYWlsLmNvbSIsInNjb3BlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9BRE1JTiJ9XSwiaXNzIjoiaHR0cDovL2RldmdsYW4uY29tIiwiaWF0IjoxNjU0MDU5MzMzLCJleHAiOjE2NTQwNzczMzN9._cJyvMKsN2B5RuVaH54uhMgvkW5nwD_pqvTel66vfs0'),(7,'236 Hoàng Quốc Việt','vuthaian14@gmail.com',_binary '','https://res.cloudinary.com/dwrcr5anf/image/upload/v1683206351/profileImage_ug8g1i.png','An Vũ Thái','$2a$10$izcP8P7YRxD09PzBQp9KEOgz19qhJ9ZkOlWVU7sqX1my97FpxT8tS','0915252142','2022-06-01',_binary '','eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2dXRoYWlhbjE0QGdtYWlsLmNvbSIsInNjb3BlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9BRE1JTiJ9XSwiaXNzIjoiaHR0cDovL2RldmdsYW4uY29tIiwiaWF0IjoxNjU0MDY4MTQxLCJleHAiOjE2NTQwODYxNDF9.E2wJfs14zsMpO-3TWNnsFJYWKr7BeYGcTpzOnhmiX7U'),(8,'236 Hoàng Quốc Việt','trantoimta@gmail.com',_binary '','https://res.cloudinary.com/dwrcr5anf/image/upload/v1683206351/profileImage_ug8g1i.png','Trần Thị Tới','$2a$10$PsxO67EMeo/HuezT4cWmIOiQSoizYWv/jKQ81QyjJJ9ZtRX/5yfn6','0915252142','2022-06-01',_binary '','eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2dXRoYWlhbjE0QGdtYWlsLmNvbSIsInNjb3BlcyI6W3siYXV0aG9yaXR5IjoiUk9MRV9BRE1JTiJ9XSwiaXNzIjoiaHR0cDovL2RldmdsYW4uY29tIiwiaWF0IjoxNjU0MDY4MTQxLCJleHAiOjE2NTQwODYxNDF9.E2wJfs14zsMpO-3TWNnsFJYWKr7BeYGcTpzOnhmiX7U');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-30 15:37:38
