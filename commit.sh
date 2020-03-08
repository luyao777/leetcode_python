
git add .
echo -n "Enter commit message: "
read commit_message
git commit -m "$commit_message"
git push -u origin master