# Miniature World · ミニチュア写真 Skill

**身近なモノを、物語のある小さな世界に。**

Codex と Claude Code で使える AI ミニチュア写真の Agent Skill です。モノの形・質感・構造から連想を探し、1枚の「ピクチャーカード」にまとめてから画像を生成します。田中達也さんの作品に見られる「見立て」の手法に着想を得た、独立した個人プロジェクトです。

[紹介ページ](https://denggui-ai.github.io/create-miniature-world/site/)（中国語） · [ギャラリー](https://denggui-ai.github.io/create-miniature-world/site/gallery.html) · [最新版をダウンロード](https://github.com/denggui-ai/create-miniature-world/releases/latest) · [English](README.en.md) · [中文](README.md)

| ノート → 駐輪場 | ポテトチップス → 秋の収穫 | マグカップ → コーヒー染みのトラック |
| --- | --- | --- |
| <img src="examples/notebook-bike-rack.png" width="260" alt="ノートのリングが小さな駐輪場になる"> | <img src="examples/potato-chip-harvest.png" width="260" alt="ポテトチップスの波が収穫中の畑になる"> | <img src="examples/mug-coffee-ring-track-20261012.png" width="260" alt="マグカップのコーヒー染みが子どもたちの徒競走のトラックになる"> |

作例画像はいずれも AI 生成で、発想の方向を示すものです。商品の再現度や既知の不具合は[作例メモ](examples/SELECTED.md)（中国語）に記載しています。

## 30 秒ではじめる

**1. インストール**（初めて入れる場合。同名の Skill がすでにある場合は、先に[インストール説明](docs/INSTALL.md)（中国語）に沿ってバックアップと比較をしてください）

```bash
git clone https://github.com/denggui-ai/create-miniature-world.git
# Claude Code：プロジェクトにコピー
mkdir -p your-project/.claude/skills && cp -R create-miniature-world/skills/create-miniature-world your-project/.claude/skills/
# Codex：.agents/skills を使う
mkdir -p your-project/.agents/skills && cp -R create-miniature-world/skills/create-miniature-world your-project/.agents/skills/
```

入れるのは `skills/create-miniature-world/` フォルダだけです。リポジトリ全体を Skill にしないでください。

**2. 新しいセッションで、商品写真と一言の指示を送る**（写真がなければモノの名前だけでも可）

| 環境 | 送る文 |
| --- | --- |
| Claude Code | `/create-miniature-world この商品写真でミニチュア写真を作って。まず案を見せて、まだ生成しないで。` |
| Codex | `$create-miniature-world を使って、この商品写真でミニチュア写真を作って。まず案を見せて、まだ生成しないで。` |

**3. 案を選ぶ。**「案1で1枚生成、商品の見た目はそのままで」と伝え、画像を見てから直したい点を1つだけ伝えます。

生成と編集には、お使いの環境に備わった画像ツールを使います。Codex / ChatGPT の内蔵生成で動作を確認済みです。検証した Claude Code 環境には内蔵生成がないため、案とプロンプトを受け取り、お手持ちの画像ツールで生成し、その画像を同じ会話に戻して講評を受ける形になります。モデル、API キー、生成クレジットは同梱していません。

## できること・できないこと

- **向いているもの**：輪郭・質感・構造・開閉のしかたから別のものが連想できるモノ。商品写真があると精度が上がります。
- **作り方は2通り**：モノの名前だけ、または写真が下地に使えない場合は直接生成（商品は描き直され、部品や穴の形が変わることがあります）。カメラが近くて低く、モノが画面に大きく写り、台がきれいで、光が柔らかい写真なら、その写真に人形と小物だけを足す編集ルートを使い、商品はそのまま残します。
- **商品の再現**：文字・部品・寸法は誤ることがあります。アイデアが良くても、特定商品の正確な再現を保証するものではありません。
- **未検証**：別のマシン、別の OS、デスクトップでの自動起動は未検証で、安定した成功率も保証していません。各バージョンで何を検証したかは[リリースノート](https://github.com/denggui-ai/create-miniature-world/releases)（中国語）にあります。

## 着想と敬意

ミニチュア写真家・見立て作家の**田中達也さん**と [MINIATURE CALENDAR](https://miniature-calendar.com/about/) に敬意を表します。本プロジェクトの手順は作品の観察と自分たちの試作から整理したもので、作家ご本人が公開した制作方法ではありません。作品ケースカードは文章と公式サイトの記事ページへのリンクのみで、原作画像の収録・転載・生成ツールへの入力は一切行いません。人形の動きや造形は [Preiser 公式サイト](https://www.preiserfiguren.de/)を参考にしています。

本プロジェクトは田中達也さん、MINIATURE CALENDAR、Preiser、および作例に登場する商品ブランドとは公式な提携・推薦関係にありません。コードと自作の文書は [MIT ライセンス](LICENSE)です。作例画像と第三者素材には MIT は自動では適用されません（[素材について](THIRD_PARTY_NOTICES.md)）。

不具合は[報告テンプレート](https://github.com/denggui-ai/create-miniature-world/issues/new?template=bug_report.md)からお知らせください（日本語・英語・中国語いずれも可）。
