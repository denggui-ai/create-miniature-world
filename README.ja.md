# Miniature World · ミニチュア写真 Skill

**身近なモノを、物語のある小さな世界に。**

Codex と Claude Code で使える AI ミニチュア写真の Agent Skill です。モノの形・質感・構造から連想を探し、まず画面を思い描いてから画像を生成します。田中達也さんの作品に見られる「見立て」の手法に着想を得た、独立した個人プロジェクトです。

[紹介ページ](https://denggui-ai.github.io/create-miniature-world/site/ja/) · [ギャラリー](https://denggui-ai.github.io/create-miniature-world/site/gallery.html)（説明は中国語） · [最新版をダウンロード](https://github.com/denggui-ai/create-miniature-world/releases/latest) · [English](README.en.md) · [中文](README.md)

| クリップ → ハードル走 | おろし金 → パターゴルフ | ハサミ → リレー |
| --- | --- | --- |
| <img src="examples/paperclip-hurdles-20261020.png" width="260" alt="立てた3本のクリップがハードルになり、小さなランナーが跳び越える"> | <img src="examples/grater-golf-20261020.png" width="260" alt="寝かせたおろし金の大きな穴がゴルフのカップになる"> | <img src="examples/scissors-handle-relay-20261021.png" width="260" alt="ハサミの黒い持ち手の輪がリレーのトラックになる"> |
| ハードル決勝、先頭はもう宙を舞う。 | パットを打つ選手とキャディー。 | 持ち手の輪を走るリレー。 |

AI 生成の作例で、各1回の生成です。制作の過程は[作例記録](examples/PICTURE_CARD_CASES_20261021.md)（中国語）にあります。ほかの作例は[ギャラリー](https://denggui-ai.github.io/create-miniature-world/site/gallery.html)へ。

## まずは文章だけの案から

Codex または Claude Code が必要です。これは Agent が読む創作用 Skill で、紹介サイト自体には画像生成機能はありません。**写真がなくても試せます。最初の依頼では画像生成ツールを呼び出しません。**

**1. 使っている環境にインストール**

[最新版 Release](https://github.com/denggui-ai/create-miniature-world/releases/latest)に添付された Skill の ZIP とチェックサムを入手し、[インストール説明](docs/INSTALL.md)（中国語）または[英語ガイド](docs/GETTING_STARTED.en.md)に沿って確認・展開します。`SKILL.md` を含む `create-miniature-world` フォルダを使います。ソース内の場所は `skills/create-miniature-world/` です。

| 使う環境 | 初回のプロジェクト内インストール先 |
| --- | --- |
| Codex | `your-project/.agents/skills/create-miniature-world/` |
| Claude Code | `your-project/.claude/skills/create-miniature-world/` |

使う環境の一行だけを選び、Skill フォルダ全体を入れてください。`SKILL.md` だけ、またはリポジトリ全体をコピーしないでください。同名のものがあれば、先にバックアップと比較を行います。新しいセッションで実際に読み込まれた Skill を確認してください。コピーできたことだけでは、読み込み成功とは言えません。

**2. 写真なしで、一文を送る**

| 環境 | 送る文 |
| --- | --- |
| Claude Code | `/create-miniature-world 普通のマグカップでミニチュア写真を考えて。まず文章だけの案を二つ見せて。画像はまだ生成しないで。日本語で答えて。` |
| Codex | `$create-miniature-world を使って、普通のマグカップでミニチュア写真を考えて。まず文章だけの案を二つ見せて。画像はまだ生成しないで。日本語で答えて。` |

カップのどの部分が何になり、誰が何をしていて、どこから撮るのかが文章で示されます。この段階では画像は生成しません。Skill が読み込まれていなければインストールを確認し、先に画像が生成された場合は問題として報告してください。

**3. 一案を選び、一枚だけ生成する**

画像ツールがあれば「案1で一枚生成して」と依頼します。なければ「案1の画像生成プロンプトだけください。生成しないで」と依頼し、すでに使っている画像ツールに渡せます。次に自分の商品写真で試すときは、変えたくない部分を伝えてください。

生成・編集は、現在の環境で実際に利用できる画像ツールに依存します。すべての Codex や Claude Code で生成できるわけではありません。モデル、API キー、生成クレジットは同梱していません。

画像を見たら、どんな場面に見えるか一言で説明してから修正を決めます。インストールで止まった場合も、[初回体験のフィードバック](https://github.com/denggui-ai/create-miniature-world/issues/new?template=first_use.md)に記録できます。日本語でも構いません。

## できること・できないこと

- **向いているもの**：輪郭・質感・構造・開閉のしかたから別のものが連想できるモノ。商品写真があると精度が上がります。
- **作り方は2通り**：モノの名前だけ、または写真が下地に使えない場合は直接生成（商品は描き直され、部品や穴の形が変わることがあります）。カメラが近くて低く、モノが画面に大きく写り、台がきれいで、光が柔らかい写真なら、その写真に人形と小物だけを足す編集ルートを使い、商品はそのまま残します。
- **商品の再現**：文字・部品・寸法は誤ることがあります。アイデアが良くても、特定商品の正確な再現を保証するものではありません。
- **未検証**：別のマシン、別の OS、デスクトップでの自動起動は未検証で、安定した成功率も保証していません。各バージョンで何を検証したかは[リリースノート](https://github.com/denggui-ai/create-miniature-world/releases)（中国語）にあります。

## 着想と敬意

ミニチュア写真家・見立て作家の**田中達也さん**と [MINIATURE CALENDAR](https://miniature-calendar.com/about/) に敬意を表します。本プロジェクトの手順は作品の観察と自分たちの試作から整理したもので、作家ご本人が公開した制作方法ではありません。作品ケースカードは文章と公式サイトの記事ページへのリンクのみで、原作画像の収録・転載・生成ツールへの入力は一切行いません。人形の動きや造形は [Preiser 公式サイト](https://www.preiserfiguren.de/)を参考にしています。

本プロジェクトは田中達也さん、MINIATURE CALENDAR、Preiser、および作例に登場する商品ブランドとは公式な提携・推薦関係にありません。コードと自作の文書は [MIT ライセンス](LICENSE)です。作例画像と第三者素材には MIT は自動では適用されません（[素材について](THIRD_PARTY_NOTICES.md)）。

不具合は[報告テンプレート](https://github.com/denggui-ai/create-miniature-world/issues/new?template=bug_report.md)からお知らせください（日本語・英語・中国語いずれも可）。

紹介・掲載をご検討の方へ：[プロジェクト概要と作例リンク](docs/SHARING.md)（中国語・英語）。
