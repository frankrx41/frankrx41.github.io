# 本博客的更新日志

说真的, 懒得写, 直接看 git 的 log 就好了

而且反反复复改来改去的都是那几个文件

所以我这里写一些 log 里面没有的东西

## 为什么使用 commonmark 替代标准的 markdown

**短答案:** 因为 vscode 渲染所用的是 commonmark

**长答案:**

在早期我确实使用 markdown 来翻译 md 文件的, 但是很快我就发现, 标准的 markdown 竟然连代码块都不支持

然后我加了个 fenced_code 的插件, 临时的修复了一下

但是, 我又发现, 它连 table 也不支持

嗯, 还是和之前一样, 我加了个 tables 的插件, 暂时看起来是好了

但是又很快我发现, li 中加入 code block 它也都不支持

然后我就开始, 和之前的一样, 继续找插件

这次新找的插件, 会在生成的 `li` 周围加一圈的 `div`, 这是我不能忍受的

继续换了几家插件, 还是没有遇到喜欢的

之后, 我就开始思考, 在 vscode 中的 markdown 是支持的这些功能的

所以, vscode 使用的渲染器是谁家的呢?

结果就是, 用的是 commonmark

这个是 [commonmark 的使用指南](https://markdown-it-py.readthedocs.io/en/latest/plugins.html)

## 本博客已经实现的机能和计划中的机能

- [x] 本地预览博客

    现在用的是 npm 的 http-server

- [x] 自动化生成博客流程

    现在使用的是一个自己写的 py 脚本

- [ ] 加入对博客渲染结果的自动化测试

- [x] 主页的文章加入第一段的文本

    集成在 generat-blog.py 中

- [ ] 加入标签, 并且可以按标签进行分类

- [ ] 加入搜索功能

- [x] 图片可以单击放大

    使用 css 和 js 实现

- [x] 代码块可以显示行号

    使用 css 和 js 实现

- [x] 代码会进行语法高亮

    现在使用的是 highlight.js, 还有些 bug, 比如 cmd reg 格式的不会被高亮

- [x] 可以快速选择代码块

    使用 js 实现

- [ ] `H2` `H3` 段加入 link

- [ ] 美化 footer

- [ ] 生成文章结构目录

- [ ] 生成文章二维码

- [ ] 加入响应式的 css

- [ ] 加入 light dark 主题的切换

- [ ] 加入更多的选项

- [ ] 一个秘密内容的更新
