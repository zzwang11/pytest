

'''
# 代码示例
window = QWidget
window.resize(500, 500)

frame = QFrame(window)
frame.resize(100, 100)
frame.move(100, 100)
# 尽管已经创建了这样一个对象，但是我们并不能直接的看到之歌控件

setFrameShape(QFrame.Shape)

# QFrame.Shape枚举值
QFrame.NoFrame  # QFrame什么都没画
QFrame.Box      # QFrame围绕其内容绘制一个框
QFrame.Panel    # QFrame绘制一个面板，使内容显得凸起或凹陷
QFrame.VLine    # QFrame绘制一条无框架的垂直线（用作分隔符）
QFrame.StyledPanel  # 绘制一个矩形面板，其外观取决于当前的GUI样式。它可以升起或凹陷。
QFrame.HLine    # QFrame绘制一条没有框架的水平线（用作分隔符）

# 获取形状
frameShape() -> QFrame.Shape

'''