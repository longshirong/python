from database import loadData
import pyecharts.options as opts
from pyecharts.charts import Line
import numpy as np

version_id = 1
# 得到的是二维列表
data = loadData.load_data_from_database(version_id)
column_name = ['ID', 'java_heap', 'native_heap', 'code', 'stack', 'graphics', 'private_other', 'system',
               'total', 'version_id', 'time']


# 把数据转化为标准的横纵坐标值，便于绘图
def trans_data_to_use(dataset: list):
    size = len(dataset)
    # 元组中可能数据大小不一致，因此先进行转化
    dataset = np.array(dataset)
    k = 1 / 1024
    # 得到测试的时刻
    x_data = dataset[:, 10]
    y_data_1 = np.array(dataset[:, 1], float) * k
    y_data_1 = np.round(y_data_1, decimals=1)
    y_data_2 = np.array(dataset[:, 2], float) * k
    y_data_2 = np.round(y_data_2, decimals=1)
    y_data_3 = np.array(dataset[:, 3], float) * k
    y_data_3 = np.round(y_data_3, decimals=1)
    y_data_4 = np.array(dataset[:, 4], float) * k
    y_data_4 = np.round(y_data_4, decimals=1)
    y_data_5 = np.array(dataset[:, 5], float) * k
    y_data_5 = np.round(y_data_5, decimals=1)
    y_data_6 = np.array(dataset[:, 6], float) * k
    y_data_6 = np.round(y_data_6, decimals=1)
    y_data_7 = np.array(dataset[:, 7], float) * k
    y_data_7 = np.round(y_data_7, decimals=1)
    y_data_8 = np.array(dataset[:, 8], float) * k
    y_data_8 = np.round(y_data_8, decimals=1)
    (
        Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="java_heap",
            y_axis=y_data_1,
            linestyle_opts=opts.LineStyleOpts(width=2),
        )
            .add_yaxis(
            series_name="native_heap", y_axis=y_data_2, linestyle_opts=opts.LineStyleOpts(width=2)
        )
            .add_yaxis(
            series_name="code", y_axis=y_data_3, linestyle_opts=opts.LineStyleOpts(width=2)
        )
            .add_yaxis(
            series_name="stack", y_axis=y_data_4, linestyle_opts=opts.LineStyleOpts(width=2)

        )
            .add_yaxis(
            series_name="graphics", y_axis=y_data_5, linestyle_opts=opts.LineStyleOpts(width=2)

        )
            .add_yaxis(
            series_name="private_other", y_axis=y_data_6, linestyle_opts=opts.LineStyleOpts(width=2)

        )
            .add_yaxis(
            series_name="system", y_axis=y_data_7, linestyle_opts=opts.LineStyleOpts(width=2)

        )
            .add_yaxis(
            series_name="total", y_axis=y_data_8, linestyle_opts=opts.LineStyleOpts(width=2)

        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="memory information", pos_left="center"),
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}"),
            legend_opts=opts.LegendOpts(pos_left="left"),
            xaxis_opts=opts.AxisOpts(type_="category", name="x"),
            yaxis_opts=opts.AxisOpts(
                type_="log",
                name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,
            ),
        )
            .render("memory.html")
    )


if __name__ == '__main__':
    trans_data_to_use(data)