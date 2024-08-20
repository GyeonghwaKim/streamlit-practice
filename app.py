import streamlit as st
from config import type_emoji_dict, pokemons

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/mosterball.png"
)

st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요")



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

