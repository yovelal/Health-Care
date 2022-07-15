import unittest
from Modules import Function


class Function_Test(unittest.TestCase):

    def test_CheckUserName(self):
        self.assertEqual(Function.CheckUserName("qwert"), False)
        self.assertEqual(Function.CheckUserName("wertyuwerr"), False)
        self.assertEqual(Function.CheckUserName("qwer123"), False)
        self.assertEqual(Function.CheckUserName("wertyu%"), False)
        self.assertEqual(Function.CheckUserName("yovel12"), True)
        self.assertEqual(Function.CheckUserName("Yovelal"), True)

    def test_CheckID(self):
        self.assertEqual(Function.CheckID("12345678"), False)
        self.assertEqual(Function.CheckID("1234567890"), False)
        self.assertEqual(Function.CheckID("123456a78"), False)
        self.assertEqual(Function.CheckID("123123456"), True)

    def test_CheckPassword(self):
        self.assertEqual(Function.CheckPassword("11qq##"), False)
        self.assertEqual(Function.CheckPassword("1111qqqq####"), False)
        self.assertEqual(Function.CheckPassword("qwert12"), False)
        self.assertEqual(Function.CheckPassword("qwertyui#"), False)
        self.assertEqual(Function.CheckPassword("1234567#"), False)
        self.assertEqual(Function.CheckPassword("1qqqqqq#"), True)

    def test_CheckUserFullName(self):
        self.assertEqual(Function.CheckUserFullName("a"), False)
        self.assertEqual(Function.CheckUserFullName("yov6l"), False)
        self.assertEqual(Function.CheckUserFullName("yovel"), True)


    def test_CheckDictionaryValues1(self):
       self.assertEqual(Function.CheckDictionaryValues1({"WBC":"-34","Neut":"34","Lymph":"34","RBC":"34","HCT":"34","Urea":"34","Hb":"34","Creatinine":"34","Iron":"34","HDL":"34","AP":"34"}), 2)
       self.assertEqual(Function.CheckDictionaryValues1({"WBC":"A","Neut":"34","Lymph":"34","RBC":"34","HCT":"34","Urea":"34","Hb":"34","Creatinine":"34","Iron":"34","HDL":"34","AP":"34"}), 1)
       self.assertEqual(Function.CheckDictionaryValues1({"WBC":"34","Neut":"34","Lymph":"34","RBC":"34","HCT":"34","Urea":"34","Hb":"34","Creatinine":"34","Iron":"34","HDL":"34","AP":"34"}), 3)

    def test_Return_LOWorHIGHorNORMAL(self):
        self.assertEqual(Function.Return_LOWorHIGHorNORMAL(10,20,15), "NORMAL")
        self.assertEqual(Function.Return_LOWorHIGHorNORMAL(10,20,30), "HIGH")
        self.assertEqual(Function.Return_LOWorHIGHorNORMAL(10,20,5), "LOW")


    def test_WBC(self):
        self.assertEqual(Function.WBC(4600, 18), "NORMAL")
        self.assertEqual(Function.WBC(4600, 4), "LOW")
        self.assertEqual(Function.WBC(17000, 2), "NORMAL")


    def test_Naut(self):
        self.assertEqual(Function.Naut(30), "NORMAL")
        self.assertEqual(Function.Naut(27), "LOW")
        self.assertEqual(Function.Naut(55), "HIGH")

    def test_Lymph(self):
        self.assertEqual(Function.Lymph(53), "NORMAL")
        self.assertEqual(Function.Lymph(36), "NORMAL")
        self.assertEqual(Function.Lymph(35), "LOW")
        self.assertEqual(Function.Lymph(53), "HIGH")

    def test_RBC(self):
        self.assertEqual(Function.RBC(5), "NORMAL")
        self.assertEqual(Function.RBC(4.4), "LOW")
        self.assertEqual(Function.RBC(6.1), "HIGH")


    def test_HCT(self):
        self.assertEqual(Function.HCT(32,"F"), "LOW")
        self.assertEqual(Function.HCT(48,"F"), "HIGH")
        self.assertEqual(Function.HCT(40,"F"), "NORMAL")

        self.assertEqual(Function.HCT(36,"M"), "LOW")
        self.assertEqual(Function.HCT(55,"M"), "HIGH")
        self.assertEqual(Function.HCT(40,"M"), "NORMAL")

    def test_Urea(self):
        self.assertEqual(Function.Urea(18, "Middle-Eastren"), "LOW")
        self.assertEqual(Function.Urea(48, "Middle-Eastren"), "HIGH")
        self.assertEqual(Function.Urea(20, "Middle-Eastren"), "NORMAL")

        self.assertEqual(Function.Urea(16, "Other"), "LOW")
        self.assertEqual(Function.Urea(44, "Other"), "HIGH")
        self.assertEqual(Function.Urea(18, "Other"), "NORMAL")

    def test_Hb(self):
        self.assertEqual(Function.Hb(11,16,"M"), "LOW")
        self.assertEqual(Function.Hb(15.6,16,"M"), "HIGH")
        self.assertEqual(Function.Hb(11.9,16,"M"), "NORMAL")

        self.assertEqual(Function.Hb(11.9,19,"F"), "LOW")
        self.assertEqual(Function.Hb(16.1,19,"F"), "HIGH")
        self.assertEqual(Function.Hb(15.6,19,"F"), "NORMAL")

        self.assertEqual(Function.Hb(11,19,"M"), "LOW")
        self.assertEqual(Function.Hb(19,19,"M"), "HIGH")
        self.assertEqual(Function.Hb(17,19,"M"), "NORMAL")

    def test_Creatinine(self):
        self.assertEqual(Function.Creatinine(0.1,1), "LOW")
        self.assertEqual(Function.Creatinine(0.6,1), "HIGH")
        self.assertEqual(Function.Creatinine(0.3,1), "NORMAL")

        self.assertEqual(Function.Creatinine(0.4,17), "LOW")
        self.assertEqual(Function.Creatinine(1.1,17), "HIGH")
        self.assertEqual(Function.Creatinine(0.6,17), "NORMAL")

        self.assertEqual(Function.Creatinine(0.4,59), "LOW")
        self.assertEqual(Function.Creatinine(1.1,59), "HIGH")
        self.assertEqual(Function.Creatinine(0.7,59), "NORMAL")

        self.assertEqual(Function.Creatinine(0.5,60), "LOW")
        self.assertEqual(Function.Creatinine(1.3,60), "HIGH")
        self.assertEqual(Function.Creatinine(1.1,60), "NORMAL")

    def test_Iron(self):
        self.assertEqual(Function.Iron(47, "F"), "LOW")
        self.assertEqual(Function.Iron(129, "F"), "HIGH")
        self.assertEqual(Function.Iron(100, "F"), "NORMAL")

        self.assertEqual(Function.Iron(59, "M"), "LOW")
        self.assertEqual(Function.Iron(161, "M"), "HIGH")
        self.assertEqual(Function.Iron(100, "M"), "NORMAL")

    def test_HDL(self):
        self.assertEqual(Function.HDL(33, "F","Other"), "LOW")
        self.assertEqual(Function.HDL(83, "F","Other"), "HIGH")
        self.assertEqual(Function.HDL(70, "F","Other"), "NORMAL")

        self.assertEqual(Function.HDL(28, "M", "Other"), "LOW")
        self.assertEqual(Function.HDL(62, "M", "Other"), "HIGH")
        self.assertEqual(Function.HDL(50, "M", "Other"), "NORMAL")

        self.assertEqual(Function.HDL(40, "F", "Ethiopian"), "LOW")
        self.assertEqual(Function.HDL(99, "F", "Ethiopian"), "HIGH")
        self.assertEqual(Function.HDL(83, "F", "Ethiopian"), "NORMAL")

    def test_AP(self):
        self.assertEqual(Function.AP(29, "Other"), "LOW")
        self.assertEqual(Function.AP(91,"Other"), "HIGH")
        self.assertEqual(Function.AP(59, "Other"), "NORMAL")

        self.assertEqual(Function.AP(59, "Middle-Eastren"), "LOW")
        self.assertEqual(Function.AP(121,"Middle-Eastren"), "HIGH")
        self.assertEqual(Function.AP(100, "Middle-Eastren"), "NORMAL")





if __name__ == '__main__':
    unittest.main()
