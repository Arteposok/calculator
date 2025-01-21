import dearpygui.dearpygui as dpg
from math import *
from numpy import *
from random import *
dpg.create_context()
dpg.create_viewport(width=650,
                    height=650,
                    title="calculator:)",
                    x_pos=200,
                    y_pos=200,
                    small_icon="image.ico",
                    large_icon="image.ico",
                    always_on_top=True)

with dpg.font_registry():
    main=dpg.add_font(".\\font.ttf", 16)
    dpg.bind_font(main)

with dpg.window(tag="pw"):
    dpg.add_input_text(label="formula", tag="formula")
    dpg.add_input_float(label="x", tag="x", step=1)
    dpg.add_input_float(label="y", tag="y", step=1)
    dpg.add_input_float(label="z", tag="z", step=1)
    button=dpg.add_button(label="calculate", width=100, height=30)
    output=dpg.add_input_text(default_value="result here")
    def calculate(sender, add_data):
        x=dpg.get_value("x")
        y=dpg.get_value("y")
        z=dpg.get_value("z")

        dpg.set_value(output, eval(dpg.get_value("formula")))

    dpg.set_item_callback(button, calculate)

    dpg.add_input_text(label="line formula", tag="y_formula", default_value="y")
    dpg.add_input_text(label="line 2 formula", tag="y_formula2", default_value="y")
    dpg.add_input_int(label="graph size", tag="size", default_value=100, step=10)
    make_graph=dpg.add_button(label="create graph")
    with dpg.plot(label="graphical calculator",tag="graph", height=400, width=400):
        dpg.add_plot_axis(dpg.mvXAxis, label="X")
        dpg.add_plot_axis(dpg.mvYAxis, label="Y", tag="y_axis")
        x = [i for i in range(1,100)]
        y = [y for y in x]
        y2 = [y+20 for y in x]
        series=dpg.add_line_series(x, y, label="Y", parent="y_axis")
        series2=dpg.add_line_series(x, y2, label="Y2", parent="y_axis")
    def make_line_series(e,c):
        global series, x
        x=[x for x in range(0, dpg.get_value("size"))]
        dpg.set_value(series,
                      [x,[eval(dpg.get_value("y_formula")) for y in x]])
        dpg.set_value(series2,
                      [x, [eval(dpg.get_value("y_formula2")) for y in x]])
        dpg.focus_item("graph")
    dpg.set_item_callback(make_graph, make_line_series)


    with dpg.group(horizontal=True):
        mean=dpg.add_input_text(label="mean")
        meanb=dpg.add_button(label="calculate algorithmic")
    mean_result = dpg.add_input_text(label="output")
    def meanc(x,s):
        items=dpg.get_value(mean).split(" ")
        result=0
        for i in items:
            result+=int(i)
        result/=len(items)
        dpg.set_value(mean_result, result)
    dpg.set_item_callback(meanb, meanc)

    with dpg.group(horizontal=True):
        med=dpg.add_input_text(label="median")
        medb=dpg.add_button(label="calculate algorithmic")
    med_result = dpg.add_input_text(label="output")
    def medc(x, s):
        items = list(map(int,dpg.get_value(med).split(" ")))
        items.sort()
        if len(items)%2==0:
            i1 = items[int(len(items) / 2 - 0.5)]
            i2 = items[int(len(items) / 2 + 0.5)]
            dpg.set_value(med_result, (i1 + i2) / 2)
        else:
            ind=int(len(items) / 2+0.5)
            dpg.set_value(med_result, items[ind])


    dpg.set_item_callback(medb, medc)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("pw", True)
dpg.start_dearpygui()
dpg.destroy_context()