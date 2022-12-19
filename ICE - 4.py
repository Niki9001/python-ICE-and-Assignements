"""
变量和对象
       对象并没有直接存储到变量中，在python中变量更像是给对想起了一个别名
       变量中存储的不是对象的值，而是对象的id（内存地址），
              当我们使用变量时，实际上就是在通过对象id在查找对象
       变量中保存的对象，只有在重新赋值时才会改变
       变量和变量之间是相互独立的，修改一个变量不会影响影响另一个变量
类型转换
       所谓的类型转换，将一个类型的对象转换为其他对象
       类型转换不是改变对象本身的类型，而是根据当前对象的值创建一个新对象
       int()规则：
              布尔值：True = 1，False = 0.
              浮点数：直接取整，省略小数点后的内容
              字符串：合法的整数字符串，直接转换为对应数字
                     不是合法的整数字符串，则报错 Value Error
              对于其他不可转换为整型的对象，直接抛出异常 Value Error
       float()和 int()基本一致，不同的是它会将对象转换为浮点数
       str() 可以将对象转换为字符串
              True ——> "True"，False ——> "False"，123 ——> "123"......
       bool() 可以将对象转换为布尔值，任何对象都可以转换为布尔值
              对于所有表示空性(例如 0、None和 “”）的对象都会转换成 False，其余的转换为 True
运算符（操作符）
       运算符可以对一个值或者多个值进行运算或者操作
       比如 +、-、*、/、= 都属于运算符
       运算符分类
              1.算数运算符 +、-、*、/、//（整除）、**（幂运算）、%（取模，余数）
              2.赋值运算符 =、+=（a += 5 等于 a+5 输出15）、-=、*=、/=、//=、%= （都类似+=），对浮点数运算时会返回浮点数
              3.比较运算符（关系运算符）>、<、<=、>=、==、!=，比较的是对象的值，而不是id
                     is (not) 比较两个对象是否是同一个对象，比较的对象是id
                     在python中可以对两个字符串比较运算，
                            比较两个字符串的unicode编码时，是逐位比较
                            利用该特性可以对字符串按照字母顺序进行排序，但对于中文意义不大
                            注意：如果不希望用unicode比较，则需要转换为数字后再比较
              4.逻辑运算符 用来做逻辑判断 not and or
                     not可以对符号右侧的值进行非运算 （例如 a = True b = not a，print(b) ——> False)
                            对于布尔值，非运算会对其进行取反操作，T会变成 F, F会变成 T
                            对于非布尔值，非运算会先将其转换为布尔值，然后再取反
                     and 可以对符号两侧进行与运算
                            只有在符号两侧的值都为 T 时，才会返回 T，只要有一个 F，就返回 F
                            and运算是找 F 的
                            python and运算中如果第一个值是 F，则不再看第二个值
                            非布尔值 and 运算是取 and 后面的值。除非遇到0在前，则取0
                     or 可以对符号两侧的值进行or运算
                            只要有一个是 T,则结果为 T
                            or运算是找 T 的
                            python or运算中如果第一个值是 T，则不再看第二个值
                            非布尔值 or 运算如果第一个值是 T，则直接返回第一个值，否则返回第二个值
                     逻辑运算符可以连续使用，跟中间数字进行比较
                     如果需要所有条件都满足用and，如果希望只要有一个条件满足即可用or
              5.条件运算符（三元运算符）
                     语句1 if 条件表达式 else 语句2
                     执行流程
                            先对条件表达式进行求值判断
                                   如果判断结果为T，则执行语句1并返回执行结果
                                   如果判断结果为 F，则执行语句 2并返回执行结果
       运算符优先级
              先乘除后加减
              运算符优先级可以根据优先级表格查询，位置越往下优先级越高
              如果优先级一样，则从左向右计算
              在开发中如果遇到优先级不清楚，加括号
流程控制语句
       python代码是按照自上向下执行，通过流程控制语句可以改变程序执行顺序，也可以让制定的程序反复执行多次
       流程控制语句分成两大类：
       条件判断语句（if语句）
              语法：if 条件表达式 : 语句
              执行流程：if语句在执行时，会先对条件表达式进行求值判断，如果为 T,则执行if后的语句
                     如果为 F，则不执行
              默认情况下，if语句只会控制紧随其后的那条语句，如果希望if可以控制多条语句，
                     则可以在if后跟着一个代码块
              代码块：
                     代码块中保存着一组代码，同一个代码块中的代码，要么都执行，要么都不执行
                     代码块就是一种为代码分组的机制
                     如果编写代码块，语句就不能紧随在：后面，要写在下一行或者几行（缩进）
                     代码块以缩进开始，直到代码恢复之前的缩进级别时结束
                     缩进有两种方式，tab或者四个空格，python官方文档中推荐用四个空格（不同编辑器tab不同）
                     一个文档中缩进方式必须一致
       条件判断语句（if，else）
              语法：
                     if 条件表达式：
                            代码块
                     else：
                            代码块
              执行流程
                     if-else语句在执行时，先对if后的表达条件进行求值判断
                            如果为T，则执行if后代码
                            如果为F，则执行else后的代码块
       条件判断语句（if，elif，else）
              语法：
                     if 条件表达式：
                            代码块
                     elif 条件表达式
                            代码块
                     else：
                            代码块
              执行流程：自上向下依次对条件表达式进行求值判断
                     如果表达式的结果为T，则执行当前代码块，然后结束语句
                     如果表达式结果为F，则继续向下判断，直到找到T为止
                     如果所有的表达式都是F，则执行else后代码块
              只有一个代码块会执行
       循环语句
              可以使制定的代码块重复指定的次数
              循环语句分为两种：while和 for
              while：
                     语法：
                            while 条件表达式：
                                   代码块
                            else：
                                   代码块
                     执行流程：
                            while语句在执行时，会现对while后的条件表达式进行求值判断
                            如果结果为T，则执行循环体（代码块）
                            循环体执行完毕，继续对条件表达式进行求值判断，以此类推
                            直到判断结果为F，则循环终止,如果循环有对应的else，则执行else后的代码块
              条件表达式恒为T的循环语句，为死循环，慎用
              循环的三个要件（表达式）：
                     初始表达式，通过初始化表达初始化的一个变量
                            i = 0
                     条件表达式，条件表达式用来设置循环执行的条件
                            while i < 10
                     更新表达式，修改初始化变量的值
                            i += 1 (不可以为-=，因为-=也是无穷）
                            print(i)
input()函数
       该函数用来获取用户的输入
       input()调用后，程序会立即暂停，等待用户输入
       用户输入完成后才会返回输入值
       注意:input()的返回值是一个字符串，如果前面没加int或者float的话
       input()函数可以设置一个字符串作为参数，这个字符串会作为提示文字显示
       input()也可以用于暂时阻止程序结束
"""

a = 0
sum = 0
if a < 100:
       sum += 7
       print(sum)
