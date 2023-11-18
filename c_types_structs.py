from ctypes import *

b0 = c_bool(0)
b1 = c_bool(0)

print(b0)
print(type(b0))
print(b0.value)

print(b1)
print(type(b1))
print(b1.value)

i0 = c_uint(-1)
print(i0.value)

c0 = c_char_p(b"test")
print(c0.value)

print(c0)
c0 = c_char_p(b"test2")
print(c0)
print(c0.value)

p0 = create_string_buffer(5)
print(p0)
print(p0.raw)
print(p0.value)

p0.value = b"a"
print(p0.raw)
print(p0)

i = c_int(42)
pi = pointer(i)

print(i)
print(pi)
print(pi.contents)

print(p0.value)
print(p0)
print(hex(addressof(p0)))

pt = byref(p0)
print(pt)

print(cast(pt, c_char_p).value)

print(cast(pt, POINTER(c_int)).contents)
print(ord('a'))

class PERSON(Structure):
    _fields_ = [('name', c_char_p),
                ('age', c_int)]
    
bender = PERSON(b'bender', 1001)
print(bender.name)
print(bender.age)

leela = PERSON(b'leela', 1001)
print(leela.name)
print(leela.age)

person_array_t = PERSON * 4
print(person_array_t)

person_array = person_array_t()

person_array[0] = PERSON(b'bender', 1002)
person_array[1] = PERSON(b'leela', 36)
person_array[2] = PERSON(b'fry', 35)
person_array[3] = PERSON(b'Zoidberg', 80)

for p in person_array:
    print(p)
    print(p.name)
    print(p.age)
