# app.py
import streamlit as st
import ui                   # UIモジュール
import llm                  # LLMモジュール
import database             # データベースモジュール
import metrics              # 評価指標モジュール
import data                 # データモジュール
from config import MODEL_NAME

# --- アプリケーション設定 ---
st.set_page_config(page_title="Chatbot page", layout="centered", initial_sidebar_state="collapsed")

# --- CSS で UI を改良しました ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stSidebar {
        background-color: #ffffff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 初期化処理 ---
metrics.initialize_nltk()
database.init_db()
data.ensure_initial_data()

# --- モデルロード ---
pipe = llm.load_model()

# --- タイトル ---
st.title("チャットボットの評価サイト")
st.write("Gemmaモデルを使用したチャットボットです。回答に対してフィードバックを行えます。")
st.markdown("---")

# --- UI をタブ形式に変更 ---
tab1, tab2, tab3 = st.tabs(["チャット", "履歴閲覧", "データ管理"])

with tab1:
    if pipe:
        ui.display_chat_page(pipe)
    else:
        st.error("チャット機能を利用できません。モデルの読み込みに失敗しました。")

with tab2:
    ui.display_history_page()

with tab3:
    ui.display_data_page()

# --- フッター ---
st.sidebar.markdown("---")
st.sidebar.info("開発者: Rikuto Otsu | モデル: Gemma")
