from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nChương trình quản lý sinh viên")
    print("***************************************************")
    print("**1. Nhập sinh viên                              **")                 
    print("**2. Cập nhật thông tin sinh viên bởi ID         **")
    print("**3. Xoá sinh viên                               **")                        
    print("**4. Tìm kiếm sinh viên                          **")
    print("**5. Sắp xếp sinh viên theo điểm trung bình      **")
    print("**6. Sắp xếp sinh viên theo tên chuyên ngành     **")
    print("**7. Hiển thị danh sách sinh viên                **")
    print("**0. Thoát                                       **")
    print("***************************************************")
    
    key = int(input("Nhập lựa chọn của bạn: "))
    
    if (key == 1):
        print("\n1. Thêm sinh viên")
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công!")
        
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhât thông tin sinh viên")
            print("\nNhập ID:")
            ID = int(input(""))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh viên rỗng")
            
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoá sinh viên")
            print("\nNhập ID:")
            ID = int(input(""))
            if (qlsv.deleteSinhVien(ID)):
                print("Sinh viên có ID = {} đã được xóa" .format(ID))
            else:
                print("Sinh viên có ID = {} không tồn tại" .format(ID))
        else:
            print("\nDanh sach sinh viên rỗng")
            
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên")
            print("\nNhập tên để tìm kiếm:")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showList(searchResult)
        else:
            print("\nDanh sach sinh viên rỗng")
            
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình")
            qlsv.sortByDiemTB()
            qlsv.showList(qlsv.listSinhVien)
        else:
            print("\nDanh sach sinh viên rỗng")
            
    elif (key == 6):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên chuyên ngành")
            qlsv.sortByName()
            qlsv.showList(qlsv.listSinhVien)
        else:
            print("\nDanh sach sinh viên rỗng")
            
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh viên rỗng")
            
    elif (key == 0):
        print("\nThoát chương trình")
        break
    
    else:
        print("\nLựa chọn không hợp lệ, vui lòng nhập lại")
        print("\nHãy chọn chức năng trong menu")