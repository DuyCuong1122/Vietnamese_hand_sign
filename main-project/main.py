import os


# Lấy danh sách các chữ cái trong bảng chữ cái tiếng Anh
alphabet = "abcdđeghiklmnopqrstuvxy"

# Đường dẫn đến thư mục chứa các tệp video


# Đường dẫn đến thư mục chứa các thư mục "Class + X"
target_directory = r"F:\Projects\vietnamese_hand_sign-main\classes_point"  # Thay thế bằng đường dẫn thực tế của bạn

# Lấy danh sách các tệp video trong thư mục video


# Kiểm tra xem số lượng video có đủ để thêm vào từng thư mục không
for i in range(len(alphabet)):
        letter = alphabet[i]
        folder_name = "Class " + letter.upper()  # Tạo tên thư mục
        folder_path = os.path.join(target_directory, folder_name)  # Đường dẫn đến thư mục mới

        # Kiểm tra xem thư mục đã tồn tại chưa
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)  # Tạo thư mục mới
            print("Created folder:", folder_path)

       