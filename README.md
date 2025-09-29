Bài toán k-means

Trong lĩnh vực kinh doanh, việc hiểu rõ hành vi tiêu dùng của khách hàng là chìa khóa để xây dựng chiến lược tiếp thị hiệu quả. Bài toán đặt ra là phân nhóm khách hàng dựa trên các yếu tố như thu nhập hằng năm và mức chi tiêu.

Mục đích nghiên cứu

Nhận diện những nhóm khách hàng có đặc điểm tương đồng.
Hỗ trợ doanh nghiệp thiết kế các chương trình khuyến mãi, dịch vụ và sản phẩm phù hợp.
Cải thiện trải nghiệm khách hàng và tối ưu chi phí tiếp thị.

Thuật toán áp dụng: K-Means Clustering
K-Means là một thuật toán học không giám sát, được dùng phổ biến trong phân cụm dữ liệu. Nguyên lý hoạt động của K-Means:

Chọn số cụm K cần phân chia.
Khởi tạo ngẫu nhiên K tâm cụm.
Mỗi điểm dữ liệu được gán vào cụm có tâm gần nhất.
Tính lại tâm cụm mới dựa trên trung bình của các điểm trong cụm.
Lặp lại quá trình cho đến khi các tâm cụm ổn định.

Phương pháp hỗ trợ lựa chọn K

Elbow Method: Quan sát đồ thị SSE để tìm "khuỷu tay", tức số cụm hợp lý.
Silhouette Score: Kiểm tra mức độ phân tách giữa các cụm để đánh giá chất lượng phân cụm.

Công cụ và thư viện sử dụng

Ngôn ngữ: Python.
Thư viện:
pandas để xử lý dữ liệu.
matplotlib, seaborn để vẽ biểu đồ.
scikit-learn để triển khai KMeans, StandardScaler và Silhouette Score.
Flask: xây dựng giao diện web trực quan, hiển thị kết quả phân cụm.

Kết quả kỳ vọng
Mô hình sẽ phân tách tập khách hàng thành nhiều nhóm rõ ràng, ví dụ:

Nhóm thu nhập cao nhưng chi tiêu thấp.
Nhóm thu nhập trung bình, chi tiêu cao.
Nhóm thu nhập thấp, chi tiêu hạn chế.

<img width="765" height="444" alt="{C5A50692-EACC-4C93-9DC8-73614AF415C4}" src="https://github.com/user-attachments/assets/b98044fc-a7d0-4e67-beb5-02f79c2d0321" />
