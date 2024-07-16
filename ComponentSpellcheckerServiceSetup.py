import language_tool_python

# First service start downloads LanguageTool automatically using a local server
# Language = english
tool = language_tool_python.LanguageTool('en-US')
tool.close()
