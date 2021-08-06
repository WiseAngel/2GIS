class DataGenerator():

    def foo(self, value):
        num = len(max(value, key=len))
        list_by_number_of_endpoints = []
        for i in range(num):
            list_by_number_of_endpoints.append([])
        return list_by_number_of_endpoints

    def urovnyat_dlinu_massivov(self, value):
        max_value_len = len(max(value, key=len))
        while not len(value[0]) == max_value_len:
            for i, v in enumerate(value):
                if len(v) < max_value_len:
                    diff = max_value_len - len(v)
                    v += v[:diff]
        return(value)

    def bar(self, *value):
        list_by_number_of_endpoints = self.foo(value)
        value = self.urovnyat_dlinu_massivov(value)
        for i, e in enumerate(value):
            for q, v in enumerate(e):
                list_by_number_of_endpoints[q].append(v)
        return (list_by_number_of_endpoints)

