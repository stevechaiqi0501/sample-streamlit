import streamlit as st

st.title("シンプル計算機")

# 入力フィールド
num1 = st.number_input("最初の数字を入力してください")
num2 = st.number_input("二番目の数字を入力してください")

# 演算子の選択
operation = st.selectbox(
    "演算を選択してください",
    ("+", "-", "*", "/")
)

# 計算ボタン
if st.button("計算"):
    if operation == "+":
        result = num1 + num2
        st.success(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        st.success(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        st.success(f"{num1} * {num2} = {result}")
    elif operation == "/" and num2 != 0:
        result = num1 / num2
        st.success(f"{num1} / {num2} = {result}")
    elif operation == "/" and num2 == 0:
        st.error("0で割ることはできません！")

# 使い方の説明
st.markdown("### 使い方")
st.write("1. 二つの数字を入力します")
st.write("2. 演算子を選択します")
st.write("3. 「計算」ボタンをクリックします")