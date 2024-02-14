import graphviz
from enum import Enum

class Code(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
# Graphvizのオブジェクトを作成
dot = graphviz.Digraph(format='png')

# ノードを4つ作成
dot.node(Code.A.name, 'A')
dot.node(Code.B.name, 'B')
dot.node(Code.C.name, 'C')
dot.node(Code.D.name, 'D')

# ノードを接続する
dot.edge(Code.A.name, Code.B.name)
dot.edge(Code.A.name, Code.D.name)
dot.edge(Code.B.name, Code.C.name)
dot.edge(Code.D.name, Code.C.name)

# 表示
# dot.view()  # `dot`オブジェクトで`view`メソッドを呼び出す
dot.render('graph')  # 画像を保存
