# インポート
import matplotlib.pyplot as plt
import japanize_matplotlib          # 日本語表示に対応
import numpy as np
import pandas as pd

# URLからデータセットを読み込む
url = "https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv"
data = pd.read_csv(url)

# 必要なデータの整理
data_week = data.loc[139:, ['No', '公表_年月日', '曜日']]
data_week.head()

# 公表_年月日ごとの新規感染者数の小計を取る
data_count = data_week.groupby('公表_年月日').size()

# 曜日ごとのデータにする
data_mon = data_count[::7]
data_tue = data_count[1::7]
data_wed = data_count[2::7]
data_thu = data_count[3::7]
data_fri = data_count[4::7]
data_sat = data_count[5::7]
data_sun = data_count[6::7]
week = len(data_mon)

## 曜日別のグラフ
# グラフ用変数の設定
t1 = data_mon.index
y1 = data_mon.values
y2 = data_tue.values
y3 = data_wed.values
y4 = data_thu.values
y5 = data_fri.values
y6 = data_sat.values
y7 = data_sun.values

c1,c2,c3,c4,c5,c6,c7 = "red","orange","yellow","green","blue","purple","pink"      # 各プロットの色
l1,l2,l3,l4,l5,l6,l7 = "月","火","水","木","金","土","日"   # 各ラベル

# 行数がweekに満たないデータにはNoneを付加する
if len(y7) < week:
    y7 = np.append(y7, None)
    if len(y6) < week:
        y6 = np.append(y6, None)
        if len(y5) < week:
            y5 = np.append(y5, None)
            if len(y4) < week:
                y4 = np.append(y4, None)
                if len(y3) < week:
                    y3 = np.append(y3, None)
                    if len(y2) < week:
                        y2 = np.append(y2, None)

# 曜日ごとのグラフ描画
fig, ax = plt.subplots()

ax.set_xlabel('週始まりの月曜日の日付')  # x軸ラベル
ax.set_ylabel('新規感染者数')  # y軸ラベル
ax.set_title('曜日別新規感染者数') # グラフタイトル
# ax.set_aspect('equal') # スケールを揃える
ax.grid()            # 罫線
#ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
#ax.set_ylim([0, 1])    # y方向の描画範囲を指定
ax.plot(t1, y1, color=c1, label=l1)
ax.plot(t1, y2, color=c2, label=l2)
ax.plot(t1, y3, color=c3, label=l3)
ax.plot(t1, y4, color=c4, label=l4)
ax.plot(t1, y5, color=c5, label=l5)
ax.plot(t1, y6, color=c6, label=l6)
ax.plot(t1, y7, color=c7, label=l7)
ax.legend(loc=0)    # 凡例
plt.xticks(rotation=90)     # x軸の文字を90度回転
fig.tight_layout()  # レイアウトの設定（保存の直前に入れて調整）
plt.savefig('tokyo/week.png', dpi=300) # 画像の保存

## 日別のグラフ
# 日別のデータ
t_daily = data_count.index
y_daily = data_count.values
y_mean7 = np.zeros(len(y_daily)) # 7日間平均
for i in range(6, len(y_daily)):
    y_mean7[i] = np.mean(y_daily[i-6:i+1])

# ========================
# 日ごとのグラフ描画
# ========================
fig, ax = plt.subplots()

ax.set_xlabel('日付（月曜日）')  # x軸ラベル
ax.set_ylabel('感染者数')  # y軸ラベル
ax.set_title('日別新規感染者数及び7日間平均') # グラフタイトル
# ax.set_aspect('equal') # スケールを揃える
ax.grid()            # 罫線
#ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
#ax.set_ylim([0, 1])    # y方向の描画範囲を指定
ax.plot(t_daily[:], y_daily[:], color='blue', label='新規感染者数')
ax.plot(t_daily[:], y_mean7[:], color='red', label='7日間平均')
# ax.legend(loc=0)    # 凡例
ax.legend()
ax.set_xticks(data_count[::7].index)       # 月曜日の日付のみ軸に表示する
plt.xticks(rotation=90)     # x軸の文字を90度回転
fig.tight_layout()  # レイアウトの設定（保存の直前に入れて調整）
plt.savefig('tokyo/daily.png', dpi=300) # 画像の保存


# ========================
# 日ごとのグラフ描画（log）
# ========================
fig, ax = plt.subplots()

ax.set_xlabel('日付（月曜日）')  # x軸ラベル
ax.set_ylabel('感染者数')  # y軸ラベル
ax.set_title('日別新規感染者数及び7日間平均') # グラフタイトル
# ax.set_aspect('equal') # スケールを揃える
ax.grid()            # 罫線
#ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
#ax.set_ylim([0, 1])    # y方向の描画範囲を指定
ax.plot(t_daily[:], y_daily[:], color='blue', label='新規感染者数')
ax.plot(t_daily[:], y_mean7[:], color='red', label='7日間平均')
plt.yscale("log")
# ax.legend(loc=0)    # 凡例
ax.legend()
ax.set_xticks(data_count[::7].index)       # 月曜日の日付のみ軸に表示する
plt.xticks(rotation=90)     # x軸の文字を90度回転
fig.tight_layout()  # レイアウトの設定（保存の直前に入れて調整）
plt.savefig('tokyo/daily_log.png', dpi=300) # 画像の保存

