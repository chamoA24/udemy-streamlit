class Person:
    #初期設定
    def __init__(self, name, nationality, age):
        self.name = name
        self.nationality = nationality
        self.age = age

    def __call__(self,name):
        print(f'{name}さんこんにちは。私は{self.name}です。')

    def say_hello(self,name):
        print(f'{name}さんこんにちは。私は{self.name}です。')

ozaki = Person(name='尾﨑', nationality='日本', age=27)
mike = Person(name='マイク', nationality='アメリカ', age=23)

ozaki.say_hello(name = '鈴木')

ozaki(name='佐藤')