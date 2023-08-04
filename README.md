# What is this?

This is a plugin (tool) for the [Cheshire Cat Project](https://github.com/pieroit/cheshire-cat), which generate a Regular Expression (regex) from its description.

# Install

Download the **cc_easy_regex** folder into the **cheshire-cat/core/cat/plugins** one.

# Usage

Ask to the cat "regex description_of_a_regular_expression"

Examples:

Input: regex a string that contain an email address
Output: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b

Input: regex two digits, alphanumerical chars, dash, end with .py
Output: \d{2}[a-zA-Z0-9-]+\.py
