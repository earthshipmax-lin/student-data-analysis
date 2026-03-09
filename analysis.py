import pandas as pd
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv("data/student.csv")

#基本统计
print("学生人数:", len(data))
print("平均成绩:", data["score"].mean())
print("最高成绩:", data["score"].max())
print("最低成绩:", data["score"].min())

#画成绩分布图
plt.hist(data["score"], bins=5)

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")

#保存图片
plt.savefig("score_disturibution.png")

print("成绩分布图已保存为 score_distribution.png")

#按成绩排序（从高到低）
sorted_data = data.sort_values(by="score", ascending=False)

print("\n成绩排名: ")
print(sorted_data)

print("\n前三名学生: ")
print(sorted_data.head(3))

