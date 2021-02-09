# Python Polynome class
Allow you to use Polynome of any degrees in python.

# How to use ? 
To create a polynome use 
```python
p= Polynome([1,2,1],[2,1,0])
print(p)
# 1 * x**2 + 2 ** x + 1
```
To add two polynomes use : 
```python
p1 = Polynome(...)
p2 = Polynome(...)
p1+p2
```
To plot a polynome use :
```python
p = Polynome(...)
p.trace()
```
