import streamlit as st
import re

st.set_page_config(page_title="Code Error Helper", page_icon="🐞")

st.title("🐞 Code Error Helper")
st.write("Explains common programming errors in simple English.")

# Error knowledge base
ERROR_DATABASE = {
    "syntaxerror": {
        "meaning": "There is a typing or grammar mistake in your code.",
        "reason": "You may have missed a colon, bracket, or quote.",
        "fix": [
            "Check brackets (), {}, []",
            "Check quotes ' or \"",
            "Check colons and commas"
        ],
        "example": "if x == 5:\n    print(x)"
    },
    "typeerror": {
        "meaning": "You are using the wrong type of data.",
        "reason": "For example, adding a number to a string.",
        "fix": [
            "Check variable types",
            "Convert types using int(), str(), float()"
        ],
        "example": "age = int('20')"
    },
    "nullpointer": {
        "meaning": "You tried to use something that is empty (null).",
        "reason": "The object was never created or assigned.",
        "fix": [
            "Check if the object is null",
            "Initialize the object before use"
        ],
        "example": "if (obj != null) { obj.run(); }"
    }
}

error_input = st.text_area(
    "Paste your error message:",
    height=200
)

if st.button("Explain Error"):
    if not error_input.strip():
        st.warning("Please paste an error message.")
    else:
        error_lower = error_input.lower()

        found = False
        for key in ERROR_DATABASE:
            if re.search(key, error_lower):
                found = True
                data = ERROR_DATABASE[key]

                st.subheader("📌 What this error means")
                st.write(data["meaning"])

                st.subheader("❓ Why it happens")
                st.write(data["reason"])

                st.subheader("🛠 How to fix it")
                for step in data["fix"]:
                    st.write("•", step)

                st.subheader("✅ Example Fix")
                st.code(data["example"])
                break

        if not found:
            st.info("Error not recognized. Try checking syntax, variable names, or data types.")
