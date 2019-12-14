CREATE TABLE `share_data15` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `share_id` varchar(255) DEFAULT NULL COMMENT '股票代码',
  `share_name` varchar(255) DEFAULT NULL COMMENT '股票名称',
  `have_number` varchar(255) DEFAULT NULL COMMENT '持仓量',
  `have_time` varchar(255) DEFAULT NULL COMMENT '建仓时间',
  `profit_loss_cost` varchar(255) DEFAULT NULL COMMENT '盈亏成本',
  `present_price` varchar(255) DEFAULT NULL COMMENT '现价',
  `today_gains` varchar(255) DEFAULT NULL COMMENT '今日涨幅',
  `stock_market_capitalization` varchar(255) DEFAULT NULL COMMENT '股票市值',
  `profit_loss_ratio` varchar(255) DEFAULT NULL COMMENT '盈亏率',
  `floating_p_l` varchar(255) DEFAULT NULL COMMENT '浮动盈亏',
  `create_time` varchar(255) DEFAULT NULL COMMENT '创建时间',
  `warehouse_position` varchar(255) DEFAULT NULL COMMENT '仓位',
  `success` varchar(255) DEFAULT NULL COMMENT '成功率',
  `count_number` varchar(255) DEFAULT NULL COMMENT '操作次数',
  `user_add_time` varchar(255) DEFAULT NULL COMMENT '加入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8 COMMENT='数据';