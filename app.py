import streamlit as st
from config import type_emoji_dict, pokemons

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/mosterball.png"
)

st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요")


with st.form(key="form"):
    col1,col2=st.columns(2)
    with col1:
        name=st.text_input(label="포켓몬 이름")
    with col2:
        types=st.multiselect(
            label="포켓몬 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2
        )
    image_url=st.text_input(label="포켓몬 이미지 URL")
    submit=st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입려해주세요")
        if len(types) ==0:
            st.error("포켓몬의 속성을 적어도 한 개 설정해주세요")
        else:
            st.success("포켓몬을 추가할 수 있습니다")
            pokemons.append(
                {
                    "name":name,
                    "types":types,
                    "image_url": image_url if image_url else "./images/default.png"
                }
            )



for i in range(0,len(pokemons),3):
    row_poketmons=pokemons[i:i+3]
    cols=st.columns(3)
    for j in range(len(row_poketmons)):
        with cols[j]:
            pokemon=row_poketmons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']}**",expanded=True):
                st.image(pokemon["image_url"])
                emoji_types=[
                    f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]
                ]
                st.subheader(" / ".join(emoji_types))

