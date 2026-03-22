# cn-patent-disclosure-writing-skill

公开发布用的 Codex Skill 仓库，包含一个通用的中文专利交底书写作与文档交付技能：

- `skills/cn-patent-disclosure-docx`

本仓库仅包含通用写作方法、模板骨架、检查清单和辅助脚本，不包含任何具体项目材料、样稿、客户数据或未公开内容。

## 使用说明

将本仓库发布到公网后，可让其他用户按其 Codex 环境支持的方式引入该技能目录。

技能目录：

- `skills/cn-patent-disclosure-docx`

## 发布前检查

在仓库根目录执行：

```bash
python3 skills/cn-patent-disclosure-docx/scripts/public_release_audit.py skills/cn-patent-disclosure-docx
```

如输出存在风险项，请先人工复核并清理后再发布。

也可直接执行：

```bash
chmod +x scripts/prepare_publish.sh
./scripts/prepare_publish.sh
```

该脚本会同时完成公开审计并生成 ZIP 发布包。

## 重要说明

- 公开仓库中的文件天然可被读取，因此不要把任何需要保密的提示词、样稿、客户信息、未公开技术内容或内部资料放入本仓库。
- 运行时的固定免责声明、固定拒绝语和提示词保护规则，见 `skills/cn-patent-disclosure-docx/SKILL.md`。
- 若需要真正保密的提示词或运行规则，请改用私有仓库、受控分发或服务端托管方案。

## 许可

发布前请自行补充合适的开源许可证；若未添加许可证，默认不授予他人额外复制、修改和分发权利。
