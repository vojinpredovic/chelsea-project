import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("chelsea_data.csv")
df = df[df.groupby("referee")["referee"].transform("count") >= 2]

ref = df.groupby("referee").agg(
    games=("result", "count"),
    wins=("result", lambda x: (x == "W").sum())
).reset_index()

ref["win_pct"] = ref["wins"] / ref["games"] * 100
ref = ref.sort_values("win_pct")

fig, ax = plt.subplots(figsize=(8, 6))

ax.barh(ref["referee"], ref["win_pct"])
ax.axvline(50, color="red", linestyle="--", label="50%")
ax.set_xlabel("Win %")
ax.set_title("Chelsea Win Rate by Referee")
ax.legend()

plt.tight_layout()
plt.savefig("referee_winrate.png", bbox_inches = "tight")