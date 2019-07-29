# 关于生成能带高对称点路径的说明
-   ###  UserWarning: The input structure does not match the expected standard primitive! The path can be incorrect. Use at your own risk. 问题

pymatgen.symmetry.bandstructure模块的要求是‘It should be used with primitive structures that comply with the definition from the paper.’，所以它第一步会把输入结构的矩阵用get_primitive_standard_structure(international_monoclinic=False)命令将其转化为[Computational Materials Science,49(2), 299-312. doi:10.1016/j.commatsci.2010.05.010](https://www.sciencedirect.com/science/article/pii/S0927025610002697)中规定的标准基矢下的原胞。

从materialsproject（后简称MP）下载的原胞可能和标准原胞的 lattice matrix不一致，即基矢的具体表示形式不同，但代表的基矢还是一个东西。
-  MP原胞POSCAR
```
si2                                     
   1.00000000000000     
     3.8264369800603437    0.0000000000000000    0.0000000000000000
     1.9132184900301719    3.3137916306793720   -0.0000000000003706
     1.9132184900301719    1.1045972102590917    3.1242727113877939
   Si
     2
Direct
  0.7499999790000018  0.7499999830000021  0.7499999970000033
  0.5000000069999970  0.4999999890000026  0.4999999979999998
```
- 标准基矢原胞primitive_standard_structure_POSCAR
```
Si2
1.0
0.000000 2.734364 2.734364
2.734364 0.000000 2.734364
2.734364 2.734364 0.000000
Si
2
direct
0.250000 0.250000 0.250000 Si
1.000000 1.000000 1.000000 Si
```
如果MP中下载的原胞基矢a,b,c顺序和get_primitive_standard_structure生成的顺序一致的话，结果不会有影响（原子坐标和之后生成的高对称点都是direct 【fractional】形式的），但会有warning。然而，一旦基矢不一一对应，比如a!=b!=c，顺序还是自己定的，结果肯定有问题。这时候需要先把结构用get_primitive_standard_structure转化为标准基矢下的原胞，然后再做进一步操作。


所以请使用标准基矢下的原胞作为计算能带前的初始结构（包括之前结构优化和自洽），可使用`get_primitive_standard_structure.py`生成标准基矢的POSCAR以及高对称点的KPOINTS，此时不会有UserWarning。
