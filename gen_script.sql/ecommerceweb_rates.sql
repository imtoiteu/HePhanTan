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
-- Table structure for table `rates`
--

DROP TABLE IF EXISTS `rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rates` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comment` varchar(255) DEFAULT NULL,
  `rate_date` datetime DEFAULT NULL,
  `rating` double DEFAULT NULL,
  `order_detail_id` bigint DEFAULT NULL,
  `product_id` bigint DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKoesgfm245y1ula1pn74fw9mkk` (`order_detail_id`),
  KEY `FK4mdsmkrr7od84tpgxto2v3t2e` (`product_id`),
  KEY `FKanlgavwqngljux10mtly8qr6f` (`user_id`),
  CONSTRAINT `FK4mdsmkrr7od84tpgxto2v3t2e` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `FKanlgavwqngljux10mtly8qr6f` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `FKoesgfm245y1ula1pn74fw9mkk` FOREIGN KEY (`order_detail_id`) REFERENCES `order_details` (`order_detail_id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rates`
--

LOCK TABLES `rates` WRITE;
/*!40000 ALTER TABLE `rates` DISABLE KEYS */;
INSERT INTO `rates` VALUES (1,'Iphone 13 thích quá, phải bán thận mua thôi !!!','2022-05-20 00:00:00',5,9,7,3),(2,'mua về nấu cơm cho mẹ !!! cho 5sao','2022-05-20 00:00:00',5,19,42,3),(3,'đồng hồ đôi đẹp quá, nhưng không có người yêu !!! 1 sao','2022-05-20 00:00:00',1,14,32,3),(4,'tivi siêu nét, nét hơn người yêu cũ!','2022-05-20 00:00:00',4,13,55,3),(5,'Đẹp quá, nét hơn nyc!','2022-05-20 00:00:00',5,20,3,3),(6,'màu đẹp, có free ship không ạ','2022-05-20 00:00:00',5,21,4,3),(7,'đợi em bán thận đã nhé!','2022-05-20 00:00:00',5,23,6,3),(8,'cũ rồi không ai muốn dùng nữa, bán rẻ điii','2022-05-20 00:00:00',4,27,12,3),(9,'Quá đẹp, 2022 rồi không ai xài nữa.','2022-05-20 00:00:00',3,28,11,3),(10,'Chờ em bán thận rồi em quay lại nhé !','2022-05-20 00:00:00',5,29,7,3),(11,'Chờ em bán thận rồi em quay lại nhé !','2022-05-20 00:00:00',5,30,9,3),(12,'Chờ em bán thận rồi em quay lại nhé !','2022-05-20 00:00:00',5,31,8,3),(13,'Nét hơn người yêu cũ luôn !','2022-05-20 00:00:00',5,32,10,3),(14,'mua bàn ủi về mùa đông ủi cho ấm !','2022-05-20 00:00:00',5,36,38,3),(15,'máy hơi yếu, ae đừng mua ','2022-05-20 00:00:00',2,37,39,3),(16,'lắp điều hòa dùng đi, máy này chạy không mát gì cả.','2022-05-20 00:00:00',2,38,40,3),(17,'LOL quá mượt','2022-05-20 00:00:00',5,39,16,3),(18,'best lag, không nên mua nhé\n','2022-05-20 00:00:00',5,40,21,3),(19,'con này mà code thì sướng phải biết.','2022-05-20 00:00:00',5,43,23,3),(20,'quá vip, vừa code vừa chơi game, cân mọi thể loại game','2022-05-20 00:00:00',5,42,22,3),(21,'coi không nét, muốn trả lại quá !','2022-05-20 00:00:00',2,45,46,3),(22,'Nét hơn người yêu cũ','2022-05-20 00:00:00',5,47,51,3),(23,'google: \"cách cướp tiền ngân hàng\" :))','2022-05-20 00:00:00',5,4,9,3),(24,'đừng mua, có tiền thì thêm mà mua prm dùng cho nó sướng !','2022-05-20 00:00:00',3,5,7,3),(25,'tivi đểu, đừng mua','2022-05-20 00:00:00',5,44,47,3),(26,'full viền, coi đã mắt quá, nên mua','2022-05-20 00:00:00',5,49,53,3),(27,'cũng đẹp đấy, nhưng không mua!','2022-05-20 00:00:00',4,16,28,3),(28,'quá đẹp luôn, mua đi ae','2022-05-20 00:00:00',5,17,24,3),(29,'Đúng hết nước chấm luôn ! quá đẹp cho 5 sao!','2022-05-20 00:00:00',5,50,36,3),(30,'đồ đều, ae đừng mua nhé, vote 1 sao.','2022-05-20 00:00:00',1,35,37,3),(31,'Đẹp quá!','2022-05-20 00:00:00',5,66,33,3),(32,'Quá nét!','2022-05-20 00:00:00',5,67,32,3),(33,'Đẹp nhưng đắt quá!','2022-05-20 00:00:00',5,68,34,3),(35,'Quá nét cho 1 siêu phẩm!','2022-05-20 00:00:00',5,70,36,3),(36,'Best sản phẩm nên có ở trong nhà, quá tiện lợi, nên mua đi mọi người ơi','2022-05-20 00:00:00',5,55,44,3),(37,'cắm cơm nhớ bật nút nghe các bạn!','2022-05-20 00:00:00',5,57,42,3),(38,'Đắt quá, lắp điều hòa nó hợp lý hơn!','2022-05-20 00:00:00',5,59,45,3),(39,'Đéo có người yêu mà mua!!','2022-05-20 00:00:00',2,64,30,3),(40,'mua prm mà dùng, không nên mua ip12 mini nhé!','2022-05-20 00:00:00',3,33,14,3),(41,'Đồng hồ nam đẹp quá, mà đéo có ny mua tặng !!','2022-05-20 00:00:00',4,73,36,4),(42,'xấu quá cho 1 sao','2022-05-20 00:00:00',1,78,32,4);
/*!40000 ALTER TABLE `rates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-30 15:37:37
