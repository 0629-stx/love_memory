import streamlit as st
from datetime import datetime

# ---------------------- 页面基础配置 ----------------------
st.set_page_config(
    page_title="致我的男孩💌",
    page_icon="💖",
    layout="wide"
)

# ---------------------- CSS + JS 浪漫特效集合 ----------------------
def set_all_romantic_style():
    css = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://img0.baidu.com/it/u=3841342314,3072442314&fm=253&fmt=auto&app=138&f=JPEG?w=1920&h=1080");
        background-size: cover;
        background-attachment: fixed;
    }
    .love-title{
        font-size:48px;
        font-weight:bold;
        text-align:center;
        background: linear-gradient(90deg,#ff4477,#ff88cc,#ff4477);
        -webkit-background-clip:text;
        color:transparent;
        animation: shine 2.5s linear infinite;
    }
    @keyframes shine{
        0%{filter:brightness(1);}
        50%{filter:brightness(1.4);}
        100%{filter:brightness(1);}
    }
    .text-box{
        background-color:rgba(255,255,255,0.85);
        padding:28px;
        border-radius:22px;
        box-shadow: 0 0 20px #ff77aa88, 0 0 35px #ffbbddee;
    }
    .time-line{
        color:#cc2255;
        font-weight:bold;
        font-size:20px;
    }
    .countdown-box{
        background: linear-gradient(135deg,#ff77aa,#ffb3cc);
        padding:16px;
        border-radius:16px;
        text-align:center;
        color:white;
        font-weight:bold;
        font-size:22px;
        box-shadow:0 0 15px #ff88bb;
    }
    /* 飘落爱心 */
    .heart {
        position: fixed;
        top: -10px;
        z-index: 9999;
        animation: fall linear forwards;
        color: #ff5588;
        font-size: 24px;
        pointer-events: none;
    }
    @keyframes fall {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(100vh) rotate(720deg);
            opacity: 0;
        }
    }
    /* 烟花星光粒子 */
    .spark{
        position:fixed;
        z-index:9998;
        pointer-events:none;
        font-size:18px;
        animation:sparkFly 1.6s ease-out forwards;
    }
    @keyframes sparkFly{
        0%{transform:translate(0,0);opacity:1;}
        100%{transform:translate(var(--tx),var(--ty));opacity:0;}
    }
    </style>
    """
    # JS：持续爱心下落 + 鼠标点击炸开星光烟花 ✨💫
    effect_js = """
    <script>
    // 持续爱心下落
    function createHeart() {
        const heart = document.createElement('div');
        heart.classList.add('heart');
        heart.innerHTML = '❤️';
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDuration = Math.random() * 3 + 4 + 's';
        document.body.appendChild(heart);
        setTimeout(()=>heart.remove(), 7000);
    }
    setInterval(createHeart, 350);

    // 鼠标点击，炸开星光烟花
    const starList = ['✨','💫','⭐','🌟','💖'];
    document.addEventListener('click',function(e){
        for(let i=0;i<12;i++){
            const s = document.createElement('div');
            s.className='spark';
            s.innerText = starList[Math.floor(Math.random()*starList.length)];
            s.style.left = e.clientX + 'px';
            s.style.top = e.clientY + 'px';
            const angle = Math.random() * Math.PI * 2;
            const dis = 40 + Math.random()*90;
            s.style.setProperty('--tx', Math.cos(angle)*dis + 'px');
            s.style.setProperty('--ty', Math.sin(angle)*dis + 'px');
            document.body.appendChild(s);
            setTimeout(()=>s.remove(),1600);
        }
    })
    </script>
    """
    st.markdown(css, unsafe_allow_html=True)
    st.components.v1.html(effect_js, height=0)

# ---------------------- 密码解锁模块 ----------------------
if "pass_ok" not in st.session_state:
    st.session_state["pass_ok"] = False

PASSWORD = "20260624" # ✅ 修改成你们的专属密码！

if not st.session_state["pass_ok"]:
    st.markdown('<div class="love-title">🔐 专属告白空间</div>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    pwd_input = st.text_input("请输入专属密码解锁这份爱意：", type="password")
    if st.button("开启💌"):
        if pwd_input == PASSWORD:
            st.session_state["pass_ok"] = True
            st.rerun()
        else:
            st.error("密码不对哦，再试试～")
    st.stop()

# 密码正确加载特效
set_all_romantic_style()

# 🎵背景音乐
audio_html = """
<audio autoplay loop>
  <source src="https://music.163.com/song/media/outer/url?id=186126.mp3" type="audio/mpeg">

"""
st.components.v1.html(audio_html, height=0)


# ---------------------- 标题区 ----------------------
st.markdown('<div class="love-title">💌 属于我们的甜蜜回忆录 💌</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["✨开篇告白", "📸甜蜜瞬间相册", "⏳我们的时间线", "💌最后的悄悄话"])

with tab1:
    st.markdown('<div class="text-box">', unsafe_allow_html=True)
    st.subheader("嗨，我的男孩：")
    love_text = """
    嗨，我的男孩：

    我常常偷偷庆幸，人海里能够和你相遇。
    和你在一起之后，普通的日子也裹上了甜甜的滤镜。
    一起散步、聊天、分享琐碎，难过的时候有你拥抱，开心的事第一时间想讲给你听。

    我不需要多么轰轰烈烈的浪漫，
    只要身边一直是你，慢慢走，慢慢相爱就很好。
    谢谢你包容我的小情绪，接住我的所有不安。
    往后的朝朝暮暮，我想一直陪着你。
    我喜欢你，不止今天。
    """
    st.write(love_text)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="text-box">', unsafe_allow_html=True)
    st.subheader("📸 我们的照片合集（上传你们的合照）")
    st.info("在这里可以上传你们的甜蜜照片，一次可以多选！")
    upload_imgs = st.file_uploader("上传照片", type=["jpg","png","jpeg"], accept_multiple_files=True)
    if upload_imgs:
        col1, col2, col3 = st.columns(3)
        for idx, img in enumerate(upload_imgs):
            with [col1,col2,col3][idx%3]:
                st.image(img, caption=f"甜蜜瞬间 {idx+1}", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="text-box">', unsafe_allow_html=True)
    st.subheader("⏳ 我们重要的时间节点")

    # =========【重点修改这里！】=========
    together_day = datetime(2026,6,24)  # 你们在一起的日期
    next_anniversary = datetime(2027,6,24) # 下一个周年纪念日
    today = datetime.now()

    delta = next_anniversary.date() - today.date()
    if delta.days > 0:
        countdown_text = f"💖 距离下一个周年纪念日还有：{delta.days} 天"
    else:
        countdown_text = "💖 今天就是我们的纪念日！快乐！"

    st.markdown(f'<div class="countdown-box">{countdown_text}</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    timeline = [
        ("2026-06-17", "✨我们产生羁绊"),
        ("2026-06-24", "💌正式在一起"),
        ("2026-06-27", "🎱一起打台球"),
        ("2026-07-03", "🥘一起吃来菜"),
        ("2026-07-03", "🎤一起唱KTV"),
        ("2026-07-04", "🚆错过火车，一起吃豆皮"),
        ("2026-07-04", "✝第一次听说十字架治蚊子包"),
        ("2026-07-05", "🎦一起看电影"),
        ("2026-08-12", "🎁噜噜定情"),
        ("2026-08-19", "📿第一个七夕"),
        ("2026-09-05", "❤久别重逢"),
        ("2026-09-19", "🍨一起吃不颠哥"),
        ("2026-09-26", "🥖一起吃超长蛋挞"),
        ("2026-10-01", "🥩一起吃豪客来"),
        ("2026-10-04", "🎾一起打网球"),
        ("2026-10-05", "🍲一起吃海底捞"),
        ("未来", "🚩无数个还没实现的约定")
    ]
    for date, event in timeline:
        st.markdown(f'<p class="time-line">▪ {date} ｜ {event}</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="text-box">', unsafe_allow_html=True)
    st.subheader("💖 想对你说的悄悄话")
    secret_msg = """
    我不奢求永远这个词有多宏大，
    我只希望，我们的每一个当下，都真诚热烈。

    开心我们一起分享，压力和疲惫我也愿意和你分担。
    我会一直站在你这边，支持你的热爱与梦想。
    不用追赶世界，你只管往前走，我一直在身后陪着你。

    千千万万遍，我偏向你。
    💕 喜欢你的小石
    """
    st.write(secret_msg)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;color:#ff4477;text-align:center;'>I Love You Forever 💞</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 底部闪光装饰
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div style="text-align:center;font-size:34px">✨ 💖 ✨ 💫 💖 ✨ 💫 💖 ✨</div>', unsafe_allow_html=True)
