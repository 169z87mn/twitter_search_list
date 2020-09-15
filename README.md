# twitter_search_list
Twitterのリスト検索が死んだのでいろいろ試すAWS Lambda

# deploy
```bash
cd twitter_search_list
pip install -t ./package -r requirements.txt
cd package
zip -r9 ${OLDPWD}/function.zip .
cd $OLDPWD
zip -g function.zip twitter_search_list.py
aws lambda update-function-code --function-name twitter_search_list --zip-file fileb://function.zip
```