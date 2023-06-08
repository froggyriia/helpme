# объукт Человек и Мемы. кто то листает одни мемы другой другие. из разных источников.
from PIL import Image
from dataclasses import dataclass, field
import requests


@dataclass
class Meme:
    link = 'https://api.thecatapi.com/v1/images/search'
    image: Image = None
    likes_amount: int = 0
    text: str = ""  # подпись
    is_funny: bool = False

    def show_meme(self, consumer: 'Person'):
        consumer.consume(self)

        answer: list[dict: str | int] = requests.get(Meme.link).json()
        url = answer[0].get('url')
        # print(answer, url, sep= '\n') я чисто чекнула то у менявообще в переменных или хуйня какая-то лежит
        frmt = url.rsplit(".")[-1]
        data = requests.get(url).content
        f = open(f'img.{frmt}', 'wb')
        f.write(data)
        f.close()
        img = Image.open(f'img.{frmt}')
        img.show()

    def like_meme(self):
        self.likes_amount += 1


@dataclass
class Person:
    name: str
    friends: list['Person'] = field(default_factory=list)

    def add_friend(self, friend: 'Person'):
        self.friends.append(friend)

    def consume(self, meme: Meme):

        if meme.is_funny:
            print(f'{self.name}: hahhahahah')
            for friend in self.friends:
                self.share_meme(friend, meme)

    def react_on_stupid_meme(self, meme: Meme):
        if meme.is_funny:
            print(f'< {self.name}: АХПХПХЗРАПХЗРЗПОЗХНОХГОТЫЫЫЫЫЫ')
        else:
            print(f'< {self.name}: lol))')
        meme.like_meme()

    def share_meme(self, target: 'Person', meme: Meme):
        target.react_on_stupid_meme(meme)


#
friend1 = Person('biba')
# friend2 = Person('boba')
# friend3 = Person('Hitler')
# friend3.add_friend(friend1)
# friend1.add_friend(friend3)
# friend1.add_friend(friend2)
# print(friend1.friends)
# uncat_meme = Meme(text='unfunny text')
#
cat_meme = Meme(text='funny text', is_funny=True)
# friend1.consume(uncat_meme)
# friend1.share_meme(friend2, uncat_meme)
# friend1.consume(cat_meme)
# cat_meme.like_meme()
# print(cat_meme.likes_amount)
cat_meme.show_meme(friend1)
