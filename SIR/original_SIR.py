# -*- coding: utf-8 -*-
# 参考url
# http://www.yamamo10.jp/yamamoto/comp/Python/library/SciPy/OrdinaryDiffEq/index.php

import numpy as np 
import matplotlib.pyplot as plt
import japanize_matplotlib
from mpl_toolkits.mplot3d import Axes3D 
from scipy.integrate import odeint 

# ========================
# 常微分方程式を解くクラス
# ========================
class ODE(object):
    
    # ========================
    # コンストラクター
    # ========================
    def __init__(self, diff_eq, init_con):
        self.diff_eq = diff_eq
        self.init_con =init_con 
    
    # ========================
    # 常微分方程式の計算
    # ========================
    def cal_equation(self, t_min, t_max, N):
        t = np.linspace(t_min, t_max, N)            # xの配列の生成
        v = odeint(self.diff_eq, self.init_con, t)  # 方程式の計算
        return v

# ========================
# 解くべき常微分方程式
# ========================
def diff_eq(v, t):
    beta = 1 
    alpha0 = 1
    alpha1 = 0.00001
    gamma = 1 
    dSdt = - beta * alpha0 * v[0] * v[1] - alpha1 * v[0] * v[1] * (beta * alpha0 * v[0] * v[1] - gamma * v[1]) / (1 + beta * alpha1 * v[0] * v[1])
    dIdt = (beta * alpha0 * v[0] * v[1] - gamma * v[1]) / (1 + beta * alpha1 * v[0] * v[1])
    dRdt = gamma * v[1] 
    return [dSdt, dIdt, dRdt]

# ========================
# プロット 
# ========================
def plot(t, S, I, R):
    fig, ax = plt.subplots()

    c1,c2,c3 = "blue","red","black"
    l1,l2,l3 = "S","I","R"

    ax.set_xlabel('t')
    ax.set_ylabel('人数')
    ax.set_title(r'人数の変化')
    ax.grid()            # 罫線
    ax.plot(t, S, color=c1, label=l1)
    ax.plot(t, I, color=c2, label=l2)
    ax.plot(t, R, color=c3, label=l3)
    ax.legend(loc=0)    # 凡例
    # スクリーン表示
    fig.tight_layout()  # レイアウトの設定（保存の直前に入れて調整）
    plt.savefig('Original_SIR.png')
    plt.show()

# ========================
# メイン関数
# ========================
if __name__ == "__main__":
    N = 10000           # 分割数
    min_t = 0           # tの最小
    max_t = 100         # tの最大
    initial_condition = np.array([10000, 1, 0])     # 初期条件

    ode = ODE(diff_eq, initial_condition)
    t, v = ode.cal_equation(min_t, max_t, N)

    plot(t, v[:,0], v[:,1], v[:,2])
