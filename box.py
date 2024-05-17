import os
from OCC.Core.gp import gp_Pnt
from OCC.Core.TColgp import TColgp_Array1OfPnt
from OCC.Core.GeomAPI import GeomAPI_PointsToBSpline
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeWire
from OCC.Display.SimpleGui import init_display
# 读取文件中的点
import pyclipper
def read_points_from_file(file_path):
    points = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # 使用空格分隔点
                parts = line.strip().split()
                if len(parts) == 2:
                    x, y = map(int, parts)
                    points.append((x, y))
                else:
                    print(f"Invalid line format: {line}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return points

# 文件路径
file_path = r'新建文件夹 (3)\output_wall.txt'

display, start_display, add_menu, add_function_to_menu = init_display()
# 确保文件存在
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found.")

# 获取点
points = read_points_from_file(file_path)
lines = []
for i in range(0, len(points), 2):
    if i + 1 < len(points):
        lines.append([points[i], points[i + 1]])

# 使用 Clipper 库处理线段并生成多边形
clipper = pyclipper.Pyclipper()
for line in lines:
    clipper.AddPath(line, pyclipper.PT_SUBJECT, False)

#这里就错了
solution = clipper.Execute(pyclipper.CT_UNION, pyclipper.PFT_NONZERO)



# try:
#     solution = clipper.Execute(pyclipper.CT_UNION, pyclipper.PFT_NONZERO)
# 检查是否读取到点
# if not points:
#     raise ValueError("No points found in the file.")
#
# # 创建 gp_Pnt 对象列表
# gp_points = [gp_Pnt(x, y, 0) for x, y in points]
# edges = []
# for i in range(0, len(gp_points), 2):
#     if i + 1 < len(gp_points):
#         edge = BRepBuilderAPI_MakeEdge(gp_points[i], gp_points[i + 1]).Edge()
#         display.DisplayShape(edge, update=True)
#
# # 启动显示窗口
# start_display()
