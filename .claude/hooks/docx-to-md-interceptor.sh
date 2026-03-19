#!/bin/bash
# Hook 7: DOCX-to-Markdown Interceptor (Tier 1 - PreToolUse)
# Intercepts Read calls targeting .docx files, converts to .md using mammoth,
# then blocks the read with a redirect message so Claude reads the .md instead.

# Read the tool input JSON from stdin
INPUT=$(cat)

# Extract file_path from the JSON
FILE_PATH=$(echo "$INPUT" | python -c "
import sys, json
try:
    data = json.load(sys.stdin)
    # Handle both flat and nested structures
    if 'tool_input' in data:
        print(data['tool_input'].get('file_path', ''))
    else:
        print(data.get('file_path', ''))
except:
    print('')
" 2>/dev/null)

# If no file_path or not a .docx file, allow the read
if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Check if the file ends in .docx (case-insensitive)
if ! echo "$FILE_PATH" | grep -qi '\.docx$'; then
  exit 0
fi

# Normalize the path for the OS (handle Windows-style paths in Git Bash)
NORM_PATH="$FILE_PATH"

# Check the .docx file actually exists
if [ ! -f "$NORM_PATH" ]; then
  exit 0
fi

# Derive the .md output path (same directory, same name, .md extension)
# Use sed for case-insensitive extension replacement to avoid double-.md bug
MD_PATH=$(echo "$NORM_PATH" | sed -E 's/\.[dD][oO][cC][xX]$/.md/')

# Convert if .md doesn't exist or is older than the .docx
NEEDS_CONVERT=false
if [ ! -f "$MD_PATH" ]; then
  NEEDS_CONVERT=true
elif [ "$NORM_PATH" -nt "$MD_PATH" ]; then
  NEEDS_CONVERT=true
fi

if [ "$NEEDS_CONVERT" = true ]; then
  # Run mammoth to convert docx to markdown
  CONVERT_OUTPUT=$(python -c "
import mammoth
import sys
import os

docx_path = sys.argv[1]
md_path = sys.argv[2]

try:
    with open(docx_path, 'rb') as f:
        result = mammoth.convert_to_markdown(f)
        md_content = result.value

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    if result.messages:
        for msg in result.messages:
            print(f'Warning: {msg}', file=sys.stderr)

    print('OK')
except Exception as e:
    print(f'FAIL: {e}', file=sys.stderr)
    print('FAIL')
" "$NORM_PATH" "$MD_PATH" 2>&1)

  if echo "$CONVERT_OUTPUT" | grep -q "FAIL"; then
    # Conversion failed; let Claude read the .docx directly as fallback
    rm -f "$MD_PATH"
    exit 0
  fi

  # Sanity check: if the .md file is empty or tiny, conversion was bad
  MD_SIZE=$(wc -c < "$MD_PATH" 2>/dev/null || echo 0)
  if [ "$MD_SIZE" -lt 10 ]; then
    rm -f "$MD_PATH"
    exit 0
  fi
fi

# Block the .docx read and redirect to the .md file
echo "REDIRECTED: Converted \"$(basename "$NORM_PATH")\" to Markdown. Read \"$MD_PATH\" instead. [Hook 7: DOCX-to-MD Interceptor]" >&2
exit 2
