import streamlit as st
from typeArr import type_emoji_dict

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/mosterball.png"
)

st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요")
# 속성추가

pokemon={
    "name":"누오",
    "types":["물","땅"],
    "image_url":"https://i.namu.wiki/i/e-W40ZAdGkzTIHMZmWcWNVy1FD6R2Wbt45XAQvpmwtQBB7YxpgHGvt21U8YKdIRmGKo5wjk2Wj9xFwSGqlqm-SljkhjFFVn_NWqAWdJAr0428ckPbBTGjc7tt8yqZwlg88XJuhm7BNVeiipPQBW_kw.webp"
}
with st.expander(label=pokemon["name"],expanded=True):
    st.image(pokemon["image_url"])
    emoji_types=[
        f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]
    ]
    st.subheader(" / ".join(emoji_types))