> Thinking:
> 
> **Examining the Core Task**
> 
> I've been meticulously analyzing the user's request, focusing on the core goal: crafting an extended text to validate Markdown and HTML functionality. I'm taking into consideration the need for diverse Markdown elements, ensuring adequate length, and exploring the best approach to meet the specified requirements.
> 
> **Defining the Test's Scope**
> 
> I'm expanding the test text's scope. I'm incorporating various Markdown elements: headings, lists, code blocks, blockquotes, links, and images, along with essential HTML tags. I'm focusing on the final format— a raw Markdown code block for easy copy-pasting—and ensuring that the content integrates the user's interests in coding, keyboards, and Stirling engines for greater engagement.
> 
> **Incorporating Personal Interests**
> 
> I'm now integrating the user's interests, like Stirling engines, keyboards, and coding in Go/Kratos, to create a "Personal Knowledge Base" mock-up. The structure is taking shape: headings, bold/italic text, code blocks (Go/Python), and an experimental math section using standard Markdown syntax, focusing on CommonMark/GFM compliance. I'm also including lists, tables (with alignment tests), blockquotes, and HTML elements like details/summary, with a preference for modern HTML.
> 
> **Expanding Detailed Elements**
> 
> Now, I'm working to expand the content with more diverse Markdown and HTML elements. I'm adding `<u>` and `<mark>` tags, and the list is expanded to include H2 links & images. I'm building a detailed developer's cheat sheet that includes sections on Kratos microservices and Stirling engines, and I'm ensuring all the Markdown features work correctly. I'm meticulously incorporating Go and Python code samples. I'm also preparing to finalize the draft.
> 
> **Structuring the Document's Form**
> 
> I'm now focusing on formatting the output. The user specifically asked for a raw Markdown code block, so that's what I'll provide. I'll include a concise introduction before presenting the code block. I'm finalizing the header, introduction, and the Stirling engine parameter table. I will also incorporate Go code examples and Stirling engine formulas, testing LaTeX compatibility within the Markdown block. Finally, I will also incorporate &lt;kbd\> elements to show some keyboard shortcuts.
> 
> **Validating Keyboard Shortcuts**
> 
> I'm now integrating key bindings for keyboards. Also, I'm verifying the inclusion of valid HTML tags, making sure to escape backticks for nested code blocks, while planning the content generation based on the current plan. I am also making sure that the generated Markdown content will be rendered properly. Finally, I will make sure to check all of the generated output for potential issues.

好的，没问题。这份文档模拟了一个开发者的“个人知识库”页面，涵盖了你感兴趣的后端开发（Golang/Kratos）、斯特林发动机项目笔记以及机械键盘配置。

它包含了：

1.  **基础排版**（标题、粗体、斜体、删除线、分割线）
2.  **列表**（无序、有序、任务列表）
3.  **引用**（嵌套引用）
4.  **代码**（行内代码、多语言代码块）
5.  **表格**（对齐方式）
6.  **链接与图片**
7.  **数学公式**（LaTeX）
8.  **HTML 标签**（折叠卡片、按键样式、上下标、高亮等）

你可以直接复制下面的代码块去测试你的 Markdown 渲染器或编辑器（比如 Obsidian、VS Code 等）。

# 🛠️ Markdown & HTML 综合渲染测试文档 v2025

> **简介**：这是一个用于测试 Markdown 解析器兼容性的综合文档。涵盖了 CommonMark 标准语法以及部分 GitHub Flavored Markdown (GFM) 和 HTML 扩展语法。
>
> *最后更新时间：2025-12-01*

---

## 1. 文本样式 (Text Formatting)

这段文本包含 **粗体 text**，*斜体 text*，以及 ***粗斜体混合***。
有时候我们需要 ~~删除线~~ 来表示过时的内容，或者用 `行内代码` 来强调技术术语。

* **高亮 (HTML)**: 使用 `<mark>` 标签可以 <mark>高亮重要文本</mark>。
* **下划线 (HTML)**: 使用 `<u>` 标签可以 <u>添加下划线</u>。
* **键盘按键 (HTML)**: 按下 <kbd>Ctrl</kbd> + <kbd>C</kbd> 复制。
* **上下标 (HTML)**: 水的化学式是 H<sub>2</sub>O，勾股定理是 a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>。

---

## 2. 列表与任务 (Lists)

### 无序列表
* 项目 A
    * 子项目 A.1
    * 子项目 A.2
* 项目 B
    -   子项目 B.1
    +   子项目 B.2

### 有序列表
1.  第一步：初始化项目
2.  第二步：编写代码
    1.  定义接口
    2.  实现业务逻辑
3.  第三步：部署上线

### 任务列表 (Task Lists)
- [x] **学习 Kratos 框架基础**
- [x] 完成斯特林发动机热力学分析
- [ ] 优化 Robocon 视觉识别模型 (YOLO)
- [ ] 组装新的机械键盘 (红轴)

---

## 3. 代码块 (Code Blocks)

### Golang (Kratos HTTP Server)
```go
package main

import (
	"[github.com/go-kratos/kratos/v2](https://github.com/go-kratos/kratos/v2)"
	"[github.com/go-kratos/kratos/v2/transport/http](https://github.com/go-kratos/kratos/v2/transport/http)"
	"log"
)

// main 是入口函数
func main() {
	srv := http.NewServer(http.Address(":8000"))
	app := kratos.New(
		kratos.Name("helloworld"),
		kratos.Server(srv),
	)
	if err := app.Run(); err != nil {
		log.Fatal(err)
	}
}
```

### Python (数据处理)

```python
def calculate_efficiency(work_output, heat_input):
    """
    计算热机效率
    """
    if heat_input == 0:
        return 0.0
    return (work_output / heat_input) * 100

print(f"Efficiency: {calculate_efficiency(50, 200)}%")
```

### JSON (配置文件)

```
{
  "project": "robocon_vision",
  "version": "1.0.2",
  "settings": {
    "use_gpu": true,
    "framework": "pytorch"
  }
}
```

4\. 表格 (Tables)
---------------

| 发动机参数 | 数值  | 单位  | 备注  |
| --- | --- | --- | --- |
| 活塞直径 | 40  | mm  | _需精密加工_ |
| 连杆长度 | 120 | mm  | 碳纤维材质 |
| 飞轮质量 | 0.5 | kg  | **加重以增加惯性** |
| 理论效率 | 35  | %   | 卡诺循环上限 |

* * *

5\. 引用 (Blockquotes)
--------------------

> 这是一个一级引用。
> 
> > 这是一个嵌套的二级引用，通常用于回复或附加说明。
> 
> > "Stay hungry, stay foolish."
> 
> 回到一级引用。

* * *

6\. 数学公式 (LaTeX Support)
------------------------

如果你的编辑器支持 MathJax 或 KaTeX，下面的公式应该能正确显示。

**行内公式**： 质能方程是  $E=mc^{2}$ 。

**块级公式**： 斯特林循环的理想效率  $\eta$  计算如下：

$$
\eta =1-\frac{T_{cold}}{T_{hot}}
$$

其中  $T_{cold}$  和  $T_{hot}$  分别是低温热源和高温热源的绝对温度。

* * *

7\. 高级 HTML 元素
--------------

### 折叠详情 (`<details>` & `<summary>`)

<details> <summary><b>👉 点击这里查看详细的部署步骤 (Click to expand)</b></summary>

Docker build

Kubernetes apply

Check logs 

<pre><code>Running... OK</code></pre>

</details>

### 居中与换行

<div align="center"> <p>这段文字是居中对齐的。</p> <img src="https://www.google.com/search?q=https://go-kratos.dev/img/logo.png" width="100" alt="Kratos Logo"></div>

* * *

8\. 链接与图片
---------

*   **普通链接**: 
    [Kratos 官方文档](https://go-kratos.dev/)
*   **带标题的链接**: 
    [Google](https://google.com)
*   **自动链接**: 
    [https://github.com](https://github.com)

**Markdown 图片**:

* * *

**End of Document**