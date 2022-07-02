# 这个博客使用的 markdown 语法和 css 样式

这篇文章介绍这个博客所使用的 markdown 语法和渲染的效果

我使用的 markdown 渲染器是 Commonmark, 另外加入了一些自己的扩展

## 标准的 markdown

### 标题

```markdown
#### H4

##### H5

###### H6
```

#### H4

##### H5

###### H6

### 段落

```markdown
这是一行文字, 这里有 `代码` *斜体* **粗体** ***粗斜体***
末尾跟着两个空格会自动换行  
不过我不推荐使用它
```

这是一行文字, 这里有 `代码` *斜体* **粗体** ***粗斜体***
末尾跟着两个空格会自动换行  
不过我不推荐使用它

### 块

```markdown
> 这是一个 block
>
> 这是第二行
>> 这是一个两层 block
```

> 这是一个 block
>
> 这是第二行
>> 这是一个两层 block

### 列表

```markdown
1. 1
1. 2
1. 3
    1. 1.1
    1. 1.2
1. 4
    * a
    * b
1. 5
```

1. 1
1. 2
1. 3
    1. 1.1
    1. 1.2
1. 4
    * a
    * b
1. 5

### 连接

```markdown
<http://google.com>

[谷歌](http://google.com)
```

<http://google.com>

[谷歌](http://google.com)

### 图片

```markdown
![example-image](./Clip_20220630_061432.png)
```

![example-image](./Clip_20220630_061432.png)

## Commonmark 的扩展

### 支持删除线

```markdown
在段落中可以使用 ~~删除线~~
```

在段落中可以使用 ~~删除线~~

### 支持表格

```markdown
| head  | foo   | foo
| -     | -     | -
| 1     | 2     | 3
| 2     | 2     | 3
```

| head  | foo   | foo
| -     | -     | -
| 1     | 2     | 3
| 2     | 2     | 3

### 支持在 List 中放入块

```markdown
1. 块可以被正确放在 list 中

    ```c
    int foo;
    ```

    > block
    >
    > line 2

1. 2
```

1. 块可以被正确放在 list 中

    ```c
    int foo;
    ```

    > block
    >
    > line 2

1. 2

### 支持在 List 后面添加段落标志

```markdown
1. 如果所有的 序号 都紧密相连, 那么在 li 的后面不会有 p
2. 2
3. 3
```

1. 如果所有的 序号 都紧密相连, 那么在 li 的后面不会有 p
2. 2
3. 3

```markdown
1. 如果 list 之间有空格的话, 只要其中一行有空格, li 里面的文字会被解释成段
2. 2

3. 3
```

1. 如果 list 之间有空格的话, 只要其中一行有空格, li 里面的文字会被解释成段
2. 2

3. 3

### 支持站内连接

```markdown
[主页](/)
```

[主页](/)

## 本博客的扩展

### 支持 Alert

```markdown
> **Tip**
>
> 这是一个 Tip
```

> **Tip**
>
> 这是一个 Tip

```markdown
> **Note**
>
> 这是一个 Note
```

> **Note**
>
> 这是一个 Note

```markdown
> **Important**
>
> 这是一个 Important
```

> **Important**
>
> 这是一个 Important

```markdown
> **Tip**
> 可以在后面不添加空行, 让他显示在一行中
```

> **Tip**
> 可以在后面不添加空行, 让他显示在一行中

```markdown
> **Tip** 也可以直接写在后面
```

> **Tip** 也可以直接写在后面

### 支持图片 float 和放大

```markdown
可以在图片的 [] 中加入 `>` `<` `><` 来表示 左漂浮, 右漂浮 和 居中

![example-image <](./Clip_20220630_061432.png)
![example-image >](./Clip_20220630_061432.png)
![example-image ><](./Clip_20220630_061432.png)

另外, 图片被点击后可以被放大
```

可以在图片的 [] 中加入 `>` `<` `><` 来表示 左漂浮, 右漂浮 和 居中

![example-image <](./Clip_20220630_061432.png)
![example-image >](./Clip_20220630_061432.png)
![example-image ><](./Clip_20220630_061432.png)

另外, 图片被点击后可以被放大

### 支持 kbd

```markdown
会自动把被 ` 引起来的一些字符翻译成按键, 比如

功能按键 `Ctrl` `Shift` `Win` `Esc` `Alt` `Backspace` `Space`

字母按键 `A` `B` `C` `D`

方向按键 `Up` `Down` `Left` `Right` `<-` `->`
```

会自动把被 ` 引起来的一些字符翻译成按键, 比如

功能按键 `Ctrl` `Shift` `Win` `Esc` `Alt` `Backspace` `Space`

字母按键 `A` `B` `C` `D`

方向按键 `Up` `Down` `Left` `Right` `<-` `->`

### 支持代码高亮

```c
main()
{
    return 0;
}
```

```python
hello = 'hello world'
print(f'{hello}')
```

```javascript
function(a)
{
    return a => a+1;
}
```

### 支持代码控件

```markdown
左上角会显示这段代码的语言, 另外可以点击右上角的功能进行全选.
如果超过了一行, 会在代码的前面显示行号
```

左上角会显示这段代码的语言, 另外可以点击右上角的功能进行全选.
如果超过了一行, 会在代码的前面显示行号

```markdown
如果只有一行, 那么会隐藏行号
```

如果只有一行, 那么会隐藏行号

### 支持 checkbox

```markdown
[x] 这是被选择的

[ ] 这是没有被选择的
```

[x] 这是被选择的

[ ] 这是没有被选择的
