from categories.сategory import Category

class Spendings_Category(Category):
    CATEGORY_TYPE= "SPENDINGS CATEGORY"

    def get_type(self):
        return self.CATEGORY_TYPE
