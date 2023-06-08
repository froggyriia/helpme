from  __future__ import annotations # теперь в хинтах можем писать даже еще не созданные классы (и вообще всякую дичь)
def func(a: list[int]):
    pass
#ну или нельзя хуйняя получилась
print(func.__annotations__['a']())