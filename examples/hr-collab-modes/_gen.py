# -*- coding: utf-8 -*-
# 科技深色·亮电光青（hr-2up 同款）· 人机协同 3 类 6 种模式 · 16:9 → stack 2合1
import os
OUT=os.path.dirname(os.path.abspath(__file__))

HEAD='''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"/>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0f0f1e}
.slide{width:1280px;height:720px;position:relative;overflow:hidden;color:#e8ecf5;
 font-family:"Noto Sans SC",sans-serif;padding:42px 56px;display:flex;flex-direction:column;
 background:radial-gradient(1100px 620px at 86% -12%,rgba(0,217,255,.14),transparent 58%),
            radial-gradient(820px 520px at -6% 120%,rgba(168,85,247,.12),transparent 55%),
            #1a1a2e;}
.grid{position:absolute;inset:0;pointer-events:none;
 background-image:linear-gradient(rgba(0,217,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(0,217,255,.06) 1px,transparent 1px);
 background-size:48px 48px;-webkit-mask-image:radial-gradient(960px 560px at 72% 18%,#000,transparent 82%)}
.title-font{font-family:"Orbitron","Noto Sans SC",sans-serif}
header{position:relative;z-index:2;margin-bottom:16px}
.kicker{display:inline-flex;align-items:center;gap:8px;background:rgba(0,217,255,.1);border:1px solid rgba(0,217,255,.45);
 color:#00d9ff;padding:7px 16px;border-radius:999px;font-size:14px;font-weight:700;letter-spacing:2px;font-family:"Orbitron","Noto Sans SC"}
.kicker .material-icons{font-size:17px}
h1.t{font-size:33px;font-weight:900;margin-top:13px;line-height:1.22;color:#fff}
h1.t .c{color:#00d9ff}h1.t .o{color:#ff9f00}
.rule{height:3px;width:100%;margin-top:13px;border-radius:3px;background:linear-gradient(90deg,#00d9ff,rgba(0,217,255,0))}
main{position:relative;z-index:2;flex:1;min-height:0;display:flex;flex-direction:column}
.pageno{position:absolute;right:50px;bottom:24px;font-family:"Orbitron";font-size:13px;color:rgba(0,217,255,.5);z-index:3;letter-spacing:1px}
.acct{position:absolute;left:56px;bottom:24px;font-size:12px;color:rgba(255,255,255,.28);z-index:3}
.card{background:rgba(0,217,255,.06);border:1px solid rgba(0,217,255,.2);border-radius:14px;padding:17px 20px}
.lead{font-size:18px;line-height:1.6;color:#c5cee0}.lead b{color:#fff}.lead .c{color:#00d9ff}.lead .o{color:#ff9f00}
.two{display:grid;grid-template-columns:438px 1fr;gap:20px;flex:1;min-height:0}
.col{display:flex;flex-direction:column;gap:13px;min-height:0}
.chead{display:flex;align-items:center;gap:9px;font-size:16px;font-weight:800;color:#fff;margin-bottom:9px}
.chead .material-icons{font-size:20px}
.badge{font-family:"Orbitron","Noto Sans SC";font-size:12px;font-weight:800;padding:4px 11px;border-radius:999px;margin-left:auto}
.def-body{font-size:14px;line-height:1.62;color:#aab4c8}.def-body b{color:#fff}
.tasks{display:grid;grid-template-columns:1fr;gap:10px}
.task{display:flex;align-items:flex-start;gap:10px;background:rgba(0,217,255,.06);border-left:3px solid #00d9ff;
 border-radius:8px;padding:11px 14px;font-size:14px;font-weight:500;color:#dbe3f0;line-height:1.4}
.task .material-icons{color:#00d9ff;font-size:18px;margin-top:1px;flex:none}
.keybox{background:rgba(255,159,0,.08);border:1px solid rgba(255,159,0,.35);border-radius:12px;padding:13px 17px}
.keybox .kh{display:flex;align-items:center;gap:8px;color:#ff9f00;font-weight:800;font-size:15px;margin-bottom:7px}
.keybox .kh .material-icons{font-size:18px}
.keybox .kb{font-size:13.5px;line-height:1.58;color:#e7ebf3}.keybox .kb b{color:#ffb84d}
.fit{font-size:13px;color:#9aa7bd;margin-top:2px}.fit b{color:#cdd6e6}
</style></head><body><div class="slide"><div class="grid"></div>
'''
FOOT='<div class="acct">@人机协同组织研究</div><div class="pageno">{p} / 12</div></div></body></html>'

def W(name,inner,p=None):
    open(f"{OUT}/{name}.html","w").write(HEAD+inner+('' if p is None else FOOT.format(p=p)))
def hdr(icon,en,title):
    return (f'<header><div class="kicker"><span class="material-icons">{icon}</span>{en}</div>'
            f'<h1 class="t">{title}</h1><div class="rule"></div></header>')

# 谁主导 配色：cyan=人主导 / orange=AI主导 / blue=人+AI / purple=多AI
ACC={'cyan':('#00d9ff','rgba(0,217,255,.14)','rgba(0,217,255,.5)'),
     'orange':('#ff9f00','rgba(255,159,0,.14)','rgba(255,159,0,.5)'),
     'blue':('#5bb7ff','rgba(59,130,230,.16)','rgba(59,130,230,.55)'),
     'purple':('#c084fc','rgba(168,85,247,.16)','rgba(168,85,247,.5)')}

# ---------- slide01 封面 ----------
def pill(name,acc):
    c,bg,bd=ACC[acc]
    return f'<span class="title-font" style="background:{bg};color:{c};border:1px solid {bd};font-weight:800;padding:9px 16px;border-radius:9px;font-size:15px">{name}</span>'
W('slide01',f'''<main style="justify-content:center">
<div class="kicker" style="align-self:flex-start;margin-bottom:26px"><span class="material-icons">groups</span>HUMAN × AI · 6 MODES</div>
<div class="title-font" style="font-size:66px;font-weight:900;line-height:1.12;color:#fff">人机协同</div>
<div class="title-font" style="font-size:66px;font-weight:900;line-height:1.12;color:#00d9ff;text-shadow:0 0 32px rgba(0,217,255,.35)">到底是什么？</div>
<div style="font-size:23px;color:#c5cee0;font-weight:600;margin-top:20px">把 <b style="color:#fff">3 类 6 种</b>模式讲清楚——HR 和 AI 到底怎么配合</div>
<div style="font-size:15px;color:#9aa7bd;margin-top:13px;border-left:3px solid #ff9f00;padding-left:16px;line-height:1.5">分层解决「把哪些活交给 AI」；<br>这一篇解决「交了之后，人和 AI 具体怎么配合」。</div>
<div style="display:flex;gap:10px;margin-top:30px;flex-wrap:wrap">
{pill('副驾驶','cyan')}{pill('委派','orange')}{pill('监工','orange')}{pill('接力','blue')}{pill('辩论','purple')}{pill('编排','purple')}
</div></main>''','01')

# ---------- slide02 分层 vs 模式 ----------
W('slide02',hdr('alt_route','为什么这篇 · WHY','分层之后，还有一个问题没解决')+'''<main style="justify-content:center;gap:16px">
<div class="lead">上一篇 L0–L3 讲完，后台最多人问：<b class="c">具体到一件事，人和 AI 到底怎么配合？</b></div>
<div style="display:flex;gap:16px">
<div class="card" style="flex:1;background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.14)"><div class="chead"><span class="material-icons" style="color:#9aa7bd">layers</span>上一篇 · 分层</div><div class="def-body">L0–L3 解决「<b>把哪些活交给 AI</b>」——这是<b style="color:#cdd6e6">分层</b>。分错了，你给 AI 干了不该干的事。</div></div>
<div class="card" style="flex:1;border-color:rgba(0,217,255,.45);background:rgba(0,217,255,.08)"><div class="chead"><span class="material-icons" style="color:#00d9ff">handshake</span>这一篇 · 模式</div><div class="def-body">交了之后「<b style="color:#fff">人和 AI 怎么配合</b>」——这是<b style="color:#00d9ff">模式</b>。选错了，AI 在你身边也不知道怎么用。</div></div>
</div>
<div class="keybox" style="background:rgba(0,217,255,.06);border-color:rgba(0,217,255,.25)"><div class="kb"><span style="color:#00d9ff;font-weight:800">分层是「交哪些」，模式是「怎么配」</span>——两件完全不同的事。市面上的协同模式，可归纳成 <b style="color:#fff">3 类 6 种</b>。</div></div>
</main>''','02')

# ---------- slide03 三类骨架 ----------
def classbar(num,name,face,w,acc):
    c,bg,bd=ACC[acc]
    return (f'<div style="width:{w}%;background:{bg};border:1px solid {bd};border-radius:13px;padding:0 24px;height:96px;display:flex;align-items:center;gap:18px">'
            f'<span class="title-font" style="font-size:21px;font-weight:900;color:{c};flex:none">第{num}类</span>'
            f'<div><div style="font-size:21px;font-weight:900;color:#fff">{name}</div>'
            f'<div style="font-size:14px;color:#c5cee0;margin-top:3px">接触面 = {face}</div></div></div>')
W('slide03',hdr('account_tree','三类骨架 · STRUCTURE','三大类，按「接触面」分')+f'''<main style="justify-content:center;gap:16px">
<div class="lead" style="margin-bottom:2px">区别在于<b class="c">人和 AI 的接触面长什么样</b>——复杂度从低到高：</div>
<div style="display:flex;flex-direction:column;align-items:center;gap:12px">
{classbar('一','单步协作','一件事 · 1 人 + 1 AI',60,'cyan')}
{classbar('二','流程协作','一条流程 · 多步骤工作流',80,'blue')}
{classbar('三','多 Agent 协作','一个 Agent 网络 · 1 人 + 多 AI',100,'purple')}
</div>
<div class="keybox" style="background:rgba(0,217,255,.06);border-color:rgba(0,217,255,.25)"><div class="kb"><b style="color:#00d9ff">简单的事用简单模式，复杂的事再上重武器。</b> 每一类内部又分 2 种，共 6 种——下面一个个拆。</div></div>
</main>''','03')

# ---------- 模式页模板 04-06, 08-09 ----------
def modepage(name,cls_en,icon,title,zhudao,acc,definition,scenes,keytitle,keytext,pit,fit,p):
    c,bg,bd=ACC[acc]
    tasks=''.join(f'<div class="task" style="border-left-color:{c}"><span class="material-icons" style="color:{c}">{ic}</span>{tx}</div>' for ic,tx in scenes)
    W(name,hdr(icon,cls_en,title)+f'''<main class="two">
<div class="col" style="justify-content:center">
<div class="card" style="border-color:{bd}"><div class="chead"><span class="material-icons" style="color:{c}">{icon}</span>定义<span class="badge" style="background:{bg};color:{c};border:1px solid {bd}">{zhudao}</span></div>
<div class="def-body">{definition}</div>
<div class="fit">适合：<b>{fit}</b></div></div>
<div class="card" style="border-color:{bd};background:{bg}"><div class="chead" style="font-size:15px;margin-bottom:6px"><span class="material-icons" style="color:{c}">tune</span>{keytitle}</div><div class="def-body" style="color:#cdd6e6">{keytext}</div></div>
</div>
<div class="col" style="justify-content:center">
<div style="font-size:13px;color:#9aa7bd;font-weight:700;letter-spacing:1px;margin-bottom:1px">HR 场景</div>
<div class="tasks">{tasks}</div>
<div class="keybox"><div class="kh"><span class="material-icons">report_problem</span>容易踩的坑</div><div class="kb">{pit}</div></div>
</div></main>''',p)

modepage('slide04','第一类 单步 · COPILOT','co_present','模式一 · 副驾驶：<span class="c">人主导，AI 实时建议</span>','人主导','cyan',
  '你在做事，AI 在旁边随时给建议（像 GitHub Copilot、Notion AI）。<b>选择权永远在你。</b>',
  [('record_voice_over','HRBP 做组织诊断，AI 实时分析录音、提示要追问的点'),
   ('payments','COE 写薪酬方案，AI 拉市场 benchmark、提醒公平性风险'),
   ('co_present','面试官面试，AI 实时记录、生成面评草稿、提示追问')],
  '关键设计','AI 的建议必须<b style="color:#fff">可接受、可拒绝、可忽略</b>——不强制弹窗、不打断思考。「你转头就在，你不看也不烦」。',
  '别用成「逼自己接受 AI 建议」。若发现开始无脑接受，说明这事其实该用<b>「委派」</b>，而不是副驾驶。',
  'HRBP、COE、面试官','04')

modepage('slide05','第一类 单步 · DELEGATION','outbox','模式二 · 委派：<span class="o">AI 执行，人下达 + 验收</span>','AI 主导','orange',
  '你不参与过程，只负责「派活」和「收货」。AI 端到端完成，你做终审。',
  [('upload_file','「把这 1000 份简历筛出符合 JD 的 50 份」→ AI 完成，HR 验收'),
   ('event','「下周三全员培训，会议室/邀请/提醒/签到全包」→ AI 完成'),
   ('description','「季度 People 报告」「5 个岗位 JD 初稿」→ AI 做，HR 终审')],
  '关键设计','派活的<b style="color:#fff">指令清晰度，决定 80% 的结果</b>。「筛简历」vs「按 5 硬 3 软条件筛、优先大厂、排除频繁跳槽」——输出天差地远。',
  '别把该判断的活（绩效校准、离职面谈）委派出去。<b>只委派「目标明确、可量化、错了能重来」的活。</b>',
  'SSC、招聘运营、事务性工作','05')

modepage('slide06','第二类 流程 · SUPERVISOR','visibility','模式三 · 监工：<span class="o">AI 干活，人监督</span>','AI 主导','orange',
  '上一篇 L3 的标配。AI 跑在前面，人在后面抽查、看异常、调阈值。',
  [('forum','AI Bot 答员工政策问题，HR 每周抽查 5% 对话日志'),
   ('filter_alt','AI 筛简历，HR 每周看「被筛掉但有亮点」的边界 case'),
   ('receipt_long','AI 审小额报销，HR 看月度异常报表')],
  '关键设计（三件事）','<b style="color:#fff">抽查 5–10% + 异常自动转人工 + 月度 review</b>。缺这三条，监工就是定时炸弹。',
  '监着监着就不监了——AI 表现好就放松，直到出错被发现、信任崩塌。本质是<b>「结构化的不信任」：信任来自验证。</b>',
  'People Ops、SSC Manager','06')

# ---------- slide07 接力（流程图）----------
def relaystep(stage,who,acc,last=False):
    c,_,bd=ACC[acc]
    arrow='' if last else '<div style="width:2px;height:13px;background:rgba(0,217,255,.3);margin:2px 0 2px 13px"></div>'
    return (f'<div style="display:flex;align-items:center;gap:11px"><span style="width:26px;height:26px;border-radius:7px;background:{ACC[acc][1]};border:1px solid {bd};color:{c};font-size:12px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none" class="title-font">{who}</span>'
            f'<span style="font-size:14.5px;color:#dbe3f0;font-weight:500">{stage}</span></div>{arrow}')
relay=''.join([
 relaystep('Sourcing 扫 LinkedIn / 拉群 / 推荐','AI','orange'),
 relaystep('Screening 简历语义匹配 + 自动剔除','AI','orange'),
 relaystep('初面 30 分钟视频','人','cyan'),
 relaystep('背调 跑公司 / 学历 / 社交关系','AI','orange'),
 relaystep('终面 + Offer 谈判','人','cyan'),
 relaystep('入职准备 发合同 / 建账号 / 排课','AI','orange'),
 relaystep('入职第一天 Welcome 谈话','人','cyan'),
 relaystep('30/60/90 天反馈 自动调研 + 报告','AI','orange',last=True)])
W('slide07',hdr('sync_alt','第二类 流程 · RELAY','模式四 · 接力：<span class="c">各司其职，按棒传递</span>')+f'''<main class="two">
<div class="col" style="justify-content:center;gap:7px">
<div style="font-size:13px;color:#9aa7bd;font-weight:700;letter-spacing:1px">招聘漏斗 · 每一棒交给最适合的「选手」</div>
{relay}</div>
<div class="col" style="justify-content:center">
<div class="card" style="border-color:rgba(0,217,255,.45)"><div class="chead" style="font-size:15px"><span class="material-icons" style="color:#00d9ff">swap_horiz</span>关键：交接传的是上下文</div><div class="def-body">AI 把简历交给 HR，要附<b style="color:#fff">推荐理由 + 评分依据 + 淘汰对比</b>；HR 把决策交给 AI，要附理由。每一棒该谁干，看它是 L0–L3 哪一层。</div></div>
<div class="keybox"><div class="kh"><span class="material-icons">report_problem</span>容易踩的坑</div><div class="kb">别把接力做成<b>断点</b>。每个交接点要么「自动转下一棒」，要么有「等待中」状态——<b>没有状态，就没有流程。</b></div></div>
<div class="fit" style="margin-top:2px">适合：<b>整条流程的 owner（招聘 / Onboarding / 离职负责人）</b></div>
</div></main>''','07')

# ---------- slide08 辩论 ----------
modepage('slide08','第三类 多 Agent · DEBATE','balance','模式五 · 辩论：<span style="color:#c084fc">多 AI 对抗，人当裁判</span>','多 AI + 人裁判','purple',
  '多个 AI 各自从不同立场分析同一件事，最后由人综合判断（借鉴学术辩论、法庭对抗）。',
  [('how_to_reg','晋升评估：正方 AI 列优势+业绩，反方 AI 列短板+风险，HR 综合'),
   ('groups_2','文化匹配：3 个 AI 分别从专业 / 协作 / 抗压视角评，HR 看分歧'),
   ('balance','关键定薪：一 AI 主张外部对标，一 AI 主张内部公平，HR 平衡')],
  '关键设计','每个 AI 必须有明确<b style="color:#fff">立场 + 约束</b>，不能都「中立」。<b style="color:#fff">对抗的价值在差异，不在结论</b>——帮你看到没看到的角度。',
  '别用成「找 AI 帮我背书」。若你心里已有答案，只想 AI 证明它对——<b>那就别开这场辩论。</b>',
  'HRD、HRVP、CHO、高风险决策','08')

# ---------- slide09 编排 ----------
modepage('slide09','第三类 多 Agent · ORCHESTRATION','hub','模式六 · 编排：<span style="color:#c084fc">主 Agent 调度子 Agent</span>','主 AI 调度','purple',
  '多 Agent 协作的<b>最高形态</b>：主 Agent 拆任务、分配子 Agent、整合结果；子 Agent 各自专精一域。',
  [('public','全球招聘：主 Agent 协调 Sourcing + Screening + Compliance + Offer + Onboarding'),
   ('account_tree','大规模组织调整：薪酬影响 + 沟通方案 + 法务审查 + 系统更新 Agent'),
   ('school','全员培训：内容生成 + 排程 + 学习追踪 + 效果评估 Agent')],
  '关键设计','比指令更关键的是<b style="color:#fff">人在哪个节点介入</b>——设计时就标出 critical decision points：哪些必须人拍板、哪些 AI 自主、哪些 AI 给选项。',
  '别<b>过早上编排</b>。副驾驶/委派/监工还没玩明白就上，99% 翻车。<b>编排是终极形态，不是起点。</b>',
  'CHRO、组织发展、AI Native HR Strategist','09')

# ---------- slide10 速查表 ----------
def trow(mode,acc,who,face,fit):
    c,bg,bd=ACC[acc]
    return (f'<tr><td style="text-align:center;width:130px"><span class="title-font" style="display:inline-block;background:{bg};color:{c};border:1px solid {bd};border-radius:10px;padding:9px 0;width:92px;font-size:16px;font-weight:900">{mode}</span></td>'
            f'<td style="color:{c};font-weight:800;font-size:15px;width:150px">{who}</td>'
            f'<td style="font-size:14px;color:#dfe4ef;width:140px">{face}</td>'
            f'<td style="font-size:14px;color:#9aa7bd;line-height:1.5">{fit}</td></tr>')
rows=''.join([
 trow('副驾驶','cyan','人','一件事','HRBP 诊断、COE 方案、面试'),
 trow('委派','orange','AI','一件事','简历筛选、报告生成、流程执行'),
 trow('监工','orange','AI','流程','政策问答、自动审批、AI 筛选复审'),
 trow('接力','blue','人 + AI','流程','端到端招聘、Onboarding、离职'),
 trow('辩论','purple','多 AI + 裁判','决策点','晋升评估、定薪、文化匹配'),
 trow('编排','purple','主 AI','Agent 网络','全球招聘、组织调整、大型项目')])
W('slide10',hdr('table_chart','速查表 · CHEAT SHEET','6 种模式，一张表选对')+f'''<main style="justify-content:flex-start;gap:0">
<table style="width:100%;border-collapse:separate;border-spacing:0 9px">
<thead><tr style="color:#00d9ff;font-size:14px;font-weight:700"><th style="text-align:center">模式</th><th style="text-align:left">谁主导</th><th style="text-align:left">接触面</th><th style="text-align:left">适合什么 HR 工作</th></tr></thead>
<tbody>{rows}</tbody></table>
<style>tbody tr td{{background:rgba(0,217,255,.05);border-top:1px solid rgba(0,217,255,.14);border-bottom:1px solid rgba(0,217,255,.14);padding:12px 14px;vertical-align:middle}}
tbody tr td:first-child{{border-left:1px solid rgba(0,217,255,.14);border-radius:11px 0 0 11px}}
tbody tr td:last-child{{border-right:1px solid rgba(0,217,255,.14);border-radius:0 11px 11px 0}}</style>
<div class="keybox" style="margin-top:8px;background:rgba(0,217,255,.06);border-color:rgba(0,217,255,.25)"><div class="kb"><span style="color:#00d9ff;font-weight:800">选择原则：从简单到复杂、从低风险到高风险。</span> 先把副驾驶/委派玩熟，再扩到流程协作，最后才上多 Agent。</div></div>
</main>''','10')

# ---------- slide11 三个共通坑 ----------
def pitrow(n,title,body):
    return (f'<div class="keybox"><div style="display:flex;align-items:flex-start;gap:13px">'
            f'<div class="title-font" style="width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,#ff9f00,#ff7a00);color:#1a1208;font-size:17px;font-weight:900;display:flex;align-items:center;justify-content:center;flex:none">{n}</div>'
            f'<div><div style="font-size:17px;font-weight:800;color:#ffb84d;margin-bottom:3px">{title}</div>'
            f'<div style="font-size:14px;line-height:1.55;color:#e7ebf3">{body}</div></div></div></div>')
W('slide11',hdr('dangerous','三个共通坑 · PITFALLS','这三个坑，踩任何一种模式都会出事')+f'''<main style="justify-content:center;gap:14px">
{pitrow('1','用错模式','该用辩论的（高风险）拿去委派 = 让 AI 单独对一个人下结论；该用副驾驶的（专业判断）拿去监工 = 干完才发现方向错了。<b style="color:#fff">模式选错，后面全是补救。</b>')}
{pitrow('2','没有 fallback','监工模式 AI 挂了怎么办？编排主 Agent 卡死怎么办？任何模式都要有「AI 失灵时人怎么接管」的预案。<b style="color:#fff">没有 fallback，AI 就是单点故障。</b>')}
{pitrow('3','不留学习数据','人每次对 AI 的修正、否决，都该被记下来喂模型。只用 AI 却不收集「人在哪里改了它」——<b style="color:#fff">这个 AI 永远停在出厂状态。</b>')}
</main>''','11')

# ---------- slide12 演化结尾 ----------
def evo(day,mode,acc):
    c,bg,bd=ACC[acc]
    return (f'<div style="flex:1;background:{bg};border:1px solid {bd};border-radius:13px;padding:18px;display:flex;flex-direction:column;gap:7px;align-items:center;justify-content:center">'
            f'<div class="title-font" style="font-size:14px;font-weight:700;letter-spacing:.5px;color:#9aa7bd">{day}</div>'
            f'<div class="title-font" style="font-size:22px;font-weight:900;color:{c}">{mode}</div></div>')
W('slide12',hdr('update','演化 · EVOLUTION','模式的边界，会随模型能力模糊')+f'''<main style="justify-content:center;gap:22px">
<div style="display:flex;align-items:stretch;gap:14px">
{evo('今天','副驾驶','cyan')}<div style="display:flex;align-items:center;color:#00d9ff"><span class="material-icons" style="font-size:28px">arrow_forward</span></div>
{evo('明年','接力','blue')}<div style="display:flex;align-items:center;color:#00d9ff"><span class="material-icons" style="font-size:28px">arrow_forward</span></div>
{evo('后年','编排','purple')}</div>
<div style="text-align:center;font-size:17px;line-height:1.6;color:#c5cee0">不用把 6 种模式背成圣经——要建立一种 <b style="color:#fff">「模式思维」</b>。</div>
<div style="background:linear-gradient(90deg,rgba(0,217,255,.14),rgba(168,85,247,.12));border:1px solid rgba(0,217,255,.3);border-radius:12px;padding:18px;text-align:center" class="title-font">
<span style="font-size:19px;font-weight:800;color:#fff">遇到一件事先问：这件事<span style="color:#00d9ff">接触面</span>多大？<span style="color:#ff9f00">风险</span>多高？</span><br><span style="font-size:15px;color:#c5cee0;font-weight:700">然后选最匹配的协作姿势。</span></div>
</main>''','12')

print("generated slide01-12 ->",OUT)
