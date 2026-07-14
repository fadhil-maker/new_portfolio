import re

file_path = "c:\\Users\\vavac\\OneDrive\\Desktop\\port\\src\\app\\page.tsx"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Accessibility (Contrast Ratios)
content = content.replace("text-gray-400", "text-gray-600 dark:text-gray-300")
content = content.replace("text-gray-500", "text-gray-700 dark:text-gray-400")

# 2. Fix Performance (Non-Composited Animations)
# Replace 'transition-all' with 'transition-transform' to avoid animating layout properties (top, left, width)
content = content.replace("transition-all", "transition-transform")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Optimized page.tsx")
