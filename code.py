# from collections import defaultdict

# # Đọc dữ liệu từ file text và chuyển đổi thành list các dòng
# with open('C:\\Users\\admin\\Desktop\\data.txt', 'r') as file:
#     lines = file.readlines()

# # # Tạo một dictionary để lưu trữ tổng thời gian và số lượng cho mỗi VMID
# # vmid_data = defaultdict(lambda: {'total_time': 0, 'count': 0})

# # # Lặp qua từng dòng trong dữ liệu và tính tổng thời gian và số lượng cho mỗi VMID
# # for line in lines[1:]:  # Bỏ qua dòng tiêu đề
# #     cloudlet_id, status, datacenter_id, vmid, time, start_time, finish_time = line.strip().split()
# #     vmid_data[int(vmid)]['total_time'] += float(time)
# #     vmid_data[int(vmid)]['count'] += 1

# # # Tính toán thời gian trung bình cho mỗi VMID
# # average_times = {}
# # for vmid, data in vmid_data.items():
# #     if data['count'] > 0:
# #         average_times[vmid] = data['total_time'] / data['count']

# # # Sắp xếp kết quả theo VMID
# # sorted_average_times = sorted(average_times.items())

# # # In ra kết quả đã sắp xếp
# # for vmid, average_time in sorted_average_times:
# #     print(f"VMID {vmid}: Average Time = {average_time:.2f}")




# # Khởi tạo biến tổng thời gian và số lượng VMID
# total_time = 0
# total_count = 0

# # Lặp qua từng dòng trong dữ liệu và tính tổng thời gian và số lượng VMID
# for line in lines[1:]:  # Bỏ qua dòng tiêu đề
#     _, _, _, _, time, _, _ = line.split()
#     total_time += float(time)
#     total_count += 1

# # Tính toán thời gian trung bình cho toàn bộ VMID
# if total_count > 0:
#     average_time = total_time / total_count
#     print(f"Average Time for all VMIDs: {average_time:.2f}")
# else:
#     print("No data available to compute average time.")



# import matplotlib.pyplot as plt

# # Dữ liệu thời gian trung bình cho 2VM và 4VM
# vm_2 = [471.41, 920.70, 1499.60, 1900.95, 2436.17, 2879.73, 3423.56, 3954.36, 4425.79, 5096.61]
# vm_4 = [280.96, 502.17, 885.18, 1129.79, 1429.03, 2073.37, 2186.85, 2308.89, 2553.25, 2889.56]

# # Tạo danh sách số lượng VMID (tương ứng với số lượng dữ liệu)
# x_values = list(range(1, len(vm_2) + 1))

# # Vẽ biểu đồ
# plt.plot(x_values, vm_2, label='2VM', marker='o')
# plt.plot(x_values, vm_4, label='4VM', marker='o')

# # Đặt tên cho trục x và trục y
# plt.xlabel('Number of VMs')
# plt.ylabel('Average Time')

# # Đặt tiêu đề cho biểu đồ
# plt.title('Average Time for 2VM and 4VM')

# # Thêm chú thích
# plt.legend()

# # Hiển thị biểu đồ
# plt.grid(True)
# plt.show()

import matplotlib.pyplot as plt

# Dữ liệu thời gian trung bình cho 2VM và 4VM
vm_2 = [471.41, 920.70, 1499.60, 1900.95, 2436.17, 2879.73, 3423.56, 3954.36, 4425.79, 5096.61]
vm_4 = [280.96, 502.17, 885.18, 1129.79, 1429.03, 2073.37, 2186.85, 2308.89, 2553.25, 2889.56]

# Tạo danh sách số lượng cloudlet (tương ứng với số lượng dữ liệu)
x_values = list(range(120, 1201, 120))  # Bắt đầu từ 120, kết thúc ở 1200, bước nhảy là 120

# Vẽ biểu đồ
plt.plot(x_values, vm_2, label='2VM', marker='o')
plt.plot(x_values, vm_4, label='4VM', marker='o')

# Đặt tên cho trục x và trục y
plt.xlabel('Number of Cloudlets')
plt.ylabel('Average Time')

# Đặt tiêu đề cho biểu đồ
plt.title('Average Time for 2VM and 4VM')

# Thêm chú thích
plt.legend()

# Hiển thị biểu đồ
plt.grid(True)
plt.show()
