# 解答：
##  第1题
#### **图灵为什么要证明停机问题：**
   通俗地讲，停机问题是为了证明是否有这样一个“程序”，可以判断任意一个程序是否会无限地运行下去。
#### **证明方法：**
   - 首先给定一个“程序”，该“程序”可以判断一个图灵机在任何输入上是否会停机。
   - 然后用一台图灵机执行此“程序”，判断自己是否停机。如果结论是停机，则这台图灵机将会不停机；而如果结论是不停机，这台图灵机将会停机。
   - 如此一来，这台图灵机将在停机的输入上不停机，在不停机的输入上停机。形成悖论，所以不存在如此的“程序”。
     - 证毕。
#### **数学原理：**
康托对角线法：
图灵停机问题、哥德尔不完备性定理、罗素悖论都是运用的康托对角线法。
## 第2题  
##### 同学们，大家都知道电脑进行数据处理使用的是二进制。简便易懂起见，我们这次只说四位的二进制数。
##### 二进制计算中也有加法和减法。计算机做减法时，不会像我们人类一样比较两个减数和被减数的大小。我们以十进制为例，234-432=-198，计算机计算时只会算出0234-0432=9802，计算机不够减了，需要借位（像小学数学里的减法借位原理一样），这时计算机会把减数与被减数对调，做第二次减法432-234=198，加上负号得到最终正确结果。可见计算机做减法时最多需要做两次，比简单的一次计算效率降低了一半。
##### 为了解决这个尴尬的问题，计算机中表示数据就用到了补码：对于正数，我们只需要将二进制数前面补一个0，表示正号，如0010，补码可以表示为00010。而对于负数，我们首先把二进制码的每一位求反（1代表0，0代表1），然后在最后一位加1，最后在前面加上1表示负号。这样得到的新二进制数补码和原码之和是2的n次方。例如求-0011的补码的过程如下：
##### `-0011→1100→1101→11101。`
##### 11101就是-0011的补码，11101+0011=1000000，正如99999+1=100000一样，这就类似我们刚刚提到的借位。
##### 这样一来在二进制中计算2-3，可以有：
##### `（00010）+（11101）=（11111）`
##### 结果11111是一个补码，用我们刚刚说过的原码补码的逆转换，可以得到结果为：10001，即-1。运算结果正确。
##### 同学们，补码就是计算机表示数的一种方式，通过这种方式，我们可以进行二进制任意的加减法，提高效率。这就是二进制补码的原理。:+1: 
##  第3题
### `Sign`—— `Exp`——`Frac`——`Value`
#### `*`———`000 0000`——`0000 0000`——`±0.0`
#### `0`———`011 1111`——`0000 0000`——`+1.0`
#### `1`———`011 1111`——`0000 0000`——`-1.0`
#### `*`———`111 1110`——`1111 1111`——`±(2−2^{−8})×2^{63})`——`最大规范化数`
#### `*`———`000 0001`——`0000 0000`——`±2^{−62}`——`最小规范化数`
#### `*`———`000 0000`——`1111 1111`——`±(1-2^{-8})×2^{-62})`——`最大非规范化数`
#### `*`———`000 0000`——`0000 0001`——`±(2^{-8}×2^{-62})`——`最小非规范化数`
#### `*`———`111 1111`——`0000 0000`——`±∞`
#### `*`———`111 1111`——`非 全 0`———`NaN`
