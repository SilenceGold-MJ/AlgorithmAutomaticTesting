from pyecharts.charts import Pie  # 饼图所导入的包
from pyecharts import options as opts  # 全局设置所导入的包
from framework.logger import Logger
logger = Logger(logger="Fanchar").getlog()


class Fanchar():
    def Pie1(self,dic):
        pie = (
            Pie()
                .add("", dic['listdata'])  # 加入数据
                .set_global_opts(title_opts=opts.TitleOpts(title=dic['title']),
                                 legend_opts=opts.LegendOpts(pos_left=160))  # 全局设置项
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}")))  # 样式设置项
        pie.render("./static/html/%s" % dic['htmlname'])  # 保存图片为HTML网页

        # return pie
    def Generating(self,dic):#生成多个扇形图

        data=dic['datalist'][0]
        dabl=str(data["StandardRate"]*100)+"%"#识别率准确率达标率
        shibl=str(round(data['Sum_Pass']/data["Sum_Numbers"],4)*100)+"%"#整体识别准确率
        liatdata_bzt=dic["dic_dbl"]["datalist"]
        logger.info("饼状图基础数据%s"%liatdata_bzt)
        list=[
            ['准确率占比图:','dabiaolv.html', liatdata_bzt

             ],
            ['整体准确率:'+shibl,'shibiaocg.html',
             [
                 ['识别准确数',str(data['Sum_Pass'])],
                 ['识别错误数', str(data['Sum_Fail'])]
             ]
             ]
        ]
        htmlname=[]
        for i in list:
            # listdata = [['农林牧', '67538'], ['工业增', '305160.2'], ]
            dicdata = {

                'title': i[0],
                'htmlname': i[1],
                'listdata': i[2],
            }
            logger.info(dicdata)
            Fanchar().Pie1(dicdata)
            htmlname.append(i[1])
        return htmlname






