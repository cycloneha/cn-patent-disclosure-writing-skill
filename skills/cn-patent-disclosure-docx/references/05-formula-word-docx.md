# 公式、LaTeX、Word 与 DOCX

## 目标

- 让公式适合 Word 原生公式录入或后续 DOCX 生成。
- 保持数学含义完整，不因记号简化而丢失定义。

## 不可做的简化

- 只写“归一化后记为某量”，却省略归一化定义式
- 只写“按某组材料选择参数”，却省略选择规则
- 把一般形式直接压成具体特例，却不说明这是默认实现

## 记号选择建议

- 若要求严格对应论文，优先保留论文逻辑层次，必要时只简化花体集合和排版复杂符号。
- 若要求 Word 更稳，可以把复杂帽子、波浪号改成更平的记号，但要同时保留定义式。
- 若原文对不同部分、不同步骤或不同类别做了严格区分，记号也应保持相同区分，不要随意合并。

## Word 公式录入建议

- 在 Word 中使用 `Alt` + `=` 插入公式框。
- 先写线性 LaTeX/UnicodeMath，再让 Word 自动转换。
- 关键公式独占一行，次级关系尽量放入段落。
- 独占一行公式不要过多；但对核心定义式不要为了省版面而删掉。

## DOCX 渲染工作流

若工作区存在 `generate_patent_docx.py`，优先使用本地渲染器：

```bash
python3 scripts/render_patent_docx.py \
  --source disclosure.md \
  --output disclosure.docx \
  --formula-mode latex
```

如需指定模板：

```bash
python3 scripts/render_patent_docx.py \
  --source disclosure.md \
  --output disclosure.docx \
  --template template.docx \
  --formula-mode latex
```

## 输出后检查

- 是否存在乱码、倒问号、方框
- 首次缩写引入是否丢失
- 行距、首行缩进、标题层级是否延续模板样式
- 公式前后解释句是否仍在
