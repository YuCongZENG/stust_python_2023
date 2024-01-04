class FriedChicken:
    def __init__(self, flavor, size, time, price, special_sauce):
        self.flavor = flavor #炸雞的口味
        self.size = size #炸雞的份量
        self.time = time #炸炸雞所需時間
        self.price = price #一份炸雞的價格
        self.special_sauce = special_sauce #炸雞的醬料

    def display_info(self):#印出屬性
        print(f"炸雞的口味: {self.flavor}")
        print(f"炸雞的份量: {self.size}")
        print(f"炸炸雞所需時間: {self.time}")
        print(f"一份炸雞的價格: {self.price}元")
        print(f"炸雞的醬料: {self.special_sauce}")
        print("")
    
    def chang_size(self,new_size): #更改大小份
        self.size=new_size

    def chang_flavor(self,new_flavor): #更改炸雞的口味
        self.flavor=new_flavor

    def chang_price(self,new_price): #更改一份炸雞的價格
        self.price=new_price

# 建立四個物件
chicken1 = FriedChicken(flavor="大辣",size="特大份",time="10分鐘",price= 120,special_sauce="BBQ")#建立炸機的物件
chicken2 = FriedChicken(flavor="中辣",size="大份",time=  "8分鐘",price= 100,special_sauce= "Honey Mustard")
chicken3 = FriedChicken(flavor="小辣",size="中份",time=  "6分鐘",price= 80,special_sauce= "Garlic Aioli")
chicken4 = FriedChicken(flavor="微辣",size="小份",time=  "4分鐘",price= 50,special_sauce= "Teriyaki Glaze")

# 呼叫副函式

print("Chicken 1 Information:")
chicken1.display_info()#未改
chicken1.chang_size("大份")
chicken1.chang_flavor("微辣")
chicken1.chang_price(100)
chicken1.display_info()#改完

print("Chicken 2 Information:")
chicken2.display_info()#未改
chicken2.chang_size("中份")
chicken2.chang_flavor("大辣")
chicken2.chang_price(80)
chicken2.display_info()#改完

print("Chicken 3 Information:")
chicken3.display_info()#未改
chicken3.chang_size("中份")
chicken3.chang_flavor("微辣")
chicken3.chang_price(50)
chicken3.display_info()#改完

print("Chicken 4 Information:")
chicken4.display_info()#未改
chicken4.chang_size("特大份")
chicken4.chang_flavor("小辣")
chicken4.chang_price(120)
chicken4.display_info()#改完