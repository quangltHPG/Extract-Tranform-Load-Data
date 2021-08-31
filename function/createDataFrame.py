#from datetime import datetime
#start = datetime.now()
#a = 0
import pandas as pd
def create_dataframe(filename):

    file = filename
    df = pd.read_csv(file)
    thoiGian = []
    nameMe = []
    ca = []
    meGang = []
    thoiGianRaGang = []
    gianCach = []
    thoiGianRaXi = []
    tiLeThoiGianRaXiTrenRaGang = []
    doSauLoGang = []
    luongBunBit = []
    sanLuongGang = []
    sanRaGang = []
    nhietDoGang = []
    soThung = []
    khoiLuong = []
    loaiGang = []
    TPHH_C = []
    TPHH_Si = []
    TPHH_Mn = []
    TPHH_S = []
    TPHH_P = []
    TPHH_Ti = []
    TPHH_SiO2 = []
    TPHH_Al2O3 = []
    TPHH_CaO = []
    TPHH_MgO = []
    TPHH_TiO2 = []
    TPHH_Ri = []
    for i in range(df.shape[0]):
        data = df.loc[i]
        strData = str(data[0])
        strData = strData.replace('[m.]', '')
        strData = strData.split(";")
        thoiGian.append(strData[0])
        nameMe.append(strData[2] + strData[12])
        ca.append(strData[1])
        meGang.append(strData[2])
        thoiGianRaGang.append(strData[3])
        gianCach.append(strData[4])
        thoiGianRaXi.append(strData[5])
        tiLeThoiGianRaXiTrenRaGang.append(strData[6])
        doSauLoGang.append(strData[7])
        luongBunBit.append(strData[8])
        sanLuongGang.append(strData[9])
        sanRaGang.append(strData[10])
        nhietDoGang.append(strData[11])
        soThung.append(strData[12])
        khoiLuong.append(strData[13])
        loaiGang.append(strData[14])
        TPHH_C.append(strData[15])
        TPHH_Si.append(strData[16])
        TPHH_Mn.append(strData[17])
        TPHH_S.append(strData[18])
        TPHH_P.append(strData[19])
        TPHH_Ti.append(strData[20])
        TPHH_SiO2.append(strData[21])
        TPHH_Al2O3.append(strData[22])
        TPHH_CaO.append(strData[23])
        TPHH_MgO.append(strData[24])
        TPHH_TiO2.append(strData[25])
        TPHH_Ri.append(strData[26])
    luyenGang_df = pd.DataFrame({'date':thoiGian,
                            'ten':nameMe,
                            'Ca':ca,
                            'mẻ Gang':meGang,
                            'thời Gian Ra Gang': thoiGianRaGang,
                            'giản Cách':gianCach,
                            'thời Gian Ra Xỉ':thoiGianRaXi,
                            'Thời Gian Ra Xỉ trên Ra Gang':tiLeThoiGianRaXiTrenRaGang,
                            'độ Sâu Lỗ Gang':doSauLoGang,
                            'lượng Bùn Bịt':luongBunBit,
                            'sản Lượng Gang':sanLuongGang,
                            'sàn ra Gang':sanRaGang,
                            'nhiệt độ Gang':nhietDoGang,
                            'số thùng':soThung,
                            'khối lượng':khoiLuong,
                            'loại Gang':loaiGang,
                            'Thành phần hóa học C':TPHH_C,
                            'Thành phần hóa học Si':TPHH_Si,
                            'Thành phần hóa học Mn':TPHH_Mn,
                            'Thành phần hóa học S':TPHH_S,
                            'Thành phần hóa học P':TPHH_P,
                            'Thành phần hóa học Ti':TPHH_Ti,
                            'Thành phần hóa học SiO2':TPHH_SiO2,
                            'Thành phần hóa học Al2O3':TPHH_Al2O3,
                            'Thành phần hóa học CaO':TPHH_CaO,
                            'Thành phần hóa học MgO':TPHH_MgO,
                            'Thành phần hóa học TiO2':TPHH_TiO2,
                            'Thành phần hóa học Ri':TPHH_Ri})
    #print (luyenGang_df.shape)
    _luyenGang_df = luyenGang_df.sort_values("date")
    
    #print (_luyenGang_df.shape)
    #__luyenGang_df = _luyenGang_df.drop_duplicates(subset=['ten'], keep='last')
    #print (__luyenGang_df.shape)
    #print (datetime.now() - start)
    return _luyenGang_df

def create_dataframe_from_str(strData):

    thoiGian = []
    nameMe = []
    ca = []
    meGang = []
    thoiGianRaGang = []
    gianCach = []
    thoiGianRaXi = []
    tiLeThoiGianRaXiTrenRaGang = []
    doSauLoGang = []
    luongBunBit = []
    sanLuongGang = []
    sanRaGang = []
    nhietDoGang = []
    soThung = []
    khoiLuong = []
    loaiGang = []
    TPHH_C = []
    TPHH_Si = []
    TPHH_Mn = []
    TPHH_S = []
    TPHH_P = []
    TPHH_Ti = []
    TPHH_SiO2 = []
    TPHH_Al2O3 = []
    TPHH_CaO = []
    TPHH_MgO = []
    TPHH_TiO2 = []
    TPHH_Ri = []

    strData = strData.replace('[m.]', '')
    strData = strData.split(";")
    thoiGian.append(strData[0])
    nameMe.append(strData[2] + strData[12])
    ca.append(strData[1])
    meGang.append(strData[2])
    thoiGianRaGang.append(strData[3])
    gianCach.append(strData[4])
    thoiGianRaXi.append(strData[5])
    tiLeThoiGianRaXiTrenRaGang.append(strData[6])
    doSauLoGang.append(strData[7])
    luongBunBit.append(strData[8])
    sanLuongGang.append(strData[9])
    sanRaGang.append(strData[10])
    nhietDoGang.append(strData[11])
    soThung.append(strData[12])
    khoiLuong.append(strData[13])
    loaiGang.append(strData[14])
    TPHH_C.append(strData[15])
    TPHH_Si.append(strData[16])
    TPHH_Mn.append(strData[17])
    TPHH_S.append(strData[18])
    TPHH_P.append(strData[19])
    TPHH_Ti.append(strData[20])
    TPHH_SiO2.append(strData[21])
    TPHH_Al2O3.append(strData[22])
    TPHH_CaO.append(strData[23])
    TPHH_MgO.append(strData[24])
    TPHH_TiO2.append(strData[25])
    TPHH_Ri.append(strData[26])
    luyenGang_df = pd.DataFrame({'date':thoiGian,
                            'ten':nameMe,
                            'Ca':ca,
                            'mẻ Gang':meGang,
                            'thời Gian Ra Gang': thoiGianRaGang,
                            'giản Cách':gianCach,
                            'thời Gian Ra Xỉ':thoiGianRaXi,
                            'Thời Gian Ra Xỉ trên Ra Gang':tiLeThoiGianRaXiTrenRaGang,
                            'độ Sâu Lỗ Gang':doSauLoGang,
                            'lượng Bùn Bịt':luongBunBit,
                            'sản Lượng Gang':sanLuongGang,
                            'sàn ra Gang':sanRaGang,
                            'nhiệt độ Gang':nhietDoGang,
                            'số thùng':soThung,
                            'khối lượng':khoiLuong,
                            'loại Gang':loaiGang,
                            'Thành phần hóa học C':TPHH_C,
                            'Thành phần hóa học Si':TPHH_Si,
                            'Thành phần hóa học Mn':TPHH_Mn,
                            'Thành phần hóa học S':TPHH_S,
                            'Thành phần hóa học P':TPHH_P,
                            'Thành phần hóa học Ti':TPHH_Ti,
                            'Thành phần hóa học SiO2':TPHH_SiO2,
                            'Thành phần hóa học Al2O3':TPHH_Al2O3,
                            'Thành phần hóa học CaO':TPHH_CaO,
                            'Thành phần hóa học MgO':TPHH_MgO,
                            'Thành phần hóa học TiO2':TPHH_TiO2,
                            'Thành phần hóa học Ri':TPHH_Ri})
    #print (luyenGang_df.shape)
    _luyenGang_df = luyenGang_df.sort_values("date")
    
    #print (_luyenGang_df.shape)
    #__luyenGang_df = _luyenGang_df.drop_duplicates(subset=['ten'], keep='last')
    #print (__luyenGang_df.shape)
    #print (datetime.now() - start)
    return _luyenGang_df