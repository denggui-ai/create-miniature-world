# 拍法路由：田中风格 / 实拍光影

出图前选一条拍法，写进提示的光线、机位部分，交付时说明用了哪条。用户没提拍法、或点名田中风格时走“田中风格”；用户提到实拍感、光影感、自然光、氛围、像真的拍出来、微距感等时走“实拍光影”。用户指定具体光线时按用户。创意、人偶外观、商品保真两条路线相同；人偶大小只在超标判定上有差别（见实拍光影）。

“田中风格”指受田中达也作品启发的明亮布景拍法，不代表作者本人的工作流程或认可。

## 田中风格（默认）
按[人偶与取景](figure-framing.md)第 7 条：一个柔和偏暖的主光，从左上或右上来，像大窗或柔光箱；物件有亮面和暗面，影子短而柔；米白或白色哑光纸，受光处亮、远处略暗；机位接近人偶视平或略俯。画面干净明亮，商品交代清楚。不写夕阳、低角度阳光、长投影、暗调等戏剧光。后期 `--dof none`（只加颗粒）；机位略俯、前后有纵深时可用 `--dof mild`。

## 实拍光影
用相机与曝光的物理写法，不用 soft、high-key、gentle 之类形容词描述整体光线：100mm 微距镜头拍桌面，机位略高于物件上沿；景深只有几毫米，只有人偶和它们接触的那一小块清楚，最近的边缘、后方部分和背景逐渐化开；按人偶曝光，最亮的高光冲白，背光的凹处变暗；只有一束光（与故事相配的柔和窗光，或从左后方斜射的低角度暖阳），没有补光，影子朝同一方向；细微胶片颗粒。可写如“a real tabletop photograph through a 100mm macro lens, camera a little above the object's top edge. One window light from the left, no fill. Depth of field is only a few millimetres: only the figures and the patch they touch are in sharp focus; the nearest edge, the far parts and the backdrop blur progressively. Exposed for the figures, so the brightest highlights clip to white and shaded hollows go dark. Fine film grain.”需要暖阳时把光源句换成“one low warm sunbeam from behind left rakes across the scene, no fill; long blurred-edge shadows fall toward the front right”。不写 clearest、全部清楚。

人偶大小句照写（普通约 9%）。微距会把人偶画大一些，这条路线可接受：普通大小分支的超标线从画面高 12% 放宽到 15%，物件长边 1/5 不变；超过才按人偶与取景编辑缩小。后期 `--dof mild`；画面已有明显前后虚化时用 `--dof none`，只加颗粒。

## 后期
两条路线都按[人偶与取景](figure-framing.md)“出图后必看图”第 5 条做本机后期：另存一张，原图与后期版都交付，标明哪张是后期。后期只加颗粒和轻微虚化，强度用脚本预设，不再加强。
