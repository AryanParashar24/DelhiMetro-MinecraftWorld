for file in docs/*.md; do
  if head -n 1 "$file" | grep -q "^## "; then
    sed -i '1s/^## /# /' "$file"
  fi
done
