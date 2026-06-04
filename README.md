# Sakura Open Props

这个静态页面已经通过 CDN 接入 [Open Props](https://open-props.style/)，可直接使用 Open Props 的 CSS 变量构建设计系统原型。

## 本地运行

```bash
npm run dev
```

然后打开 <http://localhost:5173>。

## Open Props 配置

`src/styles.css` 顶部引入了：

- `https://unpkg.com/open-props`：核心设计 token。
- `https://unpkg.com/open-props/normalize.min.css`：基于 Open Props 的 normalize 样式。
- `https://unpkg.com/open-props/buttons.min.css`：基于 Open Props 的按钮样式。

页面示例展示了圆角、阴影、渐变、颜色、间距和排版等 token 的用法。
