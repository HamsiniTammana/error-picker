import streamlit as st
import re

st.set_page_config(page_title="Common Code Errors Guide", page_icon="📘")

st.title("📘 Common Code Errors – Simple Explanation")
st.write("Paste a programming error and get a simple explanation and fix.")

# -------------------------------
# COMMON ERRORS DATABASE
# -------------------------------
ERROR_DATABASE = {
    "syntaxerror": {
        "title": "Syntax Error",
        "meaning": "There is a grammar mistake in your code.",
        "reason": "Python could not understand your code structure.",
        "fix": [
            "Check colons (:) at the end of if/for/while",
            "Check brackets (), {}, []",
            "Check quotes ' or \"",
        ],
        "example": "if x == 5:\n    print(x)"
    },

    "indentationerror": {
        "title": "Indentation Error",
        "meaning": "Your code indentation (spaces) is incorrect.",
        "reason": "Python uses indentation to define code blocks.",
        "fix": [
            "Use the same number of spaces for each block",
            "Do not mix tabs and spaces",
        ],
        "example": "if x > 0:\n    print(x)"
    },

    "typeerror": {
        "title": "Type Error",
        "meaning": "You are using the wrong data type.",
        "reason": "For example, adding a number to a string.",
        "fix": [
            "Check variable types",
            "Convert values using int(), str(), float()",
        ],
        "example": "age = int('20')"
    },

    "nameerror": {
        "title": "Name Error",
        "meaning": "You are using a variable that does not exist.",
        "reason": "The variable was never defined.",
        "fix": [
            "Check spelling of variable names",
            "Define the variable before using it",
        ],
        "example": "x = 10\nprint(x)"
    },

    "indexerror": {
        "title": "Index Error",
        "meaning": "You tried to access an index that does not exist.",
        "reason": "The list is shorter than the index you used.",
        "fix": [
            "Check list length using len()",
            "Use valid index numbers",
        ],
        "example": "nums = [1, 2, 3]\nprint(nums[2])"
    },

    "keyerror": {
        "title": "Key Error",
        "meaning": "The key does not exist in the dictionary.",
        "reason": "You tried to access a missing key.",
        "fix": [
            "Check dictionary keys",
            "Use dict.get(key) instead of dict[key]",
        ],
        "example": "data = {'a': 1}\nprint(data.get('b'))"
    },

    "zerodivisionerror": {
        "title": "Zero Division Error",
        "meaning": "You tried to divide a number by zero.",
        "reason": "Division by zero is not allowed.",
        "fix": [
            "Check divisor before dividing",
            "Use conditional statements",
        ],
        "example": "if b != 0:\n    print(a / b)"
    },

    "nullpointer": {
        "title": "Null Pointer Exception (Java)",
        "meaning": "You are using an object that is null.",
        "reason": "The object was never created.",
        "fix": [
            "Check if object is null",
            "Initialize object before use",
        ],
        "example": "if (obj != null) { obj.run(); }"
    }
}

# -------------------------------
# USER INPUT
# -------------------------------
error_input = st.text_area(
    "Paste your error message here:",
    height=200
)

if st.button("Explain Error"):
    if not error_input.strip():
        st.warning("Please paste an error message.")
    else:
        error_lower = error_input.lower()
        found = False

        for key, data in ERROR_DATABASE.items():
            if re.search(key, error_lower):
                found = True

                st.subheader(f"📌 {data['title']}")
                st.write("*What it means:*", data["meaning"])
                st.write("*Why it happens:*", data["reason"])

                st.subheader("🛠 How to fix it")
                for step in data["fix"]:
                    st.write("•", step)

                st.subheader("✅ Example Fix")
                st.code(data["example"])
                break

        if not found:
            st.info(
                "This error is not in the manual database.\n\n"
                "Try checking:\n"
                "• Syntax mistakes\n"
                "• Variable names\n"
                "• Data types\n"
                "• Indentation"
            )
