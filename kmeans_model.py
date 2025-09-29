# kmeans_model.py
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def run_kmeans(file_path="Mall_Customers.csv", n_clusters=5):
    # 1) Đọc dữ liệu
    df = pd.read_csv(file_path)

    # 2) Chọn đặc trưng để phân cụm
    X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

    # Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3) Huấn luyện KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X_scaled)

    # 4) Tính Silhouette Score
    score = silhouette_score(X_scaled, df["Cluster"])

    # 5) Lấy tâm cụm
    centers = scaler.inverse_transform(kmeans.cluster_centers_)

    return df, score, centers
