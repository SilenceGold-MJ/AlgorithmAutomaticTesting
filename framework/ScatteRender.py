from pyecharts.charts import Scatter
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import pandas as pd
from framework.logger import Logger
logger = Logger(logger="Fanchar").getlog()
class ScatterRender:
    def scatter_render(self,dic,htmlname):
        logger.info(dic)
        df = pd.DataFrame(dic)
        df.sort_values("文物编号", inplace=True, ascending=True)  # 按年龄对数据做升序排序
        c = (
            Scatter()
                .add_xaxis(df.文物编号.values.tolist())
                .add_yaxis(
                "识别准确率",
                df[["准确率", "文物名称",]].values.tolist(),  # 传入信用分与姓名组合，方便js回调函数显示标签
                label_opts=opts.LabelOpts(
                    formatter=JsCode(
                        "function(params){return params.value[2];}"  # 通过定义JavaScript回调函数自定义标签
                    )
                )
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="识别准确率分布图"),

                xaxis_opts=opts.AxisOpts(
                    name='文物编号',
                    type_="value",  # x轴数据类型是连续型的
                    min_=0  # x轴范围最小为20
                ),
                yaxis_opts=opts.AxisOpts(
                    name='准确率值',
                    min_=0  # y轴范围最小为700
                )
            )
        )
        # xaxis_opts = opts.AxisOpts(name='AC(刷题数)', type_='value', min_=20),  # x轴从20开始，原点不为0
        # yaxis_opts = opts.AxisOpts(name='ACB(能力值)', min_=100),  # y轴起始点的值
        c.render('./static/html/%s' % htmlname)
        return  htmlname




