import streamlit as st
from Forward_chaining import forward
from Backward_chaining import backward
from parser import read_rules, read_facts



with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main title with animation
st.markdown("""
    <div class="main-title-container">
        <div class="sticker">🧠</div>
        <div class="main-title">Production System: Forward & Backward Chaining</div>
    </div>
""", unsafe_allow_html=True)


# File upload
col1, col2 = st.columns(2)
with col1:
    rules_file = st.file_uploader("📜 Upload rules.txt", type="txt")
with col2:
    facts_file = st.file_uploader("📘 Upload facts.txt", type="txt")


# Algorithm choice and goal input

algorithm = st.selectbox("🧩 Choose Inference Algorithm", ["Select...", "Forward Chaining", "Backward Chaining"])
goal = st.text_input("🎯 Enter a goal:")


if rules_file and facts_file:
    try:
        # Read and validate rules
        rules_content = rules_file.read().decode("utf-8")
        if not rules_content:
            st.error("❌ 'rules.txt' is empty!")
            st.stop()

        for line in rules_content.strip().splitlines():
            if 'IF' not in line.upper() or 'THEN' not in line.upper():
                st.error(f"❌ Invalid rule: `{line}`. Rule must contain 'IF' and 'THEN'.")
                st.stop()

        rules_file.seek(0)  # Reset file pointer
        rules = read_rules(rules_file)

        # Read and validate facts
        facts_content = facts_file.read().decode("utf-8")
        if not facts_content:
            st.error("❌ 'facts.txt' is empty!")
            st.stop()

        for line in facts_content.strip().splitlines():
            if 'IF' in line.upper() or 'THEN' in line.upper():
                st.error(f"❌ Invalid fact: `{line}`. Facts must not contain 'IF' or 'THEN'.")
                st.stop()

        facts_file.seek(0)
        facts = read_facts(facts_file)

    except Exception as e:
        st.error(f"❌ Error reading files: {e}")
        st.stop()


    st.subheader("📚 Input Data")

    col3, col4 = st.columns(2)
    with col3:
      st.markdown("Rules")
      st.code("\n".join([str(r) for r in rules]), language="text")
    with col4:
      st.markdown("Facts")
      st.code("\n".join(facts), language="text")


    if algorithm == "Forward Chaining":

        inferred_facts, cycles = forward(rules, facts, goal if goal else None)
        st.subheader("🚀 Forward Chaining Result")
        st.markdown("### 🌀 Inference Cycles")
        if cycles:
            st.code("\n\n".join(cycles), language="text")
        else:
            st.info("No rules were fired.")
        st.success(inferred_facts)
        st.code("\n".join(inferred_facts), language="text")

        if goal:
            if goal in inferred_facts:
                st.success(f"✅ The goal `{goal}` was successfully inferred.")
            else:
                st.error(f"❌ The goal `{goal}` could not be inferred.")
        else:
            st.info("All inferable facts are listed above.")

    elif algorithm == "Backward Chaining":
        if not goal:
            st.warning("⚠️ Please enter a goal.")
        else:
            result , trace = backward(rules, facts, goal)
            st.subheader("🔍 Backward Chaining Result")

            st.markdown("### 🌀 Inference Steps")
            st.code("\n".join(trace), language="text")

            if result:
                st.success(f"✅ The goal `{goal}` was successfully inferred.")
            else:
                st.error(f"❌ The goal `{goal}` could not be inferred.")

