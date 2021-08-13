class DataGenerator():
    def __init__(self, *value):
        self.max_value_len = 0
        self.value = value
        self.list_of_lists_by_number_of_endpoints = [] 

    def get_max_len(self,value):
        self.max_value_len = len(max(self.value, key=len))
        return self.max_value_len

    def fill_list(self, num):
        self.list_of_lists_by_number_of_endpoints = [[] for _ in range(self.max_value_len)]
        return self.list_of_lists_by_number_of_endpoints

    # def equalize_length_of_lists(self, value):
    #     sorted_list = sorted(self.value, key=len)
    #     while not len(sorted_list[0]) == self.max_value_len:
    #         sorted_list = sorted(self.value, key=len)
    #         for v in self.value:
    #             if len(v) < self.max_value_len:
    #                 diff = self.max_value_len - len(v)
    #                 v += v[:diff]
    #     return(self.value)

    def equalize_length_of_lists(self, value):
        value  = self.value
        for v in value:
            if len(v) < self.max_value_len:
                diff = self.max_value_len - len(v)
                v += v[:diff]
        return(value)

    def bar(self):
        print(self.value)
        self.get_max_len(self.value)
        self.fill_list(self.max_value_len)
        equalized_lists_data  = self.equalize_length_of_lists(self.value)
        print(equalized_lists_data)
        for e in equalized_lists_data :
            for i, v in enumerate(e):
                self.list_of_lists_by_number_of_endpoints[i].append(v)
        return (self.list_of_lists_by_number_of_endpoints)
