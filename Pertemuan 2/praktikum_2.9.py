import my_package.alfa
print(my_package.alfa.FunctionA())

import my_package.beta
print(my_package.beta.FunctionB())

import my_package.subpakage1.subpakageA.gama as gama
print(gama.FunctionC())

import my_package.subpakage1.subpakageA.delta as delta
print(delta.FunctionD())

from my_package.subpakage2 import epsilon
print(epsilon.FunctionE())

from my_package.subpakage2 import zeta
print(zeta.FunctionF())