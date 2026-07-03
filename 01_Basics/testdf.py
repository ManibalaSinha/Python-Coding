import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ----------------------------
# Dataset: Shopping Behavior
# ----------------------------
data = {
    "Annual_Spend": [200, 300, 250, 400, 500, 600, 700, 800, 850, 900],
    "Visits_Per_Month": [1, 2, 2, 3, 4, 5, 6, 7, 7, 8],
    "Online_Orders": [0, 1, 1, 2, 3, 4, 4, 5, 5, 6]
}

df = pd.DataFrame(data)

print("Customer Dataset:\n")
print(df)

# =====================================================
# 1️⃣ UNSUPERVISED LEARNING (K-Means Clustering)
# =====================================================
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(df)

print("\nUnsupervised Learning (Clusters):\n")
print(df)

# =====================================================
# 2️⃣ SUPERVISED LEARNING (Classification)
#    Use cluster labels as target
# =====================================================
X = df[["Annual_Spend", "Visits_Per_Month", "Online_Orders"]]
y = df["Cluster"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nSupervised Learning Accuracy:", accuracy_score(y_test, pred))

# =====================================================
# 3️⃣ REINFORCEMENT LEARNING (Simple Reward System)
#    Marketing strategy based on cluster
# =====================================================

def reward_action(cluster):
    if cluster == 0:
        return "Send Discount Offers (Reward: +10)"
    elif cluster == 1:
        return "Send Loyalty Rewards (Reward: +20)"
    else:
        return "Send Premium Ads (Reward: +15)"

print("\nReinforcement Learning Decisions:\n")

for i in range(len(df)):
    action = reward_action(df["Cluster"][i])
    print(f"Customer {i} -> Cluster {df['Cluster'][i]} -> {action}")
 
