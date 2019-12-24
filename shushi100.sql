CREATE TABLE `cms_shushi_question` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `shushi_id` int(11) DEFAULT NULL COMMENT '舒适id',
  `content` varchar(3000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7382 DEFAULT CHARSET=utf8 COMMENT='舒适100问题';

CREATE TABLE `cms_shushi_answer` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL COMMENT '问题id',
  `best_answer` tinyint(3) DEFAULT '0' COMMENT '最佳答案 0否 1是',
  `content` text COMMENT '内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='舒适100答案';