# Markji_Convert
## 简介
- Python 脚本，用于将 MarkDown 笔记格式转换为 [Markji](https://www.markji.com/app) 格式的填空题记忆卡，祝大家学习愉快
## 使用方法
- 命令行 `python markji_convert.py <源文件夹> <替换样式编号>`
## 支持样式
- 1: `*text*`
- 2: `**text**`
- 3: ` ==text== `
- 4: `***text***`
## 注意
- 该脚本不会直接修改原文件，而是在同一路径下，生成一个包含格式化后文件的输出文件夹
