# app.py
from flask import Flask, render_template, request
import os
from kmeans_model import run_kmeans

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Người dùng có thể chọn số cụm
        n_clusters = int(request.form.get("clusters", 5))
        df, score, centers = run_kmeans("Mall_Customers.csv", n_clusters)

        # Lấy 10 dòng đầu để hiển thị
        preview = df[["Gender","Age","Annual Income (k$)","Spending Score (1-100)","Cluster"]].head(10).to_html(classes="table table-striped", index=False)

        return render_template("result.html",
                               tables=preview,
                               score=round(score, 3),
                               centers=centers,
                               n_clusters=n_clusters)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
