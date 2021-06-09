class buckets():
    def __init__(self, tara):
        """
        :param tara: выбираем объем для ведра
        """
        self.bucket_tara = tara
        self.bucket_napolnen = 0

    def result(self):
        """
        :return: посмотреть состояние ведер
        """
        return print(f"""В {a.bucket_tara}-литровом ведре {a.bucket_napolnen} литров
В {b.bucket_tara}-литровом ведре {b.bucket_napolnen} литра""")

    def popoln(self):
        """
        :return: пополняем ведро
        """
        self.bucket_napolnen = self.bucket_tara

    def out(self):
        """
        :return: выливаем ведро
        """
        self.bucket_napolnen = 0

    def pereliv_v5(self):
        """
        :return: переливаем с 3-х в 5-ти литровое ведро
        """
        a.bucket_napolnen = a.bucket_napolnen + b.bucket_napolnen
        b.bucket_napolnen = 0
        if a.bucket_napolnen > 5:
            b.bucket_napolnen = a.bucket_napolnen - 5
            a.bucket_napolnen = 5

    def pereliv_v3(self):
        """
        :return: переливаем с 5-ти в 3-х литровое ведро
        """
        b.bucket_napolnen = b.bucket_napolnen + a.bucket_napolnen
        a.bucket_napolnen = 0
        if b.bucket_napolnen > 3:
            a.bucket_napolnen = b.bucket_napolnen - 3
            b.bucket_napolnen = 3

a = buckets(5)
b = buckets(3)


