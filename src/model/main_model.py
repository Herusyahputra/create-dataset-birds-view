class Model:
    def __init__(self):
        super(Model, self).__init__()
        self.__image_original = [None] * 4
        self.__list_image_surrounding = [None] * 4
        self.__image_surrounding = None

        self.__list_image_anypoint = [None] * 4
        self.__image_bird_view = None
        self.__image_bird_view_overlay = None
        self.__image_bird_view_cropping = None

        self.__list_data_selected_point = None

        self.__list_image_wide_view = [None] * 4
        self.__list_image_side_view = [None] * 4
        self.__image_side_view = None

        self.__properties_image = None

    @property
    def list_data_selected_point(self):
        return self.__list_data_selected_point

    @list_data_selected_point.setter
    def list_data_selected_point(self, value):
        self.__list_data_selected_point = value

    @property
    def image_original(self):
        return self.__image_original

    @image_original.setter
    def image_original(self, value):
        self.__image_original = value

    # ----------------------------------- surrounding view -----------------------------
    @property
    def image_surrounding(self):
        return self.__image_surrounding

    @image_surrounding.setter
    def image_surrounding(self, value):
        self.__image_surrounding = value

    @property
    def list_image_surrounding(self):
        return self.__list_image_surrounding

    @list_image_surrounding.setter
    def list_image_surrounding(self, value):
        self.__list_image_surrounding = value

    # ----------------------------------- wide view -----------------------------
    @property
    def list_image_wide_view(self):
        return self.__list_image_wide_view

    @list_image_wide_view.setter
    def list_image_wide_view(self, value):
        self.__list_image_wide_view = value

    # ----------------------------------- bird view ----------------------------
    @property
    def list_image_anypoint(self):
        return self.__list_image_anypoint

    @list_image_anypoint.setter
    def list_image_anypoint(self, value):
        self.__list_image_anypoint = value

    @property
    def image_bird_view_overlay(self):
        return self.__image_bird_view_overlay

    @image_bird_view_overlay.setter
    def image_bird_view_overlay(self, value):
        self.__image_bird_view_overlay = value

    @property
    def image_bird_view(self):
        return self.__image_bird_view

    @image_bird_view.setter
    def image_bird_view(self, value):
        self.__image_bird_view = value

    @property
    def image_bird_view_cropping(self):
        return self.__image_bird_view_cropping

    @image_bird_view_cropping.setter
    def image_bird_view_cropping(self, value):
        self.__image_bird_view_cropping = value

    # ---------------------------- side image ----------------------------
    @property
    def list_image_side_view(self):
        return self.__list_image_side_view

    @list_image_side_view.setter
    def list_image_side_view(self, value):
        self.__list_image_side_view = value

    @property
    def image_side_view(self):
        return self.__image_side_view

    @image_side_view.setter
    def image_side_view(self, value):
        self.__image_side_view = value

    # ---------------------------- properties image ----------------------------
    @property
    def properties_image(self):
        return self.__properties_image

    @properties_image.setter
    def properties_image(self, value):
        self.__properties_image = value
