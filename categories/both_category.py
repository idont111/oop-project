from categories.сategory import Category


class Both_Catgory(Category):
    CATEGORY_TYPE = "BOTH CATEGORY"

    def get_type(self):
        return self.CATEGORY_TYPE
