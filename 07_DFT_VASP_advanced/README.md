# VASP 计算上机实例

![](./img/Silicon-unit-cell-3D-balls.png)

我们以钻石结构的 Si 为例进行计算. 

本文件夹内共包含 8 个文件夹, **除了 7-1 和 7-2 需要复制第 6 步自洽计算得到的电荷密度文件以外, 其余文件夹中均已经包含所有必须的 VASP 输入文件, 提交任务脚本以及绘图脚本.** 各文件夹说明如下所示.

-   `0_diamond_a`: 晶格常数测试.
-   `1_diamondSi_encut`: 截断能测试.
-   `2_diamondSi_kpoint`: k-网格密度测试.
-   `3_diamondSi_sigma`: sigma 参数测试.
-   `4_diamondSi_vol_rex`: 利用 VASP 内置算法优化晶格常数.
-   `5-1_diamondSi_relax`: 利用 VASP 内置算法优化原子位置.
-   `5-2_diamondSi_relax_select`: 利用 VASP 内置算法优化原子位置.
-   `6_diamondSi_self_c`: 自洽计算, 为后续能带和态密度计算准备电荷密度文件.
-   `7-1_diamondSi_band`: Si 能带计算.
-   `7-2_diamondSi_dos`: Si 态密度计算.

更多 VASP 计算实例, 可以参考 [VASP wiki examples](https://cms.mpi.univie.ac.at/wiki/index.php/Category:Examples).