# -*- coding: utf-8 -*-
"""
科技深色·亮电光青 通用起手生成器（hr-2up / L0–L3 / 人机协同模式卡 同款）。
用法（路径相对本仓库根目录）：
  1) cp 本文件到 你的输出目录/<slug>/_gen.py
  2) 改最底部「你的 slides」区：按分镜调用 cover()/modepage()/classbar()/relay…/trow()/pitrow()/evo()，
     或直接 W('slideNN', '<main>…</main>', p='NN')。改 TOTAL = 总页数。
  3) python3 _gen.py        # 生成 slide01..N.html（写在脚本同目录）
  4) python3 /path/to/xhs-ppt/tools/render_cards.py . 1280x720 2
     BG=#1a1a2e python3 /path/to/xhs-ppt/tools/stack_cards.py --pairs . 2up
组件函数即 _components.html 的九件套；色编码 ACC：cyan=人主导 / orange=AI主导 / blue=人+AI / purple=多AI。
不要改 HEAD 里的 <style> token——那是 hr-2up 样张观感的来源。
"""
import os
OUT = os.path.dirname(os.path.abspath(__file__))
TOTAL = 12   # ← 改成你的总页数（footer NN / TOTAL）

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
FOOT='<div class="acct">@人机协同组织研究</div><div class="pageno">{p} / %d</div></div></body></html>' % TOTAL

# 谁主导 配色：cyan=人主导 / orange=AI主导 / blue=人+AI / purple=多AI
ACC={'cyan':('#00d9ff','rgba(0,217,255,.14)','rgba(0,217,255,.5)'),
     'orange':('#ff9f00','rgba(255,159,0,.14)','rgba(255,159,0,.5)'),
     'blue':('#5bb7ff','rgba(59,130,230,.16)','rgba(59,130,230,.55)'),
     'purple':('#c084fc','rgba(168,85,247,.16)','rgba(168,85,247,.5)')}

def W(name,inner,p=None):
    open(f"{OUT}/{name}.html","w").write(HEAD+inner+('' if p is None else FOOT.format(p=p)))
def hdr(icon,en,title):
    return (f'<header><div class="kicker"><span class="material-icons">{icon}</span>{en}</div>'
            f'<h1 class="t">{title}</h1><div class="rule"></div></header>')

# ① 封面 HERO
def cover(name,kicker_icon,kicker_en,line1,line2,sub,quote,pills,p='01'):
    pillhtml=''.join(f'<span class="title-font" style="background:{ACC[a][1]};color:{ACC[a][0]};border:1px solid {ACC[a][2]};font-weight:800;padding:9px 16px;border-radius:9px;font-size:15px">{t}</span>' for t,a in pills)
    W(name,f'''<main style="justify-content:center">
<div class="kicker" style="align-self:flex-start;margin-bottom:26px"><span class="material-icons">{kicker_icon}</span>{kicker_en}</div>
<div class="title-font" style="font-size:66px;font-weight:900;line-height:1.12;color:#fff">{line1}</div>
<div class="title-font" style="font-size:66px;font-weight:900;line-height:1.12;color:#00d9ff;text-shadow:0 0 32px rgba(0,217,255,.35)">{line2}</div>
<div style="font-size:23px;color:#c5cee0;font-weight:600;margin-top:20px">{sub}</div>
<div style="font-size:15px;color:#9aa7bd;margin-top:13px;border-left:3px solid #ff9f00;padding-left:16px;line-height:1.5">{quote}</div>
<div style="display:flex;gap:10px;margin-top:30px;flex-wrap:wrap">{pillhtml}</div></main>''',p)

# ② 组合图·逐项详解（左 定义+关键 / 右 场景+坑）
def modepage(name,icon,kicker_en,title,zhudao,acc,definition,scenes,keytitle,keytext,pit,fit,p):
    c,bg,bd=ACC[acc]
    tasks=''.join(f'<div class="task" style="border-left-color:{c}"><span class="material-icons" style="color:{c}">{ic}</span>{tx}</div>' for ic,tx in scenes)
    W(name,hdr(icon,kicker_en,title)+f'''<main class="two">
<div class="col" style="justify-content:center">
<div class="card" style="border-color:{bd}"><div class="chead"><span class="material-icons" style="color:{c}">{icon}</span>定义<span class="badge" style="background:{bg};color:{c};border:1px solid {bd}">{zhudao}</span></div>
<div class="def-body">{definition}</div><div class="fit">适合：<b>{fit}</b></div></div>
<div class="card" style="border-color:{bd};background:{bg}"><div class="chead" style="font-size:15px;margin-bottom:6px"><span class="material-icons" style="color:{c}">tune</span>{keytitle}</div><div class="def-body" style="color:#cdd6e6">{keytext}</div></div>
</div>
<div class="col" style="justify-content:center">
<div style="font-size:13px;color:#9aa7bd;font-weight:700;letter-spacing:1px;margin-bottom:1px">场景</div>
<div class="tasks">{tasks}</div>
<div class="keybox"><div class="kh"><span class="material-icons">report_problem</span>容易踩的坑</div><div class="kb">{pit}</div></div>
</div></main>''',p)

# ⑤ 阶梯条（递增宽度，编码复杂度/层级）
def classbar(tag,name,sub,w,acc):
    c,bg,bd=ACC[acc]
    return (f'<div style="width:{w}%;background:{bg};border:1px solid {bd};border-radius:13px;padding:0 24px;height:96px;display:flex;align-items:center;gap:18px">'
            f'<span class="title-font" style="font-size:21px;font-weight:900;color:{c};flex:none">{tag}</span>'
            f'<div><div style="font-size:21px;font-weight:900;color:#fff">{name}</div>'
            f'<div style="font-size:14px;color:#c5cee0;margin-top:3px">{sub}</div></div></div>')

# ⑥ 流程步骤（竖向链，每步标 AI/人 等角色）
def relaystep(stage,who,acc,last=False):
    c,_,bd=ACC[acc]
    arrow='' if last else '<div style="width:2px;height:13px;background:rgba(0,217,255,.3);margin:2px 0 2px 13px"></div>'
    return (f'<div style="display:flex;align-items:center;gap:11px"><span style="width:26px;height:26px;border-radius:7px;background:{ACC[acc][1]};border:1px solid {bd};color:{c};font-size:12px;font-weight:800;display:flex;align-items:center;justify-content:center;flex:none" class="title-font">{who}</span>'
            f'<span style="font-size:14.5px;color:#dbe3f0;font-weight:500">{stage}</span></div>{arrow}')

# ⑥ 流程横卡（今天→明年→后年 等）
def evo(day,label,acc):
    c,bg,bd=ACC[acc]
    return (f'<div style="flex:1;background:{bg};border:1px solid {bd};border-radius:13px;padding:18px;display:flex;flex-direction:column;gap:7px;align-items:center;justify-content:center">'
            f'<div class="title-font" style="font-size:14px;font-weight:700;letter-spacing:.5px;color:#9aa7bd">{day}</div>'
            f'<div class="title-font" style="font-size:22px;font-weight:900;color:{c}">{label}</div></div>')
ARROW='<div style="display:flex;align-items:center;color:#00d9ff"><span class="material-icons" style="font-size:28px">arrow_forward</span></div>'

# ⑦ 全景表行
def trow(badge,acc,*cells):
    c,bg,bd=ACC[acc]
    tds=''.join(f'<td style="font-size:14px;color:#9aa7bd;line-height:1.5">{x}</td>' for x in cells)
    return (f'<tr><td style="text-align:center;width:130px"><span class="title-font" style="display:inline-block;background:{bg};color:{c};border:1px solid {bd};border-radius:10px;padding:9px 0;width:92px;font-size:16px;font-weight:900">{badge}</span></td>{tds}</tr>')
TABLE_CSS='<style>tbody tr td{background:rgba(0,217,255,.05);border-top:1px solid rgba(0,217,255,.14);border-bottom:1px solid rgba(0,217,255,.14);padding:12px 14px;vertical-align:middle}tbody tr td:first-child{border-left:1px solid rgba(0,217,255,.14);border-radius:11px 0 0 11px}tbody tr td:last-child{border-right:1px solid rgba(0,217,255,.14);border-radius:0 11px 11px 0}</style>'

# ④ 编号红线/坑 行
def pitrow(n,title,body):
    return (f'<div class="keybox"><div style="display:flex;align-items:flex-start;gap:13px">'
            f'<div class="title-font" style="width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,#ff9f00,#ff7a00);color:#1a1208;font-size:17px;font-weight:900;display:flex;align-items:center;justify-content:center;flex:none">{n}</div>'
            f'<div><div style="font-size:17px;font-weight:800;color:#ffb84d;margin-bottom:3px">{title}</div>'
            f'<div style="font-size:14px;line-height:1.55;color:#e7ebf3">{body}</div></div></div></div>')

# ===================== 你的 slides（按分镜替换；下面是各组件最小示例）=====================
if __name__ == "__main__":
    # 封面
    cover('slide01','groups','YOUR DECK · EN','主标题第一行','主标题第二行','一句话副标题',
          '一句钩子，<br>承接/反差。', [('标签A','cyan'),('标签B','orange'),('标签C','purple')], p='01')
    # 组合图（一个概念多面）
    modepage('slide02','co_present','章节 · SECTION','小标题：<span class="c">一句主张</span>','人主导','cyan',
        '定义 2–3 句，<b>加粗命门</b>。',
        [('record_voice_over','场景一'),('payments','场景二'),('description','场景三')],
        '关键设计','把这层的关键写完，<b style="color:#fff">完整结论</b>。','坑：一句最容易踩的。','适合的角色','02')
    # 阶梯总览
    W('slide03',hdr('account_tree','总览 · STRUCTURE','一句话总览')+f'''<main style="justify-content:center;gap:16px">
<div class="lead">引导句：</div>
<div style="display:flex;flex-direction:column;align-items:center;gap:12px">
{classbar('第一','名称','副说明',60,'cyan')}{classbar('第二','名称','副说明',80,'blue')}{classbar('第三','名称','副说明',100,'purple')}</div>
<div class="keybox" style="background:rgba(0,217,255,.06);border-color:rgba(0,217,255,.25)"><div class="kb"><b style="color:#00d9ff">一句小结。</b></div></div></main>''','03')
    print("starter demo -> slide01-03.html in", OUT)
