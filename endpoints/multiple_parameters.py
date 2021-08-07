class DataGenerator():

    max_value_len: int

    def get_max_len(self, value):
        self.max_value_len = len(max(value, key=len))
        return self.max_value_len

    def fill_list(self, num):
        list_of_lists_by_number_of_endpoints = [[] for i in range(num)]
        return list_of_lists_by_number_of_endpoints

    def equalize_length_of_lists(self, value):
        sorted_list = sorted(value, key=len)
        while not len(sorted_list[0]) == self.max_value_len:
            sorted_list = sorted(value, key=len)
            for v in value:
                if len(v) < self.max_value_len:
                    diff = self.max_value_len - len(v)
                    v += v[:diff]
        return(value)

    def bar(self, *value):
        max_len = self.get_max_len(value)
        list_by_number_of_endpoints = self.fill_list(max_len)
        equalized_lists_data  = self.equalize_length_of_lists(value)
        for e in equalized_lists_data :
            for i, v in enumerate(e):
                list_by_number_of_endpoints[i].append(v)
        return (list_by_number_of_endpoints)
