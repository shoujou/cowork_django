# 仕様
```mermaid
sequenceDiagram
  actor User
  User ->> ブログ: 
  actor Admin
  Admin ->> ブログ:　ログイン & 書き換え
```

# フローチャート
```mermaid
  flowchart LR
  User-->ホーム
  ホーム-->|URL1|Page1
  ホーム-->|URL2|Page2
```