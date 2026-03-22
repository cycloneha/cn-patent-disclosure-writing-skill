# GitHub 上传步骤

当前目录已经整理为可公开发布版本。

## 方式一：直接上传目录

将整个目录上传到你新建的 GitHub 仓库：

- `cn-patent-disclosure-writing-skill/`

## 方式二：先生成压缩包

在仓库根目录执行：

```bash
chmod +x scripts/prepare_publish.sh
./scripts/prepare_publish.sh
```

生成文件位置：

- `../dist/cn-patent-disclosure-writing-skill.zip`

## 若你本机有 git

在你的本机环境中执行：

```bash
cd cn-patent-disclosure-writing-skill
git init
git add .
git commit -m "Initial public release"
git branch -M main
git remote add origin https://github.com/<your-username>/cn-patent-disclosure-writing-skill.git
git push -u origin main
```

## 注意

- 发布前先人工检查 `PUBLISH_CHECKLIST.md`
- 如未添加许可证，默认不授予他人额外复制、修改和分发权利
