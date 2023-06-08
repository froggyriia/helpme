n = 2
a = [None] * n
l = 0
def add_elem(x):
    global l, n, a, a_new
    if l == n:
        n = 2 * n
        a_new = [None] * n
        for i in range(l):
            a_new[i] = a[i]
        a = a_new

    a[l] = x
    l += 1

def print_list():
    for i in range(l):
        print(a[i], end=' ')

add_elem(10)
add_elem(11)
add_elem(13)

g = print_list
g()