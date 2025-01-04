# DrinkingMoreWater
An android app to calculate how much the rate of cold water and hot water is possible to drink
## 基于冬季热饮的便利性驱动算法

我们都知道，在冬天喝上一口暖乎乎的热水是一件很麻烦的事情
（我是懒狗，*everything is a chore for me.*）
你将面临以下几种情况：

1. 烫成傻逼。  
2. 冷成傻逼。  

那么有什么事情可以避免上述两类结果并喝上一瓶舒心且暖心的温水呢？

不妨假设一个不发生热交换的系统，根据那谁家小谁的定律有：  
$$
Q\text{放} = Q\text{吸}
$$  
$$
c \cdot m \cdot \Delta T_吸 = c \cdot m \cdot \Delta T_放
$$  
*（不考虑其他因素的c = 4.2×10³）*

那么我们需要的是：  
$$
k = \frac{m_{热水}}{m_{冷水}}
$$  

时间 $\Delta t$，我们得知：  
$$
\Delta T\text{冷} = 45^\circ C - 15^\circ C
$$  
$$
\Delta T\text{热} = 100^\circ C - 45^\circ C
$$  

当然这是理想情况，将外部环境影响的水作为支配部分得到：  
$$
c \cdot m_{冷水} \cdot \Delta T\text{热} = c \cdot m_{热水} \cdot \Delta T\text{冷}
$$  

代入解得：  
$$
k = \frac{\Delta T\text{热}}{\Delta T\text{冷}} = \frac{11}{6} = 2
$$  

我们可以看到，装热水时可以接$\frac{1}{3}$冷水，然后便合理得到一杯喝到爽的热水。

---

### 改进：

- 可以根据不同季节的水温变化来找到合适的k值（365天让女朋友多喝热水）。  
- 可以根据热水机的出水量建立**温度-时间微分方程**求解更精确的k值。  
（唯一带点物理的部分）
