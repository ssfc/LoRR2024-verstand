# AAAI Press Anonymous Submission Instructions for Authors Using LATEX

(Prompt: translate title of article in Chinese)

AAAI 出版社：使用 LATEX 的作者匿名投稿指南







## Abstract

(Prompt: Generalize abstract of article in Chinese)

AAAI 直接使用作者提供的电子源文件制作会议论文集、工作笔记和技术报告。为了确保出版物中的所有论文具有统一的外观，作者必须遵守以下说明。

Keywords:  

### Q: 这篇文章发表会议/期刊属于CCF哪类？这篇文章在google scholar引用次数多少？



### Q: arXiv是什么网站？



### Q: Introduce authors of article in Chinese one by one



## 1 Preparing an Anonymous Submission

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

本文详细描述了匿名提交的格式要求。这些要求与最终定稿论文的格式要求基本一致，但有以下几处显著不同：

- **匿名提交不得包含作者姓名和单位信息**。请将“Anonymous Submission”写为唯一的“作者名称”，并将单位信息留空。
- **PDF文档的元数据应在提交前使用元数据清理工具清除**，以防止泄露身份信息。
- **引用文献须匿名化**，如果读者能从中推测出引用的是作者的过往成果，则需要进行隐匿处理。
- **第一页底部不应包含AAAI的版权声明**。
- **此阶段仅需要提交PDF版本**。无需提交源文件版本，也不需要提交版权转让表格。

为了删除版权声明并确保作者姓名不显示，可以在加载`aaai25`宏包时使用“submission”选项，例如：

```latex
\documentclass[letterpaper]{article}
\usepackage[submission]{aaai25}
```

本文剩余部分为原定稿说明。准备匿名提交时，若上述几点与原说明相矛盾，应以上述要求为准。

## 2 Camera-Ready Guidelines

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

恭喜您的论文被选中收录到AAAI Press的论文集或技术报告中！本文档详细说明了使用PDFLATEX让您已接受论文出版所需的要求。如果您使用Microsoft Word，请参考另一份文档提供的指引。AAAI Press不支持任何其他格式化软件。

以下说明是为有经验的LATEX用户提供的一般指南。如果您不了解如何使用LATEX，请在当地寻求帮助。AAAI无法为您提供支持，随附的样式文件不能保证完全正常运行。如果您所获得的结果不符合已接收到的规格，您必须修改源文件以达到正确的结果。

这些说明是通用的。因此，它们不包括具体的日期、版面费等内容。请参考会议的具体书面说明以获取提交相关的详细信息。请通读整个文档以了解可能适用于您具体情况的要求。所有作者必须遵守以下条款：

- 您必须使用2025 AAAI Press的LATEX样式文件和aaai25.bst参考文献样式文件，这些文件位于2025 AAAI作者包中（aaai25.sty, aaai25.bst）。
- 您必须在截止日期前完成、签署并提交AAAI版权表格（如果AAAI Press要求改用AAAI分发许可，应遵循相关指示）。
- 您必须根据作者格式要求阅读并格式化您的论文源文件和PDF文件。
- 您必须按时通过我们的电子提交表单提交电子文件和摘要。
- 您必须向AAAI Press支付所需的版面或格式化费用，确保它们在截止日期前到账。
- 您必须在提交论文前仔细检查，确保其编译无错误，并符合AAAI作者包中的指南。

## 3 Copyright

(Prompt: Generalize content from "xxx" to "xxxx" of article in Chinese)

所有提交给 AAAI Press 出版的论文必须附有一份有效签署的版权表格。同时，论文的首页底部必须包含 AAAI 的**版权声明**。这些要求没有例外。如果您未能提供签署的版权表格或取消版权声明，我们将无法出版您的论文。此政策没有例外。您可以在 AAAI 作者工具包（AuthorKit）中找到 AAAI 版权表格的 PDF 版本。有关提交的具体细节，请参阅您所在会议的具体说明。

comment:  用AuthorKit模板生成的PDF会自动加上版权声明

## 4 Formatting Requirements in Brief

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

我们需要可用于多种用途并能够在多种设备上输出的源文件和 PDF 文件。论文的设计和外观必须严格遵守 AAAI 样式文件（aaai25.sty）。您不得对 AAAI 样式文件进行任何修改，也不得在您自己的论文中使用任何改变该设计的命令、包、样式文件或宏，包括但不限于行距、浮动元素、边距、字体、字号和外观等。AAAI 对您的源文件和 PDF 文件提出了一系列必须遵守的要求。大多数这些要求是基于我们标准化会议论文属性和布局的努力。提交给 AAAI 出版的所有论文将被重新编译以实现标准化。因此，每份论文提交都必须符合以下要求：

- 您的 .tex 文件必须使用 PDFLATEX 编译—（不得包含 .ps 或 .eps 图形文件）。
- PDF 文件中必须嵌入所有字体，包括图形中的字体。
- 不得直接或通过文档中的命令对样式文件进行任何修改，尤其是不得为了避免额外的页面费用或调整论文页数而进行修改。
- 不得使用 Type 3 字体（包括插图中的 Type 3 字体）。
- 不得修改标题、插图、图表说明、标题和小标题的上下间距。
- 不得更改任何文本元素、脚注、标题元素、图表说明或标题信息的字体大小（对于参考文献和数学公式，请参见本文提供的有限例外情况）。
- 不得更改文本的行间距。
- 您的标题必须遵循标题大小写格式规则（不能使用句子大小写格式）。
- LATEX 文档必须使用 Times 或 Nimbus 字体包（不得使用 Computer Modern 字体作为文本字体）。
- 不得使用或提交 LATEX 209 文档。
- 您的源文件中不得要求使用非罗马字母字体。如果您的论文中包括其他语言的符号（例如但不限于阿拉伯语、中文、希伯来语、日语、泰语、俄语及其他西里尔语系语言），必须将其限制为位图图形。需要非英文语言支持的字体（CID 和 Identity-H）必须转换为轮廓或 300 dpi 位图，或者从文档中移除（即使它们是在嵌入文档的图形文件中）。
- 所有论文必须采用 AAAI 样式的两栏格式。
- 最终提交的论文必须为不例外的 US Letter 大小。
- 源文件必须与 PDF 完全一致。
- 论文的边距不得超出限制（不得出现超出边框的情况）。
- 页数和文件大小必须符合您所参与活动的具体要求。
- 文档不得设置密码保护。
- PDF 文件和源文件中均不得包含嵌入链接或书签（禁止使用 hyperref 或 navigator 包）。
- 源文件和 PDF 文件中不得带有页码、页脚或页眉（禁止使用 pagestyle 命令）。
- PDF 文件必须与 Acrobat 5 或更高版本兼容。
- 除参考文献外，LATEX 源文件必须为单个文件（不得使用 “input” 命令）。
- 图形必须在 LATEX 外部调整到适当大小（不得使用 “clip” 或 “trim” 命令）。

如果您未遵循上述要求，您的论文将被退回以修正不足之处。

## 5 What Files to Submit

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

您需要提交以下内容以确保您的论文能够发表：

- 一份完全合规的 PDF 文件。  
- 您的 LATEX 源文件，必须作为单个 `.tex` 文件提交（请勿使用 “input” 命令将论文的各个部分包含进来——每个部分必须整合到一个源文件中）。唯一允许的例外是 `.bib` 文件，应该单独包含。  
- 文献目录文件（`.bib` 文件）。  
- 您的源文件必须能够在我们的系统上编译，我们的系统只包含标准的 LATEX 2020 TeXLive 支持文件。  
- 用于编译论文的图形文件。  
- LATEX 生成的文件（例如 `.aux`、`.bbl` 文件、PDF文件等）。  

您的 LATEX 源文件将会在我们的系统上进行审查和重新编译。如果无法编译，您的论文将被退回给您。请勿以多个文本文件提交源文件。您的单个 LATEX 源文件必须包含您的所有文本、文献目录（使用 `aaai25.bst` 格式化）、以及任何自定义宏。  

您的文件必须能够在任何安装了标准 LATEX 分发版（除了程序本身之外没有其他支持文件）的计算机上正常工作。  

请勿发送未实际使用在论文中的文件。避免包括任何与编译论文无关的文件，例如说明文件、未使用的图形文件、样式文件、为论文审稿目的附上的额外材料、中间生成的编译文件等。  

请确保不使用过时的样式文件。某些常用软件包（例如一些用于算法的包）的命令可能已经更改，请确保您的论文没有使用旧或过时的样式文件。  

最终的归档文件：请将您的所有源文件放置在一个压缩档案中，并使用 `.zip` 格式进行压缩。最终文件大小不得超过 10 MB。请使用第一作者的姓氏为源文件命名，即使第一作者不是您本人。

## 6 Using LATEX to Format Your Paper

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

最新版的 AAAI 样式文件可以在 AAAI 的官方网站上获取。下载该文件并将其放置在 TEX 搜索路径中。将其与论文放置在同一目录中也应可行。您必须下载最新版的完整 AAAI 作者工具包，以确保获取最新的说明文件和样式文件。

### 6.1 Document Preamble

(Prompt: Generalize Section "6.1 xxxxx" of article in Chinese)

在您的 LaTeX 论文源文件中，您必须按照本小节中的示例配置以下内容。以下命令的设置适用于三位作者，如需增减作者或地址信息，可根据需要添加或删除相应行，并取消注释适用部分。在大多数情况下，这就是您完成论文格式化所需的全部操作，以便使用 Times 字体。`helvet` 宏包将会使无衬线字体使用 Helvetica。这些文件属于 PSNFSS2e 包的一部分，可在许多互联网网站上免费下载（通常已包含在标准安装中）。

将用于设置章节编号深度的 `setcounter` 保持注释状态并设置为 0，除非您希望在论文中添加章节编号。如果需要添加章节编号，需取消对该行的注释，并将数字改为 1（表示章节编号）或 2（表示章节和小节编号）。样式文件不支持对“子小节”编号的正确处理，因此请勿使用大于 2 的数字。

以下代码必须出现在您的导言部分：

```latex
\documentclass[letterpaper]{article} % DO NOT CHANGE THIS
\usepackage[submission]{aaai25} % DO NOT CHANGE THIS
\usepackage{times} % DO NOT CHANGE THIS
\usepackage{helvet} % DO NOT CHANGE THIS
\usepackage{courier} % DO NOT CHANGE THIS
\usepackage[hyphens]{url} % DO NOT CHANGE THIS
\usepackage{graphicx} % DO NOT CHANGE THIS
\urlstyle{rm} % DO NOT CHANGE THIS
\def\UrlFont{\rm} % DO NOT CHANGE THIS
\usepackage{graphicx} % DO NOT CHANGE THIS
\usepackage{natbib} % DO NOT CHANGE THIS
\usepackage{caption} % DO NOT CHANGE THIS
\frenchspacing % DO NOT CHANGE THIS
\setlength{\pdfpagewidth}{8.5in} % DO NOT CHANGE THIS
\setlength{\pdfpageheight}{11in} % DO NOT CHANGE THIS
%
% 保持以下 \pdfinfo 配置不变，无需添加 /Title 和 /Author 标记
\pdfinfo{
/TemplateVersion (2025.1)
}
```

### 6.2 Preparing Your Paper

(Prompt: Generalize Section "6.2 xxxxx" of article in Chinese)

在上述序言之后，您应该按照以下步骤准备论文：

```latex
\begin{document}
\maketitle
\begin{abstract}
%...
\end{abstract}
```

如果您希望在论文中添加代码、数据集以及扩展版本的链接等内容，可以在一个链接环境中添加它们：

```latex
\begin{links}
\link{代码}{https://aaai.org/example/guidelines}
\link{数据集}{https://aaai.org/example/datasets}
\link{扩展版本}{https://aaai.org/example}
\end{links}
```

请确保这些链接不会暴露您的身份。

接下来，您可以继续撰写论文正文。您的论文必须以参考文献部分结束，并按照以下方式插入参考文献：

```latex
% 参考文献及文章结束部分
% 以下内容必须放在文章的末尾
\bibliography{Bibliography-File}
\end{document}
```

完整内容示例：

```latex
\begin{document}
\maketitle
...
\bibliography{Bibliography-File}
\end{document}
```

### 6.3 Commands and Packages That May Not Be Used

(Prompt: Generalize Section "6.3 xxxxx" of article in Chinese)

有许多与 `aaai25.sty` 不兼容的包、命令、脚本和宏。常见的不兼容项列在表 1 和表 2 中。通常情况下，任何修改浮动对象、边距、字体、大小设置、行间距或参考文献及引用格式的命令、包、脚本或宏都是不可接受的。请注意，**负值的 `vskip` 和 `vspace` 只能在某些极少数情况使用，且绝不能用于表格、图片、标题、章节、副章节、子副章节或参考文献周围。**

### 6.4 Page Breaks

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

在您提交最终定稿的论文时，不得使用任何分页命令。参考文献必须紧接正文，并且没有任何间隔。请注意，某些会议在审稿过程中要求参考文献单独占一页。然而，AAAI出版社对最终论文并没有这一要求。

### 6.5 Paper Size, Margins, and ColumnWidth

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

论文必须排版为两栏格式，并打印在 **8.5 x 11 英寸的 US Letter 标准纸** 上。页面边距必须严格如下：

- **上边距**：1.25 英寸（首页），其余页面为 0.75 英寸  
- **左边距**：0.75 英寸  
- **右边距**：0.75 英寸  
- **下边距**：1.25 英寸  

大多数 LATEX 安装的默认纸张尺寸为 A4。然而，由于我们要求您的电子论文采用 US Letter 尺寸，因此我们提供的导言部分（preamble）中包含了将默认纸张尺寸更改为 US Letter 尺寸的命令。  

请注意，**使用任何其他包（例如 Geometry 包等）来更改页面尺寸**，将导致您的最终论文被退回并需要修改。

---

**列宽和边距**：为了确保最佳的可读性，您的论文必须采用两栏格式。每一栏应为 **3.3 英寸宽**（稍多于 3.25 英寸），两栏之间应留有 **0.375 英寸（0.952 厘米）的空白间距**。使用 `aaai25.sty` 文件将会自动为您设置这些列的格式。

### 6.6 Overlength Papers

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

如果你的论文过长，并试图通过格式调整的小技巧来使其符合要求，很可能会被退回审核。保持论文可读性的最佳方法是删减文本、图表或表格。在不影响可读性的前提下，有几种可以接受的方式来减少论文篇幅。

首先，启用`\frenchspacing`命令，可以缩小句号后的空格。接着，将你所有的图表移到页面顶部。可以考虑删减图表中不太重要的部分。如果在图表环境中使用`\centering`替代`\begin{center}`，也可以节省一些空间。对于数学环境，可以缩小字体大小，但不得低于6.5点。

禁止使用更改页面布局的命令，其中包括（但不限于）：`\columnsep`、`\float`、`\topmargin`、`\topskip`、`\textheight`、`\textwidth`、`\oddsidemargin`以及`\evensizemargin`。如果更改了页面布局，你将被要求支付额外的页面费用。其他可能不被接受的命令包括：`\parindent`和`\parskip`。此外，禁止更改章节间距的命令，并且不允许使用 `titlesec` 宏包。

无论采取何种措施，如果论文明显“压缩过度”，将不会被接受。减少论文篇幅的可选方法包括缩小图表尺寸、删减文本，或者支付额外页面的费用（如果允许提供这一选项）。

### 6.7 Type Font and Size

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

您的论文必须使用 Times Roman 或 Nimbus 字体格式。  
我们不接受使用 Computer Modern、Palatino 或其他字体作为正文或标题字体的论文。  
无衬线字体（Sans serif）应使用 Courier。数学公式仅可使用 Symbol、Lucida 或 Computer Modern 字体。  

不要在论文的任何部分（包括图形）中使用 Type 3 字体。Type 3 位图字体是为固定分辨率打印机设计的。这些字体通常以 300 dpi 的分辨率打印，即使打印机的分辨率为 1200 dpi 或更高。此外，它们还经常导致高分辨率图像设备崩溃。因此，AAAI 不接受包含过时 Type 3 字体的电子文件。包含这些字体的文件（即使仅在图形中）将被拒绝。（使用黑板体符号的作者必须避免使用依赖 Type 3 字体的包。）  

幸运的是，有有效的解决方法可以避免您的文件嵌入 Type 3 位图字体。最简单的解决方法是，在 LATEX2e 中使用规定的 times、helvet 和 courier 包。（请注意，通过这种方式格式化的论文，其数学部分仍然使用 Computer Modern 字体。为了使数学部分看起来更美观，您需使用 Symbol 或 Lucida，或者安装 Type 1 的 Computer Modern 字体。有关这些字体的更多信息，请参阅“Obtaining Type 1 Computer Modern”部分。）  

如果您不确定论文是否包含 Type 3 字体，可以在 Acrobat Reader 中查看 PDF 文件。属性/字体窗口将显示文档中所有字体的名称、字体类型和编码属性。如果不确定图形是否包含 Type 3 字体（且文件为 PostScript 或包含的 PostScript 文档），请将其转换为 PDF，并在 Acrobat Reader 的属性窗口中检查字体信息。  

您的正文字体的默认大小必须为 10 点，行间距为 12 点。除第一页外，其余页面均需直接从页顶边距下方开始。（标题页的格式说明请参见下一部分。）段落开始时需缩进 10 点，除非段落直接出现在标题或子标题下方。  

关于在 LATEX 中获取 Type 1 Computer Modern 字体。如果您在论文的数学部分使用 Computer Modern 字体（正文中不能使用该字体），则可能需要下载 Type 1 版本的 Computer Modern 字体。这些字体可从美国数学学会免费下载：https://www.ams.org/tex/type1-fonts.html。  

非罗马字体。如果您的论文中包含其他语言的符号（例如但不限于阿拉伯语、中文、希伯来语、日语、泰语、俄语及其他斯拉夫语），则需将其限制为位图图形格式。

### 6.8 Title and Authors

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

标题必须以16磅加粗字体（行距为24磅）居中显示在两列文本上方。标题必须按照《芝加哥手册》的标题大小写规则使用标题大小写书写。这些规则较为复杂，但一般来说，动词（包括短动词如 be、is、using 和 go）、名词、副词、形容词和代词（包括连字符连接的两个单词）都需要大写，而冠词、连词和介词则应为小写，除非它们直接跟随冒号或长破折号。你可以使用在线工具 [https://titlecaseconverter.com/](https://titlecaseconverter.com/) 检查正确的大小写（选择“Chicago”样式并勾选“Show explanations”选框）。

论文标题下方居中位置应显示作者姓名，使用12磅字体（行距为15磅），并附上作者的所属机构和完整地址（如果有的话，包括电子邮件地址），这些信息应使用9磅罗马字体（行距为12磅）。当到达摘要部分时，应开始使用双栏格式。

### 作者信息排版
根据以下规范设置作者信息，具体取决于是否只有一个或多个隶属于不同机构的作者。**不可**使用表格或 \authorblk.sty 宏包。

#### 单一机构的作者格式
对于来自同一机构的一位或多位作者，应使用逗号分隔作者姓名，所有机构信息直接写在其下方（每行一个机构），使用以下宏包：

```latex
\author{
Author 1, ..., Author n\\
}
\affiliations{
Address line\\
...\\
Address line\\
}
```

#### 不同机构作者的格式
对于来自不同机构的作者，需要使用 \textsuperscript{\rm x} 将作者与其各自机构对应起来。注意，作者姓名（或其后跟随的逗号）和上标之间不应有空格。例如：

```latex
\author{
AuthorOne\equalcontrib\textsuperscript{\rm 1,\rm 2},
AuthorTwo\equalcontrib\textsuperscript{\rm 2},
AuthorThree\textsuperscript{\rm 3},\\
AuthorFour\textsuperscript{\rm 4},
AuthorFive\textsuperscript{\rm 5}}
}
\affiliations{
\textsuperscript{\rm 1}AffiliationOne,\\
\textsuperscript{\rm 2}AffiliationTwo,\\
\textsuperscript{\rm 3}AffiliationThree,\\
\textsuperscript{\rm 4}AffiliationFour,\\
\textsuperscript{\rm 5}AffiliationFive\\
\{email, email\}@affiliation.com,
email@affiliation.com,
email@affiliation.com,
email@affiliation.com
}
```

你可以通过使用 \equalcontrib 指令来表示一些作者做出了同等贡献。这样将会在作者姓名后添加一个标记，并在首页脚注上注明相关信息。

值得注意的是，为了更好的视觉效果，你可能希望通过简单的换行符（`\\`）手动调整作者列表的显示格式。

### 6.9 LATEX Copyright Notice

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

版权声明会在使用 aaai25.sty 时自动显示。它已被硬编码，无法禁用。

### 6.10 Credits

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

如果需要向资助机构致谢，应在“致谢”部分中进行，除非资助机构要求放置在其他位置。如果需要在首页包含这些信息，可以在`\author`或`\title`命令中使用`\thanks`。例如：

```latex
\title{Very Important Results in AI\thanks{This work is supported by everybody.}}
```

可以使用多个`\thanks`命令，每一个都会在标题或作者名称处生成一个独立的脚注标记，并将在文档第一页第一栏的底部显示相应的文本内容。

需要注意的是，`\thanks`命令是易受影响（fragile）的，因此需要使用`\protect`。  
请不要在文档中包含`\pubnote`命令。

### 6.11 Abstract

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

请按照本文档中的示例命令创建摘要。使用命令 \begin{abstract} 时，文本块将自动缩进，请勿再额外缩进。摘要中不得包含参考文献！

### 6.12 Page Numbers

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

请勿在论文上打印任何页码。禁止使用 \pagestyle 命令。

### 6.13 Text

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

论文正文必须使用黑色的十号Times Roman字体，并设定十二点的行距（line spacing）。不得缩小字体大小或减少行距。禁止使用任何修改字体大小或行距的指令（包括但不限于baselinestretch、baselineshift、linespread及其他相关指令）。此外，正文中不得使用彩色文本。

### 6.14 Citations

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

文中引用应包括作者的姓氏和年份，例如 (Newell 1980)。如果年份存在歧义，请在年份后附上小写字母。多位作者的引用格式如下：(Feigenbaum and Engelmore 1988) 或 (Ford, Hayes, and Glymour 1992)。对于四位或更多作者的情况，仅列出第一位作者，后面加上“et al.”，例如 (Ford et al. 1997)。

### 6.15 Extracts

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

长篇引用和摘录应从左右页边分别缩进十个点。  
以下是一个摘录或引用的示例：注意两边的缩进。  
如果通过这种方式将文本以块状分隔开，并且在正文中正确标识和引用，则不需要使用引号。  

### 6.16 Footnotes

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

谨慎使用脚注，因为它会打断正文的阅读。当需要使用时，应以阿拉伯数字的上标形式在全文中连续编号。脚注应位于页面底部，与正文之间用空行和细半磅宽的横线分隔。

### 6.17 Headings and Sections

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

必要时，应使用标题将论文的主要部分分隔开。请记住，您正在撰写的是一篇短论文，而不是一本冗长的书！过多的标题可能会让您的论文看起来更像是一个大纲而不是一篇论文。`aaai25.sty`包会为您创建标题。请勿更改标题的尺寸或其上下的间距。

**章节编号**  
在 AAAI Press 论文中，章节编号的使用是可选的。若要在 LATEX 中使用章节编号，请在文档的前导部分取消对 `setcounter` 行的注释，并将值从 0 改为 1。在短篇海报论文和/或扩展摘要中不应使用章节编号。

**章节标题**  
章节内容应按如下顺序排列并注明标题：  
1. 主要内容部分  
2. 附录（可选）  
3. 伦理声明（可选，无编号）  
4. 致谢（可选，无编号）  
5. 参考文献（无编号）  

**附录**  
所有附录必须位于主要内容之后。如果主要章节已编号，则附录应使用字母作为章节编号，而不是阿拉伯数字。在 LATEX 中，可以使用 `\appendix` 命令来实现这一效果，然后正常使用 `\section{Heading}` 撰写附录的章节标题。

**伦理声明**  
您可以撰写一份关于您的工作潜在伦理影响的声明，包括其广泛的社会影响（包括正面和负面）。如包含此部分，该声明必须以未编号的标题“伦理声明”作为标题。

**致谢**  
如果包含致谢部分，需置于参考文献之前，标题为“致谢”，并且不应编号（在 LATEX 中使用 `\section*{Acknowledgements}`）。此部分包括对同事的帮助表示感谢、对资助机构和财务支持的鸣谢，以及出版许可的说明；请在此部分中感谢其他贡献者、资助支持等。不要将致谢写为第一页的脚注。如果资助机构要求在第一页脚注对资助进行鸣谢，则仅限于所需说明，其他致谢内容请放在全文末尾。请尽量将致谢内容限制在三句话以内。

**参考文献**  
参考文献部分应用标题“参考文献”标示，且必须出现在论文的最末尾（不要在参考文献之后再单独插入一个图片页面）。说明文档中有给出参考文献示例，请遵循一致的格式准备参考文献。不完整或粗劣的参考文献会影响您论文及研究的质量形象，因此请确保参考文献的完整性和准确性。

### 6.18 Illustrations and Figures

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

您的文章必须使用 PDFLATEX 编译。因此，所有的插图必须为 .jpg、.png 或 .pdf 格式。不得使用 .gif（分辨率过低）、.ps 或 .eps 文件格式的插图。

插图、图表、表格和照片应放置在文中首次提及的页面（或随后的一页）中。切勿将它们集中放在文章的末尾。如果插图放置在页面顶部，可以横跨两栏。插图不得侵占页面的顶部、底部或侧边的边距区域。插图必须使用 \usepackage{graphicx} 插入。插图需按顺序编号，例如图 1、图 2 等。不要使用 minipage 将图组组合在一起。

如果您通常使用 pgfplots 创建插图，请先创建插图，然后将它们以正确的边界框作为 pdf 导入，因为由 pgfplots 创建的边界框和裁剪框易受破坏且无效。

当插入插图时，必须在 LATEX 之外对它们进行裁剪。命令 \includegraphics*[clip=true, viewport 0 0 10 10]... 可能会生成看起来很好的 PDF，但图像实际上没有被真正裁剪。当应用页码或标准化颜色空间时，完整图像可能会重新出现（并覆盖任何与之重叠的内容）。图 1 和图 2 显示了一些经常出现的不良结果。

如果您的文章包括与 PDFTEX 不兼容的插图（如 .eps 或 .ps 格式的文档），您需要将它们转换为 PDF。通常可以使用 epstopdf 包处理 eps 文件。而 ps 文件必须转换为 PDF。

**插图说明**  
插图编号和说明必须出现在插图下方。插图中包含的标签及其他文字的字体应至少为 9 号大小。然而，插图说明的字体和大小必须为 10 号罗马字体。不要将其设置为更小、加粗或斜体。（具体词语如果需要区分语义，可以单独使用斜体。）

### 6.19 Tables

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

表格的排版和格式：

**表格排版**
- 表格内容应使用 10 点 Times Roman 字体。如果需要，可以调整为 9 点字体。
- 禁止使用 `\resizebox` 或其他命令调整整个表格大小，因为这种方式无法控制最终字体尺寸。
- 如果表格过大，可以采取以下措施：
  - 使用 `\setlength{\tabcolsep}{1mm}` 压缩列间距。
  - 调整内容，例如减少数字精度、缩短列标题，或将部分列改为双行显示以缩小表格宽度。

**跨栏表格**
- 如果表格无法放入单栏中，需将其放置在双栏空间中。
- 如果表格即便跨栏且使用上述处理后仍然无法适应页面宽度，则必须将其拆分为两个独立的表格。

**表格标题**
- 表格编号和标题必须放置于表格下方（而不是上方）。
- 标题字体为 10 点 Times Roman 字体，不得缩小、加粗或倾斜（特殊上下文需要时可以对单词使用斜体）。
  
---

**低分辨率位图**
- 禁止使用低分辨率（如 72 dpi）的屏幕截图和 GIF 格式文件。
  - GIF 文件的像素太少会造成模糊效果，打印时尤其不清晰。
  - 彩色文件在转换为黑白时会变得难以辨认。
- 屏幕截图的分辨率可以通过以下方法提升：
  - 缩小原始文件打印尺寸，同时保留像素数量。
  - 在 PhotoShop 等软件中处理以放大文件。
- 插入文档时，图片分辨率应为 300 dpi。

---

**LATEX 跨页溢出**
- 在 LATEX 中可能会出现图表或公式的部分内容超出页边距的情况。若遇到此问题，需采取以下措施：
  - 将表格或图形改为跨双栏显示。
  - 如果必须，可以缩小图表，重新排版公式或调整表格配置。
- 注意检查日志文件！必须解决任何出现在 LATEX 中的“overfull box”问题，禁止任何内容超出边距或页面中缝。

---

**颜色使用**
- 仅允许在图表中使用颜色，正文部分禁止使用颜色。
- 使用的颜色必须符合 WCAG 2.0 标准，确保对比度不低于 4.5:1，无论字体大小如何。
- 必须使用 CMYK 色彩模式，而非 RGB。
- 提交的彩色图表：
  - 打印版将转换为黑白灰度模式。
  - 在线版本需满足阅读辅助工具的可访问性需求。
- 由于颜色转换后的效果可能不理想（例如红色变黑，黄色可能消失等），建议避免使用彩色图表。如果必须使用：
  - 确保色彩是 CMYK 模式。
  - 提醒读者可以不依赖颜色来区分信息。

---

**绘图和插图**
- 建议使用专业绘图软件（如 Adobe Illustrator）或在必要时使用 Word 中的绘图工具，不要使用 Microsoft Publisher。
- 插图注意事项：
  - 所有线条宽度应均匀（介于 0.5 到 2 点之间）。
  - 禁止在阴影区域上添加标签。
  - 阴影的线密度应尽可能为 133 lpi。
  - 插图内的文字优先使用 Times Roman 或 Helvetica，不得使用“发丝宽度”线条，线条宽度不少于 0.5 点。

---

**照片与图像**
- 建议使用灰度图片（彩色照片打印效果差，例如红色会变黑，黄色会消失）。
- 分辨率最低设置为 300 dpi，禁止提前筛选图像。

---

**图形缩放**
- 在插入 LATEX 代码前调整图形大小，禁止使用 `\includegraphics` 命令中的 trim 或 clip 选项。
- 使用图形编辑工具调整 PDF 的 media box。

---

**插图字体**
- 所有插图中使用的字体必须嵌入后才能导入 LATEX 文档。

---

**算法格式**
- 算法和程序等特殊插图应优先浮动到页面顶部或底部。
- 算法标题格式：
  - 标题需左对齐并置于水平线之间（如示例 Algorithm 1）。
  - 算法主体结束时需添加另一条水平线。
  - 是否展示行号、如何格式化注释等细节，由作者根据需求自行决定。
- 在 LATEX 中，算法可使用 `algorithm` 和 `algorithmic` 宏包，也可选择其他适用包。

---

**代码清单**
- 代码清单与算法的排版方式类似：
  - 优先浮动到页面顶部或底部。
  - 标题格式为左对齐，置于水平线之间（如示例 Listing 1）。
  - 主体内容结束时添加水平线。
  - 禁止使用背景色，行号（若存在）需出现在文本列中。

### 6.20 References

(Prompt: Generalize Section "6.4 xxxxx" of article in Chinese)

AAAI 风格包含一组用于使用 BibTeX 格式化参考文献的定义。这些定义使得参考文献的样式非常接近下面“参考文献示例”附录中指定的样式。要使用这些定义，还需要 BibTeX 样式文件“aaai25.bst”，可以从 AAAI 网站上的 AAAI 作者工具包中获取。然后，在论文的结尾但在 `\enddocument` 之前，需要添加以下几行代码：

```
\bibliography{bibfile1,bibfile2,...}
```

请注意，`aaai25.sty` 类已经为您设置了参考文献样式，因此无需在文档中单独加入任何 `\bibliographystyle` 命令。

`aaai25.sty` 文件与 `hyperref` 和 `navigator` 软件包不兼容。如果您使用了其中任一个，您的参考文献将会出现错误并导致您的文章被退回。

参考文献的字体可以与周围正文保持一致。然而，仅在本节中，如果您的文章超出了允许的页数，可以将字体大小缩小为 `\small`（9pt）。但是字体小于9pt且行间距小于10pt是不允许的。

`\bibliography` 命令中的文件列表应该是您的 BibTeX 源文件的名称（即文章中引用的 `.bib` 文件）。

以下命令可用于引用参考文献：
- `\cite`：引用给定的参考文献，显示完整的引用。这的显示格式为一个引用为 “(作者 年份)”，多个引用为 “(作者 年份；作者 年份)”。
- `\shortcite`：仅引用年份。这的显示格式为一个引用为 “(年份)” 或多个引用为 “(年份；年份)”.
- `\citeauthor`：仅显示作者名称，不带括号。
- `\citeyear`：仅显示年份，不带括号。

您还可以使用任意 natbib 引用命令。

## 7 Proofreading Your PDF

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

请检查您PDF文件的所有页面。最常被忽略的内容是致谢部分——尤其是正确的资助号。作者还经常忘记为源文件添加元数据，使用了错误的参考文献样式文件，或者未正确遵守作者标题信息的大小写规则或逗号位置规则。另一个常见问题是文本（尤其是公式）超出页面边距。在提交文件之前，您需要解决这些常见错误。

## 8 Improperly Formatted Files

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

过去，AAAI 会为作者提交的格式不正确的文件进行修正。然而，不幸的是，这已成为我们无法再承担的日益沉重的负担。因此，如果您的文件格式不正确，我们会将其退回给您进行修改。

## 9 Naming Your Electronic File

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

我们要求您以第一作者的姓氏（家族姓氏）命名您的 LATEX 源文件，以便能够轻松区分其他提交的文件。完整的文件命名说明将在提交指南中提供给您。

## 10 Submitting Your Electronic Files to AAAI

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

论文提交的相关说明将会在您的录取通知书中提供给您。

## 11 Inquiries

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

如果您对本文档中有关论文准备或提交的说明有任何疑问，请通过以下地址联系 AAAI Press。如果您对使用 AAAI 样式文件的技术实现有疑问，请联系您所在机构的技术专家。我们不提供 LATEX 或任何其他软件包的技术支持。为避免出现问题，请保持您的论文简单，不要使用复杂的宏或样式文件。

AAAI Press  
1101 Pennsylvania Ave, NW Suite 300  
Washington, DC 20004 USA  
电话：1-202-360-4062  
电子邮件：请参考您所参加的会议或活动的提交说明。

## 12 Additional Resources

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

LATEX 是一个较难掌握的程序。如果您曾使用过这个软件，而本文件未能帮助您解决问题，或者某些内容解释得不够清楚，我们建议您阅读 Michael Shell 撰写的出色文档（testflow doc.txt V1.0a，2002/08/13）。该文档关于如何在 LATEX 系统上获得正确的 PS/PDF 输出（虽然为其他目的而写，但也具有普遍适用性）。您可以在 www.ctan.org 的 tex-archive 中找到该文档。

## 13 Reference Examples

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

格式化的参考文献应如下列示例所示。  
建议使用 BibTeX 生成参考文献。  
编译参考文献时缺失字段是不被接受的，通常表明使用了错误的条目类型（BibTeX 类）。  

### **书籍（多作者）**  
使用 `@book` 类：  

Engelmore, R.; 和 Morgan, A., 编者. 1986. *Blackboard Systems*. Reading, Mass.: Addison-Wesley.  

---

### **期刊和杂志文章**  
使用 `@article` 类：  

Robinson, A. L. 1980. 新方法让微电路更小。*Science*, 208(4447): 1019–1022.  

Hasling, D.W.; Clancey, W. J.; 和 Rennels, G. 1984. 诊断咨询系统的战略解释。*International Journal of Man-Machine Studies*, 20(1): 3–19.  

---

### **会议论文（由社团、出版社出版）**  
使用 `@inproceedings` 类，可缩写 booktitle 字段，但需确保会议版本信息清晰：  

Clancey, W. J. 1984. 分类问题求解。在 *Proceedings of the Fourth National Conference on Artificial Intelligence*, 45–54. Menlo Park, Calif.: AAAI Press.  

Clancey, W. J. 1983. *Communication, Simulation, and Intelligent Agents: Implications of Personal Intelligent Machines for Medical Education*. 在 *Proceedings of the Eighth International Joint Conference on Artificial Intelligence (IJCAI-83)*, 556–560. Menlo Park, Calif: IJCAI Organization.  

---

### **大学技术报告**  
使用 `@techreport` 类：  

Rice, J. 1986. *Poligon: A System for Parallel Problem Solving*. Technical Report KSL-86-19, Dept. of Computer Science, Stanford Univ.  

---

### **学位论文（博士或硕士论文）**  
使用 `@phdthesis` 类：  

Clancey, W. J. 1979. *Transfer of Rule-Based Expertise through a Tutorial Dialogue*. Ph.D. 论文, Dept. of Computer Science, Stanford Univ., Stanford, Calif.  

---

### **即将出版的文献**  
使用 `@misc` 类并注记 `note="Forthcoming"`：  

```BibTeX
@misc(key,
[...]
note="Forthcoming",
)
```

Clancey,W. J. 2021. *The Engineering of Qualitative Models*. 即将出版.  

---

### **ArXiv 论文**  
从 ArXiv 网站的“导出 BibTeX 引用”链接获取 BibTeX 条目。注意，这里使用的是 `@misc` 类而不是 `@article` 类，包括 `eprint` 和 `archivePrefix` 键：  

```BibTeX
@misc(key,
[...]
eprint="xxxx.yyyy",
archivePrefix="arXiv",
)
```

Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A. N.; Kaiser, L.; 和 Polosukhin, I. 2017. *Attention Is All You Need*. arXiv:1706.03762.  

---

### **网站或在线资源**  
使用 `@misc` 类，将 URL 添加到 `howpublished` 字段，并在 `note` 字段注明访问日期：  

```BibTeX
@misc(key,
[...]
howpublished="\url{http://...}",
note="Accessed: YYYY-mm-dd",
)
```

NASA. 2015. *Pluto: The ’Other’ Red Planet*. https://www.nasa.gov/nh/pluto-the-other-red-planet. 访问日期: 2018-12-06.  

---

### **获取 AAAI 最新参考文献格式**  
请参考 AI Magazine 作者指南的最新版本：  
[https://aaai.org/ojs/index.php/aimagazine/about/submissions#authorGuidelines](https://aaai.org/ojs/index.php/aimagazine/about/submissions#authorGuidelines)  

## 14 Acknowledgments

(Prompt: Generalize content from "xxxx" to "xxxxx" of article in Chinese)

AAAI 特别感谢 Peter Patel Schneider 他为实现最初的 `aaai.sty` 文件所做的工作，他在此过程中大量借鉴了其他风格开发者（如 Barbara Beeton）的创意。同时，我们也感谢 George Ferguson 的工作，他编写了关于使用该风格文件和 BibTeX 文件的指南 —— 该指南已被纳入本文档中。此外，我们对 Hans Guesgen 提供的几项及时修改表示感谢，以及那些不时提出改进 AAAI 风格建议的许多其他人。我们尤其感谢 Francisco Cruz、Marc Pujol-Gonzalez 和 Mico Loretan 在 2020 年对 BibTeX 和 LaTeX 文件所做的改进。

用于实现这些说明的 LaTeX 和 BibTeX 文件的准备工作得到了 Schlumberger Palo Alto Research、AT&T Bell Laboratories、Morgan Kaufmann Publishers、The Live Oak Press, LLC 和 AAAI Press 的支持。书目样式的修改由 Sunil Issar 添加，`\pubnote` 是由 J. Scott Penberthy 添加的，而 George Ferguson 增加了打印 AAAI 版权标识的支持。Francisco Cruz 和 Marc Pujol-Gonzalez 对 `aaai25.sty` 和 `aaai25.bst` 文件进行了其他改动。

感谢您仔细阅读这些说明，我们期待收到您的电子文件！

## References

(Prompt: Generalize Section "9 Conclusion" of article in Chinese)

Clancey, W. J. 1979. Transfer of Rule-Based Expertise 
through a Tutorial Dialogue. Ph.D. diss., Dept. of Computer
Science, Stanford Univ., Stanford, Calif.
Clancey,W. J. 1983. Communication, Simulation, and Intelligent
Agents: Implications of Personal Intelligent Machines
for Medical Education. In Proceedings of the Eighth International
Joint Conference on Artificial Intelligence (IJCAI-
83), 556–560. Menlo Park, Calif: IJCAI Organization.
Clancey, W. J. 1984. Classification Problem Solving. In
Proceedings of the Fourth National Conference on Artificial
Intelligence, 45–54. Menlo Park, Calif.: AAAI Press.
Clancey,W. J. 2021. The Engineering of Qualitative Models.
Forthcoming.
Engelmore, R.; and Morgan, A., eds. 1986. Blackboard Systems.
Reading, Mass.: Addison-Wesley.
Hasling, D.W.; Clancey,W. J.; and Rennels, G. 1984. Strategic
explanations for a diagnostic consultation system. International
Journal of Man-Machine Studies, 20(1): 3–19.
NASA. 2015. Pluto: The ’Other’ Red Planet. https://www.
nasa.gov/nh/pluto-the-other-red-planet. Accessed: 2018-
12-06.
Rice, J. 1986. Poligon: A System for Parallel Problem Solving.
Technical Report KSL-86-19, Dept. of Computer Science,
Stanford Univ.
Robinson, A. L. 1980. New Ways to Make Microcircuits
Smaller. Science, 208(4447): 1019–1022.
Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones,
L.; Gomez, A. N.; Kaiser, L.; and Polosukhin, I. 2017. Attention
Is All You Need. arXiv:1706.03762.

Keywords:  