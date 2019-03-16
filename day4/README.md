执行控制层         run.py (发现并执行所有用例，生成测试报告，发送邮件)
    |
用例层             test/
                        test_add_fuel_card.py
                        test....py
     |                   
数据层（公共方法） lib/
                        db.py（数据库操作）  
                        excel.py（读取用例数据） 
                        send_email.py（发送邮件）
      |                  
全局配置文件config.py 项目路径/数据库配置/日志配置/报告/邮件配置

其他：data/   放置数据文件
      log/    放log文件
      report/ 放报告文件
