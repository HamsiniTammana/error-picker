import streamlit as st

st.set_page_config(page_title="Default Code Errors", page_icon="⚠")

st.title("⚠ Default Programming Errors Explained")
st.write("Paste a common programming error to get a simple explanation.")

# -------------------------------
# DEFAULT ERROR DATABASE
# -------------------------------
ERRORS = {
    "syntaxerror": {
        "meaning": "There is a grammar mistake in your code.",
        "reason": "The code structure is incorrect or incomplete.",
        "fix": [
            "Check colons (:)",
            "Check brackets (), {}, []",
            "Check quotes ' or \"\""
        ],
        "example": "if x == 5:\n    print(x)"
    },

    "indentationerror": {
        "meaning": "Your code indentation is incorrect.",
        "reason": "Python uses indentation to group code blocks.",
        "fix": [
            "Use consistent spaces",
            "Do not mix tabs and spaces"
        ],
        "example": "if x > 0:\n    print(x)"
    },

    "typeerror": {
        "meaning": "You are using incompatible data types.",
        "reason": "Example: adding a number and a string.",
        "fix": [
            "Check variable types",
            "Convert values using int(), str(), float()"
        ],
        "example": "x = int('10')"
    },

    "nameerror": {
        "meaning": "You are using a variable that does not exist.",
        "reason": "The variable was never defined.",
        "fix": [
            "Check spelling",
            "Define variables before use"
        ],
        "example": "x = 10\nprint(x)"
    },

    "indexerror": {
        "meaning": "You tried to access an invalid list index.",
        "reason": "The index is out of range.",
        "fix": [
            "Check list length",
            "Use valid index numbers"
        ],
        "example": "nums = [1, 2, 3]\nprint(nums[2])"
    },

    "keyerror": {
        "meaning": "The dictionary key does not exist.",
        "reason": "You accessed a missing key.",
        "fix": [
            "Check dictionary keys",
            "Use dict.get()"
        ],
        "example": "data = {'a': 1}\nprint(data.get('b'))"
    },

    "zerodivisionerror": {
        "meaning": "You tried to divide by zero.",
        "reason": "Division by zero is not allowed.",
        "fix": [
            "Check denominator",
            "Use condition before dividing"
        ],
        "example": "if b != 0:\n    print(a / b)"
    }
}

# -------------------------------
# USER INPUT
# -------------------------------
error_input = st.text_area("Paste error message:", height=200)

if st.button("Explain Error"):
    if not error_input.strip():
        st.warning("Please paste an error message.")
    else:
        error_text = error_input.lower()
        found = False

        for key in ERRORS:
            if key in error_text:
                found = True
                data = ERRORS[key]

                st.subheader("📌 What it means")
                st.write(data["meaning"])

                st.subheader("❓ Why it happens")
                st.write(data["reason"])

                st.subheader("🛠 How to fix it")
                for step in data["fix"]:
                    st.write("•", step)

                st.subheader("✅ Example")
                st.code(data["example"])
                break

        if not found:
            st.info(
                "Default error not detected.\n\n"
                "Try checking:\n"
                "• Syntax\n"
                "• Variable names\n"
                "• Data types\n"
                "• Indentation"
            )
