# -*- coding: utf-8 -*-

from qqbot.utf8logger import INFO

'''
本插件启动时加载使用方法如下：

    （1） 将本文件保存到插件目录中（如：C:\\Users\\xxx\\.qqbot-tmp\\plugins ）。

    （2） 修改配置文件 v2.3.conf ，增加一个用户配置，增加以下内容：
    
             "myuser" : {
                "plugins" : [
                    "qqbot.plugins.schedrestart",
                    "getgroupfullinfo"
                ],
                "pluginsConf" : {
                    "qqbot.plugins.schedrestart" : "8:00",
                    "getgroupfullinfo" : {
                        "群名1" : "群号1",
                        "群名2" : "群号2",
                        "群名3" : "群号3",
                    }
                }
            }

         并修改其中的 "群名", "群号" .

    （3） 启动 qqbot ： qqbot -u myuser

'''

def onUpdate(bot, tinfo):
    # 当组更新完毕时,添加手动设置的QQ号
    if tinfo == 'group':
        group_manager = bot.conf.pluginsConf.get(__name__, {})
        for group_name,group_qq in group_manager.iteritems():
            groups = bot.List('group', group_name)
            if len(groups) >= 1:
                group = groups[0]  # 获取第一个
                bot.contactdb.db.Modify('group', group, qq=str(group_qq))  # 更新qq号
                INFO('[组员详细信息插件]组名称:%s设置群号为:%s', group_name, group_qq)
